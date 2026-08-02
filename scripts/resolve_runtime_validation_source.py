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
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_source_config(args.config, args.schema)
    if args.print_source_commit:
        print(config["source_commit"])
        return 0
    raise RuntimeValidationSourceError("select --print-source-commit")


if __name__ == "__main__":
    raise SystemExit(main())
