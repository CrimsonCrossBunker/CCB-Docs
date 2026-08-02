#!/usr/bin/env python3
"""Validate docs-catalog.yml and generate every derived documentation index."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "docs-catalog.yml"
LANGUAGES = ("zh_CN", "en")
GENERATED_PATHS = {
    "llms": ROOT / "docs/llms.txt",
    "llms_full": ROOT / "docs/llms-full.txt",
    "index": ROOT / "docs/ai/docs-index.json",
    "chunks": ROOT / "docs/ai/docs-chunks.jsonl",
    "bilingual": ROOT / "docs/ai/bilingual-map.json",
    "navigation": ROOT / "docs/ai/navigation.json",
    "search": ROOT / "docs/ai/search-allowlist.json",
    "ai": ROOT / "docs/ai/ai-allowlist.json",
    "archive": ROOT / "docs/ai/archive-exclusions.json",
    "redirects": ROOT / "docs/ai/redirects.json",
    "sitemap": ROOT / "docs/ai/sitemap-metadata.json",
}
METADATA_FIELDS = (
    "id",
    "title",
    "language",
    "status",
    "doc_type",
    "audiences",
    "owners",
    "reviewers",
    "review_interval_days",
    "last_human_reviewer",
    "source_paths",
    "source_symbols",
    "source_queries",
    "source_fingerprint",
    "authority",
    "verified_commit",
    "verified_at",
    "generated",
    "generated_by",
    "include_in_search",
    "include_in_ai_index",
    "translation_status",
    "translation_stale_since",
    "translation_source_fingerprint",
    "prerequisites",
    "depends_on",
    "redirect_from",
    "supersedes",
    "license",
    "attribution",
    "example_validation_ids",
    "api_version",
    "deprecated",
    "deprecation_replacement",
    "risk_group",
    "risk_level",
    "pending_source_pr",
    "stale_reason",
)
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


class CatalogError(ValueError):
    """Catalog content does not satisfy CCB-Docs policy."""


def load_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise CatalogError(f"{path.relative_to(ROOT)} must contain a mapping")
    return data


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def combined_schema() -> dict:
    catalog_schema = load_json(ROOT / "schemas/docs-catalog.schema.json")
    page_schema = load_json(ROOT / "schemas/page-metadata.schema.json")
    result = copy.deepcopy(catalog_schema)
    result["properties"]["pages"]["items"]["allOf"][0] = page_schema
    return result


def page_source(page: dict) -> Path:
    return ROOT / "docs" / page["language"] / page["path"]


def content_body(content: str) -> str:
    """Remove generated YAML front matter before hashing or indexing prose."""
    if not content.startswith("---\n"):
        return content.lstrip("\n")
    end = content.find("\n---\n", 4)
    if end < 0:
        raise CatalogError("unterminated generated front matter")
    return content[end + len("\n---\n"):].lstrip("\n")


def body_fingerprint(page: dict) -> str:
    path = page_source(page)
    if not path.is_file():
        raise CatalogError(f"missing page source: {path.relative_to(ROOT)}")
    body = content_body(path.read_text(encoding="utf-8"))
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def validate_policy(catalog: dict) -> None:
    pages = catalog["pages"]
    keys = [(page["id"], page["language"]) for page in pages]
    paths = [(page["language"], page["path"]) for page in pages]
    if len(keys) != len(set(keys)):
        raise CatalogError("duplicate document id/language pair")
    if len(paths) != len(set(paths)):
        raise CatalogError("two catalog entries point to the same language path")

    known_ids = {page["id"] for page in pages}
    redirect_owners: dict[str, tuple[str, str]] = {}
    groups: dict[str, list[dict]] = defaultdict(list)
    for page in pages:
        groups[page["translation_group"]].append(page)
        if page["translation_group"] != page["id"]:
            raise CatalogError(
                f"{page['id']} must use its stable id as translation_group"
            )
        for source_path in page["source_paths"]:
            parts = Path(source_path).parts
            if Path(source_path).is_absolute() or "obj-lua" in parts:
                raise CatalogError(
                    f"forbidden source path for {page['id']}: {source_path}"
                )
        for dependency in page["prerequisites"] + page["depends_on"]:
            if dependency not in known_ids:
                raise CatalogError(
                    f"{page['id']} references unknown dependency {dependency}"
                )
        for redirect in page["redirect_from"]:
            key = f"{page['language']}:{redirect}"
            owner = (page["id"], page["language"])
            if key in redirect_owners and redirect_owners[key] != owner:
                raise CatalogError(f"duplicate redirect path: {key}")
            redirect_owners[key] = owner
        if page["generated"] and not page.get("generated_by"):
            raise CatalogError(f"generated page {page['id']} needs generated_by")
        if not page["generated"] and page.get("generated_by") is not None:
            raise CatalogError(
                f"non-generated page {page['id']} cannot declare generated_by"
            )
        if page["status"] in {"draft", "archived"}:
            if page["include_in_search"] or page["include_in_ai_index"]:
                raise CatalogError(
                    f"{page['id']} {page['language']} {page['status']} "
                    "must be excluded from search and AI indexes"
                )
        if page["status"] == "archived" and page["doc_type"] != "archive":
            raise CatalogError(f"archived page {page['id']} must use archive doc_type")
        if page["status"] == "stale":
            if not page.get("stale_reason"):
                raise CatalogError(f"stale page {page['id']} needs stale_reason")
            if page["include_in_ai_index"]:
                raise CatalogError(f"stale page {page['id']} must leave AI index")
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
        if page["deprecated"] and not page.get("deprecation_replacement"):
            raise CatalogError(
                f"deprecated page {page['id']} needs deprecation_replacement"
            )

    for group, entries in groups.items():
        languages = {entry["language"] for entry in entries}
        if languages != set(LANGUAGES):
            raise CatalogError(f"{group} must have zh_CN and en entries")
        published = [
            entry for entry in entries if entry["status"] in {"active", "stale"}
        ]
        if published and len(published) != 2:
            raise CatalogError(f"published page {group} must include both languages")

        chinese = next(entry for entry in entries if entry["language"] == "zh_CN")
        english = next(entry for entry in entries if entry["language"] == "en")
        actual_fingerprint = body_fingerprint(chinese)
        if chinese["translation_source_fingerprint"] != actual_fingerprint:
            raise CatalogError(
                f"{group} zh_CN translation_source_fingerprint is stale"
            )
        if english["translation_status"] == "current":
            if english["translation_source_fingerprint"] != actual_fingerprint:
                raise CatalogError(
                    f"{group} English translation fingerprint does not match zh_CN"
                )


def load_catalog(path: Path = CATALOG_PATH) -> dict:
    catalog = load_yaml(path)
    validator = jsonschema.Draft202012Validator(
        combined_schema(), format_checker=jsonschema.FormatChecker()
    )
    errors = sorted(validator.iter_errors(catalog), key=lambda item: list(item.path))
    if errors:
        messages = [
            f"{'/'.join(map(str, error.path))}: {error.message}" for error in errors
        ]
        raise CatalogError("\n".join(messages))
    validate_policy(catalog)
    return catalog


def public_url(catalog: dict, page: dict) -> str:
    base = catalog["site"]["base_url"].rstrip("/") + "/"
    prefix = "" if page["language"] == "zh_CN" else "en/"
    path = page["path"]
    if path == "index.md":
        suffix = ""
    elif path.endswith("/index.md"):
        suffix = path[:-len("index.md")]
    else:
        suffix = path[:-len(".md")] + "/"
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
    return front_matter + content_body(content)


def page_outputs(catalog: dict) -> dict[Path, str]:
    outputs: dict[Path, str] = {}
    for page in catalog["pages"]:
        path = page_source(page)
        if not path.is_file():
            raise CatalogError(f"missing page source: {path.relative_to(ROOT)}")
        content = path.read_text(encoding="utf-8")
        outputs[path] = replace_front_matter(content, generated_front_matter(page))
    return outputs


def index_payload(catalog: dict) -> dict:
    pages = []
    bilingual: dict[str, dict[str, str]] = defaultdict(dict)
    navigation: dict[str, list[dict]] = {language: [] for language in LANGUAGES}
    ai_allowlist = []
    search_allowlist = []
    search_exclusions = []
    archive_exclusions = []
    redirects: dict[str, str] = {}
    sitemap = []

    for page in catalog["pages"]:
        url = public_url(catalog, page)
        record = {field: page.get(field) for field in METADATA_FIELDS}
        record.update({"path": page["path"], "url": url})
        pages.append(record)
        bilingual[page["id"]][page["language"]] = url
        if page["include_in_ai_index"]:
            ai_allowlist.append(url)
        if page["include_in_search"]:
            search_allowlist.append(url)
        else:
            search_exclusions.append(url)
        if page["status"] == "archived":
            archive_exclusions.append(url)
        for old_path in page["redirect_from"]:
            redirects[f"{page['language']}:{old_path}"] = url
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
            sitemap.append(
                {
                    "id": page["id"],
                    "language": page["language"],
                    "url": url,
                    "last_verified": page["verified_at"],
                    "status": page["status"],
                    "alternate": bilingual[page["id"]],
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
        "ai_allowlist": sorted(ai_allowlist),
        "ai_index": sorted(ai_allowlist),
        "search_allowlist": sorted(search_allowlist),
        "search_exclusions": sorted(search_exclusions),
        "archive_exclusions": sorted(archive_exclusions),
        "redirects": dict(sorted(redirects.items())),
        "navigation": navigation,
        "sitemap": sorted(sitemap, key=lambda item: (item["id"], item["language"])),
    }


def llms_text(catalog: dict) -> str:
    lines = [
        "# CCB Developer Documentation",
        "",
        "> Generated from docs-catalog.yml; do not edit by hand.",
        "> Runtime and project contracts remain authoritative in the CCB source repository.",
        "",
    ]
    included = [page for page in catalog["pages"] if page["include_in_ai_index"]]
    if not included:
        lines.append(
            "No active pages are currently admitted to the AI index. "
            "Draft, stale, and archived pages are intentionally excluded."
        )
    else:
        for page in sorted(included, key=lambda item: (item["id"], item["language"])):
            lines.append(
                f"- [{page['language']}] {page['title']}: {public_url(catalog, page)}"
            )
    return "\n".join(lines) + "\n"


def llms_full_text(catalog: dict) -> str:
    lines = [
        "# CCB Developer Documentation — full indexed text",
        "",
        "> Generated from docs-catalog.yml. Only AI-allowlisted pages are included.",
        "",
    ]
    for page in sorted(
        (item for item in catalog["pages"] if item["include_in_ai_index"]),
        key=lambda item: (item["id"], item["language"]),
    ):
        body = content_body(page_source(page).read_text(encoding="utf-8")).rstrip()
        lines.extend(
            [
                f"## {page['id']} [{page['language']}] — {page['title']}",
                "",
                f"Canonical: {public_url(catalog, page)}",
                f"Verified commit: {page['verified_commit']}",
                "Sources: " + ", ".join(page["source_paths"]),
                "",
                body,
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def markdown_chunks(catalog: dict) -> list[dict]:
    chunks: list[dict] = []
    for page in sorted(
        (item for item in catalog["pages"] if item["include_in_ai_index"]),
        key=lambda item: (item["id"], item["language"]),
    ):
        body = content_body(page_source(page).read_text(encoding="utf-8"))
        heading = page["title"]
        block: list[str] = []

        def flush() -> None:
            text = "\n".join(block).strip()
            if not text:
                return
            chunks.append(
                {
                    "id": page["id"],
                    "language": page["language"],
                    "title": page["title"],
                    "heading": heading,
                    "url": public_url(catalog, page),
                    "verified_commit": page["verified_commit"],
                    "source_paths": page["source_paths"],
                    "content": text,
                }
            )

        for line in body.splitlines():
            match = HEADING.match(line)
            if match and block:
                flush()
                block = []
            if match:
                heading = match.group(2)
            block.append(line)
        flush()
    return chunks


def json_text(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def jsonl_text(records: list[dict]) -> str:
    return "".join(
        json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n"
        for record in records
    )


def all_outputs(catalog: dict) -> dict[Path, str]:
    outputs = page_outputs(catalog)
    payload = index_payload(catalog)
    outputs[GENERATED_PATHS["llms"]] = llms_text(catalog)
    outputs[GENERATED_PATHS["llms_full"]] = llms_full_text(catalog)
    outputs[GENERATED_PATHS["index"]] = json_text(payload)
    outputs[GENERATED_PATHS["chunks"]] = jsonl_text(markdown_chunks(catalog))
    outputs[GENERATED_PATHS["bilingual"]] = json_text(payload["bilingual_map"])
    outputs[GENERATED_PATHS["navigation"]] = json_text(payload["navigation"])
    outputs[GENERATED_PATHS["search"]] = json_text(payload["search_allowlist"])
    outputs[GENERATED_PATHS["ai"]] = json_text(payload["ai_allowlist"])
    outputs[GENERATED_PATHS["archive"]] = json_text(payload["archive_exclusions"])
    outputs[GENERATED_PATHS["redirects"]] = json_text(payload["redirects"])
    outputs[GENERATED_PATHS["sitemap"]] = json_text(payload["sitemap"])
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
