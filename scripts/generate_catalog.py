#!/usr/bin/env python3
"""Validate docs-catalog.yml and generate every derived documentation index."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "docs-catalog.yml"
LLMS_PATH = ROOT / "docs/llms.txt"
LLMS_FULL_PATH = ROOT / "docs/llms-full.txt"
JSON_INDEX_PATH = ROOT / "docs/ai/docs-index.json"
BILINGUAL_MAP_PATH = ROOT / "docs/ai/bilingual-map.json"
SEARCH_ALLOWLIST_PATH = ROOT / "docs/ai/search-allowlist.json"
AI_ALLOWLIST_PATH = ROOT / "docs/ai/ai-allowlist.json"
ARCHIVE_EXCLUSIONS_PATH = ROOT / "docs/ai/archive-exclusions.json"
REDIRECTS_PATH = ROOT / "docs/ai/redirects.json"
NAVIGATION_PATH = ROOT / "docs/ai/navigation.json"
SITEMAP_METADATA_PATH = ROOT / "docs/ai/sitemap-metadata.json"
CHUNKS_PATH = ROOT / "docs/ai/docs-chunks.jsonl"
LANGUAGES = ("zh_CN", "en")
METADATA_FIELDS = (
    "id",
    "title",
    "language",
    "status",
    "source_paths",
    "authority",
    "verified_commit",
    "verified_at",
    "generated",
    "include_in_search",
    "include_in_ai_index",
    "translation_status",
    "translation_stale_since",
    "risk_group",
    "risk_level",
    "pending_source_pr",
    "stale_reason",
    "doc_type",
    "audiences",
    "owners",
    "reviewers",
    "review_interval_days",
    "last_human_reviewer",
    "source_symbols",
    "source_queries",
    "source_fingerprint",
    "translation_source_fingerprint",
    "prerequisites",
    "depends_on",
    "redirect_from",
    "supersedes",
    "license",
    "attribution",
    "generated_by",
    "example_validation_ids",
    "api_version",
    "deprecated",
    "deprecation_replacement",
)


class CatalogError(ValueError):
    """Catalog content does not satisfy CCB-Docs policy."""


def load_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise CatalogError(f"{path.relative_to(ROOT)} must contain a mapping")
    return data


def combined_schema() -> dict:
    catalog_schema = load_json(ROOT / "schemas/docs-catalog.schema.json")
    page_schema = load_json(ROOT / "schemas/page-metadata.schema.json")
    result = copy.deepcopy(catalog_schema)
    result["properties"]["pages"]["items"]["allOf"][0] = page_schema
    return result


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_policy(catalog: dict) -> None:
    pages = catalog["pages"]
    document_ids = {page["id"] for page in pages}
    keys = [(page["id"], page["language"]) for page in pages]
    paths = [(page["language"], page["path"]) for page in pages]
    if len(keys) != len(set(keys)):
        raise CatalogError("duplicate document id/language pair")
    if len(paths) != len(set(paths)):
        raise CatalogError("two catalog entries point to the same language path")

    groups: dict[str, list[dict]] = defaultdict(list)
    redirects: dict[str, tuple[str, str]] = {}
    for page in pages:
        groups[page["translation_group"]].append(page)
        if page["translation_group"] != page["id"]:
            raise CatalogError(
                f"{page['id']} must use its stable id as translation_group"
            )
        for source_path in page["source_paths"]:
            parts = Path(source_path).parts
            if (
                Path(source_path).is_absolute()
                or ".." in parts
                or "obj-lua" in parts
            ):
                raise CatalogError(
                    f"forbidden source path for {page['id']}: {source_path}"
                )
        for source_query in page["source_queries"]:
            if any(ord(character) < 32 for character in source_query):
                raise CatalogError(
                    f"control character in source query for {page['id']}"
                )
            if "obj-lua" in Path(source_query).parts or "obj-lua/" in source_query:
                raise CatalogError(
                    f"forbidden source query for {page['id']}: {source_query}"
                )
        for source_symbol in page["source_symbols"]:
            if any(ord(character) < 32 for character in source_symbol):
                raise CatalogError(
                    f"control character in source symbol for {page['id']}"
                )
        for relation in (
            *page["prerequisites"],
            *page["depends_on"],
            *page["supersedes"],
        ):
            if relation not in document_ids:
                raise CatalogError(
                    f"{page['id']} references unknown document id {relation}"
                )
        if page["deprecated"] and not page["deprecation_replacement"]:
            raise CatalogError(
                f"deprecated page {page['id']} needs deprecation_replacement"
            )
        if page["deprecation_replacement"] not in document_ids | {None}:
            raise CatalogError(
                f"{page['id']} has unknown deprecation replacement"
            )
        if page["generated"] != bool(page["generated_by"]):
            raise CatalogError(
                f"{page['id']} generated and generated_by must agree"
            )
        if page["status"] == "archived" and page["doc_type"] != "archive":
            raise CatalogError(
                f"archived page {page['id']} must use the archive template"
            )
        if page["status"] != "archived" and page["doc_type"] == "archive":
            raise CatalogError(
                f"non-archived page {page['id']} cannot use archive doc_type"
            )
        if page["status"] in {"active", "stale"} and not page["last_human_reviewer"]:
            raise CatalogError(
                f"published page {page['id']} needs last_human_reviewer"
            )
        if page["status"] == "stale" and not page["stale_reason"]:
            raise CatalogError(f"stale page {page['id']} needs stale_reason")
        for redirect in page["redirect_from"]:
            previous = redirects.get(redirect)
            key = (page["id"], page["language"])
            if previous and previous != key:
                raise CatalogError(f"redirect {redirect} has multiple targets")
            redirects[redirect] = key
        if page["status"] in {"draft", "archived"}:
            if page["include_in_search"] or page["include_in_ai_index"]:
                raise CatalogError(
                    f"{page['id']} {page['language']} {page['status']} "
                    "must be excluded from search and AI indexes"
                )
        if page["status"] == "stale" and page["include_in_ai_index"]:
            raise CatalogError(
                f"stale page {page['id']} must be excluded from AI index"
            )
        if page.get("translation_status") == "translation-stale":
            if page["language"] != "en":
                raise CatalogError("only the English pair may be translation-stale")
            if not page.get("translation_stale_since"):
                raise CatalogError(
                    f"translation-stale page {page['id']} needs a start date"
                )
            if page["include_in_ai_index"]:
                raise CatalogError(
                    f"translation-stale page {page['id']} must leave AI index"
                )

    for group, entries in groups.items():
        languages = {entry["language"] for entry in entries}
        if languages != set(LANGUAGES):
            raise CatalogError(f"{group} must have zh_CN and en entries")
        published = [
            entry for entry in entries if entry["status"] in {"active", "stale"}
        ]
        if published and len(published) != 2:
            raise CatalogError(
                f"published page {group} must include both languages"
            )
        chinese = next(entry for entry in entries if entry["language"] == "zh_CN")
        expected_fingerprint = translation_source_fingerprint(chinese)
        for entry in entries:
            if entry["translation_source_fingerprint"] != expected_fingerprint:
                raise CatalogError(
                    f"{group} translation_source_fingerprint does not match "
                    "the Chinese source body"
                )


def load_catalog(path: Path = CATALOG_PATH) -> dict:
    catalog = load_yaml(path)
    validator = jsonschema.Draft202012Validator(
        combined_schema(), format_checker=jsonschema.FormatChecker()
    )
    errors = sorted(validator.iter_errors(catalog), key=lambda item: list(item.path))
    if errors:
        messages = [f"{'/'.join(map(str, error.path))}: {error.message}" for error in errors]
        raise CatalogError("\n".join(messages))
    validate_policy(catalog)
    return catalog


def page_source(page: dict) -> Path:
    return ROOT / "docs" / page["language"] / page["path"]


def markdown_body(content: str) -> str:
    """Return authored Markdown without catalog-generated front matter."""
    if not content.startswith("---\n"):
        return content.lstrip("\n")
    end = content.find("\n---\n", 4)
    if end < 0:
        raise CatalogError("unterminated generated front matter")
    return content[end + len("\n---\n"):].lstrip("\n")


def translation_source_fingerprint(page: dict) -> str:
    path = page_source(page)
    if not path.is_file():
        raise CatalogError(f"missing page source: {path.relative_to(ROOT)}")
    body = markdown_body(path.read_text(encoding="utf-8"))
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def public_url(catalog: dict, page: dict) -> str:
    base = catalog["site"]["base_url"].rstrip("/") + "/"
    prefix = "" if page["language"] == "zh_CN" else "en/"
    path = page["path"]
    if path == "index.md":
        suffix = ""
    elif path.endswith("/index.md"):
        suffix = path[:-len("index.md")]
    else:
        suffix = path[: -len(".md")] + "/"
    return base + prefix + suffix


def metadata_for(page: dict) -> dict:
    metadata = {field: page.get(field) for field in METADATA_FIELDS}
    if not page["include_in_search"]:
        metadata["search"] = {"exclude": True}
    return metadata


def generated_front_matter(page: dict) -> str:
    body = yaml.safe_dump(
        metadata_for(page), allow_unicode=True, sort_keys=False, width=100
    )
    return (
        "---\n"
        "# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.\n"
        f"{body}"
        "---\n\n"
    )


def replace_front_matter(content: str, front_matter: str) -> str:
    return front_matter + markdown_body(content)


def page_outputs(catalog: dict) -> dict[Path, str]:
    outputs: dict[Path, str] = {}
    for page in catalog["pages"]:
        path = page_source(page)
        if not path.is_file():
            raise CatalogError(f"missing page source: {path.relative_to(ROOT)}")
        content = path.read_text(encoding="utf-8")
        outputs[path] = replace_front_matter(
            content, generated_front_matter(page)
        )
    return outputs


def index_payload(catalog: dict) -> dict:
    pages = []
    bilingual: dict[str, dict[str, str]] = defaultdict(dict)
    navigation: dict[str, list[dict]] = {language: [] for language in LANGUAGES}
    ai_index = []
    search_allowlist = []
    search_exclusions = []
    archive_exclusions = []

    for page in catalog["pages"]:
        url = public_url(catalog, page)
        record = {
            field: page.get(field)
            for field in METADATA_FIELDS
        }
        record.update({"path": page["path"], "url": url})
        pages.append(record)
        bilingual[page["id"]][page["language"]] = url
        if page["include_in_ai_index"]:
            ai_index.append(url)
        if page["include_in_search"]:
            search_allowlist.append(url)
        if not page["include_in_search"]:
            search_exclusions.append(url)
        if page["status"] == "archived":
            archive_exclusions.append(url)
        if page["status"] in {"active", "stale"}:
            navigation[page["language"]].append(
                {
                    "id": page["id"],
                    "title": page["title"],
                    "section": page["nav"]["section"],
                    "order": page["nav"]["order"],
                    "path": page["path"],
                }
            )

    for language in LANGUAGES:
        navigation[language].sort(key=lambda item: (item["order"], item["id"]))
    pages.sort(key=lambda item: (item["id"], item["language"]))
    return {
        "schema_version": 2,
        "generated_from": "docs-catalog.yml",
        "pages": pages,
        "bilingual_map": dict(sorted(bilingual.items())),
        "ai_index": sorted(ai_index),
        "search_allowlist": sorted(search_allowlist),
        "search_exclusions": sorted(search_exclusions),
        "archive_exclusions": sorted(archive_exclusions),
        "navigation": navigation,
    }


def json_text(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def llms_full_text(catalog: dict) -> str:
    lines = [
        "# CCB Developer Documentation: full AI-approved text",
        "",
        "> Generated from docs-catalog.yml; do not edit by hand.",
        "> Only pages admitted by include_in_ai_index appear below.",
        "",
    ]
    pages = sorted(
        (page for page in catalog["pages"] if page["include_in_ai_index"]),
        key=lambda item: (item["id"], item["language"]),
    )
    for page in pages:
        body = markdown_body(page_source(page).read_text(encoding="utf-8")).rstrip()
        lines.extend(
            [
                f"## {page['id']} [{page['language']}] — {page['title']}",
                "",
                f"Source: {public_url(catalog, page)}",
                f"Verified commit: {page['verified_commit']}",
                f"License: {page['license']}",
                "",
                body,
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def chunks_text(catalog: dict) -> str:
    records = []
    for page in sorted(
        (page for page in catalog["pages"] if page["include_in_ai_index"]),
        key=lambda item: (item["id"], item["language"]),
    ):
        records.append(
            {
                "schema_version": 1,
                "chunk_id": f"{page['id']}:{page['language']}:0",
                "document_id": page["id"],
                "language": page["language"],
                "title": page["title"],
                "url": public_url(catalog, page),
                "content": markdown_body(
                    page_source(page).read_text(encoding="utf-8")
                ).strip(),
                "source_paths": page["source_paths"],
                "source_symbols": page["source_symbols"],
                "verified_commit": page["verified_commit"],
                "license": page["license"],
                "attribution": page["attribution"],
            }
        )
    return "".join(
        json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
        for record in records
    )


def derived_payloads(catalog: dict, index: dict) -> dict[Path, str]:
    pages = catalog["pages"]
    redirects = {}
    sitemap = []
    for page in pages:
        url = public_url(catalog, page)
        for old_path in page["redirect_from"]:
            redirects[old_path] = {
                "id": page["id"],
                "language": page["language"],
                "target": url,
            }
        if page["status"] not in {"active", "stale"}:
            continue
        pair = index["bilingual_map"][page["id"]]
        sitemap.append(
            {
                "id": page["id"],
                "language": page["language"],
                "url": url,
                "canonical": url,
                "last_verified": page["verified_at"],
                "alternates": pair,
                "deprecated": page["deprecated"],
            }
        )
    sitemap.sort(key=lambda item: (item["id"], item["language"]))
    return {
        BILINGUAL_MAP_PATH: json_text(index["bilingual_map"]),
        SEARCH_ALLOWLIST_PATH: json_text(index["search_allowlist"]),
        AI_ALLOWLIST_PATH: json_text(index["ai_index"]),
        ARCHIVE_EXCLUSIONS_PATH: json_text(index["archive_exclusions"]),
        REDIRECTS_PATH: json_text(dict(sorted(redirects.items()))),
        NAVIGATION_PATH: json_text(index["navigation"]),
        SITEMAP_METADATA_PATH: json_text(sitemap),
    }


def llms_text(catalog: dict) -> str:
    lines = [
        "# CCB Developer Documentation",
        "",
        "> Generated from docs-catalog.yml; do not edit by hand.",
        "> Runtime and project contracts remain authoritative in the CCB source repository.",
        "",
    ]
    included = [
        page for page in catalog["pages"] if page["include_in_ai_index"]
    ]
    if not included:
        lines.append(
            "No active pages are currently admitted to the AI index. "
            "Draft, stale, and archived pages are intentionally excluded."
        )
    else:
        for page in sorted(included, key=lambda item: (item["id"], item["language"])):
            lines.append(
                f"- [{page['language']}] {page['title']}: "
                f"{public_url(catalog, page)}"
            )
    return "\n".join(lines) + "\n"


def all_outputs(catalog: dict) -> dict[Path, str]:
    outputs = page_outputs(catalog)
    index = index_payload(catalog)
    outputs[LLMS_PATH] = llms_text(catalog)
    outputs[LLMS_FULL_PATH] = llms_full_text(catalog)
    outputs[JSON_INDEX_PATH] = json_text(index)
    outputs[CHUNKS_PATH] = chunks_text(catalog)
    outputs.update(derived_payloads(catalog, index))
    return outputs


def write_outputs(outputs: dict[Path, str], check: bool) -> int:
    stale = []
    for path, expected in outputs.items():
        actual = path.read_text(encoding="utf-8") if path.exists() else None
        if actual == expected:
            continue
        stale.append(path)
        if not check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding="utf-8")
    if check and stale:
        for path in stale:
            print(f"stale generated output: {path.relative_to(ROOT)}", file=sys.stderr)
        return 1
    action = "checked" if check else "generated"
    print(f"{action} {len(outputs)} catalog-derived files")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        catalog = load_catalog()
        return write_outputs(all_outputs(catalog), args.check)
    except (CatalogError, jsonschema.ValidationError) as error:
        print(error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
