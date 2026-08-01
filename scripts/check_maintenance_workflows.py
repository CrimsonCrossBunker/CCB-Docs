#!/usr/bin/env python3
"""Validate safety and operability requirements for scheduled workflows."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DIR = ROOT / ".github/workflows"
DEPENDABOT_PATH = ROOT / ".github/dependabot.yml"
EXPECTED_SCHEDULES = {
    "nightly.yml": "weekly",
    "monthly-maintenance.yml": "monthly",
    "quarterly-maintenance.yml": "quarterly",
    "docs-snapshot.yml": "snapshot_backup",
}
ALLOWED_PERMISSION_KEYS = {"actions", "contents", "issues", "pull-requests"}
ALLOWED_PERMISSION_VALUES = {"read", "write", "none"}
FORBIDDEN_WORKFLOW_PATTERNS = {
    r"\bgh\s+pr\s+merge\b": "must not merge pull requests",
    r"\bgh\s+pr\s+review\b.*\bapprove\b": "must not approve pull requests",
    r"/pulls/[^\s]+/reviews": "must not call the pull-request review API",
    r"\bauto[_-]merge\b": "must not enable auto-merge",
}


class WorkflowPolicyError(ValueError):
    """A workflow or maintenance policy document is structurally invalid."""


def load_base_yaml(path: Path) -> dict[str, Any]:
    """Load Actions YAML without YAML 1.1 turning the key `on` into True."""
    value = yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
    if not isinstance(value, dict):
        raise WorkflowPolicyError(f"{path} must contain a mapping")
    return value


def mapping(value: object) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def validate_action_pins(name: str, raw: str) -> list[str]:
    errors: list[str] = []
    for line in raw.splitlines():
        match = re.match(r"\s*uses:\s*([^#\s]+)", line)
        if not match:
            continue
        action = match.group(1)
        if not re.fullmatch(r"[^@\s]+@[0-9a-f]{40}", action):
            errors.append(f"{name}: action is not pinned to a 40-character SHA: {action}")
    return errors


def validate_permissions(name: str, workflow: dict[str, Any], raw: str) -> list[str]:
    errors: list[str] = []
    root_permissions = workflow.get("permissions")
    if not isinstance(root_permissions, dict):
        return [f"{name}: root permissions must be an explicit mapping"]
    jobs = mapping(workflow.get("jobs"))
    for job_name, job in jobs.items():
        job_data = mapping(job)
        if "permissions" in job_data:
            permissions_value = job_data.get("permissions")
            if not isinstance(permissions_value, dict):
                errors.append(f"{name}: job {job_name} permissions must be a mapping")
                continue
            permissions = permissions_value
        else:
            permissions = root_permissions
        if not permissions:
            errors.append(f"{name}: job {job_name} has no explicit permissions")
            continue
        for key, value in permissions.items():
            if key not in ALLOWED_PERMISSION_KEYS:
                errors.append(
                    f"{name}: job {job_name} has unnecessary permission: {key}"
                )
            if value not in ALLOWED_PERMISSION_VALUES:
                errors.append(
                    f"{name}: job {job_name} has invalid permission for {key}: {value}"
                )
        job_text = yaml.safe_dump(job_data, sort_keys=False)
        tracks_issues = "manage_tracking_issues.py" in job_text
        updates_drift = "manage_tracking_issues.py drift" in job_text
        downloads_artifacts = "actions/download-artifact@" in job_text
        prefix = f"{name}: job {job_name}"
        if tracks_issues and permissions.get("issues") != "write":
            errors.append(f"{prefix} Issue reconciliation requires issues: write")
        if not tracks_issues and permissions.get("issues") == "write":
            errors.append(f"{prefix} issues: write is unused")
        if downloads_artifacts and permissions.get("actions") != "read":
            errors.append(f"{prefix} artifact download requires actions: read")
        if not downloads_artifacts and permissions.get("actions") in {"read", "write"}:
            errors.append(f"{prefix} actions permission is unused")
        if updates_drift:
            if permissions.get("contents") != "write":
                errors.append(f"{prefix} drift publication requires contents: write")
            if permissions.get("pull-requests") != "write":
                errors.append(f"{prefix} drift publication requires pull-requests: write")
        else:
            if permissions.get("contents") == "write":
                errors.append(f"{prefix} contents: write is unused")
            if permissions.get("pull-requests") == "write":
                errors.append(f"{prefix} pull-requests: write is unused")
    return errors


def validate_scheduled_workflow(
    path: Path,
    expected_cron: str,
    maintenance: dict[str, Any],
) -> list[str]:
    name = path.name
    raw = path.read_text(encoding="utf-8")
    workflow = load_base_yaml(path)
    errors: list[str] = []
    triggers = mapping(workflow.get("on"))
    if "schedule" not in triggers:
        errors.append(f"{name}: missing schedule trigger")
    if "workflow_dispatch" not in triggers:
        errors.append(f"{name}: missing workflow_dispatch trigger")
    schedule = triggers.get("schedule")
    configured = maintenance.get("schedules", {}).get(expected_cron)
    observed = []
    if isinstance(schedule, list):
        observed = [mapping(item).get("cron") for item in schedule]
    if configured not in observed:
        errors.append(
            f"{name}: schedule does not match config/maintenance.yml {expected_cron}: {configured}"
        )

    concurrency = mapping(workflow.get("concurrency"))
    if not concurrency.get("group") or "cancel-in-progress" not in concurrency:
        errors.append(f"{name}: concurrency requires group and cancel-in-progress")
    jobs = mapping(workflow.get("jobs"))
    if not jobs:
        errors.append(f"{name}: no jobs are defined")
    for job_name, job in jobs.items():
        job_data = mapping(job)
        timeout = job_data.get("timeout-minutes")
        if timeout is None or not str(timeout).isdigit() or int(timeout) <= 0:
            errors.append(f"{name}: job {job_name} needs a positive timeout-minutes")

    errors.extend(validate_permissions(name, workflow, raw))
    errors.extend(validate_action_pins(name, raw))
    if "manage_tracking_issues.py" not in raw:
        errors.append(f"{name}: scheduled findings need marker-deduplicated Issue reconciliation")
    if "write_workflow_summary.py" not in raw:
        errors.append(f"{name}: missing Job Summary generation")
    if "actions/upload-artifact@" not in raw:
        errors.append(f"{name}: scheduled evidence is not uploaded as an artifact")
    for pattern, message in FORBIDDEN_WORKFLOW_PATTERNS.items():
        if re.search(pattern, raw, flags=re.IGNORECASE | re.DOTALL):
            errors.append(f"{name}: {message}")
    return errors


def validate_dependabot(maintenance: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not DEPENDABOT_PATH.is_file():
        return [".github/dependabot.yml: dependency update configuration is missing"]
    value = yaml.safe_load(DEPENDABOT_PATH.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or value.get("version") != 2:
        return [".github/dependabot.yml: version must be 2"]
    updates = value.get("updates")
    if not isinstance(updates, list):
        return [".github/dependabot.yml: updates must be an array"]
    expected = {"github-actions", "npm", "uv"}
    observed: list[str] = []
    for index, item in enumerate(updates):
        if not isinstance(item, dict):
            errors.append(f".github/dependabot.yml: update {index} must be a mapping")
            continue
        ecosystem = item.get("package-ecosystem")
        if isinstance(ecosystem, str):
            observed.append(ecosystem)
        if item.get("directory") != "/":
            errors.append(
                f".github/dependabot.yml: {ecosystem} must update the repository root"
            )
        schedule = mapping(item.get("schedule"))
        if schedule.get("interval") not in {"weekly", "monthly"}:
            errors.append(
                f".github/dependabot.yml: {ecosystem} needs a bounded weekly/monthly schedule"
            )
        if item.get("target-branch") != "main":
            errors.append(f".github/dependabot.yml: {ecosystem} must target main")
        limit = item.get("open-pull-requests-limit")
        if not isinstance(limit, int) or limit < 1 or limit > 10:
            errors.append(
                f".github/dependabot.yml: {ecosystem} needs a 1-10 PR limit"
            )
    if set(observed) != expected or len(observed) != len(expected):
        errors.append(
            ".github/dependabot.yml: ecosystems must be exactly github-actions, npm, and uv"
        )

    dependency_policy = mapping(
        mapping(maintenance.get("automation_policy")).get("dependency_updates")
    )
    if dependency_policy.get("provider") != "dependabot":
        errors.append("config/maintenance.yml: dependency provider must be dependabot")
    if set(dependency_policy.get("ecosystems", [])) != expected:
        errors.append("config/maintenance.yml: dependency ecosystems do not match Dependabot")
    if dependency_policy.get("responsible_human_review_required") is not True:
        errors.append("config/maintenance.yml: dependency PRs require Responsible-human review")
    if dependency_policy.get("action_references_remain_full_sha_pinned") is not True:
        errors.append("config/maintenance.yml: Actions updates must preserve full SHA pins")
    return errors


def validate_monthly_contracts() -> list[str]:
    path = WORKFLOW_DIR / "monthly-maintenance.yml"
    raw = path.read_text(encoding="utf-8")
    errors: list[str] = []
    required_commands = (
        "tools/lua_api/generate_public_contract.py --check",
        "tools/lua_api/check_public_contract.py",
        "tools/lua_api/check_ccb_inventory.py",
        "tools/lua_api/check_luals_declarations.py",
        "tools/lua_api/check_coverage.py --require-complete",
    )
    for command in required_commands:
        if command not in raw:
            errors.append(f"monthly-maintenance.yml: missing authoritative Lua check: {command}")
    report_position = raw.find("generate_maintenance_reports.py api-diff")
    if report_position < 0:
        errors.append("monthly-maintenance.yml: API diff report command is missing")
    else:
        for command in required_commands:
            position = raw.find(command)
            if position >= report_position:
                errors.append(
                    f"monthly-maintenance.yml: Lua check must run before API report: {command}"
                )
    coverage_position = raw.find("generate_maintenance_reports.py docs-coverage")
    if coverage_position < 0:
        errors.append("monthly-maintenance.yml: documentation coverage report is missing")
    else:
        coverage_command = raw[coverage_position:raw.find("--json-output", coverage_position)]
        for argument in ("--source-repo .build/ccb-source", "--target-ref HEAD"):
            if argument not in coverage_command:
                errors.append(
                    f"monthly-maintenance.yml: docs coverage is missing {argument}"
                )

    watch = yaml.safe_load(
        (ROOT / "config/api-contract-watch.yml").read_text(encoding="utf-8")
    )
    contracts = mapping(mapping(watch).get("contracts"))
    lua_contract = mapping(contracts.get("lua-v5"))
    lua_paths = set(lua_contract.get("paths", []))
    required_paths = {
        "data/lua/manifest.schema.json",
        "data/lua/types/ccb_api_v5.d.lua",
        "data/lua/reference/ccb_native_inventory.json",
        "data/lua/reference/ccb_public_api_v5.json",
        "data/lua/reference/ccb_public_api_v5.schema.json",
        "data/lua/reference/ccb_public_api_v5_coverage.json",
        "data/lua/reference/ccb_public_api_v5_coverage.schema.json",
    }
    missing = sorted(required_paths - lua_paths)
    if missing:
        errors.append("config/api-contract-watch.yml: missing Lua paths: " + ", ".join(missing))
    return errors


def validate_quarterly_live_audit() -> list[str]:
    raw = (WORKFLOW_DIR / "quarterly-maintenance.yml").read_text(encoding="utf-8")
    errors: list[str] = []
    required = (
        '--github-repository "${{ github.repository }}"',
        '--github-organization "${{ github.repository_owner }}"',
        "--github-token-env GITHUB_TOKEN",
        "GITHUB_TOKEN: ${{ github.token }}",
    )
    for token in required:
        if token not in raw:
            errors.append(f"quarterly-maintenance.yml: live permissions audit is missing {token}")
    return errors


def validate_snapshot_workflow(
    maintenance: dict[str, Any],
    path: Path = WORKFLOW_DIR / "docs-snapshot.yml",
) -> list[str]:
    raw = path.read_text(encoding="utf-8")
    workflow = load_base_yaml(path)
    triggers = mapping(workflow.get("on"))
    errors: list[str] = []
    if "release" in triggers:
        errors.append(
            "docs-snapshot.yml: CCB-Docs release trigger must not impersonate a game release"
        )
    dispatch = mapping(triggers.get("repository_dispatch"))
    event_type = mapping(maintenance.get("release_snapshots")).get(
        "repository_dispatch_type"
    )
    if event_type not in dispatch.get("types", []):
        errors.append("docs-snapshot.yml: authoritative CCB repository_dispatch type is missing")
    manual = mapping(triggers.get("workflow_dispatch"))
    inputs = mapping(manual.get("inputs"))
    if set(inputs) != {"source_sha", "source_tag"}:
        errors.append("docs-snapshot.yml: manual release inputs must be source_sha and source_tag")
    concurrency = mapping(workflow.get("concurrency"))
    if concurrency.get("group") != "documentation-snapshot":
        errors.append("docs-snapshot.yml: snapshot concurrency must be fixed across refs")
    if mapping(workflow.get("permissions")):
        errors.append("docs-snapshot.yml: root permissions must be empty and split by job")
    jobs = mapping(workflow.get("jobs"))
    snapshot = mapping(jobs.get("snapshot"))
    health = mapping(jobs.get("reconcile-health"))
    if mapping(snapshot.get("permissions")) != {"contents": "read"}:
        errors.append("docs-snapshot.yml: release snapshot job must remain read-only")
    health_condition = str(health.get("if", ""))
    for token in ("github.event_name == 'schedule'", "workflow_dispatch", "refs/heads/main"):
        if token not in health_condition:
            errors.append(f"docs-snapshot.yml: health Issue scope is missing {token}")
    if "repository_dispatch" in health_condition:
        errors.append(
            "docs-snapshot.yml: release dispatch must not reconcile the main health Issue"
        )
    if "needs.snapshot.result != 'cancelled'" in health_condition:
        errors.append(
            "docs-snapshot.yml: timed-out/cancelled snapshot jobs must produce health evidence"
        )
    health_steps = health.get("steps", [])
    named_steps = {
        mapping(step).get("name"): (index, mapping(step))
        for index, step in enumerate(health_steps)
        if isinstance(step, dict)
    }
    download_index, download = named_steps.get(
        "Download snapshot restore evidence",
        (-1, {}),
    )
    ensure_index, ensure = named_steps.get(
        "Ensure snapshot workflow failure evidence exists",
        (-1, {}),
    )
    reconcile_index, reconcile = named_steps.get(
        "Reconcile snapshot restore-health Issue",
        (-1, {}),
    )
    if download.get("continue-on-error") != "true":
        errors.append("docs-snapshot.yml: missing snapshot artifact download must continue")
    ensure_run = str(ensure.get("run", ""))
    ensure_env = mapping(ensure.get("env"))
    for token in (
        "--ensure-workflow-failure-report",
        "--workflow-result",
        "--json-output .build/snapshot/restore-health.json",
    ):
        if token not in ensure_run:
            errors.append(f"docs-snapshot.yml: failure-report fallback is missing {token}")
    if ensure_env.get("SNAPSHOT_JOB_RESULT") != "${{ needs.snapshot.result }}":
        errors.append("docs-snapshot.yml: failure report must record needs.snapshot.result")
    if "always()" not in str(ensure.get("if", "")):
        errors.append("docs-snapshot.yml: failure-report fallback must always run")
    if "always()" not in str(reconcile.get("if", "")):
        errors.append("docs-snapshot.yml: health Issue reconciliation must always run")
    if not (0 <= download_index < ensure_index < reconcile_index):
        errors.append(
            "docs-snapshot.yml: download, failure fallback, and Issue reconciliation "
            "order is unsafe"
        )
    required_safety_tokens = (
        "DISPATCH_SOURCE_REPOSITORY",
        "^[0-9a-f]{40}$",
        "^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$",
        "CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb",
        "Verify the CCB release tag resolves to the supplied SHA",
        "persist-credentials: false",
    )
    for token in required_safety_tokens:
        if token not in raw:
            errors.append(f"docs-snapshot.yml: release payload safety is missing {token}")
    policy = mapping(maintenance.get("release_snapshots"))
    if policy.get("health_issue_scope") != "scheduled_or_manual_main_only":
        errors.append("config/maintenance.yml: snapshot health Issue scope is unsafe")
    if policy.get("source_repository") != "CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb":
        errors.append("config/maintenance.yml: snapshot source repository is not authoritative CCB")
    if set(policy.get("payload_fields", [])) != {
        "source_sha",
        "source_tag",
        "source_repository",
    }:
        errors.append("config/maintenance.yml: release payload fields are incomplete")
    return errors


def validate_shared_safety() -> list[str]:
    errors: list[str] = []
    manager = (ROOT / "scripts/manage_tracking_issues.py").read_text(encoding="utf-8")
    required_rate_limit_tokens = (
        "MAX_RATE_LIMIT_RETRIES",
        "Retry-After",
        "X-RateLimit-Remaining",
        "status_code == 429",
    )
    for token in required_rate_limit_tokens:
        if token not in manager:
            errors.append(f"manage_tracking_issues.py: missing rate-limit handling token {token}")
    required_no_empty_tokens = (
        "if not updates:",
        "source drift produced no catalog changes; no branch or PR created",
        "source drift produced no file changes; no commit or PR created",
    )
    for token in required_no_empty_tokens:
        if token not in manager:
            errors.append(f"manage_tracking_issues.py: missing no-empty-PR guard: {token}")
    if "MAINTENANCE_MARKER_PREFIX" not in manager:
        errors.append("manage_tracking_issues.py: maintenance Issue marker is missing")
    return errors


def validate_governance_targets(maintenance: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    policy = mapping(maintenance.get("automation_policy"))
    if policy.get("auto_merge") is not False:
        errors.append("config/maintenance.yml: auto_merge must remain false")
    if policy.get("bot_approval") is not False:
        errors.append("config/maintenance.yml: bot_approval must remain false")
    if policy.get("empty_pull_requests") != "prohibited":
        errors.append("config/maintenance.yml: empty pull requests must be prohibited")
    if policy.get("issue_reconciliation") != "marker_deduplicated":
        errors.append("config/maintenance.yml: Issues must be marker-deduplicated")

    settings_path = ROOT / "repository-settings.target.yml"
    settings = yaml.safe_load(settings_path.read_text(encoding="utf-8"))
    if not isinstance(settings, dict):
        return errors + ["repository-settings.target.yml must contain a mapping"]
    target = mapping(settings.get("target"))
    ruleset = mapping(target.get("ruleset"))
    record = mapping(settings.get("manual_record"))
    minimum = mapping(settings.get("prerequisites")).get(
        "minimum_confirmed_human_reviewers", 2
    )
    reviewers = record.get("confirmed_reviewers", [])
    if not isinstance(reviewers, list):
        errors.append("repository settings confirmed_reviewers must be an array")
        reviewers = []
    if len(reviewers) < int(minimum):
        if settings.get("enforcement") != "deferred" or ruleset.get("enforcement") != "deferred":
            errors.append("repository Ruleset must remain deferred until two reviewers confirm")
        if record.get("protection_enabled_at") is not None:
            errors.append("repository protection cannot be recorded as enabled without reviewers")
    if target.get("actions_bot_may_approve") is not False:
        errors.append("repository target must prohibit Actions bot approval")
    if target.get("auto_merge") is not False:
        errors.append("repository target must prohibit auto-merge")
    required_ruleset_fields = (
        "require_pull_request",
        "required_non_author_human_approvals",
        "dismiss_stale_reviews",
        "require_conversation_resolution",
        "required_status_checks",
        "prohibit_force_push",
        "prohibit_branch_deletion",
    )
    for field in required_ruleset_fields:
        if field not in ruleset:
            errors.append(f"repository Ruleset target is missing {field}")
    bypass = mapping(ruleset.get("bypass"))
    if bypass.get("policy") != "emergency_only" or bypass.get("reason_required") is not True:
        errors.append("repository Ruleset bypass must be emergency-only and reason-recorded")

    workflow_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted(WORKFLOW_DIR.glob("*.yml"))
    )
    for issue_key in mapping(maintenance.get("issues")).values():
        if not isinstance(issue_key, str) or issue_key not in workflow_text:
            errors.append(f"maintenance Issue key is not reconciled by a workflow: {issue_key}")
    return errors


def validate_repository() -> list[str]:
    maintenance_path = ROOT / "config/maintenance.yml"
    maintenance = yaml.safe_load(maintenance_path.read_text(encoding="utf-8"))
    if not isinstance(maintenance, dict):
        raise WorkflowPolicyError("config/maintenance.yml must contain a mapping")
    errors: list[str] = []
    for filename, schedule_key in EXPECTED_SCHEDULES.items():
        path = WORKFLOW_DIR / filename
        if not path.is_file():
            errors.append(f"{filename}: required scheduled workflow is missing")
            continue
        errors.extend(validate_scheduled_workflow(path, schedule_key, maintenance))
    errors.extend(validate_dependabot(maintenance))
    errors.extend(validate_monthly_contracts())
    errors.extend(validate_quarterly_live_audit())
    errors.extend(validate_snapshot_workflow(maintenance))
    errors.extend(validate_shared_safety())
    errors.extend(validate_governance_targets(maintenance))
    return errors


def main() -> int:
    try:
        errors = validate_repository()
    except (OSError, ValueError, yaml.YAMLError) as error:
        print(error, file=sys.stderr)
        return 2
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    print("scheduled maintenance workflow policy passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
