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
uv run python scripts/generate_legacy_migration.py --source-repo /path/to/CCB --check
uv run python -m unittest discover -s tests -p 'test_*.py'
uv run python scripts/check_maintenance_workflows.py
uv run flake8 --max-line-length=100 scripts tests
uv run python scripts/build_site.py --strict --include-drafts \
  --offline-archive artifacts/ccb-docs-offline.zip
uv run python scripts/check_links.py --site-dir site --critical
uv run python scripts/check_site_quality.py --site-dir site
uv run python scripts/check_search.py --site-dir site
```

Site browser QA is pinned by `package-lock.json` and runs on Node.js 22 in CI.
After building `site/`, a machine with loopback networking can run:

```sh
npm ci
npm audit --audit-level=high
npx playwright install chromium
npm run qa:browser
npm run qa:lighthouse
```

The browser suite covers same-page language switching, canonical and hreflang
metadata, bilingual search, axe accessibility checks, migration-aware 404s,
and reviewed visual snapshots. Lighthouse enforces performance,
accessibility, best-practice, and SEO budgets. CI and Pages publish the
deterministic `ccb-docs-offline.zip`; extract it and run its bundled
`python3 serve.py` instead of opening pages directly through `file://`.

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

`docs-catalog.yml` v2 is the only checked-in machine-readable document
directory. Normal entries are maintained there; its clearly marked legacy
migration block is regenerated from the pinned CCB inventory. The catalog
generates page front matter, navigation, `llms.txt`, `llms-full.txt`, JSON and
JSONL indexes, bilingual mappings, search/AI allowlists, archive exclusions,
redirects, and sitemap metadata. Files under `docs/ai/` and generated page
front matter must not be edited by hand.

## Long-term maintenance / 长期维护

Scheduled workflows collect evidence without approving or merging changes:

- weekly link, translation-debt, and source-path drift checks;
- monthly documentation coverage and public API contract diffs;
- quarterly Agent benchmark readiness, permissions, and archive audits;
- monthly and validated CCB-release-dispatch snapshots with restore tests;
- monthly Dependabot updates for pinned Actions, npm, and uv lock data.

All schedules also support `workflow_dispatch`, use marker-deduplicated Issues,
publish artifacts and a Job Summary, and have explicit concurrency, timeouts,
and permissions. The source-drift workflow has two no-empty-change guards and
only creates a draft PR; it never auto-merges. Desired Ruleset and security
settings remain declarative in `repository-settings.target.yml` until the
recorded human and organization-policy blockers are resolved.

Reproduce the reports locally with an existing CCB checkout:

```sh
uv run python scripts/generate_maintenance_reports.py docs-coverage \
  --source-repo /path/to/Cataclysm-Cleanwater-Bomb \
  --target-ref HEAD \
  --json-output /tmp/ccb-docs-coverage.json
uv run python scripts/generate_maintenance_reports.py api-diff \
  --source-repo /path/to/Cataclysm-Cleanwater-Bomb \
  --json-output /tmp/ccb-api-diff.json
uv run python scripts/generate_maintenance_reports.py agent-benchmark \
  --source-repo /path/to/Cataclysm-Cleanwater-Bomb \
  --run-source-benchmark \
  --json-output /tmp/ccb-agent-benchmark.json
uv run python scripts/generate_maintenance_reports.py permissions \
  --github-repository CrimsonCrossBunker/CCB-Docs \
  --github-organization CrimsonCrossBunker \
  --github-token-env GITHUB_TOKEN \
  --json-output /tmp/ccb-permissions.json
uv run python scripts/generate_maintenance_reports.py archive \
  --json-output /tmp/ccb-archive.json
```

`config/api-contract-baseline.yml` is intentionally human-reviewed. Scheduled
automation reports missing or changed fingerprints but never rewrites that
baseline. Snapshot ZIPs, reports, and benchmark observation bundles are
artifacts, not source files.

The bilingual JSON/EOC registry bodies are generated from the exact CCB
contract-inventory commit by `scripts/generate_json_eoc_reference.py`. The
current draft indexes 190 JSON object types, 275 EOC conditions, and 306 EOC
effects while preserving every partial/unclassified evidence boundary.

The frozen 175-record legacy Markdown inventory is checked across repositories
by `scripts/generate_legacy_migration.py`. It owns one generated block inside
`docs-catalog.yml`, 99 missing bilingual target pairs, the bilingual
filtered-history experiment report, and
`docs/ai/legacy-migration-audit.json`. Draft and archived outputs remain outside
production navigation, search, and the AI allowlist. The four data-derived
references explicitly index only proven direct fields: 648 JSON flags, 50
proficiencies plus 21 categories, 226 Mind Over Matter spells, and 18
Aftershock item definitions plus 37 item groups.

Chinese source lives in `docs/zh_CN/` and is published at the site root.
English source lives in `docs/en/` and is published under `/en/`.

中文位于 `docs/zh_CN/` 并发布在站点根路径；英文位于 `docs/en/` 并发布到
`/en/`。
