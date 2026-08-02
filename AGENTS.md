# CCB-Docs agent instructions / CCB-Docs Agent 指南

This file is sufficient for basic offline work.

## Authority / 权威

- `docs-catalog.yml` is the only checked-in machine-readable document
  directory. Normal entries are maintained there; explicitly marked generated
  blocks remain catalog entries and are owned by their named generator.
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
| `config/` | Maintenance schedules, contract watches, approved baselines |
| `.github/workflows/` | CI, Pages, and scheduled evidence collection |

- Edit metadata in `docs-catalog.yml`, then run the generator. Do not hand-edit
  generated front matter, `docs/llms*.txt`, or any file under `docs/ai/`.
- Do not hand-edit pages whose metadata names
  `scripts/generate_lua_reference.py`; rebuild them from the pinned CCB commit
  in `config/lua-reference-v5.yml`. The source repository remains authoritative.
- JSON/EOC registry pages under `docs/*/reference/` are additionally owned by
  `scripts/generate_json_eoc_reference.py`; regenerate them from the exact CCB
  `verified_commit` instead of editing their bodies.
- The catalog block between `BEGIN/END GENERATED LEGACY MIGRATION PAGES`, its
  paired migration/archive bodies, four partial generated references, and
  `docs/ai/legacy-migration-audit.json` are owned by
  `scripts/generate_legacy_migration.py`. Regenerate them from the exact CCB
  inventory commit in `config/legacy-migration-v1.yml`; never publish rejected
  contributor identities or infer fields absent from the declared sources.
- New active pages require both languages. Incomplete migration pages are
  drafts and stay out of production navigation, search, and AI indexes.
- Never update every `verified_commit` merely because CCB master advanced.
- Do not auto-merge drift pull requests.
- `config/api-contract-baseline.yml` is reviewed evidence. Automation may report
  drift but must not update the accepted fingerprints.
- Site ZIPs, link reports, benchmark observations, and large indexes are CI
  artifacts; do not commit them unless a policy file explicitly lists them.
- Scheduled maintenance may reconcile marker-deduplicated Issues. It must not
  approve a PR, enable a Ruleset, or change organization security settings.
- Record real scheduled-run and administrator evidence in
  `repository-settings.target.yml`. If a human opens a recovery PR after
  organization policy blocks Actions, record it as manual and never claim that
  the Bot created the PR. A 409 repository-setting refusal or 403 organization
  inspection refusal is a human-only organization-owner blocker, not a reason
  to loop or fabricate success.

## Validation / 验证

```sh
uv sync --frozen
uv run python scripts/generate_lua_reference.py \
  --source-repo /path/to/CCB --check --require-luac
uv run python scripts/generate_catalog.py --check
uv run python scripts/check_catalog.py
uv run python scripts/generate_json_eoc_reference.py --source-repo /path/to/CCB --check
uv run python scripts/check_json_eoc_example_mod.py --source-repo /path/to/CCB
uv run python scripts/generate_legacy_migration.py \
  --source-repo /path/to/CCB --check
uv run python -m unittest discover -s tests -p 'test_*.py'
uv run python scripts/check_maintenance_workflows.py
uv run flake8 --max-line-length=100 scripts tests
uv run python scripts/build_site.py --strict --include-drafts \
  --offline-archive artifacts/ccb-docs-offline.zip
uv run python scripts/check_links.py --site-dir site --critical
uv run python scripts/check_site_quality.py --site-dir site
uv run python scripts/check_search.py --site-dir site
```

For browser, accessibility, and performance changes, use Node.js 22 and the
locked QA dependencies:

```sh
npm ci
npm audit --audit-level=high
npx playwright install chromium
npm run qa:browser
npm run qa:lighthouse
```

The browser commands require a loopback listener. If the execution environment
forbids local ports, run all static checks locally and leave Playwright, axe,
visual regression, and Lighthouse to the pinned `Site QA (Node 22)` CI job;
report those commands as not run locally until that job succeeds.

With a local CCB checkout, maintenance reports can be reproduced without
GitHub write access:

```sh
uv run python scripts/generate_maintenance_reports.py api-diff \
  --source-repo /path/to/CCB --json-output /tmp/ccb-api-diff.json
uv run python scripts/generate_maintenance_reports.py docs-coverage \
  --source-repo /path/to/CCB --target-ref HEAD \
  --json-output /tmp/ccb-docs-coverage.json
uv run python scripts/generate_maintenance_reports.py agent-benchmark \
  --source-repo /path/to/CCB --run-source-benchmark \
  --json-output /tmp/ccb-agent-readiness.json
```
