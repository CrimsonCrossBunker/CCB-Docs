from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from resolve_runtime_validation_source import (  # noqa: E402
    CONFIG_PATH,
    RuntimeValidationSourceError,
    load_source_config,
)


class RuntimeValidationSourceTests(unittest.TestCase):
    def test_checked_in_source_pin_is_valid(self) -> None:
        config = load_source_config()
        self.assertEqual(
            config["source_commit"],
            "747ca16a46e804986894ba9cd4c266b67c2ce124",
        )
        self.assertEqual(
            config["pending_source_pr"],
            "https://github.com/CrimsonCrossBunker/"
            "Cataclysm-Cleanwater-Bomb/pull/574",
        )
        self.assertEqual(config["build_backend"], "cmake_headless")
        self.assertEqual(config["command_timeout_seconds"], 300)

    def test_short_source_commit_is_rejected(self) -> None:
        config = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
        config["source_commit"] = "747ca16"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "runtime-example-validation.yml"
            path.write_text(yaml.safe_dump(config), encoding="utf-8")
            with self.assertRaisesRegex(
                RuntimeValidationSourceError,
                "does not match",
            ):
                load_source_config(path)

    def test_both_maintained_examples_are_required(self) -> None:
        config = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
        config["examples"] = ["ccb_lua_v5_example", "unexpected_example"]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "runtime-example-validation.yml"
            path.write_text(yaml.safe_dump(config), encoding="utf-8")
            with self.assertRaisesRegex(
                RuntimeValidationSourceError,
                "missing maintained examples",
            ):
                load_source_config(path)

    def test_timeout_too_short_for_observed_static_loading_is_rejected(self) -> None:
        config = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
        config["command_timeout_seconds"] = 120
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "runtime-example-validation.yml"
            path.write_text(yaml.safe_dump(config), encoding="utf-8")
            with self.assertRaisesRegex(
                RuntimeValidationSourceError,
                "less than the minimum of 300",
            ):
                load_source_config(path)

    def test_interactive_build_backend_is_rejected(self) -> None:
        config = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
        config["build_backend"] = "make_curses"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "runtime-example-validation.yml"
            path.write_text(yaml.safe_dump(config), encoding="utf-8")
            with self.assertRaisesRegex(
                RuntimeValidationSourceError,
                "cmake_headless.*was expected",
            ):
                load_source_config(path)


if __name__ == "__main__":
    unittest.main()
