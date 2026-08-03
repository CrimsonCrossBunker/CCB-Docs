---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.map
title: Map subsystem
language: en
status: active
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
- src/map.h
- src/map.cpp
- src/map_iterator.h
- tests/map_test.cpp
source_symbols:
- class map
source_queries: []
source_fingerprint: 549d7bfce1e4851b318b0573ee58374c0dc970e02d66474472a06e33bd986d52
authority: source-and-tests
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 5a939fd0b50343c778cfd2e4cef27495b0cf33d2b38843ff5b0f21bf450f1639
prerequisites:
- architecture.overview
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
risk_group: cpp-map
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/map/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/map/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/map/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/map/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: src/map.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/map.h
- path: src/map.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/map.cpp
- path: src/map_iterator.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/map_iterator.h
- path: tests/map_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/map_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.map%29%3A+&body=Document+ID%3A+cpp.map%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Map

## Responsibility

`map` is the loaded reality-bubble view of submaps. It coordinates terrain, furniture, fields,
traps, items, vehicles, creature-facing queries, pathing, line of sight, caches, and the
load/save boundary for nearby world state.

## Entry points

Start with `class map` in `src/map.h` and the focused `map_*.cpp` implementation. `map::load`,
`map::save`, `shift`, item/field mutators, vehicle-cache maintenance, and `map_iterator` are
the main boundaries.

## Data ownership

Loaded submaps own tile contents and vehicle instances; `map` presents and caches that data.
Creatures are indexed separately. Callers receive references or iterators whose validity is
bounded by map mutation and bubble shifts.

## Dependencies

Map depends on submaps, coordinates, terrain/furniture registries, fields, traps, items,
vehicles, creature tracking, overmap coordinates, lighting, pathfinding, and mapgen.

## Lifecycle

Submaps load around an absolute location, caches build lazily or during load, mutations mark
them dirty, bubble shifts retain/replace regions, and dirty submaps save back to world storage.

## Invariants

Coordinate types match the called API; cache entries reflect tile and vehicle state; one item
or vehicle has one owning submap; and mutations use map methods so transparency, pathing,
outside, floor, and vehicle caches are invalidated.

## Extension points

Add tile behavior through terrain/furniture/field/trap data first. Native operations belong in
a focused map component and must use typed coordinates and centralized mutation helpers.

## Serialization

`map::load` / `save` delegate durable tile state to submap/world serialization. Bubble-relative
coordinates and derived caches are not durable; absolute placement and submap contents are.

## Tests

Use map, iterator, path, memory, bash, field, vehicle, and map-helper tests. Cache changes need a
mutation and query before and after load or shift where relevant.

## Performance

Map queries sit inside rendering, AI, and movement loops. Avoid broad cache invalidation,
repeated coordinate projection, and full-bubble scans; benchmark realistic reality bubbles.

## CCB divergence

CCB may carry map behavior and caches that differ from upstream ports. A shared function name
does not make cache invalidation or save layout equivalent; use CCB tests as the contract.

## Technical debt

`map` remains a large facade over storage, simulation, rendering queries, and caches. Keep new
work in focused components and do not combine cache refactors with gameplay changes.
