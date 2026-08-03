---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.vehicle-prototypes
title: 'Legacy migration draft: vehicle prototypes'
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
- doc/JSON/VEHICLES_JSON.md
- src/veh_type.cpp
- src/veh_type.h
- data/json/road_vehicles.json
- data/json/vehicleparts/vehicle_parts.json
- tests/vehicle_export_test.cpp
source_symbols:
- vehicle_prototype::load
- vehicles::parts::load
source_queries: []
source_fingerprint: c36cc2de2b212cd6775c390386b94d7211f0e1b36e05d6e0123f2f12c395af9a
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: dd539552a7299b5a8c970873abed1d1dc9b02627eccb57b9838f4bfdf4d06e1a
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LunaGlaze, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/vehicle-prototypes/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/vehicle-prototypes/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/vehicle-prototypes/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/vehicle-prototypes/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/JSON/VEHICLES_JSON.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/VEHICLES_JSON.md
- path: src/veh_type.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/veh_type.cpp
- path: src/veh_type.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/veh_type.h
- path: data/json/road_vehicles.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/road_vehicles.json
- path: data/json/vehicleparts/vehicle_parts.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/vehicleparts/vehicle_parts.json
- path: tests/vehicle_export_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tests/vehicle_export_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.vehicle-prototypes%29%3A+&body=Document+ID%3A+json.vehicle-prototypes%0ALanguage%3A+en%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: vehicle prototypes

This is the migration draft page for `json.vehicle-prototypes`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.vehicle-prototypes`
- Target: `reference/json/vehicle-prototypes.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/vehicle-prototypes/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.vehicle-prototypes | doc/JSON/VEHICLES_JSON.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Vehicle prototype contract

A `vehicle` prototype spawns a stock vehicle; the resulting vehicle uses a different save
representation. Its generic factory owns `id`, `parts` is the core structure, and `name`, `items`,
`zones`, and `color_palette` are optional. `blueprint` is currently consumed only for compatibility
and does not drive spawning.

### Parts and installation order

Each part group requires `x`, `y`, and `parts`. An element may be a `vpart_id` string or an object
with `part`; the object can also set 0–100 `ammo`, `ammo_types`, `ammo_qty`, `fuel`, and `tools`.
`part#variant` is split at the last `#` in either form.

Array order is installation order and must satisfy in-game prerequisites for frames, mounts, wheels,
engines, turrets, and stacking. Multiple groups may append at one coordinate, but cannot bypass
installation rules. Limited copy-from applies the parent first and appends parts, items, and zones;
inspect the expanded result rather than only the child object.

### Items, zones, and export

An item spawn requires `x`, `y`, and 0–100 `chance`; it may set `items`, `item_groups`, `magazine`,
and `ammo`. An item may be a string or `{ "id", "variant" }`. A zone requires type, x, and y and may
have name or filter. It is placed only when the vehicle has a faction owner.

The debug exporter can produce parts, selected turret, fuel, and tool state, simple cargo items,
zones, and a visual blueprint. It leaves placeholder ID and name values and does not guarantee a
round trip for complex containers or comestibles. Format and review its output manually.

### Validation

Run formatting, `make -j2 json-check`, and target-Mod `--check-mods`. Spawn a complex prototype in
game and inspect refresh, installation order, cargo, owned zones, and palettes. Changes to export or
fields need a `tests/vehicle_export_test.cpp` case that serializes and reloads equivalent data.

## History and attribution

Accepted inventory contributors: LunaGlaze, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`; the aggregate source fingerprint is `c36cc2de2b212cd6775c390386b94d7211f0e1b36e05d6e0123f2f12c395af9a`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/VEHICLES_JSON.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/VEHICLES_JSON.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/VEHICLES_JSON.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
