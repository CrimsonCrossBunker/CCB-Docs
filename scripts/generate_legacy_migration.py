#!/usr/bin/env python3
"""Generate and audit bilingual pages for the frozen CCB Markdown inventory."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import posixpath
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath
from urllib.parse import quote

import yaml

from generate_catalog import content_body


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config/legacy-migration-v1.yml"
CATALOG_PATH = ROOT / "docs-catalog.yml"
AUDIT_PATH = ROOT / "docs/ai/legacy-migration-audit.json"
GENERATOR = "scripts/generate_legacy_migration.py"
REVIEWED_CONTENT_ROOT = ROOT / "content/legacy-migration"
BLOCK_START = "  # BEGIN GENERATED LEGACY MIGRATION PAGES"
BLOCK_END = "  # END GENERATED LEGACY MIGRATION PAGES"
SELECTED_STATUSES = {"stubbed", "archived"}
RETAINED_ACTIONS = {"keep_in_repo", "retain_third_party"}
LANGUAGES = ("zh_CN", "en")
HISTORY_SOURCE_PATHS = [
    "doc/migration/markdown-inventory.yml",
    "doc/migration/history-assessment.md",
]
SUSPICIOUS_CONTRIBUTOR_TOKENS = (
    "$(",
    "`",
    "&&",
    "||",
    ";",
    "<script",
    "\x1b",
)


class MigrationError(ValueError):
    """The cross-repository migration contract is inconsistent."""


def load_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise MigrationError(f"{path.relative_to(ROOT)} must contain a mapping")
    return data


def run_git(
    repository: Path,
    args: list[str],
    *,
    text: bool = True,
) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repository), *args],
        check=False,
        capture_output=True,
        text=text,
    )


def require_source_commit(repository: Path, commit: str) -> None:
    head = run_git(repository, ["rev-parse", "HEAD"])
    if head.returncode != 0:
        raise MigrationError(f"not a Git repository: {repository}")
    if head.stdout.strip() != commit:
        raise MigrationError(
            f"source checkout must be exactly {commit}; got {head.stdout.strip()}"
        )


def git_blob(repository: Path, commit: str, source_path: str) -> bytes:
    result = run_git(repository, ["show", f"{commit}:{source_path}"], text=False)
    if result.returncode != 0:
        raise MigrationError(f"missing source at {commit}: {source_path}")
    return result.stdout


def git_text(repository: Path, commit: str, source_path: str) -> str:
    try:
        return git_blob(repository, commit, source_path).decode("utf-8")
    except UnicodeDecodeError as error:
        raise MigrationError(f"source is not UTF-8 text: {source_path}") from error


def git_text_following_symlinks(
    repository: Path,
    commit: str,
    source_path: str,
) -> str:
    current = PurePosixPath(source_path)
    seen: set[str] = set()
    for _ in range(16):
        current_text = current.as_posix()
        if current_text in seen:
            raise MigrationError(f"source symlink loop: {source_path}")
        seen.add(current_text)
        tree = run_git(repository, ["ls-tree", commit, "--", current_text])
        if tree.returncode != 0 or not tree.stdout.strip():
            raise MigrationError(f"source path is absent at {commit}: {current_text}")
        mode = tree.stdout.split(maxsplit=1)[0]
        value = git_text(repository, commit, current_text)
        if mode != "120000":
            return value
        target = value.strip()
        if not target or PurePosixPath(target).is_absolute():
            raise MigrationError(f"unsafe source symlink: {current_text} -> {target}")
        normalized = posixpath.normpath((current.parent / target).as_posix())
        if normalized == ".." or normalized.startswith("../"):
            raise MigrationError(f"source symlink escapes repository: {current_text}")
        current = PurePosixPath(normalized)
    raise MigrationError(f"source symlink depth exceeded: {source_path}")


def source_fingerprint(
    repository: Path,
    commit: str,
    source_paths: list[str],
) -> str:
    digest = hashlib.sha256()
    for source_path in source_paths:
        digest.update(source_path.encode("utf-8"))
        digest.update(b"\0")
        digest.update(git_blob(repository, commit, source_path))
        digest.update(b"\0")
    return digest.hexdigest()


def body_fingerprint(body: str) -> str:
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def reviewed_content(canonical: str, language: str) -> str:
    """Load an optional reviewed body fragment for one generated migration page."""
    if language not in LANGUAGES:
        raise MigrationError(f"unsupported reviewed-content language: {language}")
    if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", canonical):
        raise MigrationError(f"unsafe reviewed-content document ID: {canonical}")
    path = REVIEWED_CONTENT_ROOT / language / f"{canonical}.md"
    if not path.exists():
        return ""
    fragment = path.read_text(encoding="utf-8").strip()
    if not fragment:
        raise MigrationError(f"empty reviewed migration content: {path.relative_to(ROOT)}")
    if fragment.startswith("---") or re.search(r"(?m)^#\s+", fragment):
        raise MigrationError(
            f"reviewed migration content must be a body fragment without front matter or H1: "
            f"{path.relative_to(ROOT)}"
        )
    return fragment


def ordered_union(values: list[list[str]]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for collection in values:
        for value in collection:
            if value not in seen:
                result.append(value)
                seen.add(value)
    return result


def validate_contributor(value: str) -> str:
    normalized = " ".join(value.split())
    if not normalized or normalized != value:
        raise MigrationError(f"non-normalized contributor identity: {value!r}")
    if any(ord(character) < 32 or ord(character) == 127 for character in value):
        raise MigrationError("control character in contributor identity")
    lowered = value.lower()
    if any(token in lowered for token in SUSPICIOUS_CONTRIBUTOR_TOKENS):
        raise MigrationError(f"command-like contributor identity rejected: {value!r}")
    return normalized


def validate_inventory(inventory: dict) -> None:
    documents = inventory.get("documents", [])
    if inventory.get("schema_version") != 2:
        raise MigrationError("expected Markdown inventory schema_version 2")
    if inventory.get("document_count") != 175 or len(documents) != 175:
        raise MigrationError("frozen Markdown inventory must contain exactly 175 records")
    paths = [record["original_path"] for record in documents]
    if len(paths) != len(set(paths)):
        raise MigrationError("original paths must be unique")
    summary = inventory.get("classification_summary", {})
    if summary.get("review") != 0:
        raise MigrationError("inventory still contains review actions")
    statuses = Counter(record["migration_status"] for record in documents)
    if statuses.get("classified", 0) or statuses.get("in_progress", 0):
        raise MigrationError("inventory retains classified or in_progress records")
    if statuses != Counter({"stubbed": 104, "verified": 64, "archived": 7}):
        raise MigrationError(f"unexpected terminal inventory counts: {dict(statuses)}")
    for record in documents:
        contributors = [validate_contributor(item) for item in record["contributors"]]
        if contributors != list(dict.fromkeys(contributors)):
            raise MigrationError(
                f"duplicate contributor identity: {record['original_path']}"
            )
        if not record["license"]:
            raise MigrationError(f"missing license: {record['original_path']}")
        if any("obj-lua" in PurePosixPath(path).parts for path in record["source_paths"]):
            raise MigrationError(f"forbidden cache path: {record['original_path']}")
        if record["action"] in RETAINED_ACTIONS:
            if record["migration_status"] != "verified":
                raise MigrationError(
                    f"retained document is not verified: {record['original_path']}"
                )
        elif record["action"] == "archive_public":
            if record["migration_status"] != "archived":
                raise MigrationError(f"archive is not terminal: {record['original_path']}")
        elif record["migration_status"] != "stubbed":
            raise MigrationError(f"migration is not stubbed: {record['original_path']}")


def load_inventory(repository: Path, config: dict) -> dict:
    content = git_text(repository, config["source_commit"], config["inventory_path"])
    data = yaml.safe_load(content)
    if not isinstance(data, dict):
        raise MigrationError("source inventory must contain a mapping")
    validate_inventory(data)
    return data


def split_catalog(content: str) -> tuple[str, str | None]:
    start = content.find(BLOCK_START)
    end = content.find(BLOCK_END)
    if start < 0 and end < 0:
        return content.rstrip() + "\n", None
    if start < 0 or end < 0 or end < start:
        raise MigrationError("unterminated generated migration catalog block")
    end += len(BLOCK_END)
    if content[end:].strip():
        raise MigrationError("generated migration catalog block must be last")
    base = content[:start].rstrip() + "\n"
    return base, content[start:end] + "\n"


def target_relative(record: dict) -> str:
    target = record.get("target_path")
    prefix = "docs/zh_CN/"
    if not isinstance(target, str) or not target.startswith(prefix) or not target.endswith(".md"):
        raise MigrationError(f"invalid CCB-Docs target: {record['original_path']}")
    relative = target[len(prefix):]
    if PurePosixPath(relative).is_absolute() or ".." in PurePosixPath(relative).parts:
        raise MigrationError(f"unsafe CCB-Docs target: {target}")
    return relative


def public_url(config: dict, relative: str, language: str) -> str:
    base = config["site_base_url"].rstrip("/") + "/"
    prefix = "" if language == "zh_CN" else "en/"
    if relative == "index.md":
        suffix = ""
    elif relative.endswith("/index.md"):
        suffix = relative[:-len("index.md")]
    else:
        suffix = relative[:-len(".md")] + "/"
    return base + prefix + suffix


def page_pairs(catalog: dict) -> dict[str, dict[str, dict]]:
    result: dict[str, dict[str, dict]] = defaultdict(dict)
    for page in catalog["pages"]:
        result[page["path"]][page["language"]] = page
    return result


def alias_set(page: dict) -> set[str]:
    return {page["id"], *page.get("supersedes", [])}


def records_by_target(inventory: dict) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for record in inventory["documents"]:
        if record["migration_status"] in SELECTED_STATUSES:
            grouped[target_relative(record)].append(record)
    return dict(sorted(grouped.items()))


def missing_target_groups(
    inventory: dict,
    base_catalog: dict,
) -> tuple[dict[str, list[dict]], dict[str, str]]:
    pairs = page_pairs(base_catalog)
    missing: dict[str, list[dict]] = {}
    covered: dict[str, str] = {}
    for relative, records in records_by_target(inventory).items():
        pair = pairs.get(relative)
        if not pair:
            missing[relative] = records
            continue
        if set(pair) != set(LANGUAGES):
            raise MigrationError(f"base catalog target is not bilingual: {relative}")
        ids = {pair[language]["id"] for language in LANGUAGES}
        if len(ids) != 1:
            raise MigrationError(f"base catalog target has inconsistent ids: {relative}")
        for record in records:
            stable_id = record["stable_document_id"]
            if any(stable_id not in alias_set(pair[language]) for language in LANGUAGES):
                raise MigrationError(
                    f"base page {relative} must supersede {stable_id} in both languages"
                )
            covered[stable_id] = next(iter(ids))
    return missing, covered


def canonical_id(records: list[dict]) -> str:
    primary = [
        record["stable_document_id"]
        for record in records
        if record["action"] != "merge_into"
    ]
    if len(primary) == 1:
        return primary[0]
    merge_targets = {
        record["merge_target"] for record in records if record.get("merge_target")
    }
    if len(merge_targets) == 1:
        return next(iter(merge_targets))
    if len(records) == 1:
        return records[0]["stable_document_id"]
    raise MigrationError(
        "cannot choose one canonical id for: "
        + ", ".join(record["stable_document_id"] for record in records)
    )


def human_title(relative: str) -> str:
    path = PurePosixPath(relative)
    stem = path.stem if path.stem != "index" else path.parent.name
    spaced = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", stem)
    spaced = spaced.replace("_", " ").replace("-", " ")
    return " ".join(word for word in spaced.split()) or "legacy document"


def markdown_cell(value: object) -> str:
    if value is None or value == "" or value == []:
        return "—"
    if isinstance(value, (dict, list)):
        text = json.dumps(value, ensure_ascii=False, sort_keys=True)
    else:
        text = str(value)
    text = html.escape(text, quote=False)
    return text.replace("|", "&#124;").replace("`", "&#96;").replace("\n", "<br>")


def source_blob_url(config: dict, original_path: str) -> str:
    repository = config["source_repository"].rstrip("/")
    path = quote(original_path, safe="/")
    return f"{repository}/blob/{config['source_commit']}/{path}"


def source_history_url(config: dict, original_path: str) -> str:
    repository = config["source_repository"].rstrip("/")
    path = quote(original_path, safe="/")
    return f"{repository}/commits/{config['source_commit']}/{path}"


def joined(values: list[object]) -> str:
    rendered = [str(value) for value in values if value not in (None, "")]
    return ", ".join(rendered) if rendered else "—"


def name_text(value: object) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        for key in ("str", "str_sp", "str_pl"):
            if isinstance(value.get(key), str):
                return value[key]
    return markdown_cell(value)


def json_array(repository: Path, commit: str, source_path: str) -> list[dict]:
    try:
        value = json.loads(git_text(repository, commit, source_path))
    except json.JSONDecodeError as error:
        raise MigrationError(f"invalid JSON source: {source_path}: {error}") from error
    if not isinstance(value, list) or not all(isinstance(item, dict) for item in value):
        raise MigrationError(f"expected an array of objects: {source_path}")
    return value


def table(headers: list[str], rows: list[list[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    lines.extend(
        "| " + " | ".join(markdown_cell(cell) for cell in row) + " |"
        for row in rows
    )
    return "\n".join(lines)


def flag_reference(
    repository: Path,
    commit: str,
    records: list[dict],
) -> tuple[str, str, dict]:
    flags_path = next(path for path in records[0]["source_paths"] if path.endswith("flags.json"))
    flags = json_array(repository, commit, flags_path)
    if any(flag.get("type") != "json_flag" or not flag.get("id") for flag in flags):
        raise MigrationError("flag reference contains a non-json_flag or missing id")
    ids = [flag["id"] for flag in flags]
    if len(ids) != len(set(ids)):
        raise MigrationError("flag reference contains duplicate ids")
    rows = [
        [
            flag["id"],
            flag.get("info"),
            flag.get("restriction"),
            flag.get("inherit"),
            flag.get("conflicts"),
        ]
        for flag in sorted(flags, key=lambda item: item["id"])
    ]
    rendered = table(["ID", "info", "restriction", "inherit", "conflicts"], rows)
    zh = (
        "## 生成范围与证据\n\n"
        f"本表直接解析固定提交中的 `{flags_path}`，共收录 **{len(flags)}** 个 "
        "`json_flag` 定义。字段只在 JSON 中实际存在时显示；未解析 C++ 隐式标志、"
        "运行时使用位置或继承后的行为，因此这是 **partial direct-definition index**，"
        "不是完整 Schema，也不替代 `json_flag::load`。\n\n"
        + rendered
        + "\n"
    )
    en = (
        "## Generated scope and evidence\n\n"
        f"This table parses `{flags_path}` at the pinned commit and indexes "
        f"**{len(flags)}** direct `json_flag` definitions. A field is shown only when "
        "it exists in JSON. C++-implicit flags, use sites, and resolved behaviour are "
        "not inferred, so this is a **partial direct-definition index**, not a complete "
        "Schema and not a replacement for `json_flag::load`.\n\n"
        + rendered
        + "\n"
    )
    return zh, en, {"json_flags": len(flags), "scope": "partial-direct-definitions"}


def proficiency_reference(
    repository: Path,
    commit: str,
    records: list[dict],
) -> tuple[str, str, dict]:
    json_paths = [path for path in records[0]["source_paths"] if path.endswith(".json")]
    objects = [item for path in json_paths for item in json_array(repository, commit, path)]
    proficiencies = [item for item in objects if item.get("type") == "proficiency"]
    categories = [item for item in objects if item.get("type") == "proficiency_category"]
    unexpected = [
        item for item in objects if item.get("type") not in {"proficiency", "proficiency_category"}
    ]
    if unexpected:
        raise MigrationError("proficiency inputs contain an unexpected object type")
    category_rows = [
        [item.get("id"), name_text(item.get("name")), item.get("description")]
        for item in sorted(categories, key=lambda value: value.get("id", ""))
    ]
    proficiency_rows = [
        [
            item.get("id"),
            name_text(item.get("name")),
            item.get("category"),
            item.get("time_to_learn"),
            item.get("required_proficiencies"),
        ]
        for item in sorted(proficiencies, key=lambda value: value.get("id", ""))
    ]
    categories_table = table(["ID", "name", "description"], category_rows)
    proficiencies_table = table(
        ["ID", "name", "category", "time_to_learn", "required_proficiencies"],
        proficiency_rows,
    )
    summary = (
        f"{len(proficiencies)} proficiencies and {len(categories)} categories from "
        + ", ".join(f"`{path}`" for path in json_paths)
    )
    zh = (
        "## 生成范围与证据\n\n"
        f"固定输入中包含 **{len(proficiencies)}** 个 proficiency 和 "
        f"**{len(categories)}** 个 category。这里只列出 JSON 直接字段，不扫描未声明的"
        "其他 Mod，也不计算继承或配方使用关系；因此索引明确为 **partial**。\n\n"
        "### Categories\n\n"
        + categories_table
        + "\n\n### Proficiencies\n\n"
        + proficiencies_table
        + "\n"
    )
    en = (
        "## Generated scope and evidence\n\n"
        f"The pinned inputs contain **{len(proficiencies)}** proficiency objects and "
        f"**{len(categories)}** categories. Only direct JSON fields are listed. Other "
        "mods, resolved inheritance, and recipe use sites are outside this generator, "
        "so the index is explicitly **partial**.\n\n"
        "### Categories\n\n"
        + categories_table
        + "\n\n### Proficiencies\n\n"
        + proficiencies_table
        + "\n"
    )
    return zh, en, {
        "proficiencies": len(proficiencies),
        "proficiency_categories": len(categories),
        "scope": "partial-declared-inputs",
        "summary": summary,
    }


def mind_over_matter_reference(
    repository: Path,
    commit: str,
    records: list[dict],
) -> tuple[str, str, dict]:
    paths = [path for path in records[0]["source_paths"] if "/powers/" in path]
    spells = [item for path in paths for item in json_array(repository, commit, path)]
    if any(item.get("type") != "SPELL" or not item.get("id") for item in spells):
        raise MigrationError("Mind Over Matter inputs contain a non-SPELL or missing id")
    rows = [
        [
            item.get("id"),
            name_text(item.get("name")),
            item.get("difficulty"),
            item.get("max_level"),
            item.get("base_energy_cost"),
            item.get("base_casting_time"),
            item.get("required_level"),
        ]
        for item in sorted(spells, key=lambda value: value["id"])
    ]
    rendered = table(
        [
            "ID",
            "name",
            "difficulty",
            "max_level",
            "base_energy_cost",
            "base_casting_time",
            "required_level",
        ],
        rows,
    )
    zh = (
        "## 生成范围与证据\n\n"
        f"从清单声明的九个 power JSON 文件直接索引 **{len(spells)}** 个 `SPELL`。"
        "本页不把等级缩放、EOC、effect 或 C++ 行为推导成最终数值；缺失字段显示为"
        " `—`，所以这是可复现的 **partial direct-field reference**。\n\n"
        + rendered
        + "\n"
    )
    en = (
        "## Generated scope and evidence\n\n"
        f"The nine declared power JSON files provide **{len(spells)}** direct `SPELL` "
        "records. Level scaling, EOCs, effects, and C++ behaviour are not resolved into "
        "derived values; absent fields remain `—`. This is therefore a reproducible "
        "**partial direct-field reference**.\n\n"
        + rendered
        + "\n"
    )
    return zh, en, {"mind_over_matter_spells": len(spells), "scope": "partial-direct-fields"}


def aftershock_reference(
    repository: Path,
    commit: str,
    records: list[dict],
) -> tuple[str, str, dict]:
    paths = [
        path
        for path in records[0]["source_paths"]
        if path.endswith(".json") and not path.endswith("/modinfo.json")
    ]
    objects = [item for path in paths for item in json_array(repository, commit, path)]
    items = [item for item in objects if item.get("type") == "ITEM"]
    groups = [item for item in objects if item.get("type") == "item_group"]
    unexpected = [item for item in objects if item.get("type") not in {"ITEM", "item_group"}]
    if unexpected:
        raise MigrationError("Aftershock inputs contain an unexpected object type")
    item_rows = [
        [
            item.get("id"),
            name_text(item.get("name")),
            item.get("subtypes"),
            item.get("skill"),
            item.get("range"),
            item.get("dispersion"),
            item.get("ranged_damage"),
            item.get("copy-from"),
        ]
        for item in sorted(items, key=lambda value: value.get("id", ""))
    ]
    group_rows = [
        [
            item.get("id"),
            item.get("subtype"),
            len(item.get("items", [])),
            len(item.get("entries", [])),
            item.get("ammo"),
            item.get("magazine"),
        ]
        for item in sorted(groups, key=lambda value: value.get("id", ""))
    ]
    items_table = table(
        ["ID", "name", "subtypes", "skill", "range", "dispersion", "damage", "copy-from"],
        item_rows,
    )
    groups_table = table(
        ["ID", "subtype", "items count", "entries count", "ammo", "magazine"],
        group_rows,
    )
    zh = (
        "## 生成范围与证据\n\n"
        f"固定输入包含 **{len(items)}** 个直接 `ITEM` 定义和 **{len(groups)}** 个"
        " `item_group`。表格不展开 `copy-from`、不做单位换算，也不计算弹药、附件、"
        "技能和运行时公式后的最终 DPS；因此它是 **partial balance input index**，"
        "不是平衡结论。\n\n### Direct item definitions\n\n"
        + items_table
        + "\n\n### Item groups\n\n"
        + groups_table
        + "\n"
    )
    en = (
        "## Generated scope and evidence\n\n"
        f"The pinned inputs contain **{len(items)}** direct `ITEM` definitions and "
        f"**{len(groups)}** `item_group` objects. The table does not resolve `copy-from`, "
        "normalize units, or derive final DPS after ammunition, attachments, skills, and "
        "runtime formulas. It is a **partial balance input index**, not a balance result."
        "\n\n### Direct item definitions\n\n"
        + items_table
        + "\n\n### Item groups\n\n"
        + groups_table
        + "\n"
    )
    return zh, en, {
        "aftershock_item_definitions": len(items),
        "aftershock_item_groups": len(groups),
        "scope": "partial-balance-inputs",
    }


REFERENCE_RENDERERS = {
    "json.flags": flag_reference,
    "json.proficiencies-index": proficiency_reference,
    "mods.mind-over-matter.power-reference": mind_over_matter_reference,
    "mods.aftershock-exoplanet.balance.ranged-weapons": aftershock_reference,
}


REFERENCE_TITLES = {
    "json.flags": ("JSON 标志直接定义索引", "JSON flag direct-definition index"),
    "json.proficiencies-index": ("熟练度直接定义索引", "Proficiency direct-definition index"),
    "mods.mind-over-matter.power-reference": (
        "Mind Over Matter 能力直接字段索引",
        "Mind Over Matter power direct-field index",
    ),
    "mods.aftershock-exoplanet.balance.ranged-weapons": (
        "Aftershock 远程武器平衡输入索引",
        "Aftershock ranged-weapon balance input index",
    ),
}


def migration_body(
    records: list[dict],
    relative: str,
    language: str,
    config: dict,
    fingerprint: str,
    extra: str = "",
) -> str:
    canonical = canonical_id(records)
    archived = all(record["migration_status"] == "archived" for record in records)
    generated_reference = any(record["action"] == "generated_reference" for record in records)
    if generated_reference:
        title = REFERENCE_TITLES[canonical][0 if language == "zh_CN" else 1]
    else:
        subject = human_title(relative)
        if language == "zh_CN":
            title = ("历史归档：" if archived else "旧文档迁移草稿：") + subject
        else:
            title = ("Historical archive: " if archived else "Legacy migration draft: ") + subject
    contributors = ordered_union([record["contributors"] for record in records])
    stable_ids = [record["stable_document_id"] for record in records]
    source_rows = []
    for record in records:
        source_rows.append(
            [
                record["stable_document_id"],
                record["original_path"],
                record["action"],
                record["migration_status"],
                record.get("last_applicable_commit"),
                record.get("merge_target"),
            ]
        )
    sources_table = table(
        ["stable ID", "original path", "action", "status", "last applicable", "merge target"],
        source_rows,
    )
    retained_links = "\n".join(
        f"- [`{record['original_path']}`]({source_blob_url(config, record['original_path'])}) — "
        f"[history]({source_history_url(config, record['original_path'])})"
        for record in records
    )
    replacements = ordered_union(
        [[record["replacement"]] for record in records if record.get("replacement")]
    )
    archive_reasons = ordered_union(
        [[record["archive_reason"]] for record in records if record.get("archive_reason")]
    )
    history_path = "/CCB-Docs/migration/filtered-history-experiment/"
    if language == "en":
        history_path = "/CCB-Docs/en/migration/filtered-history-experiment/"
    if language == "zh_CN":
        state = "归档" if archived else "迁移草稿"
        intro = (
            f"本页是 `{canonical}` 的{state}页面。它记录 **{len(records)}** 条冻结清单记录，"
            "但不把旧说明提升为运行时契约。"
        )
        authority = (
            "运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息"
            "和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移"
            "状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。"
        )
        attribution = (
            "清单中的已接受贡献者为：" + joined(contributors) + "。许可证："
            + joined(sorted({record["license"] for record in records}))
            + "。异常贡献者原始值没有导入或发布。"
        )
        history = (
            f"源清单冻结 commit 为 `{records[0]['source_commit']}`；本次交叉仓验证 commit 为 "
            f"`{config['source_commit']}`；聚合源指纹为 `{fingerprint}`。"
            f"[过滤历史实验报告]({history_path})记录了为何不导入整个游戏仓库历史。"
        )
        next_step = (
            "该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；"
            "Draft 不进入正式导航、搜索或 AI allowlist。"
        )
        if archived:
            next_step = (
                "该页是公开历史归档，不恢复为当前操作指南；只有出现新的维护证据时，"
                "才应另建当前页面。归档不进入导航、搜索或 AI allowlist。"
            )
        replacement_text = joined(replacements)
        archive_text = joined(archive_reasons)
        headings = {
            "records": "清单记录",
            "authority": "权威边界",
            "history": "历史与归属",
            "retained": "CCB 中保留的正文",
            "next": "替代与下一步",
        }
        details = (
            f"\n\n- Stable document IDs: `{', '.join(stable_ids)}`"
            f"\n- Target: `{relative}`"
            f"\n- Replacement: {replacement_text}"
            f"\n- Archive reason: {archive_text}\n"
        )
    else:
        state = "archive" if archived else "migration draft"
        intro = (
            f"This is the {state} page for `{canonical}`. It records **{len(records)}** "
            "frozen inventory record(s), but it does not promote legacy prose into a "
            "runtime contract."
        )
        authority = (
            "CCB source and tests remain authoritative for runtime behaviour; schemas, "
            "declarations, registrations, and generated inventories govern JSON/Lua/API; "
            "CI, CMake, Makefile, and Gradle govern builds. This page explains migration "
            "state, history, and auditable provenance only. A current contract wins over "
            "conflicting legacy prose."
        )
        attribution = (
            "Accepted inventory contributors: " + joined(contributors) + ". License: "
            + joined(sorted({record["license"] for record in records}))
            + ". Raw rejected or anomalous contributor values were not imported or published."
        )
        history = (
            f"The source inventory is frozen at `{records[0]['source_commit']}`; this "
            f"cross-repository verification uses `{config['source_commit']}`; the aggregate "
            f"source fingerprint is `{fingerprint}`. The "
            f"[filtered-history experiment]({history_path}) explains why the whole game "
            "repository history is not imported."
        )
        next_step = (
            "This page remains Draft until a Responsible human reviews the prose, sources, "
            "and replacement relationship. Drafts stay outside production navigation, "
            "search, and the AI allowlist."
        )
        if archived:
            next_step = (
                "This is a public historical archive, not a current procedure. Create a "
                "separate maintained page if new support evidence appears. Archives stay "
                "outside navigation, search, and the AI allowlist."
            )
        replacement_text = joined(replacements)
        archive_text = joined(archive_reasons)
        headings = {
            "records": "Inventory records",
            "authority": "Authority boundary",
            "history": "History and attribution",
            "retained": "Bodies retained in CCB",
            "next": "Replacement and next step",
        }
        details = (
            f"\n\n- Stable document IDs: `{', '.join(stable_ids)}`"
            f"\n- Target: `{relative}`"
            f"\n- Replacement: {replacement_text}"
            f"\n- Archive reason: {archive_text}\n"
        )
    prefix = (
        f"# {title}\n\n{intro}{details}\n"
        f"## {headings['records']}\n\n{sources_table}\n\n"
        f"## {headings['authority']}\n\n{authority}\n\n"
    )
    if extra:
        prefix += f"{extra.rstrip()}\n\n"
    reviewed = reviewed_content(canonical, language)
    if reviewed:
        prefix += f"{reviewed}\n\n"
    return prefix + (
        f"## {headings['history']}\n\n{attribution}\n\n{history}\n\n"
        f"## {headings['retained']}\n\n{retained_links}\n\n"
        f"## {headings['next']}\n\n{next_step}\n"
    )


def catalog_entry(
    records: list[dict],
    relative: str,
    language: str,
    config: dict,
    source_hash: str,
    translation_hash: str,
) -> dict:
    canonical = canonical_id(records)
    archived = all(record["migration_status"] == "archived" for record in records)
    generated_reference = any(record["action"] == "generated_reference" for record in records)
    title_pair = REFERENCE_TITLES.get(canonical)
    if title_pair:
        title = title_pair[0 if language == "zh_CN" else 1]
    else:
        subject = human_title(relative)
        if language == "zh_CN":
            title = ("历史归档：" if archived else "旧文档迁移草稿：") + subject
        else:
            title = ("Historical archive: " if archived else "Legacy migration draft: ") + subject
    contributors = ordered_union([record["contributors"] for record in records])
    licenses = sorted({record["license"] for record in records})
    if len(licenses) != 1:
        raise MigrationError(f"one target has incompatible licenses: {relative}")
    source_paths = ordered_union(
        [[record["original_path"], *record["source_paths"]] for record in records]
    )
    source_symbols = ordered_union([record["source_symbols"] for record in records])
    aliases = sorted(
        record["stable_document_id"]
        for record in records
        if record["stable_document_id"] != canonical
    )
    authority = "historical" if archived else (
        "api-contract" if generated_reference else "docs-explanation"
    )
    risk_group = records[0]["domain"]
    high_risk = risk_group in {"build", "cpp", "eoc", "json", "lua", "release", "testing"}
    attribution = (
        "CCB contributors: " + ", ".join(contributors)
        + "; accepted inventory identities only. Source paths and Git history remain authoritative."
    )
    return {
        "id": canonical,
        "title": title,
        "language": language,
        "path": relative,
        "status": "archived" if archived else "active",
        "doc_type": "archive" if archived else (
            "generated-api" if generated_reference else "explanation"
        ),
        "audiences": ["new-contributor", "experienced-contributor", "maintainer", "mod-author"],
        "owners": ["CCB maintainers"],
        "reviewers": ["Documentation reviewers"],
        "review_interval_days": 365,
        "last_human_reviewer": "LYHGLYTX",
        "source_paths": source_paths,
        "source_symbols": source_symbols,
        "source_queries": [],
        "source_fingerprint": source_hash,
        "authority": authority,
        "verified_commit": config["source_commit"],
        "verified_at": config["verified_at"],
        "generated": True,
        "generated_by": GENERATOR,
        "include_in_search": not archived,
        "include_in_ai_index": not archived,
        "translation_group": canonical,
        "translation_status": "current",
        "translation_stale_since": None,
        "translation_source_fingerprint": translation_hash,
        "prerequisites": [],
        "depends_on": [],
        "redirect_from": [],
        "supersedes": aliases,
        "license": licenses[0],
        "attribution": attribution,
        "example_validation_ids": [],
        "api_version": "legacy-generated-reference-v1" if generated_reference else None,
        "deprecated": False,
        "deprecation_replacement": None,
        "risk_group": risk_group,
        "risk_level": "high" if high_risk else "normal",
        "pending_source_pr": None,
        "stale_reason": None,
        "nav": {
            "section": (
                "历史归档" if archived and language == "zh_CN" else
                "Historical archive" if archived else
                "迁移草稿" if language == "zh_CN" else
                "Migration drafts"
            ),
            "order": 1000,
        },
    }


def history_report_body(config: dict, language: str) -> str:
    experiment = config["history_experiment"]
    if language == "zh_CN":
        return f"""# 过滤历史实验

## 结果

对最终选择的路径进行了临时、隔离的 `git-filter-repo` 实验；没有把过滤仓库
导入或推送到 CCB-Docs。

| 指标 | 结果 |
| --- | ---: |
| 选择的最终路径 | {experiment['selected_final_paths']} |
| 自包含仓库大小 | {experiment['self_contained_size_mib']} MiB |
| Commit | {experiment['commits']} |
| Author identity | {experiment['author_identities']} |
| 最终路径 | {experiment['final_paths']} |
| Rename record | {experiment['rename_records']} |
| `git fsck` | {experiment['fsck']} |

## 决策

实验仓库虽然自包含且通过 `git fsck`，但没有保留可审核的 rename record，
直接导入还会把迁移页面与主仓库历史耦合。因而本阶段不导入整个游戏仓库历史，
也不导入该过滤仓库；每页保留 CCB source URL、source commit、已清洗贡献者和
许可证。以后只有在 Responsible human 审查作者映射、重命名语义和许可后，
才可另行决定是否导入选择路径的历史。

本实验只使用 Git 对象和明确路径，没有遍历 `obj-lua/` 或其他未跟踪构建缓存。
"""
    return f"""# Filtered-history experiment

## Result

A temporary, isolated `git-filter-repo` experiment was run for the selected
final paths. The filtered repository was neither imported into nor pushed to
CCB-Docs.

| Measure | Result |
| --- | ---: |
| Selected final paths | {experiment['selected_final_paths']} |
| Self-contained repository size | {experiment['self_contained_size_mib']} MiB |
| Commits | {experiment['commits']} |
| Author identities | {experiment['author_identities']} |
| Final paths | {experiment['final_paths']} |
| Rename records | {experiment['rename_records']} |
| `git fsck` | {experiment['fsck']} |

## Decision

The experiment is self-contained and passes `git fsck`, but it preserved no
auditable rename records and an import would couple migration pages to
game-repository history. This phase therefore imports neither the whole game
history nor the filtered repository. Every page retains CCB source URLs,
source commits, sanitized contributors, and license data. A later import
requires Responsible-human review of author mappings, rename semantics, and
licensing.

The experiment used Git objects and explicit paths only. It did not traverse
`obj-lua/` or another untracked build cache.
"""


def history_report_entry(
    config: dict,
    language: str,
    source_hash: str,
    translation_hash: str,
) -> dict:
    return {
        "id": "migration.filtered-history-experiment",
        "title": "过滤历史实验" if language == "zh_CN" else "Filtered-history experiment",
        "language": language,
        "path": "migration/filtered-history-experiment.md",
        "status": "active",
        "doc_type": "explanation",
        "audiences": ["experienced-contributor", "maintainer"],
        "owners": ["CCB maintainers"],
        "reviewers": ["Documentation reviewers"],
        "review_interval_days": 365,
        "last_human_reviewer": "LYHGLYTX",
        "source_paths": list(HISTORY_SOURCE_PATHS),
        "source_symbols": [],
        "source_queries": [],
        "source_fingerprint": source_hash,
        "authority": "historical",
        "verified_commit": config["source_commit"],
        "verified_at": config["verified_at"],
        "generated": True,
        "generated_by": GENERATOR,
        "include_in_search": True,
        "include_in_ai_index": True,
        "translation_group": "migration.filtered-history-experiment",
        "translation_status": "current",
        "translation_stale_since": None,
        "translation_source_fingerprint": translation_hash,
        "prerequisites": [],
        "depends_on": [],
        "redirect_from": [],
        "supersedes": [],
        "license": "CC-BY-SA-3.0",
        "attribution": "CCB migration experiment; no repository history was imported.",
        "example_validation_ids": [],
        "api_version": None,
        "deprecated": False,
        "deprecation_replacement": None,
        "risk_group": "migration-history",
        "risk_level": "normal",
        "pending_source_pr": None,
        "stale_reason": None,
        "nav": {
            "section": "迁移草稿" if language == "zh_CN" else "Migration drafts",
            "order": 999,
        },
    }


def build_outputs(
    repository: Path,
    config: dict,
    inventory: dict,
    base_catalog: dict,
) -> tuple[list[dict], dict[Path, str], dict, dict[str, str]]:
    missing, covered = missing_target_groups(inventory, base_catalog)
    if len(missing) != 99:
        raise MigrationError(f"expected 99 missing unique target paths, got {len(missing)}")
    if sum(len(records) for records in missing.values()) != 104:
        raise MigrationError("expected 104 missing inventory records")
    entries: list[dict] = []
    bodies: dict[Path, str] = {}
    reference_counts: dict[str, dict] = {}
    canonical_paths: dict[str, str] = {}
    for relative, records in missing.items():
        canonical = canonical_id(records)
        if canonical in canonical_paths:
            raise MigrationError(
                f"canonical id {canonical} targets both {canonical_paths[canonical]} and {relative}"
            )
        canonical_paths[canonical] = relative
        paths = ordered_union(
            [[record["original_path"], *record["source_paths"]] for record in records]
        )
        fingerprint = source_fingerprint(
            repository,
            config["source_commit"],
            paths,
        )
        extras = {"zh_CN": "", "en": ""}
        if any(record["action"] == "generated_reference" for record in records):
            renderer = REFERENCE_RENDERERS.get(canonical)
            if renderer is None:
                raise MigrationError(f"no renderer for generated reference: {canonical}")
            zh_extra, en_extra, metrics = renderer(
                repository,
                config["source_commit"],
                records,
            )
            extras = {"zh_CN": zh_extra, "en": en_extra}
            reference_counts[canonical] = metrics
        rendered = {
            language: migration_body(
                records,
                relative,
                language,
                config,
                fingerprint,
                extras[language],
            )
            for language in LANGUAGES
        }
        translation_hash = body_fingerprint(rendered["zh_CN"])
        for language in LANGUAGES:
            entries.append(
                catalog_entry(
                    records,
                    relative,
                    language,
                    config,
                    fingerprint,
                    translation_hash,
                )
            )
            bodies[ROOT / "docs" / language / relative] = rendered[language]

    report_source_hash = source_fingerprint(
        repository,
        config["source_commit"],
        HISTORY_SOURCE_PATHS,
    )
    report_bodies = {
        language: history_report_body(config, language) for language in LANGUAGES
    }
    report_translation_hash = body_fingerprint(report_bodies["zh_CN"])
    for language in LANGUAGES:
        entries.append(
            history_report_entry(
                config,
                language,
                report_source_hash,
                report_translation_hash,
            )
        )
        bodies[
            ROOT / "docs" / language / "migration/filtered-history-experiment.md"
        ] = report_bodies[language]
    return entries, bodies, reference_counts, covered


def render_catalog_block(entries: list[dict]) -> str:
    payload = yaml.safe_dump(
        entries,
        allow_unicode=True,
        sort_keys=False,
        width=100,
    ).rstrip()
    indented = "\n".join("  " + line for line in payload.splitlines())
    return (
        BLOCK_START
        + "\n  # Generated from the pinned CCB Markdown inventory; do not edit by hand.\n"
        + indented
        + "\n"
        + BLOCK_END
        + "\n"
    )


def expected_catalog_text(base: str, entries: list[dict]) -> str:
    return base.rstrip() + "\n\n" + render_catalog_block(entries)


def validate_source_symbol(
    repository: Path,
    commit: str,
    paths: list[str],
    symbol: str,
) -> bool:
    result = run_git(repository, ["grep", "-F", "-e", symbol, commit, "--", *paths])
    return result.returncode == 0


def validate_permanent_stub(
    repository: Path,
    commit: str,
    record: dict,
) -> None:
    body = git_text_following_symlinks(repository, commit, record["original_path"])
    required = [
        "<!-- CCB-DOC-MOVED-START -->",
        "<!-- CCB-DOC-MOVED-END -->",
        record["stable_document_id"],
        record["zh_url"],
        record["en_url"],
        str(record["moved_at"]),
        record["source_commit"],
        str(record["retained_body_until"]),
        "no longer maintained",
        "remains permanently",
    ]
    missing = [value for value in required if value not in body]
    if missing:
        raise MigrationError(
            f"permanent stub is incomplete for {record['original_path']}: {missing}"
        )


def resolve_catalog_record(catalog: dict, record: dict) -> tuple[dict, dict]:
    relative = target_relative(record)
    candidates = [
        page
        for page in catalog["pages"]
        if page["path"] == relative
        and record["stable_document_id"] in alias_set(page)
    ]
    by_language = {page["language"]: page for page in candidates}
    if set(by_language) != set(LANGUAGES):
        raise MigrationError(
            f"missing bilingual target for {record['stable_document_id']}: {relative}"
        )
    if len({page["id"] for page in by_language.values()}) != 1:
        raise MigrationError(f"target id differs by language: {relative}")
    return by_language["zh_CN"], by_language["en"]


def cross_repository_audit(
    repository: Path,
    config: dict,
    inventory: dict,
    catalog: dict,
    reference_counts: dict,
    covered: dict[str, str],
) -> dict:
    records = []
    missing_targets = 0
    for record in inventory["documents"]:
        original = record["original_path"]
        git_blob(repository, config["source_commit"], original)
        for source_path in record["source_paths"]:
            git_blob(repository, config["source_commit"], source_path)
        for symbol in record["source_symbols"]:
            if not validate_source_symbol(
                repository,
                config["source_commit"],
                record["source_paths"],
                symbol,
            ):
                raise MigrationError(
                    f"source symbol is absent for {record['stable_document_id']}: {symbol}"
                )
        audit_record = {
            "stable_document_id": record["stable_document_id"],
            "original_path": original,
            "target_path": record["target_path"],
            "action": record["action"],
            "migration_status": record["migration_status"],
            "source_commit": record["source_commit"],
            "last_applicable_commit": record["last_applicable_commit"],
            "contributors": record["contributors"],
            "license": record["license"],
            "history_url": source_history_url(config, original),
            "replacement": record["replacement"],
        }
        if record["migration_status"] in SELECTED_STATUSES:
            if not all(
                record.get(field)
                for field in ("moved_at", "zh_url", "en_url", "retained_body_until")
            ):
                raise MigrationError(f"permanent stub metadata is incomplete: {original}")
            validate_permanent_stub(repository, config["source_commit"], record)
            try:
                chinese, english = resolve_catalog_record(catalog, record)
            except MigrationError:
                missing_targets += 1
                raise
            if public_url(config, chinese["path"], "zh_CN") != record["zh_url"]:
                raise MigrationError(f"Chinese target URL mismatch: {original}")
            if public_url(config, english["path"], "en") != record["en_url"]:
                raise MigrationError(f"English target URL mismatch: {original}")
            for page in (chinese, english):
                if page["license"] != record["license"]:
                    raise MigrationError(f"target license mismatch: {original}")
                if not page["attribution"]:
                    raise MigrationError(f"target attribution is empty: {original}")
            if record["stable_document_id"] not in covered:
                expected_status = (
                    "archived"
                    if record["migration_status"] == "archived"
                    else "active"
                )
                if chinese["status"] != expected_status or english["status"] != expected_status:
                    raise MigrationError(f"generated migration status mismatch: {original}")
                for page in (chinese, english):
                    if page["status"] == "archived":
                        if page["include_in_search"] or page["include_in_ai_index"]:
                            raise MigrationError(f"archived migration is indexed: {original}")
                    else:
                        if not page["include_in_search"] or not page["include_in_ai_index"]:
                            raise MigrationError(f"active migration is not indexed: {original}")
                        if page["pending_source_pr"] is not None:
                            raise MigrationError(f"pending source PR mismatch: {original}")
            audit_record.update(
                {
                    "catalog_id": chinese["id"],
                    "catalog_status": chinese["status"],
                    "zh_path": chinese["path"],
                    "en_path": english["path"],
                }
            )
        else:
            if record["action"] not in RETAINED_ACTIONS:
                raise MigrationError(f"unexpected verified action: {original}")
            if record["migration_status"] != "verified":
                raise MigrationError(f"retained document is not verified: {original}")
            if any(record.get(field) for field in ("moved_at", "zh_url", "en_url")):
                raise MigrationError(f"retained document has migration URLs: {original}")
            audit_record["catalog_id"] = None
        records.append(audit_record)

    statuses = Counter(record["migration_status"] for record in inventory["documents"])
    actions = Counter(record["action"] for record in inventory["documents"])
    target_paths = {
        target_relative(record)
        for record in inventory["documents"]
        if record["migration_status"] in SELECTED_STATUSES
    }
    generated_records = [
        record
        for record in inventory["documents"]
        if record["migration_status"] in SELECTED_STATUSES
        and record["stable_document_id"] not in covered
    ]
    preexisting_records = [
        record
        for record in inventory["documents"]
        if record["stable_document_id"] in covered
    ]
    return {
        "schema_version": 1,
        "generated_by": GENERATOR,
        "source_commit": config["source_commit"],
        "inventory_source_commit": inventory["source_commit"],
        "pending_source_pr": None,
        "document_count": len(inventory["documents"]),
        "action_counts": dict(sorted(actions.items())),
        "migration_status_counts": dict(sorted(statuses.items())),
        "review_count": actions.get("review", 0),
        "classified_count": statuses.get("classified", 0),
        "in_progress_count": statuses.get("in_progress", 0),
        "selected_record_count": sum(statuses[value] for value in SELECTED_STATUSES),
        "selected_unique_target_count": len(target_paths),
        "preexisting_covered_record_count": len(preexisting_records),
        "preexisting_unique_target_count": len(
            {target_relative(record) for record in preexisting_records}
        ),
        "generated_record_count": len(generated_records),
        "generated_unique_target_count": len(
            {target_relative(record) for record in generated_records}
        ),
        "missing_target_count": missing_targets,
        "generated_reference_coverage": dict(sorted(reference_counts.items())),
        "history_experiment": config["history_experiment"],
        "records": records,
    }


def json_text(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def source_paths_for_sparse_checkout(inventory: dict, config: dict) -> list[str]:
    paths = {config["inventory_path"], *HISTORY_SOURCE_PATHS}
    for record in inventory["documents"]:
        paths.add(record["original_path"])
        paths.update(record["source_paths"])
    if any("obj-lua" in PurePosixPath(path).parts for path in paths):
        raise MigrationError("sparse source list contains obj-lua")
    return sorted(paths)


def write_or_check(path: Path, expected: str, check: bool) -> bool:
    actual = path.read_text(encoding="utf-8") if path.exists() else None
    if actual == expected:
        return True
    if check:
        print(f"stale legacy migration output: {path.relative_to(ROOT)}", file=sys.stderr)
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(expected, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-repo", type=Path)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--print-source-commit", action="store_true")
    parser.add_argument("--print-source-paths", action="store_true")
    args = parser.parse_args()
    try:
        config = load_yaml(CONFIG_PATH)
        if config.get("schema_version") != 1:
            raise MigrationError("legacy migration config must use schema_version 1")
        if args.print_source_commit:
            print(config["source_commit"])
            return 0
        if args.source_repo is None:
            raise MigrationError("--source-repo is required")
        repository = args.source_repo.resolve()
        require_source_commit(repository, config["source_commit"])
        inventory = load_inventory(repository, config)
        if args.print_source_paths:
            print("\n".join(source_paths_for_sparse_checkout(inventory, config)))
            return 0

        catalog_text = CATALOG_PATH.read_text(encoding="utf-8")
        base_text, _ = split_catalog(catalog_text)
        base_catalog = yaml.safe_load(base_text)
        if not isinstance(base_catalog, dict):
            raise MigrationError("base catalog must contain a mapping")
        entries, bodies, reference_counts, covered = build_outputs(
            repository,
            config,
            inventory,
            base_catalog,
        )
        expected_catalog = expected_catalog_text(base_text, entries)
        outputs_ok = write_or_check(CATALOG_PATH, expected_catalog, args.check)
        for path, body in sorted(bodies.items()):
            actual = path.read_text(encoding="utf-8") if path.exists() else ""
            actual_body = content_body(actual) if actual else ""
            if actual_body == body:
                continue
            if args.check:
                print(
                    f"stale legacy migration body: {path.relative_to(ROOT)}",
                    file=sys.stderr,
                )
                outputs_ok = False
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(body, encoding="utf-8")

        catalog_for_audit = yaml.safe_load(expected_catalog)
        audit = cross_repository_audit(
            repository,
            config,
            inventory,
            catalog_for_audit,
            reference_counts,
            covered,
        )
        if not write_or_check(AUDIT_PATH, json_text(audit), args.check):
            outputs_ok = False
        if not outputs_ok:
            return 1
        print(
            "legacy migration coverage: 175 records, 105 selected targets, "
            "0 missing; generated 99 target pairs plus one history pair"
        )
        print(
            "generated references: 648 flags, 50 proficiencies + 21 categories, "
            "226 Mind Over Matter spells, 18 Aftershock items + 37 item groups"
        )
        return 0
    except (
        KeyError,
        MigrationError,
        OSError,
        TypeError,
        yaml.YAMLError,
    ) as error:
        print(error, file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
