from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_json_eoc_example_mod import validate_example  # noqa: E402
from generate_json_eoc_reference import (  # noqa: E402
    GENERATOR_ID,
    SPECS,
    catalog_source_commit,
    split_front_matter,
)


class JsonEocReferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = yaml.safe_load(
            (ROOT / "docs-catalog.yml").read_text(encoding="utf-8")
        )

    def test_generated_pages_are_draft_and_excluded(self) -> None:
        pages = [
            page
            for page in self.catalog["pages"]
            if page.get("generated_by") == GENERATOR_ID
        ]
        self.assertEqual(len(pages), 6)
        for page in pages:
            self.assertTrue(page["generated"])
            self.assertEqual(page["status"], "draft")
            self.assertFalse(page["include_in_search"])
            self.assertFalse(page["include_in_ai_index"])
            self.assertEqual(
                page["pending_source_pr"],
                "https://github.com/CrimsonCrossBunker/"
                "Cataclysm-Cleanwater-Bomb/pull/566",
            )

    def test_reference_pages_index_every_inventory_entry(self) -> None:
        for spec in SPECS:
            for path in spec.outputs.values():
                _, body = split_front_matter(path.read_text(encoding="utf-8"))
                markers = re.findall(
                    rf"ccb-contract-entry:{re.escape(spec.kind)}:",
                    body,
                )
                self.assertEqual(len(markers), spec.expected_count, path)

    def test_generated_pages_share_exact_source_commit(self) -> None:
        self.assertEqual(
            catalog_source_commit(),
            "a038c765568fc47a58ef8c523b2722d416f5f61c",
        )

    def test_example_fixture_uses_registered_contract_keys(self) -> None:
        inventories = {
            "json_object_types": {
                "entries": [
                    {"type": "MOD_INFO"},
                    {"type": "effect_on_condition"},
                ]
            },
            "eoc_conditions": {"entries": [{"key": "math"}]},
            "eoc_effects": {"entries": [{"key": "u_message"}]},
        }
        self.assertEqual(
            validate_example(inventories),
            ["MOD_INFO", "effect_on_condition"],
        )

    def test_catalog_source_paths_exclude_local_build_cache(self) -> None:
        for page in self.catalog["pages"]:
            for source_path in page["source_paths"]:
                self.assertNotIn("obj-lua", Path(source_path).parts)


if __name__ == "__main__":
    unittest.main()
