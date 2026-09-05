from __future__ import annotations

import copy
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_catalog import index_payload, load_catalog, public_url  # noqa: E402
from generate_retired_lua_pages import (  # noqa: E402
    render_body,
    synchronize,
    validate_retirement,
)


class RetiredLuaPagesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = load_catalog()
        cls.retired = [
            page for page in cls.catalog["pages"]
            if page["path"].startswith("api/lua/v5/")
        ]

    def test_old_urls_are_preserved_but_not_current_authoring_results(self) -> None:
        self.assertEqual(len(self.retired), 56)
        payload = index_payload(self.catalog)
        nav_ids = {
            page["id"] for pages in payload["navigation"].values() for page in pages
        }
        for page in self.retired:
            validate_retirement(page)
            url = public_url(self.catalog, page)
            self.assertNotIn(url, payload["search_allowlist"])
            self.assertNotIn(url, payload["ai_allowlist"])
            self.assertNotIn(page["id"], nav_ids)
            body = render_body(page)
            self.assertIn("v1/overview.md", body)
            self.assertIn('/CCB-Docs/blob/', body)
            self.assertNotIn("```lua", body)
        self.assertEqual(synchronize(self.catalog, check=True), [])

    def test_reactivating_or_indexing_retired_pages_is_rejected(self) -> None:
        for field, value in (
            ("status", "active"), ("deprecated", False),
            ("include_in_search", True), ("include_in_ai_index", True),
            ("deprecation_replacement", None),
        ):
            with self.subTest(field=field):
                page = copy.deepcopy(self.retired[0])
                page[field] = value
                with self.assertRaisesRegex(ValueError, "active metadata"):
                    validate_retirement(page)

    def test_check_does_not_rewrite_and_generation_repairs_a_stale_body(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "old.md"
            path.write_text("# Outdated tutorial\n", encoding="utf-8")
            catalog = {"pages": [self.retired[0]]}
            with patch("generate_retired_lua_pages.page_source", return_value=path):
                self.assertEqual(synchronize(catalog, check=True), [path])
                self.assertEqual(path.read_text(), "# Outdated tutorial\n")
                self.assertEqual(synchronize(catalog, check=False), [path])
                self.assertEqual(path.read_text(), render_body(self.retired[0]))

    def test_active_pages_do_not_depend_on_removed_lua_sources(self) -> None:
        retired_ids = {page["id"] for page in self.retired}
        for page in self.catalog["pages"]:
            if page["status"] != "active":
                continue
            with self.subTest(id=page["id"], language=page["language"]):
                self.assertFalse(retired_ids.intersection(page["depends_on"]))
                self.assertFalse(retired_ids.intersection(page["prerequisites"]))
                for path in page["source_paths"]:
                    self.assertNotIn("ccb_api_v5", path)
                    self.assertNotIn("catalua", path)

    def test_live_automation_has_no_removed_generator_or_runtime(self) -> None:
        for directory in (".github/workflows", "config"):
            for path in (ROOT / directory).glob("*.yml"):
                text = path.read_text(encoding="utf-8")
                for token in (
                    "generate_lua_reference.py", "generate_public_contract.py",
                    "check_ccb_inventory.py", "ccb_api_v5", "ccb_public_api_v5",
                    "CATA_ENABLE_LUA_UI", "catalua_ui", "api_v5_mod",
                ):
                    with self.subTest(path=path, token=token):
                        self.assertNotIn(token, text)

    def test_runtime_gate_rejects_crash_timeout_and_false_success(self) -> None:
        workflow = yaml.safe_load(
            (ROOT / ".github/workflows/runtime-example-mods.yml").read_text()
        )
        steps = workflow["jobs"]["runtime-examples"]["steps"]
        command = next(
            step["run"] for step in steps
            if step.get("name") == "Execute positive and negative runtime examples"
        )
        for failure_status, expected_status in ((1, 0), (0, 1), (124, 1), (134, 1)):
            with self.subTest(failure_status=failure_status), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                user = root / "user"
                target = user / "mods/ccb_docs_lua_example"
                shutil.copytree(ROOT / "examples/complete-lua-mod", target)
                (root / ".build/logs").mkdir(parents=True)
                binary = root / "fake-ccb"
                binary.write_text(
                    f"#!{sys.executable}\n"
                    "import os, pathlib, sys\n"
                    "main = pathlib.Path(os.environ['CCB_RUNTIME_USER_DIR']) / "
                    "'mods/ccb_docs_lua_example/main.lua'\n"
                    "if 'validation execution sentinel' in main.read_text():\n"
                    "    print('validation execution sentinel')\n"
                    "    sys.exit(int(os.environ['FAKE_FAILURE_STATUS']))\n"
                )
                binary.chmod(0o755)
                env = dict(os.environ, CCB_RUNTIME_USER_DIR=str(user),
                           CCB_SOURCE_DIR=str(root), CCB_RUNTIME_BINARY=str(binary),
                           GITHUB_WORKSPACE=str(ROOT), RUNTIME_COMMAND_TIMEOUT_SECONDS="5",
                           FAKE_FAILURE_STATUS=str(failure_status))
                result = subprocess.run(
                    ["bash", "-e", "-c", command], cwd=root, env=env,
                    capture_output=True, text=True, timeout=15,
                )
                self.assertEqual(result.returncode, expected_status, result.stdout + result.stderr)
                self.assertNotIn("validation execution sentinel", (target / "main.lua").read_text())


if __name__ == "__main__":
    unittest.main()
