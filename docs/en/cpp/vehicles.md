---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.vehicles
title: Vehicles subsystem
language: en
status: draft
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- mod-author
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/vehicle.h
- src/vehicle.cpp
- src/savegame_json.cpp
- tests/vehicle_test.cpp
source_symbols:
- class vehicle
source_queries: []
source_fingerprint: d74074095c884a900419468152311c7e2c9536aee794657a132b4c05f3c56edf
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: b0b38134e343955da3d09ca77b6e62b9819375d152b69d0d817aa460767b177d
prerequisites:
- cpp.map
- cpp.items
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-vehicles
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/vehicles/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/vehicles/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/vehicles/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/vehicles/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: src/vehicle.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/vehicle.h
- path: src/vehicle.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/vehicle.cpp
- path: src/savegame_json.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/savegame_json.cpp
- path: tests/vehicle_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/tests/vehicle_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.vehicles%29%3A+&body=Document+ID%3A+cpp.vehicles%0ALanguage%3A+en%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Vehicles

## Responsibility

`vehicle` models a movable assembly of `vehicle_part` instances, including mounts, cargo,
engines, batteries, controls, faults, labels, zones, power networks, motion, collisions,
autodrive, and interaction.

## Entry points

Read `src/vehicle.h` and focused `vehicle_*.cpp` files. Definition data enters through vehicle
prototypes and part registries; placement integrates with `map`; persistence is implemented in
`src/savegame_json.cpp`.

## Data ownership

A vehicle owns its part vector and part-contained items. Loaded submaps own vehicle instances;
map vehicle caches index their occupied points. A `vehicle_part_location` is a checked locator,
not independent ownership.

## Dependencies

Vehicles depend on map coordinates and caches, item pockets, part/type registries, fuels and
energy units, characters, creatures, zones, activities, and physics calculations.

## Lifecycle

A prototype spawns or a save loads a vehicle; parts install, remove, shift and refresh; the map
tracks movement and collisions; splits create distinct owners; unload/save persists each
assembly.

## Invariants

Part mount coordinates and cached occupied points agree; referenced parts remain valid only
within their documented lifetime; cargo has one owner; power and mass caches invalidate on
part changes; splits do not duplicate parts or labels.

## Extension points

Prefer JSON vehicle parts and prototypes. Native behaviors belong in a focused component and
must update refresh/cache, interaction, serialization, and split rules together.

## Serialization

`vehicle::serialize` / `deserialize` and vehicle-part persistence live in
`savegame_json.cpp`. Derived physics and map caches rebuild; durable part state needs old-save
defaults and migration handling.

## Tests

Use vehicle part, split, power, efficiency, drag, ramp, turret, export, fake-part, interaction,
and mapgen-placement tests according to the change.

## Performance

Movement recalculates occupied tiles and physics frequently. Preserve dirty flags, avoid full
part scans per queried property, and benchmark large moving assemblies.

## CCB divergence

CCB vehicle data and code are selectively ported and may not share upstream cache or save
semantics. Validate against CCB prototypes, tests, and current serialization.

## Technical debt

Parts, caches, physics, power, UI, and persistence remain tightly coupled. Refactors need a
dedicated non-behavioral change with round-trip and movement evidence.
