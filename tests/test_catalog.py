from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_catalog import validate_repository  # noqa: E402
from generate_catalog import (  # noqa: E402
    CatalogError,
    index_payload,
    load_catalog,
    validate_policy,
)


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = load_catalog()

    def test_repository_and_generated_files_match_catalog(self) -> None:
        self.assertEqual(validate_repository(self.catalog), [])

    def test_drafts_are_excluded_from_production_indexes(self) -> None:
        catalog = copy.deepcopy(self.catalog)
        for page in catalog["pages"]:
            page["status"] = "draft"
            page["include_in_search"] = False
            page["include_in_ai_index"] = False
        validate_policy(catalog)

        payload = index_payload(catalog)
        self.assertEqual(payload["navigation"], {"zh_CN": [], "en": []})
        self.assertEqual(payload["ai_index"], [])
        self.assertEqual(
            len(payload["search_exclusions"]),
            len(catalog["pages"]),
        )

    def test_new_active_page_cannot_publish_one_language_only(self) -> None:
        catalog = copy.deepcopy(self.catalog)
        catalog["pages"][0]["status"] = "draft"
        catalog["pages"][0]["include_in_search"] = False
        catalog["pages"][0]["include_in_ai_index"] = False
        with self.assertRaisesRegex(CatalogError, "both languages"):
            validate_policy(catalog)

    def test_one_language_may_be_stale_after_bilingual_publication(self) -> None:
        catalog = copy.deepcopy(self.catalog)
        catalog["pages"][0]["status"] = "stale"
        catalog["pages"][0]["include_in_ai_index"] = False

        validate_policy(catalog)

    def test_obj_lua_cannot_become_a_source_path(self) -> None:
        catalog = copy.deepcopy(self.catalog)
        catalog["pages"][0]["source_paths"] = ["obj-lua/generated/file"]
        with self.assertRaisesRegex(CatalogError, "forbidden source path"):
            validate_policy(catalog)

    def test_catalog_has_exactly_one_entry_per_id_and_language(self) -> None:
        keys = [(page["id"], page["language"]) for page in self.catalog["pages"]]
        self.assertEqual(len(keys), len(set(keys)))


if __name__ == "__main__":
    unittest.main()
