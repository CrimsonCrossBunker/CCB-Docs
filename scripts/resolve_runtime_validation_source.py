#!/usr/bin/env python3
"""Resolve the reviewed CCB commit used for executable example validation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config/runtime-example-validation.yml"
SCHEMA_PATH = ROOT / "schemas/runtime-example-validation.schema.json"


class RuntimeValidationSourceError(ValueError):
    """The executable-example source pin violates repository policy."""


def load_source_config(
    config_path: Path = CONFIG_PATH,
    schema_path: Path = SCHEMA_PATH,
) -> dict[str, Any]:
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    try:
        jsonschema.Draft202012Validator(schema).validate(config)
    except jsonschema.ValidationError as error:
        location = ".".join(str(part) for part in error.absolute_path)
        prefix = f"{location}: " if location else ""
        raise RuntimeValidationSourceError(prefix + error.message) from error

    required_examples = {"ccb_lua_v5_example", "ccb_docs_json_eoc_example"}
    examples = set(config["examples"])
    if not required_examples.issubset(examples):
        missing = ", ".join(sorted(required_examples - examples))
        raise RuntimeValidationSourceError(f"missing maintained examples: {missing}")

    expected_trigger_paths = {
        ".github/workflows/runtime-example-mods.yml",
        "config/runtime-example-validation.yml",
        "examples/**",
        "pyproject.toml",
        "schemas/runtime-example-validation.schema.json",
        "scripts/resolve_runtime_validation_source.py",
        "uv.lock",
    }
    trigger_paths = set(config["workflow_trigger_paths"])
    if trigger_paths != expected_trigger_paths:
        missing = ", ".join(sorted(expected_trigger_paths - trigger_paths))
        unexpected = ", ".join(sorted(trigger_paths - expected_trigger_paths))
        raise RuntimeValidationSourceError(
            "runtime workflow trigger paths differ from the reviewed boundary; "
            f"missing: {missing or 'none'}; unexpected: {unexpected or 'none'}"
        )

    required_validator_paths = {
        "src/CMakeLists.txt",
        "src/lua/CMakeLists.txt",
        "src/main.cpp",
        "tools/lua_api/check_cmake_contract.py",
        "tools/lua_api/test_check_cmake_contract.py",
    }
    validator_paths = set(config["validator_paths"])
    if not required_validator_paths.issubset(validator_paths):
        missing = ", ".join(sorted(required_validator_paths - validator_paths))
        raise RuntimeValidationSourceError(
            f"missing build/runtime validator paths: {missing}"
        )
    return config


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=CONFIG_PATH,
        help="runtime validation source YAML",
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=SCHEMA_PATH,
        help="runtime validation source JSON Schema",
    )
    parser.add_argument(
        "--print-source-commit",
        action="store_true",
        help="print the reviewed full CCB commit",
    )
    parser.add_argument(
        "--print-build-backend",
        action="store_true",
        help="print the reviewed non-interactive CCB build backend",
    )
    parser.add_argument(
        "--print-command-timeout-seconds",
        action="store_true",
        help="print the bounded per-process runtime-validation timeout",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_source_config(args.config, args.schema)
    if args.print_source_commit:
        print(config["source_commit"])
        return 0
    if args.print_build_backend:
        print(config["build_backend"])
        return 0
    if args.print_command_timeout_seconds:
        print(config["command_timeout_seconds"])
        return 0
    raise RuntimeValidationSourceError(
        "select --print-source-commit, --print-build-backend, or "
        "--print-command-timeout-seconds"
    )


if __name__ == "__main__":
    raise SystemExit(main())
