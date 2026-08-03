---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: tutorial.mapgen-intermediate
title: 'Legacy migration draft: intermediate'
language: en
status: active
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
last_human_reviewer: LYHGLYTX
source_paths:
- doc/JSON/JSON_Mapping_Guides/Guide_for_intermediate_mapgen.md
- src/mapgen.cpp
- src/mapgen.h
- data/json/mapgen/nested/road_vehicles_nested.json
- tests/nest_conditional_placement_test.cpp
- tests/mapgen_function_test.cpp
source_symbols:
- mapgen_function_json::setup_internal
- jmapgen_objects::load_objects
source_queries: []
source_fingerprint: ba73dc2bf13ed7271634cda4f93ee00a08389742b6b72d9cdf081c0dcec03e54
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 9241c067961ecc73472a752fd5d7078a35cafcbbcf00f2a00365553176ae66a2
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/tutorials/json-mapgen/intermediate/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/tutorials/json-mapgen/intermediate/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/tutorials/json-mapgen/intermediate/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/tutorials/json-mapgen/intermediate/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/JSON_Mapping_Guides/Guide_for_intermediate_mapgen.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_Mapping_Guides/Guide_for_intermediate_mapgen.md
- path: src/mapgen.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/mapgen.cpp
- path: src/mapgen.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/mapgen.h
- path: data/json/mapgen/nested/road_vehicles_nested.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/mapgen/nested/road_vehicles_nested.json
- path: tests/nest_conditional_placement_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/nest_conditional_placement_test.cpp
- path: tests/mapgen_function_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/mapgen_function_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28tutorial.mapgen-intermediate%29%3A+&body=Document+ID%3A+tutorial.mapgen-intermediate%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: intermediate

This is the migration draft page for `tutorial.mapgen-intermediate`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `tutorial.mapgen-intermediate`
- Target: `tutorials/json-mapgen/intermediate.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/tutorials/json-mapgen/intermediate/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| tutorial.mapgen-intermediate | doc/JSON/JSON_Mapping_Guides/Guide_for_intermediate_mapgen.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Nested, merged, and update mapgen

A full variant shares an `om_terrain` ID and replaces the whole map according to weight. Nested
mapgen overlays a local chunk inside a caller. Update mapgen changes an already existing map during
play. Their lifecycles differ, so similar JSON shapes do not make them interchangeable.

### Nested mapgen

The top level uses `nested_mapgen_id` and may provide weighted variants under one ID.
`object.mapgensize` must contain two identical positive numbers; the current implementation still
supports square nests only. Rows, palettes, placements, and nested calls operate in this local
coordinate system. Blank symbols normally preserve the underlying map. Use current null/clear
values or clearing flags when terrain, furniture, items, traps, and fields must be removed rather
than leaving half of the old state.

A caller selects weighted `chunks` through a `nested` symbol or `place_nested` coordinates; `null`
is the valid no-placement candidate. Current nested placement can also test neighbors, joins,
flags, predecessors, and z-level. `jmapgen_nested` and `nest_conditional_placement_test.cpp` define
that behavior. Keep the chunk inside the caller grid and make doors, walls, and traversable edges
consistent across every variant.

### Merged and update mapgen

A two-dimensional `om_terrain` array registers one merged definition at an offset for each OMT; rows
use continuous total coordinates. `common_check_bounds` rejects a coordinate range that crosses its
current grid boundary, so large rows do not mean every placement may span OMTs. Keep vehicles,
range-based spawns, and nests inside one OMT and cover boundaries with focused tests.

`update_mapgen_id` registers a runtime update. Its call site chooses target OMT, parameters,
mirroring/rotation, collision policy, and mission context. An update can collide with player
construction, vehicles, items, and saved state, so document idempotence, conflicts, and repeat
triggering. Do not infer all current trigger paths from an old trap example.

Validate nest weights and conditions, rotation, local clearing, NPCs and vehicles, merged
boundaries, update collision, repeat execution, and save reload. Run JSON and target-mod loading,
focused mapgen/nest/update tests, and debug generation while recording seed, position, direction,
and call parameters.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `ba73dc2bf13ed7271634cda4f93ee00a08389742b6b72d9cdf081c0dcec03e54`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/JSON_Mapping_Guides/Guide_for_intermediate_mapgen.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_Mapping_Guides/Guide_for_intermediate_mapgen.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_Mapping_Guides/Guide_for_intermediate_mapgen.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
