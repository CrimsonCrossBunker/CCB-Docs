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
    GENERATED_PATHS,
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
        catalog["pages"][0]["stale_reason"] = "source review required"

        validate_policy(catalog)

    def test_obj_lua_cannot_become_a_source_path(self) -> None:
        catalog = copy.deepcopy(self.catalog)
        catalog["pages"][0]["source_paths"] = ["obj-lua/generated/file"]
        with self.assertRaisesRegex(CatalogError, "forbidden source path"):
            validate_policy(catalog)

    def test_catalog_has_exactly_one_entry_per_id_and_language(self) -> None:
        keys = [(page["id"], page["language"]) for page in self.catalog["pages"]]
        self.assertEqual(len(keys), len(set(keys)))

    def test_catalog_and_generated_indexes_are_v2(self) -> None:
        self.assertEqual(self.catalog["schema_version"], 2)
        self.assertEqual(index_payload(self.catalog)["schema_version"], 2)
        for path in GENERATED_PATHS.values():
            self.assertTrue(path.is_file(), path)

    def test_generated_page_requires_generator(self) -> None:
        catalog = copy.deepcopy(self.catalog)
        catalog["pages"][0]["generated"] = True
        with self.assertRaisesRegex(CatalogError, "needs generated_by"):
            validate_policy(catalog)

    def test_current_english_page_tracks_chinese_fingerprint(self) -> None:
        catalog = copy.deepcopy(self.catalog)
        english = next(
            page
            for page in catalog["pages"]
            if page["id"] == "home" and page["language"] == "en"
        )
        english["translation_source_fingerprint"] = "0" * 64
        with self.assertRaisesRegex(CatalogError, "fingerprint"):
            validate_policy(catalog)

    def test_page_type_templates_exist(self) -> None:
        for name in (
            "tutorial",
            "how-to",
            "reference",
            "explanation",
            "generated-api",
            "archive",
        ):
            self.assertTrue((ROOT / "templates" / f"{name}.md").is_file())


if __name__ == "__main__":
    unittest.main()
