from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_search import evaluate_case, load_cases  # noqa: E402


class SearchQualityTests(unittest.TestCase):
    def test_search_cases_are_versioned_and_bilingual(self) -> None:
        cases = load_cases(ROOT / "config/search-cases.yml")
        self.assertEqual({case["language"] for case in cases}, {"zh_CN", "en"})

    def test_fixture_terms_must_exist_at_expected_location(self) -> None:
        case = {
            "query": "authority boundaries",
            "expected_location": "architecture/project-map/",
        }
        payload = {
            "docs": [
                {
                    "location": "architecture/project-map/",
                    "title": "Authority boundaries",
                    "text": "Project map",
                }
            ]
        }
        self.assertTrue(evaluate_case(case, payload))
        case["expected_location"] = "wrong/"
        self.assertFalse(evaluate_case(case, payload))


if __name__ == "__main__":
    unittest.main()
