---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.weather-types
title: 'Legacy migration draft: weather types'
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
- doc/JSON/WEATHER_TYPE.md
- src/weather_type.cpp
- src/weather_type.h
- src/weather_gen.cpp
- data/json/weather_type.json
- tests/weather_test.cpp
source_symbols:
- weather_type::load
- weather_types::load
- weather_generator::load
source_queries: []
source_fingerprint: 99ab7d48f3e59f2838601af2918c484918825859f5a9d6591ff856ccc0d483de
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a74043661e0c7a5ba454667e429006fd2870ffe4e389116ea1a1eaf881a0c36b
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: Anton Simakov, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/weather-types/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/weather-types/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/weather-types/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/weather-types/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/JSON/WEATHER_TYPE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/WEATHER_TYPE.md
- path: src/weather_type.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/weather_type.cpp
- path: src/weather_type.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/weather_type.h
- path: src/weather_gen.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/weather_gen.cpp
- path: data/json/weather_type.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/weather_type.json
- path: tests/weather_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tests/weather_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.weather-types%29%3A+&body=Document+ID%3A+json.weather-types%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: weather types

This is the migration draft page for `json.weather-types`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.weather-types`
- Target: `reference/json/weather-types.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/weather-types/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.weather-types | doc/JSON/WEATHER_TYPE.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Weather types and generators

A `weather_type` describes presentation and runtime effects for one weather, while a
`weather_generator` selects candidates and base climate. They are separate object types. Global
consistency requires valid `null` and `clear` weather IDs.

### Weather-type loader

Name, id, sym, ranged_penalty, sight_penalty, light_modifier, priority, sound_attn, dangerous,
precip, and rains are mandatory. Optional members include UI colors and sun symbol, temperature,
light, and sun modifiers, sound and tiles animation, duration, passive field effects, debug EOCs,
required_weathers, and condition. Duration bounds default to five minutes and minimum cannot exceed
maximum.

Condition runs with dialogue context such as `weather_location`. Candidates are sorted by priority
and required weathers must reference valid IDs. File order is not a stable priority, and historical
sound or precipitation tables are not complete; inspect current enums.

### Weather generator

A generator requires base temperature, humidity, pressure, and wind. It may configure seasonal
adjustments, wind distribution, and a weather whitelist or blacklist. The lists are mutually
exclusive. Finalization filters and sorts by priority, while a whitelist path retains clear.

### Validation

Run formatting, `make -j2 json-check`, Mod `--check-mods`, and focused weather tests. With a fixed
seed cover seasons, locations, condition and priority ties, required chains, duration bounds,
indoor/vehicle passive effects, debug EOCs, light, sight, sound, and whitelists. Weather changes may
affect current saved weather and long-term world generation, so state compatibility and balance
impact.

## History and attribution

Accepted inventory contributors: Anton Simakov, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `99ab7d48f3e59f2838601af2918c484918825859f5a9d6591ff856ccc0d483de`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/WEATHER_TYPE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/WEATHER_TYPE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/WEATHER_TYPE.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
