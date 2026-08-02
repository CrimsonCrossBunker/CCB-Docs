---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.terrain-and-furniture
title: 'Legacy migration draft: terrain and furniture'
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
- doc/JSON/MAP_SMASHING.md
- src/mapdata.cpp
- src/mapdata.h
- data/json/bash_damage_profiles.json
source_symbols:
- map_common_bash_info::load
- map_ter_bash_info::load
- map_furn_bash_info::load
source_queries: []
source_fingerprint: c8a95926e96b9f72eca1128b039e2cde13be31e6da58865907ddbf9217d5ba5c
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 1949b42ffeeadfaf63fea77fbb42edf8e117b8bc484e1d488cb640d3206eef50
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- json.map-smashing
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/terrain-and-furniture/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/terrain-and-furniture/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/terrain-and-furniture/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/terrain-and-furniture/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/JSON/MAP_SMASHING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/JSON/MAP_SMASHING.md
- path: src/mapdata.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/mapdata.cpp
- path: src/mapdata.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/mapdata.h
- path: data/json/bash_damage_profiles.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/bash_damage_profiles.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.terrain-and-furniture%29%3A+&body=Document+ID%3A+json.terrain-and-furniture%0ALanguage%3A+en%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: terrain and furniture

This is the migration draft page for `json.terrain-and-furniture`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.map-smashing`
- Target: `reference/json/terrain-and-furniture.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/terrain-and-furniture/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.map-smashing | doc/JSON/MAP_SMASHING.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | json.terrain-and-furniture |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Terrain, furniture, and bashing contracts

Terrain and furniture `bash` objects share fields loaded by `map_common_bash_info`, followed by
replacement fields from `map_ter_bash_info` or `map_furn_bash_info`. CCB stores unfinished bash
damage on the map tile. Reaching the active `str_max` value, including a blocked or supported
variant, replaces the object and clears accumulated damage.

### Strength and damage profiles

`str_min` is the armor threshold applied to each damage type and `str_max` is the object's effective
HP. `damage_to()` applies the selected `bash_damage_profile` multiplier to each weapon damage type,
subtracts the threshold from each result, and accumulates only positive values. During finalization,
valid damage types omitted by the profile receive that type's `bash_conversion_factor`. The default
profile explicitly names bash and receives all other valid types through finalization.

The historical statement that HP equals `str_max - str_min` is therefore no longer accurate. Do not
predict results from character strength or one bash number alone: weapon damage composition,
profile, blocked or supported state, and existing map damage all affect destruction.

### Common fields and replacements

- `profile` references a `bash_damage_profile` and defaults to `default`.
- `str_min_blocked`/`str_max_blocked` and `str_min_supported`/`str_max_supported` are conditional
  replacements.
- `items`, `sound*`, `hit_field`, `destroyed_field`, `explosive`, and tent or collapse fields control
  side effects.
- Terrain must provide `ter_set`; `ter_set_bashed_from_above` defaults to it.
- Furniture may omit `furn_set`, which defaults to `f_null`.

Use the three loaders for requiredness and defaults rather than inferring a contract from occurrence
counts in existing JSON.

### Changes and validation

A new profile must use valid damage types and non-negative multipliers and pass factory finalization
and checks. For a terrain or furniture `bash` change, inspect replacement IDs, item groups, field
spawns, bashing from above, support or blocking, and accumulated-damage reset together. Run the JSON
formatter and `make -j2 json-check`, then add a focused `tests/map_bash_test.cpp` case for behavioral
changes. Mod combinations also need a real `--check-mods` run.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `c8a95926e96b9f72eca1128b039e2cde13be31e6da58865907ddbf9217d5ba5c`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/MAP_SMASHING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/MAP_SMASHING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/MAP_SMASHING.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
