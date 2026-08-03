---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: getting-started.experienced-index
title: Experienced contributor quick index
language: en
status: active
doc_type: reference
audiences:
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- AGENTS.md
- CONTRIBUTING.md
- ai/project-map.yml
- ai/test-matrix.yml
- ai/generated-files.yml
source_symbols: []
source_queries: []
source_fingerprint: 9a5e0fc3170f372597fe25dcdf125de7c6cddaa8603fe0eaaab604bbdfa3da78
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 0d088e0224b1be9c50195b4a2b4c4bb6bd2b7d680f5c7ef45e45733aaf5f494e
prerequisites:
- home
depends_on:
- architecture.project-map
- validation.quickstart
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
- cpp-format
- json-load
- lua-contract
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: project-context
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/getting-started/experienced-index/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/getting-started/experienced-index/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/getting-started/experienced-index/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/getting-started/experienced-index/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/AGENTS.md
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/CONTRIBUTING.md
- path: ai/project-map.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/ai/project-map.yml
- path: ai/test-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/ai/test-matrix.yml
- path: ai/generated-files.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/ai/generated-files.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28getting-started.experienced-index%29%3A+&body=Document+ID%3A+getting-started.experienced-index%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Experienced contributor quick index

Use this page when you already know a Cataclysm-family codebase and need the CCB-specific boundaries and validation entry points.

## Three rules first

1. CCB source and tests define runtime behaviour; upstream prose does not override CCB implementation.
2. Schemas, LuaLS declarations, registrations, and generated inventories define JSON, Lua, and API contracts.
3. Read the root `AGENTS.md`, then the nearest nested `AGENTS.md` on the path you will edit.

## Route by task

| Task | Inspect first | Narrow validation entry point |
| --- | --- | --- |
| C++ behaviour or UI | `src/` and related `tests/` | `make astyle-check`, then focused tests |
| Core JSON | `data/json/` and its loader/factory | formatter and `make -j2 json-check` |
| EOC | EOC JSON, parser, and tests | JSON format, full load, focused parser test |
| Lua v5 | manifest Schema, LuaLS, native registration, generated inventory | Lua contract checks |
| Bundled mod | `data/mods/<mod>/` and dependencies | load the affected mod set |
| Android | `android/` | Gradle unit tests; name ABI and variant for builds |
| CI or packaging | `.github/workflows/`, `build-scripts/` | matching workflow or narrow local command |
| Agent or docs metadata | `ai/`, `tools/agent/` | Agent metadata tests |

The machine-readable router is `ai/project-map.yml`; `ai/test-matrix.yml` maps paths to checks. Never hand-edit a file registered in `ai/generated-files.yml`.

## CCB and upstream

For a port, record the source repository, exact commit or PR, original authors, license, CCB conflicts, and intentional divergences. Review saves, stable JSON IDs, mods, the Lua API, and desktop/Android differences. Passing upstream tests alone does not establish CCB compatibility.

## Before submission

- name the Responsible human;
- list commands actually run, platform, results, and skipped checks;
- complete documentation impact, related CCB-Docs PR, stable document IDs, and generated-reference impact;
- inspect the final diff for caches, credentials, machine paths, and unrelated formatting.
