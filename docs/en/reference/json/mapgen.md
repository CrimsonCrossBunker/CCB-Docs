---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.mapgen
title: 'Legacy migration draft: mapgen'
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
last_human_reviewer: Pending human review
source_paths:
- doc/JSON/MAPGEN.md
- src/mapgen.cpp
- src/mapgen.h
- src/mapgen_post_process.cpp
- tests/mapgen_function_test.cpp
- tests/mapgen_post_process_test.cpp
source_symbols:
- mapgen_function_json::setup_internal
- update_mapgen_function_json::setup_update
- mapgen_palette::load
- pp_generator::load
source_queries: []
source_fingerprint: 253905cb7a14f68e2ba90a3ae9cb21be544d84da2a8a2e744fa3da643dab4382
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a62beebbff4383e31dbf85d84d31470762f1faf2e4c998d2081f9649e206344a
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: dumb-kevin, ehughsbaird, RenechCDDA, Tektolnes; accepted inventory identities
  only. Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/mapgen/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/mapgen/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/mapgen/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/mapgen/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/JSON/MAPGEN.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/JSON/MAPGEN.md
- path: src/mapgen.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/mapgen.cpp
- path: src/mapgen.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/mapgen.h
- path: src/mapgen_post_process.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/mapgen_post_process.cpp
- path: tests/mapgen_function_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/mapgen_function_test.cpp
- path: tests/mapgen_post_process_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/mapgen_post_process_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.mapgen%29%3A+&body=Document+ID%3A+json.mapgen%0ALanguage%3A+en%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: mapgen

This is the migration draft page for `json.mapgen`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.mapgen`
- Target: `reference/json/mapgen.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/mapgen/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.mapgen | doc/JSON/MAPGEN.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB mapgen model

Mapgen turns one or more overmap terrains (OMTs) into map tiles, furniture, items, creatures,
and other content. A `mapgen` performs initial generation, `nested_mapgen` supplies reusable
chunks, and `update_mapgen` changes an existing map. They share palette and placing syntax but
have different size, background, and lifecycle rules.

### Standalone mapgen

```jsonc
{
  "type": "mapgen",
  "om_terrain": "ccb_example_oter",
  "weight": 1000,
  "object": {
    "fill_ter": "t_grass",
    "rows": [
      "                        "
    ]
  }
}
```

A normal OMT is generally 24 by 24; the example omits the remaining rows and is not directly
loadable. `om_terrain` can name one ID, several IDs, or an OMT grid. In grid form, row dimensions
also expand in blocks of 24. Multiple mapgens for one OMT are selected by `weight`; zero disables
that variant.

`mapgen_function_json::setup_internal` permits `fill_ter`, `predecessor_mapgen`, or
`fallback_predecessor_mapgen` to provide a background. Without one, every character in `rows`
must have a terrain definition in a local or referenced palette. Do not use a space to hide
undefined terrain.

### Rows, palettes, and placings

Mappings for `terrain`, `furniture`, fields, items, monsters, vehicles, traps, computers, zones,
and other entries connect row characters to placings. A named `palette` requires an ID and can
reference other palettes; loops are reported. Parameters and dynamic mapgen values expand the
possible results, so validate every possible ID rather than only the default.

Coordinate placings and character rows can coexist. In a multi-OMT mapgen, random coordinate
ranges must not accidentally cross OMT boundaries. Rotation, mirroring, linear-terrain suffixes,
and multiple z-levels change direction semantics and need structural tests.

### Nested and update mapgen

A `nested_mapgen` requires a positive square `mapgensize` and can replace a region of a parent
mapgen while reusing palettes. An `update_mapgen` needs no fill or row background: it loads an
existing map and applies placings for missions, EOCs, or post-processing. An update is not
automatically idempotent; repeated execution can duplicate items or NPCs, remove structures,
or change a saved map.

Handle an update's target OMT, offset, rotation, and verification failures. Initial worldgen
success does not prove that the same update is safe for an old save.

### Validation

1. Cross-check overmap-terrain and mapgen IDs, special rotation, and connections.
2. Run the formatter, `make -j2 json-check`, and `--check-mods` for the actual Mod set.
3. Run `mapgen_function_test`, plus `mapgen_post_process_test` for post-processing changes.
4. Inspect every variant, rotation, neighbour, z-level, palette parameter, and boundary character.
5. For an update, test first and repeated execution, an old save, missing targets, and occupied maps.

New contributors can start with the [mapgen tutorial](../../tutorials/json-mapgen/beginner.md).
This page defines current loader boundaries, not a substitute for checking source fields.

## History and attribution

Accepted inventory contributors: dumb-kevin, ehughsbaird, RenechCDDA, Tektolnes. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `253905cb7a14f68e2ba90a3ae9cb21be544d84da2a8a2e744fa3da643dab4382`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/MAPGEN.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/MAPGEN.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/MAPGEN.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
