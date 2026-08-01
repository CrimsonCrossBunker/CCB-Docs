from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_links import check_internal_links  # noqa: E402


class InternalLinkTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.site = Path(self.temporary.name)
        (self.site / "guide").mkdir()
        (self.site / "assets").mkdir()
        (self.site / "assets/site.css").write_text("body {}\n", encoding="utf-8")
        (self.site / "index.html").write_text(
            '<html><body id="home"><a href="guide/#answer">Guide</a>'
            '<a href="#home">Home</a><link href="assets/site.css"></body></html>',
            encoding="utf-8",
        )
        (self.site / "guide/index.html").write_text(
            '<html><body><h1 id="answer">Answer</h1>'
            '<a href="/CCB-Docs/#home">Home</a></body></html>',
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_relative_absolute_and_anchor_links_pass(self) -> None:
        failures, external = check_internal_links(self.site)
        self.assertEqual(failures, [])
        self.assertEqual(external, set())

    def test_missing_anchor_fails(self) -> None:
        (self.site / "index.html").write_text(
            '<a href="guide/#missing">Broken</a>',
            encoding="utf-8",
        )
        (self.site / "guide/index.html").write_text(
            '<h1 id="answer">Answer</h1>',
            encoding="utf-8",
        )
        failures, _ = check_internal_links(self.site)
        self.assertEqual(len(failures), 1)
        self.assertEqual(failures[0].reason, "anchor does not exist")

    def test_external_links_are_reported_separately(self) -> None:
        (self.site / "index.html").write_text(
            '<a href="https://example.invalid/docs">External</a>',
            encoding="utf-8",
        )
        (self.site / "guide/index.html").write_text(
            '<h1 id="answer">Answer</h1>',
            encoding="utf-8",
        )
        failures, external = check_internal_links(self.site)
        self.assertEqual(failures, [])
        self.assertEqual(external, {"https://example.invalid/docs"})


if __name__ == "__main__":
    unittest.main()
