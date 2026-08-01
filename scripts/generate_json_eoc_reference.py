#!/usr/bin/env python3
"""Generate bilingual JSON/EOC reference pages from CCB contract inventories.

The CCB source repository remains authoritative.  This generator reads exact
files from the catalog's verified commit with ``git show``; it never walks the
source checkout and never infers contracts from build artifacts.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "docs-catalog.yml"
GENERATOR_ID = "scripts/generate_json_eoc_reference.py"
SCHEMA_PATH = "tools/json_api/contract-inventory.schema.json"
SOURCE_BASE_URL = (
    "https://github.com/CrimsonCrossBunker/"
    "Cataclysm-Cleanwater-Bomb/blob"
)


@dataclass(frozen=True)
class InventorySpec:
    kind: str
    source_path: str
    count_key: str
    expected_count: int
    outputs: dict[str, Path]


SPECS = (
    InventorySpec(
        kind="json_object_types",
        source_path="data/reference/json/ccb_json_object_types.json",
        count_key="registered_types",
        expected_count=190,
        outputs={
            "zh_CN": ROOT / "docs/zh_CN/reference/json-object-types.md",
            "en": ROOT / "docs/en/reference/json-object-types.md",
        },
    ),
    InventorySpec(
        kind="eoc_conditions",
        source_path="data/reference/json/ccb_eoc_conditions.json",
        count_key="public_keys",
        expected_count=275,
        outputs={
            "zh_CN": ROOT / "docs/zh_CN/reference/eoc-conditions.md",
            "en": ROOT / "docs/en/reference/eoc-conditions.md",
        },
    ),
    InventorySpec(
        kind="eoc_effects",
        source_path="data/reference/json/ccb_eoc_effects.json",
        count_key="public_keys",
        expected_count=306,
        outputs={
            "zh_CN": ROOT / "docs/zh_CN/reference/eoc-effects.md",
            "en": ROOT / "docs/en/reference/eoc-effects.md",
        },
    ),
)


TEXT = {
    "zh_CN": {
        "generated": "本页由 CCB 契约清单生成，请勿手工编辑。",
        "commit": "验证提交",
        "boundary_title": "证据边界",
        "boundary": (
            "清单证明注册表、解析器分派、源码位置和已记录的示例候选；"
            "它不等于完整游戏 JSON Schema。`partial`、`unclassified`、"
            "`unknown` 和 `lexical_only` 都是有意保留的未知信息。"
        ),
        "source": "机器来源",
        "json_title": "JSON 对象类型注册表",
        "json_intro": (
            "下表覆盖当前清单中的全部 190 个已注册对象类型。191 次注册包含"
            "一个编译条件变体；类型数量按唯一 `type` 计算。"
        ),
        "condition_title": "EOC 条件注册表",
        "condition_intro": "下表覆盖解析器清单中的全部 275 个公开条件键。",
        "effect_title": "EOC 效果注册表",
        "effect_intro": "下表覆盖解析器清单中的全部 306 个公开效果键。",
        "json_headers": (
            "类型",
            "契约",
            "加载器",
            "字段证据",
            "Schema",
            "实例",
            "文档证据",
            "源码",
        ),
        "eoc_headers": (
            "键",
            "语法 / JSON 形状",
            "处理器",
            "分类状态",
            "Talker",
            "示例候选",
            "文档证据",
            "源码",
        ),
        "legend": (
            "分类状态顺序：`params` 参数、`values` 值类型、`defaults` 默认值、"
            "`nesting` 嵌套、`vars` 变量、`context` 上下文。`u_`/`npc_` 仅是"
            "历史 alpha/beta 路由别名，不能单独证明具体运行时 talker 类型。"
        ),
        "none": "无",
        "occurrences": "次词法命中",
    },
    "en": {
        "generated": "Generated from CCB contract inventories; do not edit by hand.",
        "commit": "Verified commit",
        "boundary_title": "Evidence boundary",
        "boundary": (
            "The inventories prove registry/parser dispatch, source locations, and "
            "recorded example candidates. They are not a complete game JSON Schema. "
            "`partial`, `unclassified`, `unknown`, and `lexical_only` preserve known "
            "unknowns intentionally."
        ),
        "source": "Machine source",
        "json_title": "JSON object-type registry",
        "json_intro": (
            "This table indexes all 190 unique registered object types in the current "
            "inventory. The 191 registration calls include one compile-conditional "
            "variant."
        ),
        "condition_title": "EOC condition registry",
        "condition_intro": (
            "This table indexes all 275 public condition keys in the parser inventory."
        ),
        "effect_title": "EOC effect registry",
        "effect_intro": "This table indexes all 306 public effect keys in the parser inventory.",
        "json_headers": (
            "Type",
            "Contract",
            "Loader",
            "Field evidence",
            "Schema",
            "Instances",
            "Documentation evidence",
            "Source",
        ),
        "eoc_headers": (
            "Key",
            "Syntax / JSON shape",
            "Handler",
            "Classification",
            "Talker",
            "Example candidate",
            "Documentation evidence",
            "Source",
        ),
        "legend": (
            "Classification order: `params`, `values`, `defaults`, `nesting`, `vars`, "
            "and `context`. `u_`/`npc_` are legacy alpha/beta routing aliases; they do "
            "not by themselves prove a concrete runtime talker type."
        ),
        "none": "none",
        "occurrences": "lexical hits",
    },
}


class ReferenceError(ValueError):
    """Source inventory or catalog metadata is inconsistent."""


def run_git(repository: Path, *args: str) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(repository), *args],
        check=False,
        capture_output=True,
    )
    if result.returncode:
        message = result.stderr.decode("utf-8", errors="replace").strip()
        raise ReferenceError(message or f"git {' '.join(args)} failed")
    return result.stdout


def git_show(repository: Path, commit: str, path: str) -> bytes:
    return run_git(repository, "show", f"{commit}:{path}")


def catalog_source_commit() -> str:
    catalog = yaml.safe_load(CATALOG_PATH.read_text(encoding="utf-8"))
    pages = [
        page
        for page in catalog.get("pages", [])
        if page.get("generated_by") == GENERATOR_ID
    ]
    if not pages:
        raise ReferenceError(f"no catalog pages declare generated_by: {GENERATOR_ID}")
    commits = {page.get("verified_commit") for page in pages}
    if len(commits) != 1 or None in commits:
        raise ReferenceError("JSON/EOC generated pages must share one verified_commit")
    return commits.pop()


def load_source_json(repository: Path, commit: str, path: str) -> dict:
    try:
        value = json.loads(git_show(repository, commit, path))
    except json.JSONDecodeError as error:
        raise ReferenceError(f"{path}: invalid JSON: {error}") from error
    if not isinstance(value, dict):
        raise ReferenceError(f"{path}: expected a JSON object")
    return value


def validate_inventory(
    inventory: dict,
    schema: dict,
    spec: InventorySpec,
) -> None:
    validator = jsonschema.Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(inventory), key=lambda item: list(item.path))
    if errors:
        detail = "; ".join(
            f"{'/'.join(map(str, error.path))}: {error.message}" for error in errors[:10]
        )
        raise ReferenceError(f"{spec.source_path}: inventory Schema failure: {detail}")
    if inventory.get("inventory_kind") != spec.kind:
        raise ReferenceError(f"{spec.source_path}: inventory_kind mismatch")
    entries = inventory.get("entries", [])
    if len(entries) != spec.expected_count:
        raise ReferenceError(
            f"{spec.kind}: expected {spec.expected_count} entries, found {len(entries)}"
        )
    summary_count = inventory.get("summary", {}).get(spec.count_key)
    if summary_count != spec.expected_count:
        raise ReferenceError(
            f"{spec.kind}: summary {spec.count_key} is {summary_count}, "
            f"expected {spec.expected_count}"
        )
    key_name = "type" if spec.kind == "json_object_types" else "key"
    keys = [entry[key_name] for entry in entries]
    if len(keys) != len(set(keys)):
        duplicates = sorted(key for key, count in Counter(keys).items() if count > 1)
        raise ReferenceError(f"{spec.kind}: duplicate keys: {', '.join(duplicates)}")
    if keys != sorted(keys):
        raise ReferenceError(f"{spec.kind}: entries must use deterministic key order")
    if spec.kind == "json_object_types":
        registrations = sum(len(entry["registrations"]) for entry in entries)
        declared = inventory["summary"].get("registration_calls")
        if registrations != 191 or declared != 191:
            raise ReferenceError(
                f"json_object_types: expected 191 registration calls, "
                f"found {registrations} (summary {declared})"
            )


def load_inventories(repository: Path, commit: str) -> dict[str, dict]:
    schema = load_source_json(repository, commit, SCHEMA_PATH)
    inventories = {}
    for spec in SPECS:
        inventory = load_source_json(repository, commit, spec.source_path)
        validate_inventory(inventory, schema, spec)
        inventories[spec.kind] = inventory
    return inventories


def code(value: object) -> str:
    return f"<code>{html.escape(str(value), quote=True)}</code>"


def cell(value: object) -> str:
    return str(value).replace("|", "&#124;").replace("\n", " ")


def joined_code(values: list[object], empty: str) -> str:
    return ", ".join(code(value) for value in values) if values else empty


def source_link(commit: str, source: dict) -> str:
    path = source["path"]
    line = source["line"]
    url = f"{SOURCE_BASE_URL}/{commit}/{path}#L{line}"
    label = code(f"{path}:{line}")
    return f"[{label}]({url})"


def data_reference(commit: str, evidence: dict, language: str) -> str:
    examples = evidence.get("examples", [])
    if not examples:
        return TEXT[language]["none"]
    example = examples[0]
    path = example["path"]
    pointer = example["pointer"] or "/"
    url = f"{SOURCE_BASE_URL}/{commit}/{path}"
    occurrences = evidence.get("occurrences", 0)
    return (
        f"[{code(path)}]({url}) {code(pointer)}; "
        f"{occurrences} {TEXT[language]['occurrences']} ({code('lexical_only')})"
    )


def documentation_reference(commit: str, documentation: dict, language: str) -> str:
    evidence = documentation.get("evidence", [])
    if not evidence:
        return code(documentation.get("status", TEXT[language]["none"]))
    item = evidence[0]
    url = f"{SOURCE_BASE_URL}/{commit}/{item['path']}#L{item['line']}"
    label = code(f"{item['path']}:{item['line']}")
    return (
        f"{code(documentation['status'])}: "
        f"[{label}]({url}) "
        f"({code(documentation['confidence'])})"
    )


def json_fields(entry: dict, language: str) -> str:
    contract = entry["field_contract"]
    status = contract["status"]
    if status == "unclassified":
        return code(status)
    fields = contract.get("fields", [])
    details = []
    for field in fields:
        required = "required" if field["required"] else "optional"
        details.append(f"{code(field['name'])} ({required})")
    if not details:
        return code(status)
    return f"{code(status)}: " + ", ".join(details)


def render_json_table(inventory: dict, language: str, commit: str) -> list[str]:
    headers = TEXT[language]["json_headers"]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for entry in inventory["entries"]:
        registrations = entry["registrations"]
        handlers = [
            registration.get("handler_symbol") or registration["handler_expression"]
            for registration in registrations
        ]
        sources = [source_link(commit, item["source"]) for item in registrations]
        schema = entry["schema"]
        schema_text = code(schema["status"])
        if schema.get("paths"):
            schema_text += ": " + joined_code(schema["paths"], TEXT[language]["none"])
        marker = f"<!-- ccb-contract-entry:{inventory['inventory_kind']}:{entry['type']} -->"
        lines.append(
            "| "
            + " | ".join(
                cell(value)
                for value in (
                    marker + code(entry["type"]),
                    code(entry["contract_status"]),
                    joined_code(handlers, TEXT[language]["none"]),
                    json_fields(entry, language),
                    schema_text,
                    data_reference(commit, entry["instance_evidence"], language),
                    documentation_reference(commit, entry["documentation"], language),
                    "<br>".join(sources),
                )
            )
            + " |"
        )
    return lines


def classification(entry: dict) -> str:
    fields = (
        ("params", "parameters"),
        ("values", "value_types"),
        ("defaults", "defaults"),
        ("nesting", "nesting"),
        ("vars", "variables"),
        ("context", "context"),
    )
    return "; ".join(f"{name}={code(entry[key]['status'])}" for name, key in fields)


def render_eoc_table(inventory: dict, language: str, commit: str) -> list[str]:
    headers = TEXT[language]["eoc_headers"]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for entry in inventory["entries"]:
        registrations = entry["parser_registrations"]
        sources = [source_link(commit, item["source"]) for item in registrations]
        syntax = joined_code(entry["syntaxes"], TEXT[language]["none"])
        shapes = joined_code(entry["accepted_json_shapes"], TEXT[language]["none"])
        marker = f"<!-- ccb-contract-entry:{inventory['inventory_kind']}:{entry['key']} -->"
        lines.append(
            "| "
            + " | ".join(
                cell(value)
                for value in (
                    marker + code(entry["key"]),
                    f"{syntax}<br>{shapes}",
                    joined_code(entry["handlers"], TEXT[language]["none"]),
                    f"{code(entry['contract_status'])}; {classification(entry)}",
                    code(entry["talker_semantics"]["status"]),
                    data_reference(commit, entry["example_evidence"], language),
                    documentation_reference(commit, entry["documentation"], language),
                    "<br>".join(sources),
                )
            )
            + " |"
        )
    return lines


def render_page(inventory: dict, language: str, commit: str) -> str:
    strings = TEXT[language]
    kind = inventory["inventory_kind"]
    if kind == "json_object_types":
        title = strings["json_title"]
        intro = strings["json_intro"]
        table = render_json_table(inventory, language, commit)
        related = (
            "[JSON 总览](../json/overview.md)" if language == "zh_CN"
            else "[JSON overview](../json/overview.md)"
        )
    elif kind == "eoc_conditions":
        title = strings["condition_title"]
        intro = strings["condition_intro"]
        table = render_eoc_table(inventory, language, commit)
        related = (
            "[EOC 总览](../eoc/overview.md)" if language == "zh_CN"
            else "[EOC overview](../eoc/overview.md)"
        )
    else:
        title = strings["effect_title"]
        intro = strings["effect_intro"]
        table = render_eoc_table(inventory, language, commit)
        related = (
            "[EOC 总览](../eoc/overview.md)" if language == "zh_CN"
            else "[EOC overview](../eoc/overview.md)"
        )
    summary = ", ".join(
        f"{key}={value}"
        for key, value in inventory["summary"].items()
        if isinstance(value, int)
    )
    lines = [
        f"# {title}",
        "",
        f"> {strings['generated']}",
        f"> {strings['commit']}: `{commit}` · {related}",
        "",
        intro,
        "",
        "**{}:** `{}`".format(
            strings["source"],
            next(spec.source_path for spec in SPECS if spec.kind == kind),
        ),
        "",
        f"**Inventory summary:** {summary}",
        "",
        f"## {strings['boundary_title']}",
        "",
        strings["boundary"],
        "",
    ]
    if kind != "json_object_types":
        lines.extend([strings["legend"], ""])
    lines.extend(table)
    return "\n".join(lines).rstrip() + "\n"


def split_front_matter(content: str) -> tuple[str, str]:
    if not content.startswith("---\n"):
        return "", content.lstrip("\n")
    end = content.find("\n---\n", 4)
    if end < 0:
        raise ReferenceError("unterminated generated front matter")
    boundary = end + len("\n---\n")
    return content[:boundary] + "\n", content[boundary:].lstrip("\n")


def write_outputs(outputs: dict[Path, str], check: bool) -> int:
    stale = []
    for path, expected_body in outputs.items():
        existing = path.read_text(encoding="utf-8") if path.exists() else ""
        front_matter, actual_body = split_front_matter(existing)
        if actual_body == expected_body:
            continue
        stale.append(path)
        if not check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(front_matter + expected_body, encoding="utf-8")
    if check and stale:
        for path in stale:
            print(f"stale JSON/EOC reference: {path.relative_to(ROOT)}", file=sys.stderr)
        return 1
    action = "checked" if check else "generated"
    print(f"{action} {len(outputs)} bilingual JSON/EOC reference pages")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-repo",
        type=Path,
        default=Path(os.environ["CCB_SOURCE_REPO"])
        if "CCB_SOURCE_REPO" in os.environ
        else None,
    )
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--print-source-commit", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        commit = catalog_source_commit()
        if args.print_source_commit:
            print(commit)
            return 0
        if args.source_repo is None:
            raise ReferenceError("--source-repo or CCB_SOURCE_REPO is required")
        repository = args.source_repo.resolve()
        run_git(repository, "cat-file", "-e", f"{commit}^{{commit}}")
        inventories = load_inventories(repository, commit)
        outputs = {}
        for spec in SPECS:
            for language, path in spec.outputs.items():
                outputs[path] = render_page(inventories[spec.kind], language, commit)
        return write_outputs(outputs, args.check)
    except (OSError, ReferenceError, yaml.YAMLError) as error:
        print(error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
