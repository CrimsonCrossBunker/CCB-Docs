---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: architecture.subsystem-map
title: Subsystem map
language: en
status: draft
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
source_fingerprint: a98974327840d4768d631e096b5e00042003c0e7a60e10d7d9a5ecc967584fa7
authority: docs-explanation
verified_commit: 2c899a3db790e11a6ff44d91f319064b1ee65d2a
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: ee57553c6d74fba8898eb506d3d41920225363885c18c2f865ed2e92bd6b4875
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/560
stale_reason: null
search:
  exclude: true
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
| Lua bridge | `src/catalua*`, `data/lua/` | manifest, LuaLS, registrations |
| Localization | `lang/`, `src/translations*` | extraction, PO/MO, UI |
| Android | `android/` | Gradle, JNI/native build, SDL3 |

Tests are organised around behaviour rather than mirroring every source directory. Search for the type, registration name, or stable ID, then find the same symbol and user-visible behaviour under `tests/`. Cross-subsystem changes must state object ownership, lifecycle, serialization, and performance hot paths.
