#!/usr/bin/env python3
"""Validate catalog coverage, generated output, and scoped translation debt."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path

import yaml

from generate_catalog import (
    ROOT,
    CatalogError,
    all_outputs,
    load_catalog,
    page_source,
)


TRANSLATION_WINDOW_DAYS = 30


@dataclass(frozen=True)
class TranslationDebt:
    id: str
    stale_since: str
    age_days: int
    overdue: bool
    risk_group: str
    risk_level: str


def catalog_page_keys(catalog: dict) -> set[tuple[str, str]]:
    return {(page["id"], page["language"]) for page in catalog["pages"]}


def validate_repository(catalog: dict) -> list[str]:
    errors: list[str] = []
    expected = {page_source(page).resolve() for page in catalog["pages"]}
    actual = {
        path.resolve()
        for language in catalog["site"]["languages"]
        for path in (ROOT / "docs" / language).rglob("*.md")
    }
    for path in sorted(expected - actual):
        errors.append(f"catalog page is missing: {path.relative_to(ROOT)}")
    for path in sorted(actual - expected):
        errors.append(f"uncatalogued page: {path.relative_to(ROOT)}")

    for path, expected_content in all_outputs(catalog).items():
        if not path.is_file():
            errors.append(f"generated file is missing: {path.relative_to(ROOT)}")
            continue
        if path.read_text(encoding="utf-8") != expected_content:
            errors.append(f"generated file is stale: {path.relative_to(ROOT)}")

    navigation_keys: dict[str, set[tuple[int, str]]] = {}
    for language in catalog["site"]["languages"]:
        entries = [
            page
            for page in catalog["pages"]
            if page["language"] == language
            and page["status"] in {"active", "stale"}
        ]
        keys = {(page["nav"]["order"], page["id"]) for page in entries}
        if len(keys) != len(entries):
            errors.append(f"duplicate navigation order/id in {language}")
        navigation_keys[language] = keys
    if len(navigation_keys.get("zh_CN", set())) != len(
        navigation_keys.get("en", set())
    ):
        errors.append("production navigation is not bilingual")
    return errors


def translation_debts(catalog: dict, today: date) -> list[TranslationDebt]:
    debts: list[TranslationDebt] = []
    for page in catalog["pages"]:
        if page["language"] != "en":
            continue
        if page["status"] not in {"active", "stale"}:
            continue
        if page.get("translation_status") != "translation-stale":
            continue
        stale_since = date.fromisoformat(page["translation_stale_since"])
        age_days = (today - stale_since).days
        debts.append(
            TranslationDebt(
                id=page["id"],
                stale_since=stale_since.isoformat(),
                age_days=age_days,
                overdue=age_days > TRANSLATION_WINDOW_DAYS,
                risk_group=page["risk_group"],
                risk_level=page["risk_level"],
            )
        )
    return sorted(debts, key=lambda debt: debt.id)


def run_git(args: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=check,
        text=True,
        capture_output=True,
    )


def changed_files_since(base_ref: str) -> set[str]:
    result = run_git(
        ["diff", "--name-only", "--diff-filter=ACMR", f"{base_ref}...HEAD"]
    )
    return {line for line in result.stdout.splitlines() if line}


def catalog_at_ref(base_ref: str) -> dict | None:
    result = run_git(["show", f"{base_ref}:docs-catalog.yml"], check=False)
    if result.returncode != 0:
        return None
    data = yaml.safe_load(result.stdout)
    return data if isinstance(data, dict) else None


def touched_page_keys(
    catalog: dict,
    changed_files: set[str],
    base_catalog: dict | None,
) -> set[tuple[str, str]]:
    path_to_key = {
        str(page_source(page).relative_to(ROOT)): (page["id"], page["language"])
        for page in catalog["pages"]
    }
    touched = {
        path_to_key[path] for path in changed_files if path in path_to_key
    }
    if "docs-catalog.yml" not in changed_files:
        return touched
    if base_catalog is None:
        return touched | catalog_page_keys(catalog)

    current = {
        (page["id"], page["language"]): page for page in catalog["pages"]
    }
    previous = {
        (page["id"], page["language"]): page
        for page in base_catalog.get("pages", [])
    }
    for key in current.keys() | previous.keys():
        if current.get(key) != previous.get(key):
            touched.add(key)
    return touched


def overdue_blockers(
    catalog: dict,
    debts: list[TranslationDebt],
    touched: set[tuple[str, str]],
) -> list[str]:
    pages = {
        (page["id"], page["language"]): page for page in catalog["pages"]
    }
    touched_risk_groups = {
        pages[key]["risk_group"] for key in touched if key in pages
    }
    blockers: list[str] = []
    for debt in debts:
        if not debt.overdue:
            continue
        pair_touched = any(key[0] == debt.id for key in touched)
        subsystem_touched = (
            debt.risk_level == "high" and debt.risk_group in touched_risk_groups
        )
        if pair_touched:
            blockers.append(
                f"{debt.id}: English translation is {debt.age_days} days stale "
                "and this pull request changes its bilingual pair"
            )
        elif subsystem_touched:
            blockers.append(
                f"{debt.id}: English translation is {debt.age_days} days stale "
                f"and this pull request changes high-risk subsystem {debt.risk_group}"
            )
    return blockers


def write_report(path: Path, debts: list[TranslationDebt], blockers: list[str]) -> None:
    payload = {
        "schema_version": 1,
        "window_days": TRANSLATION_WINDOW_DAYS,
        "debts": [asdict(debt) for debt in debts],
        "blockers": blockers,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref")
    parser.add_argument("--today", type=date.fromisoformat, default=date.today())
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--report-translation-debt", action="store_true")
    args = parser.parse_args()

    try:
        catalog = load_catalog()
        errors = validate_repository(catalog)
        debts = translation_debts(catalog, args.today)
        blockers: list[str] = []
        if args.base_ref:
            changed = changed_files_since(args.base_ref)
            touched = touched_page_keys(
                catalog,
                changed,
                catalog_at_ref(args.base_ref),
            )
            blockers = overdue_blockers(catalog, debts, touched)
        if args.json_output:
            write_report(args.json_output, debts, blockers)
    except (CatalogError, OSError, ValueError, subprocess.CalledProcessError) as error:
        print(error, file=sys.stderr)
        return 1

    for error in errors:
        print(error, file=sys.stderr)
    if args.report_translation_debt or debts:
        for debt in debts:
            state = "OVERDUE" if debt.overdue else "warning"
            print(
                f"translation {state}: {debt.id} is {debt.age_days} days stale",
                file=sys.stderr,
            )
    for blocker in blockers:
        print(f"translation scope failure: {blocker}", file=sys.stderr)
    return 1 if errors or blockers else 0


if __name__ == "__main__":
    raise SystemExit(main())
