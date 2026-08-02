#!/usr/bin/env python3
"""Check bilingual search configuration and deterministic query fixtures."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

from generate_catalog import ROOT, CatalogError


def load_cases(path: Path) -> list[dict]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise CatalogError("search cases must use schema_version 1")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        raise CatalogError("search cases must contain a non-empty cases list")
    return cases


def index_path(site_dir: Path, language: str) -> Path:
    prefix = Path("en") if language == "en" else Path()
    return site_dir / prefix / "search/search_index.json"


def normalized_terms(query: str) -> list[str]:
    return [part.casefold() for part in query.split() if part]


def evaluate_case(case: dict, payload: dict) -> bool:
    terms = normalized_terms(case["query"])
    for document in payload.get("docs", []):
        if document.get("location") != case["expected_location"]:
            continue
        haystack = f"{document.get('title', '')} {document.get('text', '')}".casefold()
        return all(term in haystack for term in terms)
    return False


def check_search(site_dir: Path, cases: list[dict]) -> list[str]:
    errors: list[str] = []
    payloads: dict[str, dict] = {}
    for language in {case["language"] for case in cases}:
        path = index_path(site_dir, language)
        if not path.is_file():
            errors.append(f"missing search index: {path}")
            continue
        payloads[language] = json.loads(path.read_text(encoding="utf-8"))

    chinese = payloads.get("zh_CN")
    if chinese:
        languages = chinese.get("config", {}).get("lang", [])
        if "zh" not in languages:
            errors.append("Chinese search index does not load the zh tokenizer")

    passed = 0
    for case in cases:
        payload = payloads.get(case["language"])
        if payload and evaluate_case(case, payload):
            passed += 1
        else:
            errors.append(
                f"search case {case['id']} did not find {case['expected_location']}"
            )
    print(f"bilingual search fixtures: {passed}/{len(cases)} passed")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-dir", type=Path, default=ROOT / "site")
    parser.add_argument(
        "--cases",
        type=Path,
        default=ROOT / "config/search-cases.yml",
    )
    args = parser.parse_args()
    try:
        errors = check_search(args.site_dir.resolve(), load_cases(args.cases))
    except (CatalogError, OSError, ValueError, json.JSONDecodeError) as error:
        print(error, file=sys.stderr)
        return 1
    for error in errors:
        print(error, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
