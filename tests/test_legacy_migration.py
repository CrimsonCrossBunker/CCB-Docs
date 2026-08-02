from __future__ import annotations

import json
import sys
import unittest
from collections import Counter
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_catalog import content_body, load_catalog, page_source  # noqa: E402
from generate_legacy_migration import (  # noqa: E402
    BLOCK_END,
    BLOCK_START,
    GENERATOR,
    HISTORY_SOURCE_PATHS,
    MigrationError,
    canonical_id,
    source_paths_for_sparse_checkout,
    validate_contributor,
)


class LegacyMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = load_catalog()
        cls.audit = json.loads(
            (ROOT / "docs/ai/legacy-migration-audit.json").read_text(
                encoding="utf-8"
            )
        )
        cls.generated = [
            page
            for page in cls.catalog["pages"]
            if page.get("generated_by") == GENERATOR
        ]

    def test_all_inventory_records_are_terminal_and_audited(self) -> None:
        schema = json.loads(
            (ROOT / "schemas/legacy-migration-audit.schema.json").read_text(
                encoding="utf-8"
            )
        )
        jsonschema.Draft202012Validator(
            schema,
            format_checker=jsonschema.FormatChecker(),
        ).validate(self.audit)
        self.assertEqual(self.audit["document_count"], 175)
        self.assertEqual(self.audit["review_count"], 0)
        self.assertEqual(self.audit["classified_count"], 0)
        self.assertEqual(self.audit["in_progress_count"], 0)
        self.assertEqual(self.audit["missing_target_count"], 0)
        self.assertEqual(self.audit["selected_record_count"], 111)
        self.assertEqual(self.audit["selected_unique_target_count"], 105)
        self.assertEqual(self.audit["preexisting_covered_record_count"], 7)
        self.assertEqual(self.audit["preexisting_unique_target_count"], 6)
        self.assertEqual(self.audit["generated_record_count"], 104)
        self.assertEqual(self.audit["generated_unique_target_count"], 99)
        self.assertEqual(
            self.audit["migration_status_counts"],
            {"archived": 7, "stubbed": 104, "verified": 64},
        )
        selected = [
            record
            for record in self.audit["records"]
            if record["migration_status"] in {"stubbed", "archived"}
        ]
        self.assertEqual(len(selected), 111)
        self.assertTrue(all(record["catalog_id"] for record in selected))

    def test_generator_owns_99_pairs_and_one_history_pair(self) -> None:
        self.assertEqual(len(self.generated), 200)
        self.assertEqual(len({page["id"] for page in self.generated}), 100)
        self.assertEqual(
            Counter(page["language"] for page in self.generated),
            Counter({"zh_CN": 100, "en": 100}),
        )
        self.assertEqual(
            Counter(page["status"] for page in self.generated),
            Counter({"draft": 186, "archived": 14}),
        )
        for page in self.generated:
            self.assertTrue(page["generated"])
            self.assertFalse(page["include_in_search"])
            self.assertFalse(page["include_in_ai_index"])
            self.assertEqual(
                page["pending_source_pr"],
                "https://github.com/CrimsonCrossBunker/"
                "Cataclysm-Cleanwater-Bomb/pull/568",
            )
            self.assertEqual(page["last_human_reviewer"], "Pending human review")

    def test_four_partial_references_have_exact_direct_counts(self) -> None:
        coverage = self.audit["generated_reference_coverage"]
        self.assertEqual(coverage["json.flags"]["json_flags"], 648)
        self.assertEqual(
            coverage["json.proficiencies-index"]["proficiencies"],
            50,
        )
        self.assertEqual(
            coverage["json.proficiencies-index"]["proficiency_categories"],
            21,
        )
        self.assertEqual(
            coverage["mods.mind-over-matter.power-reference"]
            ["mind_over_matter_spells"],
            226,
        )
        self.assertEqual(
            coverage["mods.aftershock-exoplanet.balance.ranged-weapons"]
            ["aftershock_item_definitions"],
            18,
        )
        self.assertEqual(
            coverage["mods.aftershock-exoplanet.balance.ranged-weapons"]
            ["aftershock_item_groups"],
            37,
        )
        reference_ids = set(coverage)
        for page in self.generated:
            if page["id"] not in reference_ids:
                continue
            body = content_body(page_source(page).read_text(encoding="utf-8"))
            self.assertIn("partial", body)

    def test_catalog_block_and_public_audit_exclude_anomaly_data(self) -> None:
        catalog_text = (ROOT / "docs-catalog.yml").read_text(encoding="utf-8")
        self.assertEqual(catalog_text.count(BLOCK_START), 1)
        self.assertEqual(catalog_text.count(BLOCK_END), 1)
        audit_text = json.dumps(self.audit, ensure_ascii=False)
        self.assertNotIn("contributor_anomaly", audit_text)
        self.assertNotIn("raw_rejected", audit_text)
        self.assertNotIn("obj-lua", audit_text)

    def test_canonical_id_prefers_primary_or_shared_merge_target(self) -> None:
        primary = {
            "stable_document_id": "tutorial.primary",
            "action": "migrate_rewrite",
            "merge_target": None,
        }
        merged = {
            "stable_document_id": "legacy.merged",
            "action": "merge_into",
            "merge_target": "tutorial.primary",
        }
        self.assertEqual(canonical_id([primary, merged]), "tutorial.primary")
        other = {
            "stable_document_id": "legacy.other",
            "action": "merge_into",
            "merge_target": "reference.shared",
        }
        merged["merge_target"] = "reference.shared"
        self.assertEqual(canonical_id([merged, other]), "reference.shared")

    def test_command_like_contributor_identity_is_rejected(self) -> None:
        for value in ("$(touch bad)", "name && command", "line\nfeed", "`command`"):
            with self.subTest(value=value):
                with self.assertRaises(MigrationError):
                    validate_contributor(value)

    def test_sparse_checkout_includes_history_report_sources(self) -> None:
        paths = source_paths_for_sparse_checkout(
            {"documents": []},
            {"inventory_path": "doc/migration/markdown-inventory.yml"},
        )
        self.assertTrue(set(HISTORY_SOURCE_PATHS).issubset(paths))
        self.assertNotIn("obj-lua", "\n".join(paths))


if __name__ == "__main__":
    unittest.main()
