from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_site_quality import (  # noqa: E402
    check_contrast,
    check_markdown_alt_text,
    contrast_ratio,
)
from generate_catalog import load_catalog  # noqa: E402


class SiteQualityTests(unittest.TestCase):
    def test_wcag_contrast_formula(self) -> None:
        self.assertAlmostEqual(contrast_ratio("#000000", "#ffffff"), 21.0)

    def test_site_color_tokens_meet_wcag_aa(self) -> None:
        self.assertEqual(check_contrast(), [])

    def test_catalog_markdown_images_have_alt_text(self) -> None:
        self.assertEqual(check_markdown_alt_text(load_catalog()), [])


if __name__ == "__main__":
    unittest.main()
