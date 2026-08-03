---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: architecture.project-map
title: Project map and authority boundaries
language: en
status: active
doc_type: explanation
audiences:
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- AGENTS.md
- ai/project-map.yml
- ai/test-matrix.yml
- ai/generated-files.yml
source_symbols: []
source_queries:
- Minimal project map
- 'kind: project_map'
source_fingerprint: 6af7fce22d5ddffa4ad3bdda05685e4d7fd8161382c1a42e74abde821be34665
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-01'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 90b4d70c065176f84f4ed848ba0683de783a5603c6447fcfc1db68832035e0b5
prerequisites:
- home
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: project-context
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/project-map/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/project-map/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/project-map/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/project-map/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/AGENTS.md
- path: ai/project-map.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/ai/project-map.yml
- path: ai/test-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/ai/test-matrix.yml
- path: ai/generated-files.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/ai/generated-files.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28architecture.project-map%29%3A+&body=Document+ID%3A+architecture.project-map%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Project map

The project map answers three questions: where to change, what not to change
incidentally, and what to validate afterwards. Root `AGENTS.md` provides the
offline minimum; `ai/project-map.yml` and `ai/test-matrix.yml` provide the
machine-readable form.

## Main areas

| Path | Responsibility | Next step |
| --- | --- | --- |
| `src/` | C++ engine, gameplay, UI, native Lua registration | Read `src/AGENTS.md` and relevant tests |
| `data/json/`, `data/core/` | Core JSON definitions | Check stable IDs, format, and loading |
| `data/lua/`, `tools/lua_api/` | Lua contracts, declarations, inventories, examples | Read `data/lua/AGENTS.md` |
| `data/mods/` | Independent mods shipped with the game | Read the mod README and dependencies |
| `tests/` | Catch2 regression and integration tests | Add focused, reproducible behavioural tests |
| `tools/` | Formatters, validators, generators | Preserve CLI behaviour and provide `--check` |
| `android/` | Android Gradle, Java UI, packaging | Do not commit SDK state, signing data, or APKs |
| `.github/`, build files | CI, build, and release contracts | Use minimum permissions and pinned action SHAs |

## Trace one behaviour

1. Start with observable behaviour, a JSON ID, action name, test name, or log
   text.
2. Use `rg` to find definitions and references instead of reading the source
   tree in directory order.
3. Locate registrations, callers, data loaders, and existing tests.
4. Check `ai/generated-files.yml` before editing generated output.
5. Select the smallest sufficient validation from the test matrix.

## Boundary

The map is navigation, not a runtime specification. Source and tests define
behaviour; schemas, LuaLS declarations, registrations, and generated
inventories define API contracts; build files and CI define builds. If the map
conflicts with those facts, mark and repair the map or this page as stale.
