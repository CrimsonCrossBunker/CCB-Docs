#!/usr/bin/env python3
"""Create and restore-test a deterministic CCB-Docs site and metadata snapshot."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)
REQUIRED_ARCHIVE_PATHS = {
    "site/index.html",
    "site/en/index.html",
    "repository/docs-catalog.yml",
    "repository/repository-settings.target.yml",
    "snapshot-manifest.json",
}
WORKFLOW_RESULTS = {"success", "failure", "cancelled", "skipped"}


class SnapshotError(ValueError):
    """The snapshot cannot be safely created or restored."""


def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def tracked_backup_paths() -> list[str]:
    result = subprocess.run(
        [
            "git",
            "ls-files",
            "-z",
            "--",
            "docs-catalog.yml",
            "repository-settings.target.yml",
            "config",
            "schemas",
            "docs/ai",
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return sorted(path for path in result.stdout.decode("utf-8").split("\0") if path)


def source_commit() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


def snapshot_entries(site_dir: Path) -> dict[str, bytes]:
    site = site_dir.resolve()
    if not site.is_dir():
        raise SnapshotError(f"site directory does not exist: {site}")
    entries: dict[str, bytes] = {}
    for path in sorted(item for item in site.rglob("*") if item.is_file()):
        if path.is_symlink() or not path.resolve().is_relative_to(site):
            raise SnapshotError(f"site snapshot refuses external symlink: {path}")
        entries[f"site/{path.relative_to(site).as_posix()}"] = path.read_bytes()
    for relative in tracked_backup_paths():
        path = ROOT / relative
        if not path.is_file():
            raise SnapshotError(f"tracked backup file is missing: {relative}")
        if path.is_symlink():
            raise SnapshotError(f"tracked backup file must not be a symlink: {relative}")
        entries[f"repository/{relative}"] = path.read_bytes()
    return entries


def zip_info(path: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(path, FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    info.create_system = 3
    return info


def create_snapshot(site_dir: Path, output: Path, label: str) -> dict:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,127}", label):
        raise SnapshotError("snapshot label must be a safe 1-128 character slug")
    entries = snapshot_entries(site_dir)
    manifest = {
        "schema_version": 1,
        "label": label,
        "source_commit": source_commit(),
        "entries": [
            {"path": path, "bytes": len(content), "sha256": sha256(content)}
            for path, content in sorted(entries.items())
        ],
    }
    entries["snapshot-manifest.json"] = (
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    ).encode("utf-8")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path, content in sorted(entries.items()):
            archive.writestr(zip_info(path), content)
    return manifest


def safe_archive_name(name: str) -> bool:
    path = PurePosixPath(name)
    return not path.is_absolute() and ".." not in path.parts and "" not in path.parts


def verify_snapshot(path: Path) -> dict:
    if not path.is_file():
        raise SnapshotError(f"snapshot does not exist: {path}")
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise SnapshotError("snapshot contains duplicate paths")
        if not all(safe_archive_name(name) for name in names):
            raise SnapshotError("snapshot contains an unsafe path")
        missing = sorted(REQUIRED_ARCHIVE_PATHS - set(names))
        if missing:
            raise SnapshotError(f"snapshot lacks required paths: {missing}")
        manifest = json.loads(archive.read("snapshot-manifest.json"))
        if not isinstance(manifest, dict) or manifest.get("schema_version") != 1:
            raise SnapshotError("snapshot manifest must use schema_version 1")
        expected = {entry["path"]: entry for entry in manifest.get("entries", [])}
        archived_payloads = set(names) - {"snapshot-manifest.json"}
        if set(expected) != archived_payloads:
            raise SnapshotError("snapshot manifest and archive entry sets differ")
        for name, record in expected.items():
            content = archive.read(name)
            if len(content) != record["bytes"] or sha256(content) != record["sha256"]:
                raise SnapshotError(f"snapshot content hash mismatch: {name}")
        with tempfile.TemporaryDirectory() as directory:
            restore_root = Path(directory).resolve()
            for name in names:
                target = (restore_root / name).resolve()
                if not target.is_relative_to(restore_root):
                    raise SnapshotError(f"restore path escapes root: {name}")
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(archive.read(name))
            for name, record in expected.items():
                restored = (restore_root / name).read_bytes()
                if sha256(restored) != record["sha256"]:
                    raise SnapshotError(f"restored content hash mismatch: {name}")
    return {
        "label": manifest["label"],
        "source_commit": manifest["source_commit"],
        "archive_sha256": sha256(path.read_bytes()),
        "entry_count": len(expected),
        "archive_bytes": path.stat().st_size,
        "restore_test": "pass",
    }


def write_report(path: Path, status: str, summary: dict, findings: list[dict]) -> None:
    payload = {
        "schema_version": 1,
        "kind": "snapshot-restore",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "status": status,
        "summary": summary,
        "findings": findings,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def ensure_workflow_failure_report(path: Path, workflow_result: str) -> bool:
    """Create failure evidence when the snapshot job ended before reporting.

    Return True when a report was synthesized. Existing reports are authoritative
    evidence from the snapshot/restore command and are never overwritten here.
    """
    if workflow_result not in WORKFLOW_RESULTS:
        raise SnapshotError(f"invalid snapshot workflow result: {workflow_result}")
    if path.is_file():
        return False
    write_report(
        path,
        "failure",
        {
            "workflow_result": workflow_result,
            "report_recovered": True,
        },
        [
            {
                "id": "snapshot-workflow-failed",
                "severity": "error",
                "message": (
                    "The snapshot workflow ended with result "
                    f"{workflow_result!r} before producing restore-health.json."
                ),
            }
        ],
    )
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=ROOT / "site")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--label")
    parser.add_argument("--json-output", type=Path, required=True)
    parser.add_argument("--ensure-workflow-failure-report", action="store_true")
    parser.add_argument("--workflow-result", choices=sorted(WORKFLOW_RESULTS))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.ensure_workflow_failure_report:
            if not args.workflow_result:
                raise SnapshotError(
                    "--ensure-workflow-failure-report requires --workflow-result"
                )
            synthesized = ensure_workflow_failure_report(
                args.json_output,
                args.workflow_result,
            )
            action = "synthesized" if synthesized else "preserved existing"
            print(f"{action} snapshot workflow report: {args.json_output}")
            return 0
        if args.workflow_result:
            raise SnapshotError(
                "--workflow-result requires --ensure-workflow-failure-report"
            )
        if args.output is None or args.label is None:
            raise SnapshotError("snapshot creation requires --output and --label")
        create_snapshot(args.site_dir, args.output, args.label)
        summary = verify_snapshot(args.output)
    except (
        OSError,
        ValueError,
        KeyError,
        subprocess.CalledProcessError,
        zipfile.BadZipFile,
    ) as error:
        write_report(
            args.json_output,
            "failure",
            {"label": args.label, "output": str(args.output)},
            [
                {
                    "id": "snapshot-restore-failed",
                    "severity": "error",
                    "message": str(error),
                }
            ],
        )
        print(error, file=sys.stderr)
        return 1
    write_report(args.json_output, "pass", summary, [])
    print(
        f"snapshot restore passed: {summary['entry_count']} entries, "
        f"{summary['archive_bytes']} bytes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
