#!/usr/bin/env python3
"""Check built-site links with scoped enforcement for external URLs."""

from __future__ import annotations

import argparse
import json
import posixpath
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests
import yaml
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
IGNORED_SCHEMES = {"data", "javascript", "mailto", "tel"}


@dataclass(frozen=True)
class LinkFailure:
    source: str
    url: str
    reason: str


def html_url(path: Path, site_dir: Path) -> str:
    relative = path.relative_to(site_dir).as_posix()
    if relative == "index.html":
        return "/"
    if relative.endswith("/index.html"):
        return "/" + relative[:-len("index.html")]
    return "/" + relative


def strip_site_prefix(path: str) -> str:
    for prefix in ("/CCB-Docs", "/ccb-docs"):
        if path == prefix:
            return "/"
        if path.startswith(prefix + "/"):
            return path[len(prefix):]
    return path


def target_candidates(
    source: Path,
    site_dir: Path,
    href_path: str,
) -> list[Path]:
    current_url = html_url(source, site_dir)
    decoded = unquote(href_path)
    if not decoded:
        target_url = current_url
    elif decoded.startswith("/"):
        target_url = strip_site_prefix(decoded)
    else:
        base = current_url if current_url.endswith("/") else posixpath.dirname(current_url) + "/"
        target_url = posixpath.join(base, decoded)
    normalized = posixpath.normpath(target_url).lstrip("/")
    if target_url.endswith("/") or not normalized:
        return [site_dir / normalized / "index.html"]

    site_root = site_dir.resolve()
    candidate = (site_root / normalized).resolve()
    if not candidate.is_relative_to(site_root):
        return []
    if candidate.suffix:
        return [candidate]
    return [candidate / "index.html", candidate.with_suffix(".html"), candidate]


def document_anchors(path: Path, cache: dict[Path, set[str]]) -> set[str]:
    if path not in cache:
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        anchors = {
            str(tag.get("id")) for tag in soup.find_all(attrs={"id": True})
        }
        anchors.update(
            str(tag.get("name")) for tag in soup.find_all("a", attrs={"name": True})
        )
        cache[path] = anchors
    return cache[path]


def check_internal_links(site_dir: Path) -> tuple[list[LinkFailure], set[str]]:
    failures: list[LinkFailure] = []
    external_urls: set[str] = set()
    anchor_cache: dict[Path, set[str]] = {}
    html_files = sorted(site_dir.rglob("*.html"))
    if not html_files:
        return [LinkFailure(".", ".", "site contains no HTML files")], set()

    for source in html_files:
        soup = BeautifulSoup(source.read_text(encoding="utf-8"), "html.parser")
        for tag in soup.find_all(href=True):
            href = str(tag["href"]).strip()
            if not href:
                continue
            parsed = urlsplit(href)
            if parsed.scheme in IGNORED_SCHEMES:
                continue
            if parsed.scheme in {"http", "https"} or parsed.netloc:
                external_urls.add(href)
                continue
            candidates = target_candidates(source, site_dir, parsed.path)
            target = next((path for path in candidates if path.exists()), None)
            source_name = source.relative_to(site_dir).as_posix()
            if target is None:
                failures.append(LinkFailure(source_name, href, "target does not exist"))
                continue
            if parsed.fragment and target.suffix.lower() == ".html":
                fragment = unquote(parsed.fragment)
                if fragment not in document_anchors(target, anchor_cache):
                    failures.append(
                        LinkFailure(source_name, href, "anchor does not exist")
                    )
    return failures, external_urls


def load_critical_links(path: Path) -> dict[str, str]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    links = data.get("links", []) if isinstance(data, dict) else []
    return {entry["url"]: entry["id"] for entry in links}


def request_url(session: requests.Session, url: str, timeout: float) -> str | None:
    last_reason = "request failed"
    for method in ("head", "get"):
        try:
            response = getattr(session, method)(
                url,
                timeout=timeout,
                allow_redirects=True,
                stream=True,
            )
        except requests.RequestException as error:
            last_reason = str(error)
            continue
        try:
            if 200 <= response.status_code < 400:
                return None
            last_reason = f"HTTP {response.status_code}"
        finally:
            response.close()
    return last_reason


def check_external_urls(
    urls: set[str],
    critical: dict[str, str],
    timeout: float,
) -> tuple[list[LinkFailure], list[LinkFailure]]:
    critical_failures: list[LinkFailure] = []
    ordinary_failures: list[LinkFailure] = []
    session = requests.Session()
    session.headers["User-Agent"] = "CCB-Docs-link-check/1.0"
    for url in sorted(urls):
        reason = request_url(session, url, timeout)
        if reason is None:
            continue
        identifier = critical.get(url)
        failure = LinkFailure("critical-links" if identifier else "site", url, reason)
        if identifier:
            critical_failures.append(failure)
        else:
            ordinary_failures.append(failure)
    return critical_failures, ordinary_failures


def write_report(
    path: Path,
    internal: list[LinkFailure],
    critical: list[LinkFailure],
    external: list[LinkFailure],
) -> None:
    payload = {
        "schema_version": 1,
        "internal_failures": [asdict(item) for item in internal],
        "critical_failures": [asdict(item) for item in critical],
        "external_failures": [asdict(item) for item in external],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-dir", type=Path, default=ROOT / "site")
    parser.add_argument("--critical", action="store_true")
    parser.add_argument("--external", action="store_true")
    parser.add_argument("--critical-config", type=Path, default=ROOT / "config/critical-links.yml")
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--json-output", type=Path)
    args = parser.parse_args()

    site_dir = args.site_dir.resolve()
    try:
        internal_failures, discovered = check_internal_links(site_dir)
        critical_links = load_critical_links(args.critical_config)
        urls: set[str] = set()
        if args.critical:
            urls.update(critical_links)
        if args.external:
            urls.update(discovered)
        critical_failures, external_failures = check_external_urls(
            urls,
            critical_links,
            args.timeout,
        )
        if args.json_output:
            write_report(
                args.json_output,
                internal_failures,
                critical_failures,
                external_failures,
            )
    except (OSError, KeyError, TypeError, yaml.YAMLError) as error:
        print(error, file=sys.stderr)
        return 1

    for failure in internal_failures:
        print(f"internal link failure: {failure}", file=sys.stderr)
    for failure in critical_failures:
        print(f"critical external link failure: {failure}", file=sys.stderr)
    for failure in external_failures:
        print(f"external link warning: {failure}", file=sys.stderr)
    if not internal_failures and not critical_failures:
        print("required link checks passed")
    return 1 if internal_failures or critical_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
