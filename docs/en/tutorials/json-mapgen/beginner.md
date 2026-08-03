---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: tutorial.mapgen-beginner
title: 'Legacy migration draft: beginner'
language: en
status: draft
doc_type: explanation
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 365
last_human_reviewer: Pending human review
source_paths:
- doc/JSON/JSON_Mapping_Guides/Guide_for_beginning_mapgen.md
- src/mapgen.cpp
- src/overmap_terrain.cpp
- data/json/mapgen/abandoned_barn.json
- data/json/overmap/overmap_terrain/overmap_terrain.json
- tests/mapgen_function_test.cpp
- doc/JSON/JSON_Mapping_Guides/JSON_ROOF_MAPGEN.md
- data/json/mapgen/apartment_complex/apartment_complex_roof.json
source_symbols:
- mapgen_function_json::setup_internal
- overmap_terrains::load
source_queries: []
source_fingerprint: fd17455973053269a603ba05b18e7a7b4b5658f7ae492d95b0412d5fbf9db9bd
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 9f3393f0b47df37c099d8e6d13b463844c2758a229f45cf38209e24dbb733507
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- tutorial.mapgen-roofs
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/tutorials/json-mapgen/beginner/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/tutorials/json-mapgen/beginner/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/tutorials/json-mapgen/beginner/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/tutorials/json-mapgen/beginner/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/JSON/JSON_Mapping_Guides/Guide_for_beginning_mapgen.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_Mapping_Guides/Guide_for_beginning_mapgen.md
- path: src/mapgen.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/mapgen.cpp
- path: src/overmap_terrain.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/overmap_terrain.cpp
- path: data/json/mapgen/abandoned_barn.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/mapgen/abandoned_barn.json
- path: data/json/overmap/overmap_terrain/overmap_terrain.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/overmap/overmap_terrain/overmap_terrain.json
- path: tests/mapgen_function_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tests/mapgen_function_test.cpp
- path: doc/JSON/JSON_Mapping_Guides/JSON_ROOF_MAPGEN.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_Mapping_Guides/JSON_ROOF_MAPGEN.md
- path: data/json/mapgen/apartment_complex/apartment_complex_roof.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/mapgen/apartment_complex/apartment_complex_roof.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28tutorial.mapgen-beginner%29%3A+&body=Document+ID%3A+tutorial.mapgen-beginner%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: beginner

This is the migration draft page for `tutorial.mapgen-beginner`. It records **2** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `tutorial.mapgen-beginner, tutorial.mapgen-roofs`
- Target: `tutorials/json-mapgen/beginner.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/tutorials/json-mapgen/beginner/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| tutorial.mapgen-beginner | doc/JSON/JSON_Mapping_Guides/Guide_for_beginning_mapgen.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |
| tutorial.mapgen-roofs | doc/JSON/JSON_Mapping_Guides/JSON_ROOF_MAPGEN.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | tutorial.mapgen-beginner |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Your first JSON mapgen

A spawnable location normally spans three contracts: `mapgen` draws reality-bubble tiles,
`overmap_terrain` supplies OMT IDs, display, and flags, and a `city_building`, region setting, or
`overmap_special` decides world placement. Start from a current similar location and follow loaders
and data references. Do not copy stale upstream paths or treat a filename as registration.

### Minimal flow

1. Define overmap-terrain IDs for each ground, floor, basement, and roof level.
2. Add a `"type": "mapgen"` with `om_terrain` bound to the target ID. Multiple implementations for
   one ID participate according to `weight`.
3. In `object`, provide `fill_ter` and fixed-size `rows`, then explain symbols with terrain,
   furniture, palettes, and placement entries. Row count and width must match the mapgen grid; the
   standard single-OMT size comes from current `SEEX`/`SEEY` constants.
4. Register a city location through current `city_building` and region data, or use an
   `overmap_special` for wilderness placement and connections. Align stairs, ladders, downspouts,
   and roof openings across every z-level point.
5. When using regional groundcover or an existing palette, inspect all inherited effects. Editing a
   shared palette can change unrelated locations.

### Content and probability

Terrain and furniture symbols may share a cell; a cell without explicit terrain uses `fill_ter`.
Item, monster, vehicle, NPC, field, trap, and liquid placements each define their own required
fields, chance/repeat behavior, and coordinate semantics. Do not infer one placement type from
another. Vehicle mount origins and rotation require real generation tests. Overmap monster density
and fixed mapgen spawns solve different problems.

### Validation

Run the project JSON formatter, `make -j2 json-check`, the target mod's `--check-mods`, and focused
mapgen tests. Use debug generation on fresh, previously ungenerated OMTs and cover every weighted
variant, four rotations, z-levels, city/special placement, season/region, loot density, and boundary
connection. Inspect terrain under furniture, door/window reachability, roofs and basements, vehicles
near OMT boundaries, lighting, sight, and save/reload. A submap already generated into a save does
not automatically rebuild after JSON changes and is not a valid sample of the new definition.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `fd17455973053269a603ba05b18e7a7b4b5658f7ae492d95b0412d5fbf9db9bd`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/JSON_Mapping_Guides/Guide_for_beginning_mapgen.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_Mapping_Guides/Guide_for_beginning_mapgen.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_Mapping_Guides/Guide_for_beginning_mapgen.md)
- [`doc/JSON/JSON_Mapping_Guides/JSON_ROOF_MAPGEN.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_Mapping_Guides/JSON_ROOF_MAPGEN.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_Mapping_Guides/JSON_ROOF_MAPGEN.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
