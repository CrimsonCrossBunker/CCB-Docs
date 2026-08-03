---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.effects
title: 'Legacy migration draft: effects'
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
- doc/JSON/EFFECTS_JSON.md
- src/effect.cpp
- src/effect.h
- data/json/effects.json
- tests/effect_test.cpp
- tests/creature_effect_test.cpp
source_symbols:
- load_effect_type
- effect_type::load_mod_data
- effect_migration::load
source_queries: []
source_fingerprint: 8ec137d6fe7ecf424e3b8578ae092348222e0e81343604637980c88dca9d208c
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 69c8a880a88ac3c55e0d301fe80fd17d51c16f9462e85e627d802817b0b49baf
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
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/effects/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/effects/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/effects/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/effects/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/JSON/EFFECTS_JSON.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/EFFECTS_JSON.md
- path: src/effect.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/effect.cpp
- path: src/effect.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/effect.h
- path: data/json/effects.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/effects.json
- path: tests/effect_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tests/effect_test.cpp
- path: tests/creature_effect_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tests/creature_effect_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.effects%29%3A+&body=Document+ID%3A+json.effects%0ALanguage%3A+en%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: effects

This is the migration draft page for `json.effects`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.effects`
- Target: `reference/json/effects.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/effects/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.effects | doc/JSON/EFFECTS_JSON.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB effect-type data

An `effect_type` defines a persistent status attached to a character or creature: names,
descriptions, intensity, duration, immunity, numerical modifiers, and periodic behavior. It is
not the same object as an Effect on Condition effect command. An EOC can add or remove an
effect type, but an `effect_type` is not an executable script.

### Basic definition

```jsonc
{
  "type": "effect_type",
  "id": "ccb_example_status",
  "name": [ "Example status" ],
  "desc": [ "You are affected by the documentation example." ],
  "max_intensity": 3,
  "max_duration": "1 hour",
  "show_in_info": true
}
```

`load_effect_type` requires a stable `id` and reads per-intensity names and descriptions,
display fields, resist, immune, block, and remove relationships, duration and intensity
evolution, messages, flags, enchantments, and modifier data. Array indexing, fallbacks, and
hardcoded behavior come from `effect.cpp` and its tests.

### Instance lifecycle

A runtime `effect` instance serializes its effect type, duration, body part, permanence,
intensity, start time, and source. Deleting or renaming a released effect ID is therefore a
save-compatibility change and needs an `effect_migration`:

```jsonc
{
  "type": "effect_migration",
  "from": "old_effect_id",
  "to": "ccb_example_status"
}
```

Confirm with current loader and deserialization tests whether omitting `to` represents removal
and when migration occurs. Consistency checking reports a missing target ID.

### Intensity, duration, and modifiers

`max_intensity`, `int_add_val`, decay fields, and `int_dur_factor` combine to control stacking
and decay. Entries below `base_mods` and `scaling_mods` for STR, DEX, PER, INT, speed, pain,
hurt, sleep, and other values use the fixed mapping in `effect_type::load_mod_data`; they are
not arbitrary property names. Bad chance, tick, min, or max combinations can create every-turn
cost or extreme values.

Body-part restrictions, resist traits or effects, immune flags, and block or remove relationships
change whether statuses can be applied or coexist. Cycles and intensity limits need focused
tests, not only a visual check of the status panel.

### Validation

1. Check `load_effect_type` and neighbouring first-party effects for shapes and intensity arrays.
2. Run the formatter, `make -j2 json-check`, and `--check-mods` for the real Mod set.
3. Run relevant `effect_test` or `creature_effect_test` cases for application, stacking, decay,
   immunity, and removal.
4. Test an old save or `effect_migration` for a released ID; never rename it silently.
5. Test periodic modifiers at intensity one, the cap, expiration, and different body parts.

For conditional execution use an [EOC](../eoc/index.md); do not hide scripted side effects in
status data.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`; the aggregate source fingerprint is `8ec137d6fe7ecf424e3b8578ae092348222e0e81343604637980c88dca9d208c`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/EFFECTS_JSON.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/EFFECTS_JSON.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/EFFECTS_JSON.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
