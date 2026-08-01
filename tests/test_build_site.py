from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_site import language_alternates  # noqa: E402


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


if __name__ == "__main__":
    unittest.main()
