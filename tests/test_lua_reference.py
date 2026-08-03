from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_catalog import content_body, load_catalog, page_source  # noqa: E402
from generate_lua_reference import (  # noqa: E402
    GENERATED_MARKER,
    anchor_for,
    load_config,
)


class LuaReferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = load_config()
        cls.catalog = load_catalog()
        cls.report = json.loads(
            (ROOT / cls.config["report_path"]).read_text(encoding="utf-8")
        )

    def test_publication_report_matches_schema_and_full_denominator(self) -> None:
        schema = json.loads(
            (ROOT / "schemas/lua-v5-reference-coverage.schema.json").read_text(
                encoding="utf-8"
            )
        )
        jsonschema.Draft202012Validator(
            schema, format_checker=jsonschema.FormatChecker()
        ).validate(self.report)
        self.assertEqual(self.report["contract_public_symbols"], 2806)
        self.assertEqual(self.report["generated_reference_symbols"], 2806)
        self.assertEqual(self.report["contract_undocumented_symbols"], {"count": 0, "ids": []})
        self.assertEqual(self.report["generated_reference_coverage_percent"], 100.0)

    def test_every_symbol_has_one_stable_bilingual_target(self) -> None:
        records = self.report["symbols"]
        identities = [record["documentation_id"] for record in records]
        anchors = [record["anchor"] for record in records]
        self.assertEqual(len(identities), len(set(identities)))
        self.assertEqual(len(anchors), len(set(anchors)))
        bodies = {
            relative: content_body((ROOT / relative).read_text(encoding="utf-8"))
            for record in records
            for relative in record["paths"].values()
        }
        for record in records:
            self.assertEqual(record["anchor"], anchor_for(record["documentation_id"]))
            for language in ("zh_CN", "en"):
                relative = record["paths"][language]
                self.assertIn("#" + record["anchor"], bodies[relative])

    def test_lua_catalog_layer_is_bilingual_published_and_indexed(self) -> None:
        pages = [
            page for page in self.catalog["pages"] if page["id"].startswith("api.lua.v5.")
        ]
        self.assertEqual(len(pages), 50)
        self.assertEqual(len({page["id"] for page in pages}), 25)
        self.assertEqual({page["language"] for page in pages}, {"zh_CN", "en"})
        self.assertTrue(all(page["status"] == "active" for page in pages))
        self.assertTrue(all(page["include_in_search"] for page in pages))
        self.assertTrue(all(page["include_in_ai_index"] for page in pages))
        self.assertTrue(all(page["api_version"] == "5" for page in pages))
        self.assertTrue(
            all(page["pending_source_pr"] is None for page in pages)
        )

    def test_generator_owns_exactly_the_configured_bilingual_pages(self) -> None:
        generated_ids = {
            page["id"] for page in self.config["generated_pages"]
        } | {self.config["example_page"]["id"]}
        generated = [
            page
            for page in self.catalog["pages"]
            if page["id"] in generated_ids
        ]
        self.assertEqual(len(generated), 2 * len(generated_ids))
        for page in generated:
            self.assertTrue(page["generated"])
            self.assertEqual(page["generated_by"], "scripts/generate_lua_reference.py")
            body = content_body(page_source(page).read_text(encoding="utf-8"))
            self.assertTrue(body.startswith(GENERATED_MARKER), page["id"])

    def test_complete_example_contains_every_source_file(self) -> None:
        for language in ("zh_CN", "en"):
            page = next(
                item
                for item in self.catalog["pages"]
                if item["id"] == self.config["example_page"]["id"]
                and item["language"] == language
            )
            body = content_body(page_source(page).read_text(encoding="utf-8"))
            for source_file in self.config["example_files"]:
                self.assertIn(f"## `{source_file}`", body)

    def test_workflows_pin_the_same_source_commit(self) -> None:
        commit = self.config["source_commit"]
        for name in ("ci.yml", "pages.yml"):
            workflow = (ROOT / ".github/workflows" / name).read_text(encoding="utf-8")
            self.assertIn(f"ref: {commit}", workflow)


if __name__ == "__main__":
    unittest.main()
