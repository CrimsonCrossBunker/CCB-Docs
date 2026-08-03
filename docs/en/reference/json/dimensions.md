---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.dimensions
title: 'Legacy migration draft: dimensions'
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
- doc/JSON/DIMENSIONS.md
- src/overmap_worldgen.cpp
- src/overmap_worldgen.h
- data/json/region_settings/region_settings/dimensions/dimensions.json
- data/json/effects_on_condition/nether_eocs/dimensions.json
source_symbols:
- dimension_world::load
- dimension_region_layout::load
source_queries: []
source_fingerprint: 9ab637a57079bd6baf25f89931aa6e5d13c24027ea38e460c71fbfdf249a3197
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: c0cbcfbf766baa5a928bc92037d3238e158bc5a1f15b6827e1dee1c3d1fa8e32
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LYHGLYTX, Anton Simakov, Maleclypse, thaelina; accepted inventory identities
  only. Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/dimensions/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/dimensions/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/dimensions/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/dimensions/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/DIMENSIONS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/DIMENSIONS.md
- path: src/overmap_worldgen.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/overmap_worldgen.cpp
- path: src/overmap_worldgen.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/overmap_worldgen.h
- path: data/json/region_settings/region_settings/dimensions/dimensions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/region_settings/region_settings/dimensions/dimensions.json
- path: data/json/effects_on_condition/nether_eocs/dimensions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/effects_on_condition/nether_eocs/dimensions.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.dimensions%29%3A+&body=Document+ID%3A+json.dimensions%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: dimensions

This is the migration draft page for `json.dimensions`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.dimensions`
- Target: `reference/json/dimensions.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/dimensions/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.dimensions | doc/JSON/DIMENSIONS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Dimension definitions and switching

A `dimension` object reads only `region_layout`; finalization reports an invalid reference and falls
back to `default`. Runtime stores non-main dimension world data in the save's dimension area and
switches the currently loaded data during travel. This is not a remote API for arbitrary map reads
or writes in an unloaded dimension.

### Data and EOC boundaries

A new dimension needs a valid `dimension_region_layout` and its region settings. The current layout
implementation supports only UNIFORM, so verify the implementation boundary in the layout page.

`u_travel_to_dimension` performs the switch. `npc_travel_radius` defaults to zero and its filter to
`all`; the consumer evaluates both to select accompanying NPCs. `item_travel_radius` defaults to -1,
meaning no item transfer, while `target_location` can change the collection and placement center.
A vehicle option also exists. Take fields, defaults, and accepted filters from the EOC registry and
`talk_effect_fun::f_travel_to_dimension`; historical snippets are examples only.

`clear_dimension` removes that dimension's persistent world data, so re-entering generates it again.
This loses its map, items, vehicles, monsters, NPCs, and other state. It is a destructive authoring
operation, not routine teleport cleanup.

### Safe workflow

Capture required location variables before travel, switch dimensions, then run mapgen updates or
teleport against the now-loaded dimension. Do not reuse bubble coordinates after the old dimension
is unloaded or assume equal coordinates identify the same place across dimensions.

Run formatting, `make -j2 json-check`, and Mod `--check-mods`. In a disposable world, cover first
creation, round trips, save reload, NPC, item, and vehicle boundaries, invalid-layout fallback, and
regeneration after clear. Never test `clear_dimension` on a valuable save.

## History and attribution

Accepted inventory contributors: LYHGLYTX, Anton Simakov, Maleclypse, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `9ab637a57079bd6baf25f89931aa6e5d13c24027ea38e460c71fbfdf249a3197`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/DIMENSIONS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/DIMENSIONS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/DIMENSIONS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
