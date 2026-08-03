---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.overmap
title: 'Legacy migration draft: overmap'
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
- doc/JSON/OVERMAP.md
- src/overmap_terrain.cpp
- src/overmap_special.cpp
- src/overmap_connection.cpp
- src/mapgen_post_process.cpp
- tests/overmap_test.cpp
source_symbols:
- overmap_terrains::load
- overmap_special::load
- overmap_connection::load
- pp_generator::load
source_queries: []
source_fingerprint: f5cf038161392828a65260a7f79ad3903e34851999d029d7aa4ce6f34a92c108
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 25bc3fb174b8fe654b4f594bb5a3b4fa1f8b4b3cafb268786183e97536eff096
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: dumb-kevin, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/overmap/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/overmap/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/overmap/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/overmap/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/OVERMAP.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/OVERMAP.md
- path: src/overmap_terrain.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/overmap_terrain.cpp
- path: src/overmap_special.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/overmap_special.cpp
- path: src/overmap_connection.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/overmap_connection.cpp
- path: src/mapgen_post_process.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/mapgen_post_process.cpp
- path: tests/overmap_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/overmap_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.overmap%29%3A+&body=Document+ID%3A+json.overmap%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: overmap

This is the migration draft page for `json.overmap`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.overmap`
- Target: `reference/json/overmap.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/overmap/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.overmap | doc/JSON/OVERMAP.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB overmap data relationships

Overmap data is split across related object types. `overmap_terrain` defines OMT types and
display or connection properties; `overmap_special` composes one or more OMTs under placement
constraints; `overmap_connection` joins linear networks such as roads and subways; mapgen then
builds local maps for the OMTs. A mismatched ID at any layer may appear only during worldgen.

### Overmap terrain and mapgen

A terrain's stable ID can finalize into rotated or linear variants, while mapgen uses its
mapgen ID. Consistency checks report an OMT with neither mapgen nor uniform terrain and validate
static spawn groups. Review a new terrain's:

- name, symbol, colour, vision, and flags;
- rotation, `LINEAR` behavior, and connection directions;
- mapgen ID, uniform terrain, and roof or underground relationships;
- monster density, extras, and location flags;
- compatibility of a released ID with mission targets, saves, and Mods.

Do not hand-build directional suffixes and assume every matcher treats them alike. Where a
field supports exact, type, subtype, prefix, or contains matching, use its current
`ot_match_type` implementation.

### Overmap specials

A fixed special composes OMTs through `overmaps` and connections; a mutable special uses a
different generation model. `occurrences` is mandatory for a real `overmap_special`. City size
or distance, locations, flags, priority, rotation, and connections jointly decide placement.
A special that fits an empty test world is not guaranteed to fit among cities, roads, other
specials, and regional blacklists.

A special can bind an inline EOC, parameters, spawns, and mapgen. Test multi-tile coordinates,
rotation centres, z-levels, and connection endpoints together. Migrating a released special
ID requires the current migration object and a save test.

### Connections and regions

An `overmap_connection` defines connectable terrains and rules. Region settings select the
intra-city and inter-city road, trail, sewer, subway, and rail connections. Changing a
connection or regional reference can reshape newly generated overmaps without rewriting
existing ones, creating old-versus-new save differences.

### Validation

Run the formatter, `make -j2 json-check`, `--check-mods` for the actual Mod set, and relevant
`overmap_test` cases. Generate multiple seeds and regions and inspect special occurrences,
rotation, roads, boundaries, z-levels, mission targets, and no-placement outcomes. Load an old
save for every released ID change.

See [mapgen](mapgen.md) for local tile layout and
[region settings](region-settings.md) for large-scale distribution.

## History and attribution

Accepted inventory contributors: dumb-kevin, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `f5cf038161392828a65260a7f79ad3903e34851999d029d7aa4ce6f34a92c108`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/OVERMAP.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/OVERMAP.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/OVERMAP.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
