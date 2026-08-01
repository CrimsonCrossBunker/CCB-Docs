from __future__ import annotations

import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_site import (  # noqa: E402
    language_alternates,
    navigation_for,
    package_offline_site,
    safe_output_path,
    write_redirect_pages,
    write_sitemap,
)
from generate_catalog import CatalogError, load_catalog  # noqa: E402


class BuildSiteTests(unittest.TestCase):
    def test_language_alternates_keep_the_project_pages_prefix(self) -> None:
        catalog = {
            "site": {
                "base_url": "https://crimsoncrossbunker.github.io/CCB-Docs/",
            }
        }

        self.assertEqual(
            language_alternates(catalog),
            [
                {"name": "中文", "link": "/CCB-Docs/", "lang": "zh"},
                {
                    "name": "English",
                    "link": "/CCB-Docs/en/",
                    "lang": "en",
                },
            ],
        )

    def test_drafts_and_archives_do_not_enter_navigation(self) -> None:
        pages = [
            {
                "id": "active",
                "title": "Active",
                "path": "active.md",
                "status": "active",
                "nav": {"section": "Docs", "order": 1},
            },
            {
                "id": "draft",
                "title": "Draft",
                "path": "draft.md",
                "status": "draft",
                "nav": {"section": "Docs", "order": 2},
            },
            {
                "id": "archive",
                "title": "Archive",
                "path": "archive.md",
                "status": "archived",
                "nav": {"section": "Docs", "order": 3},
            },
        ]
        self.assertEqual(
            navigation_for(pages),
            [{"Docs": [{"Active": "active.md"}]}],
        )

    def test_sitemap_has_complete_bilingual_alternates(self) -> None:
        catalog = load_catalog()
        with tempfile.TemporaryDirectory() as temporary:
            path = write_sitemap(catalog, Path(temporary))
            root = ElementTree.parse(path).getroot()
        namespace = {
            "s": "http://www.sitemaps.org/schemas/sitemap/0.9",
            "x": "http://www.w3.org/1999/xhtml",
        }
        entries = root.findall("s:url", namespace)
        published = [
            page
            for page in catalog["pages"]
            if page["status"] in {"active", "stale"}
        ]
        self.assertEqual(len(entries), len(published))
        for entry in entries:
            languages = {
                link.attrib["hreflang"]
                for link in entry.findall("x:link", namespace)
            }
            self.assertEqual(languages, {"zh-CN", "en", "x-default"})

    def test_offline_zip_is_deterministic_and_self_serving(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            site = root / "site"
            site.mkdir()
            (site / "index.html").write_text("hello\n", encoding="utf-8")
            first = package_offline_site(site, root / "first.zip")
            second = package_offline_site(site, root / "second.zip")
            self.assertEqual(first.read_bytes(), second.read_bytes())
            with zipfile.ZipFile(first) as bundle:
                self.assertEqual(
                    set(bundle.namelist()),
                    {"README.txt", "serve.py", "CCB-Docs/index.html"},
                )

    def test_output_path_must_be_a_safe_repository_or_temporary_child(self) -> None:
        self.assertEqual(safe_output_path(ROOT / "site"), (ROOT / "site").resolve())
        self.assertEqual(
            safe_output_path(
                ROOT / "artifacts/offline.zip",
                output_type="archive",
            ),
            (ROOT / "artifacts/offline.zip").resolve(),
        )
        with tempfile.TemporaryDirectory() as temporary:
            child = Path(temporary) / "site"
            self.assertEqual(safe_output_path(child), child.resolve())
        for broad in (
            Path("/"),
            ROOT,
            ROOT / "docs",
            ROOT / "docs-catalog.yml",
            Path(tempfile.gettempdir()),
        ):
            with self.subTest(path=broad):
                with self.assertRaises(CatalogError):
                    safe_output_path(broad)
        with self.assertRaises(CatalogError):
            safe_output_path(
                ROOT / "docs-catalog.yml",
                output_type="archive",
            )

    def test_offline_zip_rejects_site_children_and_symlinks(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            site = root / "site"
            site.mkdir()
            (site / "index.html").write_text("hello\n", encoding="utf-8")
            with self.assertRaises(CatalogError):
                package_offline_site(site, site / "offline.zip")
            outside = root / "outside.txt"
            outside.write_text("private\n", encoding="utf-8")
            link = site / "outside.txt"
            try:
                link.symlink_to(outside)
            except OSError as error:
                self.skipTest(f"symlinks are unavailable: {error}")
            with self.assertRaises(CatalogError):
                package_offline_site(site, root / "offline.zip")

    def test_redirect_pages_use_the_catalog_language(self) -> None:
        redirects = {
            "zh_CN:/old-zh.md": "https://example.invalid/zh/",
            "en:/old-en.md": "https://example.invalid/en/",
        }
        with tempfile.TemporaryDirectory() as temporary:
            site = Path(temporary) / "site"
            site.mkdir()
            with patch(
                "build_site.index_payload",
                return_value={"redirects": redirects},
            ):
                self.assertEqual(write_redirect_pages({}, site), 2)
            zh = (site / "old-zh/index.html").read_text(encoding="utf-8")
            en = (site / "en/old-en/index.html").read_text(encoding="utf-8")
        self.assertIn('<html lang="zh-CN">', zh)
        self.assertIn('<html lang="en">', en)


if __name__ == "__main__":
    unittest.main()
