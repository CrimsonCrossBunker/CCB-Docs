#!/usr/bin/env python3
"""Validate rendered metadata, accessibility basics, and color contrast."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

from generate_catalog import ROOT, load_catalog, public_url


HEX_COLOR = re.compile(r"^#[0-9a-fA-F]{6}$")
MARKDOWN_IMAGE = re.compile(r"!\[([^\]]*)\]\([^\n)]+\)")


def html_path(site_dir: Path, page: dict) -> Path:
    prefix = Path("en") if page["language"] == "en" else Path()
    path = page["path"]
    if path == "index.md":
        return site_dir / prefix / "index.html"
    if path.endswith("/index.md"):
        return site_dir / prefix / path[:-len("index.md")] / "index.html"
    return site_dir / prefix / path[:-3] / "index.html"


def relative_luminance(color: str) -> float:
    if not HEX_COLOR.match(color):
        raise ValueError(f"unsupported color: {color}")
    channels = [
        int(color[index:index + 2], 16) / 255
        for index in (1, 3, 5)
    ]

    def linear(channel: float) -> float:
        if channel <= 0.04045:
            return channel / 12.92
        return ((channel + 0.055) / 1.055) ** 2.4

    red, green, blue = (linear(channel) for channel in channels)
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def contrast_ratio(first: str, second: str) -> float:
    bright, dark = sorted(
        (relative_luminance(first), relative_luminance(second)),
        reverse=True,
    )
    return (bright + 0.05) / (dark + 0.05)


def css_variables(css: str, selector: str) -> dict[str, str]:
    pattern = re.compile(rf"{re.escape(selector)}\s*\{{(.*?)\}}", re.DOTALL)
    match = pattern.search(css)
    if not match:
        return {}
    return dict(
        re.findall(
            r"(--[a-z0-9-]+)\s*:\s*(#[0-9a-fA-F]{6})\s*;",
            match.group(1),
        )
    )


def check_contrast() -> list[str]:
    css = (ROOT / "docs/stylesheets/extra.css").read_text(encoding="utf-8")
    light = css_variables(css, ":root")
    dark = css_variables(css, "[data-md-color-scheme='slate']")
    pairs = [
        (
            "light text",
            light.get("--md-default-fg-color"),
            light.get("--md-default-bg-color"),
        ),
        (
            "light primary",
            light.get("--md-primary-fg-color"),
            light.get("--md-default-bg-color"),
        ),
        (
            "light accent",
            light.get("--md-accent-fg-color"),
            light.get("--md-default-bg-color"),
        ),
        (
            "dark text",
            dark.get("--md-default-fg-color"),
            dark.get("--md-default-bg-color"),
        ),
        (
            "dark link",
            dark.get("--md-typeset-a-color"),
            dark.get("--md-default-bg-color"),
        ),
    ]
    errors = []
    for label, foreground, background in pairs:
        if not foreground or not background:
            errors.append(f"missing contrast token for {label}")
        elif contrast_ratio(foreground, background) < 4.5:
            errors.append(f"{label} contrast is below WCAG AA")
    return errors


def check_markdown_alt_text(catalog: dict) -> list[str]:
    errors = []
    for page in catalog["pages"]:
        source = ROOT / "docs" / page["language"] / page["path"]
        content = source.read_text(encoding="utf-8")
        for match in MARKDOWN_IMAGE.finditer(content):
            if not match.group(1).strip():
                errors.append(
                    f"{source.relative_to(ROOT)} has an image without alt text"
                )
        soup = BeautifulSoup(content, "html.parser")
        for image in soup.find_all("img"):
            missing_alt = not image.get("alt", "").strip()
            if missing_alt and image.get("role") != "presentation":
                errors.append(
                    f"{source.relative_to(ROOT)} has an HTML image without alt text"
                )
    return errors


def check_rendered_page(catalog: dict, site_dir: Path, page: dict) -> list[str]:
    path = html_path(site_dir, page)
    if page["status"] == "draft" and not path.is_file():
        return []
    if not path.is_file():
        return [f"missing rendered page: {path}"]
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    errors = []
    expected = public_url(catalog, page)
    canonical = soup.select('link[rel="canonical"]')
    if len(canonical) != 1 or canonical[0].get("href") != expected:
        errors.append(f"{path}: canonical URL mismatch")
    alternates = {
        item.get("hreflang"): item.get("href")
        for item in soup.select('link[rel="alternate"][hreflang]')
    }
    if set(alternates) != {"zh", "en", "x-default"}:
        errors.append(f"{path}: incomplete hreflang mapping")
    for property_name in (
        "og:title",
        "og:description",
        "og:url",
        "og:locale",
    ):
        if not soup.select_one(f'meta[property="{property_name}"]'):
            errors.append(f"{path}: missing {property_name}")
    structured = soup.select_one('script[type="application/ld+json"]')
    try:
        payload = (
            json.loads(structured.string)
            if structured and structured.string
            else {}
        )
    except json.JSONDecodeError:
        payload = {}
    if payload.get("@type") != "TechArticle" or payload.get("url") != expected:
        errors.append(f"{path}: invalid TechArticle JSON-LD")
    if not soup.select_one(".ccb-page-provenance"):
        errors.append(f"{path}: missing source/commit provenance")
    if not soup.select_one("[data-ccb-issue-link]"):
        errors.append(f"{path}: missing page issue link")
    for image in soup.find_all("img"):
        missing_alt = not image.get("alt", "").strip()
        if missing_alt and image.get("role") != "presentation":
            errors.append(f"{path}: rendered image has no alt text")
    if page["status"] in {"draft", "stale", "archived"}:
        if not soup.select_one(f".ccb-page-banner--{page['status']}"):
            errors.append(f"{path}: missing {page['status']} banner")
    if page["generated"] and not soup.select_one(".ccb-page-banner--generated"):
        errors.append(f"{path}: missing generated banner")
    return errors


def check_site(catalog: dict, site_dir: Path) -> list[str]:
    errors = check_contrast() + check_markdown_alt_text(catalog)
    for page in catalog["pages"]:
        if page["status"] in {"active", "stale", "archived", "draft"}:
            errors.extend(check_rendered_page(catalog, site_dir, page))
    sitemap = site_dir / "sitemap.xml"
    if not sitemap.is_file():
        errors.append("bilingual sitemap is missing")
    for language in ("zh_CN", "en"):
        relative = "en/404.html" if language == "en" else "404.html"
        if not (site_dir / relative).is_file():
            errors.append(f"missing {language} 404 page")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-dir", type=Path, default=ROOT / "site")
    args = parser.parse_args()
    try:
        errors = check_site(load_catalog(), args.site_dir.resolve())
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1
    for error in errors:
        print(error, file=sys.stderr)
    if not errors:
        print("rendered metadata, alt text, and contrast checks passed")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
