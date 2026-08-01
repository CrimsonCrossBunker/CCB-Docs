#!/usr/bin/env python3
"""Append compact maintenance-report results to the GitHub Actions job summary."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any


def clean(value: object) -> str:
    """Return one safe, compact Markdown line for report-controlled text."""
    text = str(value).replace("\r", " ").replace("\n", " ")
    return " ".join(text.split()).replace("|", "\\|")


def load_report(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return None, str(error)
    if not isinstance(payload, dict):
        return None, "top-level JSON value is not an object"
    return payload, None


def report_identity(payload: dict[str, Any], path: Path) -> tuple[str, str, int]:
    findings = payload.get("findings")
    if isinstance(findings, list):
        return (
            str(payload.get("kind", path.stem)),
            str(payload.get("status", "unknown")),
            len(findings),
        )
    legacy_shapes = (
        ("debts", "translation-debt"),
        ("external_failures", "external-links"),
        ("stale_pages", "source-drift"),
    )
    for key, kind in legacy_shapes:
        entries = payload.get(key)
        if isinstance(entries, list):
            blockers = payload.get("blockers", [])
            blocked = isinstance(blockers, list) and bool(blockers)
            status = "failure" if blocked else ("attention" if entries else "pass")
            return kind, status, len(entries)
    return str(payload.get("kind", path.stem)), str(payload.get("status", "unknown")), 0


def render_summary(title: str, paths: list[Path]) -> str:
    lines = [f"## {clean(title)}", "", "| Report | Status | Findings |", "| --- | --- | ---: |"]
    loaded: list[tuple[Path, dict[str, Any]]] = []
    for path in paths:
        payload, error = load_report(path)
        if error:
            lines.append(f"| `{clean(path)}` | unavailable | — |")
            lines.append("")
            lines.append(f"> `{clean(path)}` could not be read: {clean(error)}")
            continue
        assert payload is not None
        kind, status, finding_count = report_identity(payload, path)
        lines.append(f"| `{clean(kind)}` | {clean(status)} | {finding_count} |")
        loaded.append((path, payload))

    for path, payload in loaded:
        findings = payload.get("findings", [])
        if not isinstance(findings, list) or not findings:
            continue
        lines.extend(["", f"### {clean(payload.get('kind', path.stem))}", ""])
        for item in findings[:20]:
            if not isinstance(item, dict):
                lines.append(f"- invalid finding: {clean(item)}")
                continue
            severity = clean(item.get("severity", "warning"))
            identity = clean(item.get("id", "finding"))
            message = clean(item.get("message", "No message supplied."))
            lines.append(f"- **{severity}** `{identity}` — {message}")
        if len(findings) > 20:
            lines.append(f"- … {len(findings) - 20} more findings are in the artifact.")
    lines.extend(
        [
            "",
            "Generated reports are evidence only; they never approve or merge changes.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", default="CCB-Docs maintenance")
    parser.add_argument("--report", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    rendered = render_summary(args.title, args.report)
    output = args.output
    if output is None and os.environ.get("GITHUB_STEP_SUMMARY"):
        output = Path(os.environ["GITHUB_STEP_SUMMARY"])
    if output is None:
        sys.stdout.write(rendered)
        return 0
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("a", encoding="utf-8") as handle:
            handle.write(rendered)
    except OSError as error:
        print(f"could not write workflow summary: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
