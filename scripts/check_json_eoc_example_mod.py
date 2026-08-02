#!/usr/bin/env python3
"""Validate the documentation example mod against exact CCB inventories.

This check proves JSON syntax, mod structure, registered top-level types, and
the condition/effect dispatch keys used by the controlled example.  It does
not claim to replace loading the mod with a built CCB executable.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from generate_json_eoc_reference import (
    ROOT,
    ReferenceError,
    catalog_source_commit,
    load_inventories,
    run_git,
)


EXAMPLE_ROOT = ROOT / "examples/complete-json-eoc-mod"
EXPECTED_MOD_ID = "ccb_docs_json_eoc_example"
EXPECTED_EOC_ID = "EOC_CCB_DOCS_HELLO"


def load_array(path: Path) -> list[dict]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ReferenceError(f"{path.relative_to(ROOT)}: invalid JSON: {error}") from error
    if not isinstance(value, list) or not value:
        raise ReferenceError(f"{path.relative_to(ROOT)}: expected a non-empty array")
    if not all(isinstance(item, dict) for item in value):
        raise ReferenceError(f"{path.relative_to(ROOT)}: every entry must be an object")
    return value


def validate_example(inventories: dict[str, dict]) -> list[str]:
    modinfo = load_array(EXAMPLE_ROOT / "modinfo.json")
    content = load_array(EXAMPLE_ROOT / "eocs.json")
    if len(modinfo) != 1:
        raise ReferenceError("example mod must contain exactly one MOD_INFO object")
    metadata = modinfo[0]
    if metadata.get("type") != "MOD_INFO" or metadata.get("id") != EXPECTED_MOD_ID:
        raise ReferenceError("example MOD_INFO type/id does not match the maintained fixture")
    if metadata.get("dependencies") != ["dda"]:
        raise ReferenceError("example mod must declare its dda dependency explicitly")

    registered_types = {
        entry["type"] for entry in inventories["json_object_types"]["entries"]
    }
    used_types = {entry.get("type") for entry in modinfo + content}
    missing_types = sorted(value for value in used_types if value not in registered_types)
    if missing_types:
        raise ReferenceError("unregistered example object types: " + ", ".join(missing_types))

    if len(content) != 1 or content[0].get("type") != "effect_on_condition":
        raise ReferenceError("example content must contain exactly one effect_on_condition")
    eoc = content[0]
    if eoc.get("id") != EXPECTED_EOC_ID or eoc.get("eoc_type") != "ACTIVATION":
        raise ReferenceError("example EOC id/type does not match the maintained fixture")

    condition = eoc.get("condition")
    effects = eoc.get("effect")
    if not isinstance(condition, dict) or set(condition) != {"math"}:
        raise ReferenceError("example condition must use exactly the documented math key")
    if not isinstance(effects, list) or len(effects) != 1:
        raise ReferenceError("example effect must contain exactly one effect object")
    if not isinstance(effects[0], dict) or set(effects[0]) != {"u_message"}:
        raise ReferenceError("example effect must use exactly the documented u_message key")

    condition_keys = {
        entry["key"] for entry in inventories["eoc_conditions"]["entries"]
    }
    effect_keys = {entry["key"] for entry in inventories["eoc_effects"]["entries"]}
    if "math" not in condition_keys:
        raise ReferenceError("math is absent from the condition inventory")
    if "u_message" not in effect_keys:
        raise ReferenceError("u_message is absent from the effect inventory")
    return sorted(used_types)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-repo", type=Path, required=True)
    args = parser.parse_args()
    try:
        commit = catalog_source_commit()
        repository = args.source_repo.resolve()
        run_git(repository, "cat-file", "-e", f"{commit}^{{commit}}")
        inventories = load_inventories(repository, commit)
        types = validate_example(inventories)
    except (OSError, ReferenceError) as error:
        print(error, file=sys.stderr)
        return 1
    print(
        "validated complete example mod structure against CCB inventories: "
        + ", ".join(types)
    )
    print("runtime load remains a separate CCB executable/test validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
