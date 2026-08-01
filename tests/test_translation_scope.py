from __future__ import annotations

import sys
import unittest
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_catalog import overdue_blockers, translation_debts  # noqa: E402


def page(
    identifier: str,
    language: str,
    risk_group: str,
    risk_level: str = "normal",
    translation_status: str = "current",
    stale_since: str | None = None,
) -> dict:
    return {
        "id": identifier,
        "language": language,
        "status": "active",
        "risk_group": risk_group,
        "risk_level": risk_level,
        "translation_status": translation_status,
        "translation_stale_since": stale_since,
    }


class TranslationScopeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.catalog = {
            "pages": [
                page("lua.reference", "zh_CN", "lua-api", "high"),
                page(
                    "lua.reference",
                    "en",
                    "lua-api",
                    "high",
                    "translation-stale",
                    "2026-06-01",
                ),
                page("lua.guide", "zh_CN", "lua-api", "high"),
                page("lua.guide", "en", "lua-api", "high"),
                page("style.guide", "zh_CN", "style"),
                page("style.guide", "en", "style"),
            ]
        }
        self.debts = translation_debts(self.catalog, date(2026, 7, 2))

    def test_unrelated_document_change_is_not_blocked(self) -> None:
        blockers = overdue_blockers(
            self.catalog,
            self.debts,
            {("style.guide", "zh_CN")},
        )
        self.assertEqual(blockers, [])

    def test_same_bilingual_pair_is_blocked_after_deadline(self) -> None:
        blockers = overdue_blockers(
            self.catalog,
            self.debts,
            {("lua.reference", "zh_CN")},
        )
        self.assertEqual(len(blockers), 1)
        self.assertIn("bilingual pair", blockers[0])

    def test_same_high_risk_subsystem_is_blocked_after_deadline(self) -> None:
        blockers = overdue_blockers(
            self.catalog,
            self.debts,
            {("lua.guide", "en")},
        )
        self.assertEqual(len(blockers), 1)
        self.assertIn("high-risk subsystem", blockers[0])

    def test_day_thirty_is_not_overdue(self) -> None:
        debts = translation_debts(self.catalog, date(2026, 7, 1))
        self.assertFalse(debts[0].overdue)
        blockers = overdue_blockers(
            self.catalog,
            debts,
            {("lua.reference", "en")},
        )
        self.assertEqual(blockers, [])


if __name__ == "__main__":
    unittest.main()
