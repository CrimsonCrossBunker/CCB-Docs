---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.mapgen
title: Map generation subsystem
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
- src/mapgen.h
- src/mapgen.cpp
- src/mapgendata.h
- tests/mapgen_function_test.cpp
source_symbols:
- class mapgen_function
- class mapgendata
source_queries: []
source_fingerprint: 0b3c8ae0393e04b93c3f693b6ff48eff6c2b478d5e88afd88c806b8d4afc08bb
authority: source-and-tests
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 7dd843b71a513b99479857a00e50c756f7716a3ae595bfd1ce01960c03946165
prerequisites:
- cpp.map
- cpp.overmap
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
- json-load
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-mapgen
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/mapgen/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/mapgen/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/mapgen/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/mapgen/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: src/mapgen.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/mapgen.h
- path: src/mapgen.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/mapgen.cpp
- path: src/mapgendata.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/mapgendata.h
- path: tests/mapgen_function_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/mapgen_function_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.mapgen%29%3A+&body=Document+ID%3A+cpp.mapgen%0ALanguage%3A+en%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Map generation

## Responsibility

Mapgen turns overmap terrain and regional context into submap contents. It dispatches built-in
or JSON mapgen functions, palettes, nested chunks, parameters, joins, rotations, placements,
and post-processing through `mapgendata`.

## Entry points

Start in `src/mapgen.h`, `src/mapgen.cpp`, and `src/mapgendata.h`. JSON implementations derive
from `mapgen_function_json_base`; primitives and post-processing live in focused modules;
asynchronous orchestration is isolated in `mapgen_async`.

## Data ownership

Registries own mapgen definitions and palettes. A `mapgendata` instance carries one generation
context and writes into a target `map`; generated terrain, furniture, items, fields, and
vehicles then belong to the produced submaps.

## Dependencies

Mapgen depends on overmap terrain and specials, region settings, map data registries, RNG,
coordinates, JSON loaders, palettes, and validators for spawned entities.

## Lifecycle

Definitions load and finalize, a request selects an implementation and context, generation
places and transforms content, post-processing enforces regional rules, and the finished
submaps join normal map persistence.

## Invariants

Mapgen IDs and nested references resolve; joins and rotations use the intended orientation;
coordinates stay inside the target; unique placement rules hold; and a fixed seed reproduces
the same contract where determinism is expected.

## Extension points

Prefer JSON mapgen, palettes, nested mapgen, and parameters. Add a built-in generator only for
algorithms data cannot express, register it centrally, and provide seeded tests.

## Serialization

Mapgen definitions are source data, not save records. `mapgen_arguments` can serialize where a
deferred request needs persistence; generated submaps persist through normal map saving.

## Tests

Use function, vehicle placement, post-process, remove-NPC/vehicle, rotation, special, and JSON
load tests. Record the seed and inspect every orientation affected.

## Performance

Generation may run during exploration and can block play. Avoid repeated registry scans and
unbounded rejection loops; profile large or nested generators and asynchronous handoff.

## CCB divergence

CCB's data set and selective worldgen ports define its mapgen behavior. Upstream JSON may rely
on loaders, parameters, or post-processing not present here and must be validated, not copied.

## Technical debt

Built-in and JSON generators share mutable map context but differ in validation. Move common
invariants into validators without changing generation output accidentally.
