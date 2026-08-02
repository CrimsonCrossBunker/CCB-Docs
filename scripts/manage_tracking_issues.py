#!/usr/bin/env python3
"""Maintain deduplicated debt issues and one non-merging source-drift PR."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import date, timedelta
from pathlib import Path

import requests
import yaml


ROOT = Path(__file__).resolve().parents[1]
TRANSLATION_MARKER_PREFIX = "<!-- ccb-docs:translation:"
LINK_MARKER = "<!-- ccb-docs:external-links -->"
DRIFT_PR_MARKER = "<!-- ccb-docs:source-drift -->"
MAINTENANCE_MARKER_PREFIX = "<!-- ccb-docs:maintenance:"
MAX_RATE_LIMIT_RETRIES = 3
MAX_RATE_LIMIT_SLEEP_SECONDS = 30


class TrackingError(RuntimeError):
    """A tracking operation could not be completed safely."""


class GitHubClient:
    def __init__(self, repository: str, token: str) -> None:
        self.repository = repository
        self.api_url = os.environ.get("GITHUB_API_URL", "https://api.github.com")
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {token}",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "CCB-Docs-maintenance/1.0",
            }
        )

    def request(self, method: str, path: str, **kwargs: object) -> object:
        response = None
        for attempt in range(MAX_RATE_LIMIT_RETRIES + 1):
            response = self.session.request(
                method,
                f"{self.api_url}{path}",
                timeout=30,
                **kwargs,
            )
            limited = response.status_code == 429 or (
                response.status_code == 403
                and (
                    response.headers.get("X-RateLimit-Remaining") == "0"
                    or response.headers.get("Retry-After") is not None
                )
            )
            if not limited:
                break
            reset = response.headers.get("X-RateLimit-Reset")
            retry_after = response.headers.get("Retry-After")
            if retry_after and retry_after.isdigit():
                delay = int(retry_after)
            elif reset and reset.isdigit():
                delay = max(1, int(reset) - int(time.time()))
            else:
                delay = 2 ** attempt
            if attempt >= MAX_RATE_LIMIT_RETRIES or delay > MAX_RATE_LIMIT_SLEEP_SECONDS:
                raise TrackingError(
                    "GitHub API rate limit exhausted; "
                    f"retry after {delay}s or reset at {reset or 'unknown'}"
                )
            print(
                f"GitHub API rate-limited; retrying in {delay}s "
                f"({attempt + 1}/{MAX_RATE_LIMIT_RETRIES})",
                file=sys.stderr,
            )
            time.sleep(delay)
        assert response is not None
        if response.status_code >= 400:
            raise TrackingError(
                f"GitHub API {method} {path} failed: "
                f"HTTP {response.status_code}: {response.text[:500]}"
            )
        if not response.content:
            return None
        return response.json()

    def list_issues(self) -> list[dict]:
        issues: list[dict] = []
        for page in range(1, 11):
            payload = self.request(
                "GET",
                f"/repos/{self.repository}/issues",
                params={"state": "all", "per_page": 100, "page": page},
            )
            if not isinstance(payload, list):
                raise TrackingError("GitHub issues response was not a list")
            issues.extend(item for item in payload if "pull_request" not in item)
            if len(payload) < 100:
                break
        return issues

    def create_issue(self, title: str, body: str) -> dict:
        result = self.request(
            "POST",
            f"/repos/{self.repository}/issues",
            json={"title": title, "body": body},
        )
        if not isinstance(result, dict):
            raise TrackingError("GitHub create-issue response was not an object")
        return result

    def update_issue(self, number: int, title: str, body: str, state: str) -> None:
        self.request(
            "PATCH",
            f"/repos/{self.repository}/issues/{number}",
            json={"title": title, "body": body, "state": state},
        )


def load_json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise TrackingError(f"{path} must contain a JSON object")
    return data


def issues_by_marker(issues: list[dict], marker: str) -> list[dict]:
    return [issue for issue in issues if marker in (issue.get("body") or "")]


def upsert_issue(
    client: GitHubClient,
    issues: list[dict],
    marker: str,
    title: str,
    body: str,
) -> None:
    matches = issues_by_marker(issues, marker)
    existing = next((issue for issue in matches if issue.get("state") == "open"), None)
    if existing is None and matches:
        existing = matches[0]
    if existing is not None:
        client.update_issue(existing["number"], title, body, "open")
        print(f"updated issue #{existing['number']}: {title}")
        for duplicate in matches:
            if duplicate["number"] == existing["number"]:
                continue
            close_issue(
                client,
                duplicate,
                f"Automatically closed as a duplicate of #{existing['number']}.",
            )
        return
    created = client.create_issue(title, body)
    print(f"created issue #{created['number']}: {title}")
    issues.append(created)


def close_issue(client: GitHubClient, issue: dict, note: str) -> None:
    if issue.get("state") == "closed":
        return
    body = (issue.get("body") or "").rstrip() + f"\n\n{note}\n"
    client.update_issue(issue["number"], issue["title"], body, "closed")
    print(f"closed issue #{issue['number']}: {issue['title']}")


def translation_issue_body(debt: dict) -> str:
    stale_since = date.fromisoformat(debt["stale_since"])
    due = stale_since + timedelta(days=30)
    marker = f"{TRANSLATION_MARKER_PREFIX}{debt['id']} -->"
    state = "overdue" if debt["overdue"] else "within the 30-day window"
    return (
        f"{marker}\n"
        "This issue is generated from `docs-catalog.yml`.\n\n"
        f"- Documentation ID: `{debt['id']}`\n"
        f"- English stale since: `{debt['stale_since']}`\n"
        f"- Translation deadline: `{due.isoformat()}`\n"
        f"- Current age: `{debt['age_days']}` days ({state})\n"
        f"- Risk subsystem: `{debt['risk_group']}` ({debt['risk_level']})\n\n"
        "Update the English pair, set `translation_status: current`, and regenerate "
        "catalog output. This debt does not block unrelated documentation changes.\n"
    )


def manage_translation_issues(client: GitHubClient, report: dict) -> None:
    issues = client.list_issues()
    desired: set[str] = set()
    for debt in report.get("debts", []):
        marker = f"{TRANSLATION_MARKER_PREFIX}{debt['id']} -->"
        desired.add(marker)
        title = f"[translation] Refresh English page: {debt['id']}"
        upsert_issue(
            client,
            issues,
            marker,
            title,
            translation_issue_body(debt),
        )
    for issue in issues:
        body = issue.get("body") or ""
        match = re.search(r"<!-- ccb-docs:translation:[^ ]+ -->", body)
        if match and match.group(0) not in desired:
            close_issue(client, issue, "Automatically closed: translation is current.")


def external_link_issue_body(failures: list[dict]) -> str:
    lines = [
        LINK_MARKER,
        "The scheduled external-link check found non-critical failures.",
        "These are warnings and do not fail ordinary pull requests.",
        "",
    ]
    for failure in failures:
        lines.append(f"- `{failure['url']}` — {failure['reason']}")
    lines.extend(
        [
            "",
            "Fix or replace links after confirming the failure is persistent.",
            "Critical links are maintained separately in `config/critical-links.yml`.",
        ]
    )
    return "\n".join(lines) + "\n"


def manage_link_issue(client: GitHubClient, report: dict) -> None:
    issues = client.list_issues()
    failures = report.get("external_failures", [])
    existing = issues_by_marker(issues, LINK_MARKER)
    if failures:
        upsert_issue(
            client,
            issues,
            LINK_MARKER,
            "[automation] External documentation link warnings",
            external_link_issue_body(failures),
        )
    else:
        for issue in existing:
            close_issue(client, issue, "Automatically closed: all ordinary links passed.")


def maintenance_issue_body(key: str, title: str, report: dict) -> str:
    marker = f"{MAINTENANCE_MARKER_PREFIX}{key} -->"
    findings = report.get("findings", [])
    lines = [
        marker,
        f"# {title}",
        "",
        "This issue is reconciled from a scheduled CCB-Docs maintenance report.",
        "It is deduplicated by the marker above and is never used for auto-merge or approval.",
        "",
        f"- Report schema: `{report.get('schema_version', 'unknown')}`",
        f"- Status: `{report.get('status', 'attention')}`",
        f"- Findings: `{len(findings)}`",
        "",
        "## Findings",
        "",
    ]
    for finding in findings[:100]:
        identity = str(finding.get("id", "finding"))
        severity = str(finding.get("severity", "warning"))
        message = str(finding.get("message", "No message supplied."))
        lines.append(f"- **{severity}** `{identity}` — {message}")
    if len(findings) > 100:
        lines.append(f"- … {len(findings) - 100} additional findings are in the artifact.")
    lines.extend(
        [
            "",
            "Review the workflow artifact for the complete machine-readable report.",
            "A human remains responsible for policy decisions and any repository-setting change.",
        ]
    )
    return "\n".join(lines) + "\n"


def manage_maintenance_issue(
    client: GitHubClient,
    report: dict,
    key: str,
    title: str,
) -> None:
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", key):
        raise TrackingError("maintenance issue key must be a lowercase slug")
    issues = client.list_issues()
    marker = f"{MAINTENANCE_MARKER_PREFIX}{key} -->"
    existing = issues_by_marker(issues, marker)
    findings = report.get("findings", [])
    if not isinstance(findings, list):
        raise TrackingError("maintenance report findings must be an array")
    if findings:
        upsert_issue(
            client,
            issues,
            marker,
            title,
            maintenance_issue_body(key, title, report),
        )
    else:
        for issue in existing:
            close_issue(
                client,
                issue,
                "Automatically closed: the latest report has no findings.",
            )


def run_git(args: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=check,
        text=True,
        capture_output=True,
    )


def run_command(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )


def drift_updates(report: dict, catalog: dict) -> dict[tuple[str, str], dict[str, str]]:
    stale_keys = {
        (page["id"], page["language"]): page
        for page in report.get("stale_pages", [])
    }
    updates: dict[tuple[str, str], dict[str, str]] = {}
    for page in catalog["pages"]:
        key = (page["id"], page["language"])
        drift = stale_keys.get(key)
        if not drift or page["status"] != "active":
            continue
        changed = ", ".join(drift["changed_paths"][:3])
        if len(drift["changed_paths"]) > 3:
            changed += ", …"
        reason = f"Source paths changed after {page['verified_commit'][:12]}: {changed}"
        updates[key] = {
            "status": "stale",
            "include_in_ai_index": "false",
            "stale_reason": json.dumps(reason, ensure_ascii=False),
        }
    return updates


def apply_catalog_updates(path: Path, updates: dict[tuple[str, str], dict[str, str]]) -> None:
    content = path.read_text(encoding="utf-8")
    field_pattern = re.compile(r"^    ([a-z_]+):")

    def layout(text: str) -> tuple[
        list[str],
        list[dict],
        list[tuple[int, int]],
        dict[tuple[str, str], list[int]],
    ]:
        catalog = yaml.safe_load(text)
        document = yaml.compose(text)
        if not isinstance(catalog, dict) or not isinstance(catalog.get("pages"), list):
            raise TrackingError("catalog must contain a pages array")
        if not isinstance(document, yaml.nodes.MappingNode):
            raise TrackingError("catalog YAML root must be a mapping")
        pages_node = next(
            (
                value
                for key, value in document.value
                if isinstance(key, yaml.nodes.ScalarNode) and key.value == "pages"
            ),
            None,
        )
        if not isinstance(pages_node, yaml.nodes.SequenceNode):
            raise TrackingError("catalog pages must be a YAML sequence")

        pages = catalog["pages"]
        if len(pages) != len(pages_node.value):
            raise TrackingError("catalog page values do not match their YAML nodes")
        starts = [node.start_mark.line for node in pages_node.value]
        if starts != sorted(set(starts)):
            raise TrackingError("catalog page YAML nodes overlap")
        ends = starts[1:] + (
            [pages_node.value[-1].end_mark.line] if pages_node.value else []
        )
        spans = list(zip(starts, ends))
        positions: dict[tuple[str, str], list[int]] = {}
        for index, page in enumerate(pages):
            if not isinstance(page, dict):
                raise TrackingError("catalog pages must contain mappings")
            identifier = page.get("id")
            language = page.get("language")
            if not isinstance(identifier, str) or not isinstance(language, str):
                raise TrackingError("catalog page is missing a string id or language")
            positions.setdefault((identifier, language), []).append(index)
        return text.splitlines(keepends=True), pages, spans, positions

    parsed_updates: dict[tuple[str, str], dict[str, tuple[str, object]]] = {}
    for key, changes in updates.items():
        parsed_updates[key] = {}
        for field, rendered_value in changes.items():
            if not re.fullmatch(r"[a-z_]+", field):
                raise TrackingError(f"invalid catalog field name: {field}")
            if (
                not isinstance(rendered_value, str)
                or "\n" in rendered_value
                or "\r" in rendered_value
            ):
                raise TrackingError(f"catalog update for {field} must be one YAML line")
            parsed_updates[key][field] = (
                rendered_value,
                yaml.safe_load(rendered_value),
            )

    original_lines, original_pages, spans, original_positions = layout(content)
    for key in updates:
        matches = original_positions.get(key, [])
        if not matches:
            raise TrackingError(f"catalog page not found for update: {key[0]} ({key[1]})")
        if len(matches) != 1:
            raise TrackingError(f"catalog page is duplicated: {key[0]} ({key[1]})")

    newline = "\r\n" if "\r\n" in content else "\n"

    # First replace fields explicitly present in each page.  This updates an
    # anchored source entry without reformatting the rest of the YAML.
    lines = list(original_lines)
    for key, changes in updates.items():
        start, end = spans[original_positions[key][0]]
        seen_fields: set[str] = set()
        for line_index in range(start, end):
            match = field_pattern.match(lines[line_index])
            if not match or match.group(1) not in changes:
                continue
            field = match.group(1)
            if field in seen_fields:
                raise TrackingError(
                    f"catalog page repeats field {field}: {key[0]} ({key[1]})"
                )
            seen_fields.add(field)
            ending = (
                "\r\n"
                if lines[line_index].endswith("\r\n")
                else "\n" if lines[line_index].endswith("\n") else ""
            )
            lines[line_index] = f"    {field}: {changes[field]}{ending}"
    content = "".join(lines)

    # A merge-key page may already receive the desired value through its
    # anchor.  Insert only values that still differ, keeping the textual diff
    # as small as possible while allowing language-specific overrides.
    ordered_keys = sorted(updates, key=lambda key: original_positions[key][0])
    language_order = list(dict.fromkeys(key[1] for key in ordered_keys))
    for language in language_order:
        lines, pages, spans, positions = layout(content)
        insertions: list[tuple[int, list[str]]] = []
        for key in (key for key in ordered_keys if key[1] == language):
            page_index = positions[key][0]
            page = pages[page_index]
            missing = [
                field
                for field, (_, expected) in parsed_updates[key].items()
                if page.get(field) != expected
            ]
            if not missing:
                continue
            start, end = spans[page_index]
            insert_at = next(
                (
                    line_index
                    for line_index in range(start, end)
                    if lines[line_index].startswith("    nav:")
                ),
                end,
            )
            insertions.append(
                (
                    insert_at,
                    [
                        f"    {field}: {parsed_updates[key][field][0]}{newline}"
                        for field in missing
                    ],
                )
            )
        for insert_at, inserted_lines in reversed(insertions):
            if insert_at and not lines[insert_at - 1].endswith(("\n", "\r")):
                lines[insert_at - 1] += newline
            lines[insert_at:insert_at] = inserted_lines
        content = "".join(lines)

    _, final_pages, _, final_positions = layout(content)
    all_fields = {
        field for changes in parsed_updates.values() for field in changes
    }
    for key, page_indexes in original_positions.items():
        if len(page_indexes) != 1 or len(final_positions.get(key, [])) != 1:
            raise TrackingError(f"catalog page key is not unique: {key[0]} ({key[1]})")
        original_page = original_pages[page_indexes[0]]
        final_page = final_pages[final_positions[key][0]]
        for field in all_fields:
            expected = parsed_updates.get(key, {}).get(
                field,
                ("", original_page.get(field)),
            )[1]
            if final_page.get(field) != expected:
                raise TrackingError(
                    "catalog anchor update changed an unrequested value: "
                    f"{key[0]} ({key[1]}) {field}"
                )

    path.write_text(content, encoding="utf-8")


def remote_branch_sha(branch: str) -> str | None:
    result = run_git(["ls-remote", "--heads", "origin", branch])
    line = result.stdout.strip()
    return line.split()[0] if line else None


def find_or_create_drift_pr(
    client: GitHubClient,
    base: str,
    branch: str,
    changed_ids: list[str],
) -> None:
    owner = client.repository.split("/", 1)[0]
    pulls = client.request(
        "GET",
        f"/repos/{client.repository}/pulls",
        params={"state": "open", "head": f"{owner}:{branch}", "base": base},
    )
    if not isinstance(pulls, list):
        raise TrackingError("GitHub pull response was not a list")
    body = (
        f"{DRIFT_PR_MARKER}\n"
        "Automated aggregate update based only on catalog `source_paths`.\n\n"
        "Pages marked stale:\n"
        + "\n".join(f"- `{identifier}`" for identifier in changed_ids)
        + "\n\nThis pull request is never auto-merged. A human must review and merge it.\n"
    )
    title = "docs: mark source-linked pages stale"
    if pulls:
        client.request(
            "PATCH",
            f"/repos/{client.repository}/pulls/{pulls[0]['number']}",
            json={"title": title, "body": body},
        )
        print(f"updated source-drift PR #{pulls[0]['number']}")
        return
    created = client.request(
        "POST",
        f"/repos/{client.repository}/pulls",
        json={
            "title": title,
            "body": body,
            "head": branch,
            "base": base,
            "draft": True,
            "maintainer_can_modify": True,
        },
    )
    if not isinstance(created, dict):
        raise TrackingError("GitHub create-pull response was not an object")
    print(f"created source-drift draft PR #{created['number']}")


def publish_drift(
    client: GitHubClient,
    report: dict,
    base: str,
    branch: str,
    dry_run: bool,
) -> None:
    catalog_path = ROOT / "docs-catalog.yml"
    catalog = yaml.safe_load(catalog_path.read_text(encoding="utf-8"))
    updates = drift_updates(report, catalog)
    if not updates:
        print("source drift produced no catalog changes; no branch or PR created")
        return
    if dry_run:
        identifiers = sorted({key[0] for key in updates})
        print("would update source-drift PR for: " + ", ".join(identifiers))
        return

    if run_git(["status", "--porcelain", "--untracked-files=no"]).stdout.strip():
        raise TrackingError("refusing drift publication from a dirty tracked worktree")
    run_git(["fetch", "origin", base])
    old_sha = remote_branch_sha(branch)
    run_git(["switch", "--force-create", branch, f"origin/{base}"])
    apply_catalog_updates(catalog_path, updates)
    run_command([sys.executable, "scripts/generate_catalog.py"])
    if not run_git(["status", "--porcelain", "--untracked-files=no"]).stdout.strip():
        print("source drift produced no file changes; no commit or PR created")
        return
    run_git(["config", "user.name", "ccb-docs-automation[bot]"])
    run_git(["config", "user.email", "ccb-docs-automation[bot]@users.noreply.github.com"])
    run_git(["add", "docs-catalog.yml", "docs"])
    run_git(["commit", "-m", "docs: mark source-linked pages stale"])
    push = ["push"]
    if old_sha:
        push.append(f"--force-with-lease=refs/heads/{branch}:{old_sha}")
    push.extend(["origin", f"HEAD:refs/heads/{branch}"])
    run_git(push)
    changed_ids = sorted({key[0] for key in updates})
    find_or_create_drift_pr(client, base, branch, changed_ids)


def client_from_args(args: argparse.Namespace) -> GitHubClient:
    repository = args.repository or os.environ.get("GITHUB_REPOSITORY")
    token = args.token or os.environ.get("GITHUB_TOKEN")
    if not repository:
        raise TrackingError("repository is required (or set GITHUB_REPOSITORY)")
    if not token and not args.dry_run:
        raise TrackingError("token is required (or set GITHUB_TOKEN)")
    return GitHubClient(repository, token or "dry-run")


def add_shared_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--repository")
    parser.add_argument("--token")
    parser.add_argument("--dry-run", action="store_true")


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("translation", "links"):
        add_shared_arguments(subparsers.add_parser(command))
    drift_parser = subparsers.add_parser("drift")
    add_shared_arguments(drift_parser)
    drift_parser.add_argument("--base", default="main")
    drift_parser.add_argument("--branch", default="automation/source-drift")
    maintenance_parser = subparsers.add_parser("maintenance")
    add_shared_arguments(maintenance_parser)
    maintenance_parser.add_argument("--key", required=True)
    maintenance_parser.add_argument("--title", required=True)
    args = parser.parse_args()

    try:
        report = load_json(args.report)
        client = client_from_args(args)
        if args.dry_run and args.command not in {"drift", "maintenance"}:
            count_key = "debts" if args.command == "translation" else "external_failures"
            print(f"would reconcile {len(report.get(count_key, []))} {args.command} items")
        elif args.command == "translation":
            manage_translation_issues(client, report)
        elif args.command == "links":
            manage_link_issue(client, report)
        elif args.command == "drift":
            publish_drift(client, report, args.base, args.branch, args.dry_run)
        elif args.dry_run:
            print(
                f"would reconcile {len(report.get('findings', []))} maintenance findings"
            )
        else:
            manage_maintenance_issue(client, report, args.key, args.title)
    except (
        TrackingError,
        OSError,
        ValueError,
        KeyError,
        requests.RequestException,
        subprocess.CalledProcessError,
        yaml.YAMLError,
    ) as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
