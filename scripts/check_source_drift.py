#!/usr/bin/env python3
"""Report pages whose declared CCB source paths changed after verification."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from generate_catalog import CatalogError, load_catalog


def git(
    repository: Path,
    args: list[str],
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repository), *args],
        check=check,
        text=True,
        capture_output=True,
    )


def commit_exists(repository: Path, commit: str) -> bool:
    result = git(repository, ["cat-file", "-e", f"{commit}^{{commit}}"], check=False)
    return result.returncode == 0


def is_ancestor(repository: Path, commit: str, target_ref: str) -> bool:
    result = git(
        repository,
        ["merge-base", "--is-ancestor", commit, target_ref],
        check=False,
    )
    return result.returncode == 0


def changed_source_paths(
    repository: Path,
    verified_commit: str,
    target_ref: str,
    source_paths: list[str],
) -> list[str]:
    result = git(
        repository,
        [
            "diff",
            "--name-only",
            "--diff-filter=ACMRD",
            f"{verified_commit}..{target_ref}",
            "--",
            *source_paths,
        ],
    )
    return sorted({line for line in result.stdout.splitlines() if line})


def detect_source_drift(
    pages: list[dict],
    source_repo: Path,
    target_ref: str,
) -> tuple[list[dict], list[dict]]:
    stale_pages: list[dict] = []
    skipped_pages: list[dict] = []
    cache: dict[tuple[str, tuple[str, ...]], list[str]] = {}
    for page in pages:
        if page["status"] in {"draft", "archived"}:
            skipped_pages.append(
                {
                    "id": page["id"],
                    "language": page["language"],
                    "reason": f"status is {page['status']}",
                }
            )
            continue
        commit = page["verified_commit"]
        if not commit_exists(source_repo, commit):
            raise CatalogError(
                f"verified commit is unavailable for {page['id']} "
                f"{page['language']}: {commit}"
            )
        if not is_ancestor(source_repo, commit, target_ref):
            raise CatalogError(
                f"verified commit is not an ancestor of {target_ref} for "
                f"{page['id']} {page['language']}: {commit}"
            )
        source_paths = tuple(page["source_paths"])
        key = (commit, source_paths)
        if key not in cache:
            cache[key] = changed_source_paths(
                source_repo,
                commit,
                target_ref,
                list(source_paths),
            )
        if cache[key]:
            stale_pages.append(
                {
                    "id": page["id"],
                    "language": page["language"],
                    "verified_commit": commit,
                    "source_paths": list(source_paths),
                    "changed_paths": cache[key],
                    "risk_group": page["risk_group"],
                    "risk_level": page["risk_level"],
                }
            )
    return stale_pages, skipped_pages


def report_payload(
    target_ref: str,
    target_commit: str,
    stale_pages: list[dict],
    skipped_pages: list[dict],
) -> dict:
    return {
        "schema_version": 1,
        "target_ref": target_ref,
        "target_commit": target_commit,
        "stale_pages": stale_pages,
        "skipped_pages": skipped_pages,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-repo", type=Path, required=True)
    parser.add_argument("--target-ref", default="HEAD")
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--fail-on-drift", action="store_true")
    args = parser.parse_args()

    try:
        catalog = load_catalog()
        source_repo = args.source_repo.resolve()
        target_commit = git(source_repo, ["rev-parse", args.target_ref]).stdout.strip()
        stale_pages, skipped_pages = detect_source_drift(
            catalog["pages"],
            source_repo,
            args.target_ref,
        )
        payload = report_payload(
            args.target_ref,
            target_commit,
            stale_pages,
            skipped_pages,
        )
        if args.json_output:
            args.json_output.parent.mkdir(parents=True, exist_ok=True)
            args.json_output.write_text(
                json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
    except (CatalogError, OSError, subprocess.CalledProcessError) as error:
        print(error, file=sys.stderr)
        return 2

    for page in stale_pages:
        print(
            f"source drift: {page['id']} {page['language']}: "
            + ", ".join(page["changed_paths"]),
            file=sys.stderr,
        )
    if not stale_pages:
        print("no source-path drift detected")
    return 1 if args.fail_on_drift and stale_pages else 0


if __name__ == "__main__":
    raise SystemExit(main())
