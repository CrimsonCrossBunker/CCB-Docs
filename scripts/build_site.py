#!/usr/bin/env python3
"""Build the Chinese root site and the English /en/ site from the catalog."""

from __future__ import annotations

import argparse
import copy
import shutil
import sys
from collections import OrderedDict
from pathlib import Path
from urllib.parse import urlsplit

import yaml
from mkdocs.commands.build import build
from mkdocs.config import load_config

from generate_catalog import ROOT, CatalogError, load_catalog, page_source


BUILD_ROOT = ROOT / ".build/site-source"
LANGUAGE_PREFIX = {"zh_CN": "", "en": "en"}


def language_alternates(catalog: dict) -> list[dict[str, str]]:
    """Return language-root links that work on GitHub project Pages."""
    base_path = urlsplit(catalog["site"]["base_url"]).path.rstrip("/")
    root = f"{base_path}/" if base_path else "/"
    return [
        {"name": "中文", "link": root, "lang": "zh"},
        {"name": "English", "link": f"{root}en/", "lang": "en"},
    ]


def included_pages(catalog: dict, language: str, include_drafts: bool) -> list[dict]:
    statuses = {"active", "stale"}
    if include_drafts:
        statuses.add("draft")
    return sorted(
        (
            page
            for page in catalog["pages"]
            if page["language"] == language and page["status"] in statuses
        ),
        key=lambda page: (page["nav"]["order"], page["id"]),
    )


def navigation_for(pages: list[dict]) -> list[dict]:
    """Create deterministic MkDocs navigation from catalog entries."""
    navigation: list[dict] = []
    sections: OrderedDict[str, list[dict]] = OrderedDict()
    for page in pages:
        item = {page["title"]: page["path"]}
        if page["path"] == "index.md":
            navigation.append(item)
            continue
        sections.setdefault(page["nav"]["section"], []).append(item)
    navigation.extend({section: items} for section, items in sections.items())
    return navigation


def safe_output_path(raw_path: Path) -> Path:
    path = raw_path.resolve()
    if path in {Path("/").resolve(), ROOT.resolve()}:
        raise CatalogError(f"refusing broad site output path: {path}")
    return path


def stage_language(
    catalog: dict,
    language: str,
    pages: list[dict],
    site_dir: Path,
    strict: bool,
) -> Path:
    source_dir = BUILD_ROOT / language
    source_dir.mkdir(parents=True, exist_ok=True)

    for page in pages:
        source = page_source(page)
        destination = source_dir / page["path"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    stylesheet = ROOT / "docs/stylesheets/extra.css"
    stylesheet_target = source_dir / "stylesheets/extra.css"
    stylesheet_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(stylesheet, stylesheet_target)

    if language == "zh_CN":
        for relative in ("llms.txt", "llms-full.txt"):
            source = ROOT / "docs" / relative
            destination = source_dir / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        shutil.copytree(
            ROOT / "docs/ai",
            source_dir / "ai",
            dirs_exist_ok=True,
        )
        schemas_target = source_dir / "schemas"
        shutil.copytree(ROOT / "schemas", schemas_target, dirs_exist_ok=True)

    base_config = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    config = copy.deepcopy(base_config)
    prefix = LANGUAGE_PREFIX[language]
    language_site_dir = site_dir / prefix if prefix else site_dir
    base_url = catalog["site"]["base_url"].rstrip("/") + "/"
    config.update(
        {
            "docs_dir": str(source_dir),
            "site_dir": str(language_site_dir),
            "site_url": base_url + (f"{prefix}/" if prefix else ""),
            "edit_uri": f"edit/main/docs/{language}/",
            "nav": navigation_for(pages),
            "strict": strict,
        }
    )
    config["theme"]["language"] = "zh" if language == "zh_CN" else "en"
    config.setdefault("extra", {})["alternate"] = language_alternates(catalog)
    home = next((page for page in pages if page["path"] == "index.md"), None)
    if home:
        config["site_name"] = home["title"]

    config_path = BUILD_ROOT / f"mkdocs-{language}.yml"
    config_path.write_text(
        yaml.safe_dump(config, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    mkdocs_config = load_config(config_file=str(config_path))
    build(mkdocs_config)
    return language_site_dir


def build_site(site_dir: Path, strict: bool, include_drafts: bool) -> None:
    catalog = load_catalog()
    pages_by_language = {
        language: included_pages(catalog, language, include_drafts)
        for language in catalog["site"]["languages"]
    }
    if not include_drafts and not any(pages_by_language.values()):
        raise CatalogError(
            "production site has no active or stale pages; refusing an empty deploy"
        )
    missing = [
        language for language, pages in pages_by_language.items() if not pages
    ]
    if missing:
        raise CatalogError(
            "site build has no eligible pages for language(s): " + ", ".join(missing)
        )

    output = safe_output_path(site_dir)
    if BUILD_ROOT.exists():
        shutil.rmtree(BUILD_ROOT)
    BUILD_ROOT.mkdir(parents=True)
    if output.exists():
        shutil.rmtree(output)

    for language in catalog["site"]["languages"]:
        built = stage_language(
            catalog,
            language,
            pages_by_language[language],
            output,
            strict,
        )
        print(f"built {language} site at {built}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-dir", type=Path, default=ROOT / "site")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--include-drafts", action="store_true")
    args = parser.parse_args()
    try:
        build_site(args.site_dir, args.strict, args.include_drafts)
    except (CatalogError, OSError, yaml.YAMLError) as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
