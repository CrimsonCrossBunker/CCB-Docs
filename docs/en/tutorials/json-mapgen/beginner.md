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
translation_source_fingerprint: c791f2add82774d27cc6f02293c3c9ece7d69afdf2a5a001af2b1a5557c7b670
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

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `fd17455973053269a603ba05b18e7a7b4b5658f7ae492d95b0412d5fbf9db9bd`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/JSON_Mapping_Guides/Guide_for_beginning_mapgen.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_Mapping_Guides/Guide_for_beginning_mapgen.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_Mapping_Guides/Guide_for_beginning_mapgen.md)
- [`doc/JSON/JSON_Mapping_Guides/JSON_ROOF_MAPGEN.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_Mapping_Guides/JSON_ROOF_MAPGEN.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_Mapping_Guides/JSON_ROOF_MAPGEN.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
