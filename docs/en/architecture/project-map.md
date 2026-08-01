---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: architecture.project-map
title: Project map
language: en
status: draft
source_paths:
- AGENTS.md
- ai/project-map.yml
- ai/test-matrix.yml
- ai/generated-files.yml
authority: docs-explanation
verified_commit: 11748581a0df8651380cfb8ae37ae91baafe054d
verified_at: '2026-08-01'
generated: false
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
risk_group: project-context
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/551
stale_reason: null
search:
  exclude: true
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
