---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: architecture.subsystem-map
title: Subsystem map
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
- ai/project-map.yml
- src/AGENTS.md
- data/AGENTS.md
- tests/AGENTS.md
- android/AGENTS.md
source_symbols: []
source_queries: []
source_fingerprint: 58261aa7897cf997913620fe4ca007ee9178d1c2395d2e3ab579ad979b8746a1
authority: docs-explanation
verified_commit: 3053bf160578e46c1692a89c60594aa1acc6a276
verified_at: '2026-09-05'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: c5d945384d47e5a1aafb6f39c8e495cee841d3aae379a960a94ed0cefbdd2889
prerequisites:
- architecture.overview
depends_on:
- architecture.project-map
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: architecture
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/subsystem-map/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/subsystem-map/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/subsystem-map/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/subsystem-map/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/3053bf160578e46c1692a89c60594aa1acc6a276
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3053bf160578e46c1692a89c60594aa1acc6a276/AGENTS.md
- path: ai/project-map.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3053bf160578e46c1692a89c60594aa1acc6a276/ai/project-map.yml
- path: src/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3053bf160578e46c1692a89c60594aa1acc6a276/src/AGENTS.md
- path: data/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3053bf160578e46c1692a89c60594aa1acc6a276/data/AGENTS.md
- path: tests/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3053bf160578e46c1692a89c60594aa1acc6a276/tests/AGENTS.md
- path: android/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3053bf160578e46c1692a89c60594aa1acc6a276/android/AGENTS.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28architecture.subsystem-map%29%3A+&body=Document+ID%3A+architecture.subsystem-map%0ALanguage%3A+en%0AVerified+commit%3A+3053bf160578e46c1692a89c60594aa1acc6a276%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Subsystem map

This map helps locate entry points; it does not replace source inspection. Continue with the nearest `AGENTS.md` before editing a target path.

| Subsystem | Primary paths | Common adjacent contracts |
| --- | --- | --- |
| Character / Avatar | `src/character*`, `src/avatar*` | effects, activities, mutation, save |
| Items / Inventory / Pockets | `src/item*`, `src/inventory*`, `src/item_pocket*` | JSON item types, crafting, vehicles |
| Creatures / Monsters | `src/creature*`, `src/monster*` | monster JSON, effects, map |
| Map / Mapgen | `src/map*`, `src/mapgen*` | terrain/furniture, overmap, save |
| Overmap | `src/overmap*` | overmap terrain/special, mapgen |
| Vehicles | `src/vehicle*` | vehicle-part JSON, map, activities |
| Crafting | `src/crafting*`, `src/recipe*` | item IDs, requirements, inventory |
| Mutation / Effects | `src/mutation*`, `src/effect*` | JSON factories, Character, EOC |
| Activities | `src/activity*`, `src/player_activity*` | actors, Character, serialization |
| UI / Input | `src/*ui*`, `src/input*` | SDL/curses, translation, platform |
| Save | `src/savegame*`, `src/save_snapshot*` | every serialized owner, migration |
| Mod loading | `src/mod_manager*`, `data/mods/` | dependencies, JSON load order |
| Lua bridge | `src/lua_platform*`, `data/lua/` | ModDefinition, LuaLS, registrations |
| Localization | `lang/`, `src/translations*` | extraction, PO/MO, UI |
| Android | `android/` | Gradle, JNI/native build, SDL3 |

Tests are organised around behaviour rather than mirroring every source directory. Search for the type, registration name, or stable ID, then find the same symbol and user-visible behaviour under `tests/`. Cross-subsystem changes must state object ownership, lifecycle, serialization, and performance hot paths.
