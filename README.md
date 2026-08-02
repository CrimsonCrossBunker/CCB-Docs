# CCB-Docs

CCB 的正式双语开发者解释、教程、架构与导航站。运行时行为、API 契约、构建
和治理仍分别以 CCB 主仓库的源码/测试、Schema/LuaLS/注册清单、构建文件和
治理文件为准。

The formal bilingual developer explanation, tutorial, architecture, and
navigation site for CCB. Runtime behaviour and project contracts remain
authoritative in the CCB source repository.

## Local validation / 本地验证

```sh
uv sync --frozen
uv run python scripts/generate_lua_reference.py \
  --source-repo /path/to/Cataclysm-Cleanwater-Bomb --check --require-luac
uv run python scripts/generate_catalog.py --check
uv run python scripts/check_catalog.py
uv run python scripts/generate_json_eoc_reference.py --source-repo /path/to/CCB --check
uv run python scripts/check_json_eoc_example_mod.py --source-repo /path/to/CCB
uv run python -m unittest discover -s tests -p 'test_*.py'
uv run flake8 --max-line-length=100 scripts tests
uv run python scripts/build_site.py --strict --include-drafts
uv run python scripts/check_links.py --site-dir site --critical
```

When a local CCB checkout is available, also validate source paths, symbols,
queries, and fingerprints:

```sh
uv run python scripts/check_catalog.py --source-repo /path/to/Cataclysm-Cleanwater-Bomb
```

Lua v5 generated reference bodies and
`reports/lua-v5-reference-coverage.json` are owned by
`scripts/generate_lua_reference.py`. The pinned source commit and PR live in
`config/lua-reference-v5.yml`. While that source PR is pending, all 25 Lua
document ids (50 language pages) remain drafts and are excluded from production
navigation, search, and AI indexes.

`docs-catalog.yml` v2 is the only manually maintained machine directory. It
generates page front matter, navigation, `llms.txt`, `llms-full.txt`, JSON and
JSONL indexes, bilingual mappings, search/AI allowlists, archive exclusions,
redirects, and sitemap metadata. Files under `docs/ai/` are generated.

The bilingual JSON/EOC registry bodies are generated from the exact CCB
contract-inventory commit by `scripts/generate_json_eoc_reference.py`. The
current draft indexes 190 JSON object types, 275 EOC conditions, and 306 EOC
effects while preserving every partial/unclassified evidence boundary.

Chinese source lives in `docs/zh_CN/` and is published at the site root.
English source lives in `docs/en/` and is published under `/en/`.

中文位于 `docs/zh_CN/` 并发布在站点根路径；英文位于 `docs/en/` 并发布到
`/en/`。
