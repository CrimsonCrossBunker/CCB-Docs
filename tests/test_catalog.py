from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_catalog import validate_repository  # noqa: E402
from generate_catalog import (  # noqa: E402
    AI_ALLOWLIST_PATH,
    CHUNKS_PATH,
    LLMS_FULL_PATH,
    NAVIGATION_PATH,
    REDIRECTS_PATH,
    SITEMAP_METADATA_PATH,
    CatalogError,
    all_outputs,
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
        catalog["pages"][0]["stale_reason"] = "source contract changed"

        validate_policy(catalog)

    def test_obj_lua_cannot_become_a_source_path(self) -> None:
        catalog = copy.deepcopy(self.catalog)
        catalog["pages"][0]["source_paths"] = ["obj-lua/generated/file"]
        with self.assertRaisesRegex(CatalogError, "forbidden source path"):
            validate_policy(catalog)

    def test_catalog_has_exactly_one_entry_per_id_and_language(self) -> None:
        keys = [(page["id"], page["language"]) for page in self.catalog["pages"]]
        self.assertEqual(len(keys), len(set(keys)))

    def test_catalog_v2_generates_every_machine_readable_view(self) -> None:
        self.assertEqual(self.catalog["schema_version"], 2)
        outputs = all_outputs(self.catalog)
        for path in (
            LLMS_FULL_PATH,
            CHUNKS_PATH,
            AI_ALLOWLIST_PATH,
            NAVIGATION_PATH,
            REDIRECTS_PATH,
            SITEMAP_METADATA_PATH,
        ):
            self.assertIn(path, outputs)

    def test_translation_fingerprint_must_match_chinese_body(self) -> None:
        catalog = copy.deepcopy(self.catalog)
        catalog["pages"][0]["translation_source_fingerprint"] = "0" * 64
        with self.assertRaisesRegex(CatalogError, "Chinese source body"):
            validate_policy(catalog)

    def test_generated_pages_require_a_generator(self) -> None:
        catalog = copy.deepcopy(self.catalog)
        catalog["pages"][0]["generated"] = True
        with self.assertRaisesRegex(CatalogError, "generated_by"):
            validate_policy(catalog)

    def test_unknown_dependencies_are_rejected(self) -> None:
        catalog = copy.deepcopy(self.catalog)
        catalog["pages"][0]["depends_on"] = ["missing.document"]
        with self.assertRaisesRegex(CatalogError, "unknown document id"):
            validate_policy(catalog)

    def test_all_page_templates_are_available(self) -> None:
        for name in (
            "tutorial.md",
            "how-to.md",
            "reference.md",
            "explanation.md",
            "generated-api.md",
            "archive.md",
        ):
            self.assertTrue((ROOT / "templates" / name).is_file(), name)


if __name__ == "__main__":
    unittest.main()
