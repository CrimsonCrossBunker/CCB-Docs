#!/usr/bin/env python3
"""Build the Chinese root site and the English /en/ site from the catalog."""

from __future__ import annotations

import argparse
import copy
import html
import logging
import shutil
import sys
import tempfile
import zipfile
from collections import OrderedDict
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree

import yaml
from mkdocs.commands.build import build
from mkdocs.config import load_config

from generate_catalog import (
    ROOT,
    CatalogError,
    index_payload,
    load_catalog,
    page_source,
)


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
    statuses = {"active", "stale", "archived"}
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
        if page["status"] not in {"active", "stale"}:
            continue
        item = {page["title"]: page["path"]}
        if page["path"] == "index.md":
            navigation.append(item)
            continue
        sections.setdefault(page["nav"]["section"], []).append(item)
    navigation.extend({section: items} for section, items in sections.items())
    return navigation


def safe_output_path(raw_path: Path, *, output_type: str = "site") -> Path:
    """Resolve a generated output without allowing repository source deletion."""
    path = raw_path.resolve()
    repository_roots = {
        "site": (ROOT / "site").resolve(),
        "archive": (ROOT / "artifacts").resolve(),
    }
    allowed_root = repository_roots.get(output_type)
    if allowed_root is None:
        raise CatalogError(f"unknown generated output type: {output_type}")
    repository_root = ROOT.resolve()
    if path == repository_root or path.is_relative_to(repository_root):
        if path == allowed_root or path.is_relative_to(allowed_root):
            if output_type == "archive" and path == allowed_root:
                raise CatalogError("offline archive must be a file below artifacts/")
            return path
        raise CatalogError(
            f"refusing {output_type} output outside its generated root: {path}"
        )
    temporary_root = Path(tempfile.gettempdir()).resolve()
    if path != temporary_root and path.is_relative_to(temporary_root):
        return path
    raise CatalogError(f"refusing site output outside a safe child directory: {path}")


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

    javascript_dir = ROOT / "docs/javascripts"
    if javascript_dir.is_dir():
        shutil.copytree(
            javascript_dir,
            source_dir / "javascripts",
            dirs_exist_ok=True,
        )

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
    config["theme"]["custom_dir"] = str(ROOT / "overrides")
    config["plugins"] = [
        {
            "search": {
                "lang": ["zh", "en"] if language == "zh_CN" else ["en"],
                "separator": r"[\s\u200b\u3000\-、。，．？！；]+",
            }
        }
    ]
    config.setdefault("extra", {})["alternate"] = language_alternates(catalog)
    config["extra"].update(
        {
            "catalog_root_url": base_url,
            "catalog_base_path": urlsplit(base_url).path,
            "documentation_repository": catalog["site"]["documentation_repository"],
            "source_repository": catalog["site"]["source_repository"],
            "site_language": language,
        }
    )
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


def write_sitemap(catalog: dict, site_dir: Path) -> Path:
    """Write one bilingual sitemap after both language builds."""
    namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"
    xhtml = "http://www.w3.org/1999/xhtml"
    ElementTree.register_namespace("", namespace)
    ElementTree.register_namespace("xhtml", xhtml)
    root = ElementTree.Element(f"{{{namespace}}}urlset")
    for record in index_payload(catalog)["sitemap"]:
        entry = ElementTree.SubElement(root, f"{{{namespace}}}url")
        ElementTree.SubElement(entry, f"{{{namespace}}}loc").text = record["url"]
        ElementTree.SubElement(entry, f"{{{namespace}}}lastmod").text = record[
            "last_verified"
        ]
        for language, code in (("zh_CN", "zh-CN"), ("en", "en")):
            alternate = record["alternate"][language]
            ElementTree.SubElement(
                entry,
                f"{{{xhtml}}}link",
                {"rel": "alternate", "hreflang": code, "href": alternate},
            )
        ElementTree.SubElement(
            entry,
            f"{{{xhtml}}}link",
            {
                "rel": "alternate",
                "hreflang": "x-default",
                "href": record["alternate"]["zh_CN"],
            },
        )
    path = site_dir / "sitemap.xml"
    ElementTree.ElementTree(root).write(
        path,
        encoding="utf-8",
        xml_declaration=True,
    )
    return path


def redirect_output_path(site_dir: Path, old_path: str) -> Path:
    relative = old_path.lstrip("/")
    if relative.endswith(".md"):
        relative = relative[:-3]
    if relative.endswith(".html"):
        return site_dir / relative
    return site_dir / relative.rstrip("/") / "index.html"


def write_redirect_pages(catalog: dict, site_dir: Path) -> int:
    """Materialize catalog redirects without overwriting canonical pages."""
    redirects = index_payload(catalog)["redirects"]
    written = 0
    for key, target in redirects.items():
        language, old_path = key.split(":", 1)
        prefix = "en/" if language == "en" else ""
        html_language = "en" if language == "en" else "zh-CN"
        title = "Moved" if language == "en" else "已迁移"
        message = (
            "This documentation moved."
            if language == "en"
            else "本文档已迁移。"
        )
        output = redirect_output_path(site_dir, prefix + old_path.lstrip("/"))
        resolved = output.resolve()
        if site_dir.resolve() not in resolved.parents:
            raise CatalogError(f"redirect escapes site directory: {old_path}")
        if output.exists():
            raise CatalogError(f"redirect would overwrite built page: {old_path}")
        output.parent.mkdir(parents=True, exist_ok=True)
        escaped = html.escape(target, quote=True)
        output.write_text(
            "<!doctype html>\n"
            f'<html lang="{html_language}"><head><meta charset="utf-8">\n'
            f'<link rel="canonical" href="{escaped}">\n'
            f'<meta http-equiv="refresh" content="0; url={escaped}">\n'
            f'<title>{title}</title></head><body><a href="{escaped}">'
            f"{message}</a></body></html>\n",
            encoding="utf-8",
        )
        written += 1
    return written


def package_offline_site(site_dir: Path, archive: Path) -> Path:
    """Create a deterministic ZIP intended for local HTTP serving."""
    site_dir = safe_output_path(site_dir, output_type="site")
    archive = safe_output_path(archive, output_type="archive")
    if archive == site_dir or archive.is_relative_to(site_dir):
        raise CatalogError("offline archive must be outside the generated site")
    if archive.suffix.lower() != ".zip":
        raise CatalogError("offline archive must use a .zip suffix")
    archive.parent.mkdir(parents=True, exist_ok=True)
    if archive.exists():
        archive.unlink()
    readme = (
        "CCB Developer Documentation offline snapshot\n\n"
        "Extract this archive and run: python3 serve.py\n"
        "Then open http://127.0.0.1:8000/CCB-Docs/ .\n"
    )
    serve = (
        "from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler\n"
        "from pathlib import Path\n"
        "import os\n"
        "os.chdir(Path(__file__).parent)\n"
        "ThreadingHTTPServer(('127.0.0.1', 8000), "
        "SimpleHTTPRequestHandler).serve_forever()\n"
    )
    timestamp = (1980, 1, 1, 0, 0, 0)
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for name, content in (("README.txt", readme), ("serve.py", serve)):
            info = zipfile.ZipInfo(name, timestamp)
            info.external_attr = 0o644 << 16
            bundle.writestr(info, content)
        resolved_site = site_dir.resolve()
        for path in sorted(site_dir.rglob("*")):
            if path.is_symlink():
                raise CatalogError(f"offline site contains a symlink: {path}")
            if not path.is_file():
                continue
            resolved_path = path.resolve(strict=True)
            if not resolved_path.is_relative_to(resolved_site):
                raise CatalogError(f"offline site file escapes site root: {path}")
            relative = Path("CCB-Docs") / path.relative_to(site_dir)
            info = zipfile.ZipInfo(relative.as_posix(), timestamp)
            info.external_attr = 0o644 << 16
            bundle.writestr(info, resolved_path.read_bytes())
    return archive


def build_site(
    site_dir: Path,
    strict: bool,
    include_drafts: bool,
    offline_archive: Path | None = None,
) -> None:
    catalog = load_catalog()
    pages_by_language = {
        language: included_pages(catalog, language, include_drafts)
        for language in catalog["site"]["languages"]
    }
    published = [
        page
        for pages in pages_by_language.values()
        for page in pages
        if page["status"] in {"active", "stale"}
    ]
    if not include_drafts and not published:
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

    output = safe_output_path(site_dir, output_type="site")
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
    sitemap = write_sitemap(catalog, output)
    redirects = write_redirect_pages(catalog, output)
    print(f"wrote bilingual sitemap at {sitemap}")
    print(f"wrote {redirects} catalog redirect pages")
    if offline_archive:
        archive = package_offline_site(output, offline_archive)
        print(f"wrote offline snapshot at {archive}")


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-dir", type=Path, default=ROOT / "site")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--include-drafts", action="store_true")
    parser.add_argument("--offline-archive", type=Path)
    args = parser.parse_args()
    try:
        build_site(
            args.site_dir,
            args.strict,
            args.include_drafts,
            args.offline_archive,
        )
    except (CatalogError, OSError, yaml.YAMLError) as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
