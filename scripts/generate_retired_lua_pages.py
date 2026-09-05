#!/usr/bin/env python3
"""Keep retired Lua URLs usable without rebuilding the removed v5 API."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
from pathlib import Path

from generate_catalog import CATALOG_PATH, content_body, load_catalog, load_yaml, page_source


GENERATOR = "scripts/generate_retired_lua_pages.py"
HISTORY_COMMIT = "fd69d0f47ce95fb8e707162b4bac453a2a44ff2b"
HISTORY_ROOT = "https://github.com/CrimsonCrossBunker/CCB-Docs/blob/" + HISTORY_COMMIT


def render_body(page: dict) -> str:
    relative = os.path.relpath("api/lua/v1/overview.md", Path(page["path"]).parent)
    history = f"{HISTORY_ROOT}/docs/{page['language']}/{page['path']}"
    if page["language"] == "zh_CN":
        return (
            "# Lua API v5 已停用\n\n"
            "此网址仅用于保留旧链接。旧 API v5、`game.*` 和 JSON Manifest "
            "已移除，不能用于当前 CCB MOD。\n\n"
            f"请从 [Lua Platform v1 入门]({relative}) 开始，使用 `require(\"ccb\")`。\n\n"
            f"[查看停用前的历史文档]({history})（仅供历史查阅）。\n"
        )
    return (
        "# Lua API v5 has been retired\n\n"
        "This URL preserves an old link. API v5, `game.*`, and the JSON manifest "
        "have been removed and cannot be used for current CCB Mods.\n\n"
        f"Start with [Lua Platform v1]({relative}) and use `require(\"ccb\")`.\n\n"
        f"[Read the previous documentation]({history}) for historical reference only.\n"
    )


def validate_retirement(page: dict) -> None:
    if not all((
        page["status"] == "archived",
        page["doc_type"] == "archive",
        page["deprecated"],
        page["deprecation_replacement"] == "api.lua.v1.overview",
        not page["include_in_search"],
        not page["include_in_ai_index"],
        page["generated_by"] == GENERATOR,
    )):
        raise ValueError(f"retired Lua page has active metadata: {page['id']}")


def synchronize(catalog: dict, *, check: bool) -> list[Path]:
    changed = []
    for page in catalog["pages"]:
        if not page["path"].startswith("api/lua/v5/"):
            continue
        validate_retirement(page)
        path = page_source(page)
        content = path.read_text(encoding="utf-8") if path.exists() else ""
        old_body = content_body(content)
        body = render_body(page)
        if old_body != body:
            changed.append(path)
            if not check:
                prefix = content[:-len(old_body)] if old_body else content
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(prefix + body, encoding="utf-8")
    return changed


def refresh_fingerprints(catalog: dict) -> None:
    """Refresh only derived translation hashes; preserve catalog layout and policy."""
    fingerprints = {
        page["id"]: hashlib.sha256(render_body(page).encode("utf-8")).hexdigest()
        for page in catalog["pages"]
        if page["generated_by"] == GENERATOR and page["language"] == "zh_CN"
    }

    def update(match: re.Match) -> str:
        block = match.group()
        page_id = block.splitlines()[0].removeprefix("- id: ")
        if page_id not in fingerprints:
            return block
        return re.sub(
            r"^  translation_source_fingerprint: .+$",
            "  translation_source_fingerprint: " + fingerprints[page_id],
            block, flags=re.MULTILINE,
        )

    original = CATALOG_PATH.read_text(encoding="utf-8")
    updated = re.sub(r"^- id: .*?(?=^- id: |\Z)", update, original, flags=re.MULTILINE | re.DOTALL)
    if original != updated:
        CATALOG_PATH.write_text(updated, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    catalog = load_catalog() if args.check else load_yaml(CATALOG_PATH)
    changed = synchronize(catalog, check=args.check)
    if not args.check:
        refresh_fingerprints(catalog)
    if args.check and changed:
        for path in changed:
            print(f"stale retired Lua page: {path}")
        return 1
    print(f"Retired Lua pages checked; {len(changed)} updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
