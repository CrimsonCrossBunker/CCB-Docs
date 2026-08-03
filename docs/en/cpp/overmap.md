---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.overmap
title: Overmap subsystem
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
- src/overmap.h
- src/overmap.cpp
- src/overmapbuffer.cpp
- tests/overmap_test.cpp
source_symbols:
- class overmap
source_queries: []
source_fingerprint: 4f1c926269074f731ddaf35e690803968df3af0b87142ae1d011333e858511ef
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: ee342328cb87cb48e7d7df8792b3ad573fb8d7b4a9057e89b21dd743436eb6d0
prerequisites:
- architecture.overview
depends_on:
- cpp.map
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-overmap
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/overmap/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/overmap/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/overmap/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/overmap/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: src/overmap.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/overmap.h
- path: src/overmap.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/overmap.cpp
- path: src/overmapbuffer.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/overmapbuffer.cpp
- path: tests/overmap_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/tests/overmap_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.overmap%29%3A+&body=Document+ID%3A+cpp.overmap%0ALanguage%3A+en%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Overmap

## Responsibility

`overmap` stores one large-scale world region: overmap terrain, cities, roads and connections,
special placements, monster groups, NPC/camp references, notes, visibility, and regional world
generation state. `overmapbuffer` coordinates regions.

## Entry points

Read `src/overmap.h` and focused `overmap_*.cpp` files. Region retrieval and cross-boundary
queries enter through `overmapbuffer`; `overmap::save`, `serialize`, and `unserialize` define
the persistence boundary.

## Data ownership

An overmap owns regional terrain layers and deferred world-scale records. The buffer owns or
caches loaded overmap objects. A loaded reality-bubble monster is not the same ownership form
as an overmap monster-group entry.

## Dependencies

Overmap depends on absolute overmap coordinates, terrain/special/connection registries,
regional settings, mapgen placement, monster groups, cities, weather, NPCs, and world storage.

## Lifecycle

A region is generated or loaded, linked to neighboring regions, queried and updated while the
world runs, then serialized and evicted according to buffer policy.

## Invariants

Absolute coordinates identify the correct region and local cell; connections agree at region
borders; unique specials obey placement state; and loaded/unloaded creature transitions do not
duplicate population.

## Extension points

Prefer JSON overmap terrain, specials, locations, and connections. Native generation belongs in
a focused module with deterministic placement tests and explicit neighboring-region behavior.

## Serialization

`src/savegame.cpp` persists terrain layers, groups, NPC/camp data, notes, and global overmap
state. Caches and generated summaries are rebuildable; new durable fields need old-save defaults.

## Tests

Use overmap, noise, connection, cache, special-placement, and worldfactory tests. Generation
regressions must report a seed and test region boundaries.

## Performance

World travel and generation can touch many regions. Avoid forcing loads for read-only queries,
and keep map-data summaries and route searches bounded.

## CCB divergence

CCB's overmap generation and POI handling have project-specific fixes and selective upstream
ports. Validate deletion, placement, and persistence against current CCB tests and data.

## Technical debt

Generation, runtime queries, UI data, and persistence still meet in a broad regional object.
Preserve buffer ownership and split work by responsibility rather than adding global scans.
