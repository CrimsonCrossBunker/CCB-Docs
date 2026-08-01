# CCB-Docs agent instructions / CCB-Docs Agent 指南

This file is sufficient for basic offline work.

## Authority / 权威

- `docs-catalog.yml` is the only manually maintained machine-readable document
  directory.
- CCB runtime behaviour comes from CCB source and tests.
- JSON/Lua/API contracts come from schemas, LuaLS declarations, registrations,
  and generated inventories in CCB.
- Build behaviour comes from CCB CI, CMake, Makefile, Gradle, and validators.
- Governance comes from CCB `AGENTS.md`, `CONTRIBUTING.md`, and `GOVERNANCE.md`.
- If prose conflicts with a contract, mark the page stale and repair the prose.

`docs-catalog.yml` 是机器目录的唯一手工权威；正文不能覆盖 CCB 主仓库契约。

## Map and boundaries / 地图与边界

| Path | Purpose |
| --- | --- |
| `docs/zh_CN/` | Canonical Chinese prose |
| `docs/en/` | Paired English translation |
| `schemas/` | Catalog and generated page-metadata schemas |
| `templates/` | Tutorial, how-to, reference, explanation, API, and archive templates |
| `scripts/` | Catalog generation, builds, links, drift, issue reports |
| `tests/` | Policy and generator regression tests |

- Edit metadata in `docs-catalog.yml`, then run the generator. Do not hand-edit
  generated front matter, `docs/llms*.txt`, or any file under `docs/ai/`.
- New active pages require both languages. Incomplete migration pages are
  drafts and stay out of production navigation, search, and AI indexes.
- Never update every `verified_commit` merely because CCB master advanced.
- Do not auto-merge drift pull requests.

## Validation / 验证

```sh
uv sync --frozen
uv run python scripts/generate_catalog.py --check
uv run python scripts/check_catalog.py
uv run python -m unittest discover -s tests -p 'test_*.py'
uv run flake8 --max-line-length=100 scripts tests
uv run python scripts/build_site.py --strict --include-drafts
uv run python scripts/check_links.py --site-dir site --critical
```
