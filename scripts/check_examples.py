#!/usr/bin/env python3
"""Extract and validate marked shell examples in catalog pages."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import yaml

from generate_catalog import ROOT, load_catalog, page_source


FENCE = re.compile(
    r"^```(?P<language>[^\s{]*)[^\n]*\n(?P<body>.*?)^```\s*$",
    re.MULTILINE | re.DOTALL,
)
MARKER = re.compile(r"^\s*#\s*validation:\s*([a-z0-9][a-z0-9-]*)\s*$", re.MULTILINE)
SHELL_LANGUAGES = {"bash", "console", "sh", "shell"}


@dataclass(frozen=True)
class Example:
    document_id: str
    language: str
    path: str
    validation_id: str
    commands: list[str]


def load_validation_ids(path: Path) -> set[str]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise ValueError("example validation registry must use schema_version 1")
    validations = data.get("validations")
    if not isinstance(validations, dict) or not validations:
        raise ValueError("example validation registry must not be empty")
    return set(validations)


def extract_examples(catalog: dict) -> tuple[list[Example], list[str]]:
    examples: list[Example] = []
    errors: list[str] = []
    for page in catalog["pages"]:
        path = page_source(page)
        content = path.read_text(encoding="utf-8")
        declared = set(page["example_validation_ids"])
        for block in FENCE.finditer(content):
            body = block.group("body")
            markers = list(MARKER.finditer(body))
            if not markers:
                continue
            relative = str(path.relative_to(ROOT))
            if block.group("language") not in SHELL_LANGUAGES:
                errors.append(f"{relative}: marked example must use a shell fence")
            for index, marker in enumerate(markers):
                validation_id = marker.group(1)
                if validation_id not in declared:
                    errors.append(
                        f"{relative}: {validation_id} is not declared in page metadata"
                    )
                segment_end = (
                    markers[index + 1].start() if index + 1 < len(markers) else len(body)
                )
                segment = body[marker.end():segment_end]
                commands = [
                    line.strip()
                    for line in segment.splitlines()
                    if line.strip() and not line.lstrip().startswith("#")
                ]
                if not commands:
                    errors.append(f"{relative}: {validation_id} example has no command")
                examples.append(
                    Example(
                        document_id=page["id"],
                        language=page["language"],
                        path=relative,
                        validation_id=validation_id,
                        commands=commands,
                    )
                )
    return examples, errors


def validate_examples(catalog: dict, known_ids: set[str]) -> tuple[list[Example], list[str]]:
    examples, errors = extract_examples(catalog)
    used = {example.validation_id for example in examples}
    declared = {
        validation_id
        for page in catalog["pages"]
        for validation_id in page["example_validation_ids"]
    }
    unknown = sorted(declared - known_ids)
    unused = sorted(declared - used)
    if unknown:
        errors.append("unknown example validation ids: " + ", ".join(unknown))
    if unused:
        errors.append("declared validation ids without a marked example: " + ", ".join(unused))
    return examples, errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--registry",
        type=Path,
        default=ROOT / "config" / "example-validations.yml",
    )
    parser.add_argument("--json-output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        catalog = load_catalog()
        known_ids = load_validation_ids(args.registry)
        examples, errors = validate_examples(catalog, known_ids)
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 2

    payload = {
        "schema_version": 1,
        "examples": [asdict(example) for example in examples],
        "errors": errors,
    }
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"validated {len(examples)} marked command examples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
