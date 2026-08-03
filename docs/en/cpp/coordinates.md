---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp-coordinates
title: 'Legacy migration draft: coordinates'
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
- doc/c++/POINTS_COORDINATES.md
- src/point.h
- src/coordinates.h
- src/coordinate_conversions.cpp
- tests/coordinate_test.cpp
- tests/point_test.cpp
source_symbols:
- point
- tripoint
source_queries: []
source_fingerprint: 3f3b1575495c26b727ddb4f613ecfed93103166312c54ea30fb3669e4b8e3c0d
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: c94881a1aba488064f5e6f360d13f15cd177c100b828ce518f7ecbf3b1964699
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
risk_group: cpp
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/coordinates/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/coordinates/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/coordinates/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/coordinates/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/c++/POINTS_COORDINATES.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/c++/POINTS_COORDINATES.md
- path: src/point.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/point.h
- path: src/coordinates.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/coordinates.h
- path: src/coordinate_conversions.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/coordinate_conversions.cpp
- path: tests/coordinate_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/coordinate_test.cpp
- path: tests/point_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/point_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp-coordinates%29%3A+&body=Document+ID%3A+cpp-coordinates%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: coordinates

This is the migration draft page for `cpp-coordinates`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `cpp-coordinates`
- Target: `cpp/coordinates.md`
- Replacement: cpp-coordinates
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| cpp-coordinates | doc/c++/POINTS_COORDINATES.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB coordinate types

CCB types encode dimension, origin, and horizontal scale together so a reality-bubble tile cannot
silently become an absolute world OMT. Aliases use
`(tri)point_<origin>_<scale>[_ib]` and are defined by `coords_fwd.h` and `coordinates.h`.

### Origins, scales, and axes

- `rel` is an offset and `abs` uses the fixed world origin.
- `sm`, `omt`, and `om` are relative to a submap, overmap terrain, or overmap corner.
- `bub` is relative to the current reality bubble and changes as map coverage moves.
- `ms`, `sm`, `omt`, `seg`, and `om` are horizontal units from map square to overmap.
- `point` is 2D, `tripoint` includes z, and `_ib` guarantees bounds for the relevant local origin.

x points right, y points down, and positive z points up. Horizontal scale conversion does not scale
z. Current `SEEX/SEEY`, `OMAPX/OMAPY`, and related source constants are authoritative; do not freeze
legacy numeric values as a permanent contract.

### Selection and conversion

Prefer typed points such as `tripoint_abs_ms`, `tripoint_bub_ms`, and `point_abs_omt` in new code.
Use raw `point` or `tripoint` only for mathematics with no game coordinate system. Function
signatures should expose required origin and scale so misuse fails at compile time.

```cpp
tripoint_abs_ms absolute = get_map().getglobal( local );
tripoint_bub_ms local_again = get_map().bub_from_abs( absolute );
point_abs_omt omt = project_to<coords::omt>( absolute.xy() );
```

Use `project_to` to change scale while retaining origin, `project_remain` when a coarse projection
also needs its remainder, and `project_combine` to reconstruct it. Absolute/bubble conversion needs
a specific `map`. Vehicle mount and rotated coordinates use
`vehicle::coord_translate` or `mount_to_tripoint` families, not hand-written rotation offsets.

### Operations and sentinels

Only meaningful type combinations support arithmetic: an absolute position plus a relative offset
is meaningful; two absolute positions added together are not. Select `square_dist`, `trig_dist`,
`rl_dist`, or `manhattan_dist` deliberately. `zero` is an origin; `invalid` and `is_invalid()` are
failure sentinels. Do not use zero to mean unset.

A saved field must serialize coordinates that remain meaningful after reality-bubble movement. NPC
or interruptible-activity targets normally store absolute coordinates rather than avatar-relative
bubble coordinates.

### Validation

Compile affected translation units and run relevant `point_test` and `coordinate_test` filters.
Cover negative coordinates, submap and OMT boundaries, z-levels, map shifts, vehicle rotation, and
serialization round trips. Clang-tidy point checks assist migration but do not replace boundary
tests.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `3f3b1575495c26b727ddb4f613ecfed93103166312c54ea30fb3669e4b8e3c0d`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/c++/POINTS_COORDINATES.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/c%2B%2B/POINTS_COORDINATES.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/c%2B%2B/POINTS_COORDINATES.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
