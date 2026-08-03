---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.mutations
title: 'Legacy migration draft: mutations'
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
- doc/JSON/MUTATIONS.md
- src/mutation_data.cpp
- src/mutation.cpp
- data/json/mutations/mutations.json
- data/json/effects_on_condition/mutation_eocs/changing_eocs.json
- tests/mutation_test.cpp
source_symbols:
- mutation_branch::load
- mutation_category_trait::load
- mutation_variant::load
source_queries: []
source_fingerprint: e4b74d434588fa10a89e1938e43cf2456f9ce60905f66484f8381769a4db16ab
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 1943e6b54d0d8706408538bc1ea9cfd9334c2839a7ad243caa54b40f5e48cd49
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/mutations/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/mutations/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/mutations/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/mutations/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/MUTATIONS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/MUTATIONS.md
- path: src/mutation_data.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/mutation_data.cpp
- path: src/mutation.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/mutation.cpp
- path: data/json/mutations/mutations.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/mutations/mutations.json
- path: data/json/effects_on_condition/mutation_eocs/changing_eocs.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/effects_on_condition/mutation_eocs/changing_eocs.json
- path: tests/mutation_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/mutation_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.mutations%29%3A+&body=Document+ID%3A+json.mutations%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: mutations

This is the migration draft page for `json.mutations`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.mutations`
- Target: `reference/json/mutations.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/mutations/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.mutations | doc/JSON/MUTATIONS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB Mutation contract

`mutation` objects are loaded by the `mutation_branch` factory. Current
`mutation_branch::load` requires `name`, `description`, and `points`. Activation, categories,
thresholds, equipment conflicts, and EOCs are separate systems layered onto one stable trait ID.

### Basic definition

```jsonc
{
  "type": "mutation",
  "id": "TRAIT_CCB_EXAMPLE",
  "name": { "str": "Example adaptation" },
  "description": "A documentation-only example.",
  "points": 1,
  "starting_trait": false,
  "purifiable": true,
  "category": [ "MUTCAT_CCB_EXAMPLE" ]
}
```

`points` is character-creation and valuation data, not mutation-selection weight.
`starting_trait`, `random_start_allowed`, `valid`, and `purifiable` govern different entry points.
`variants` supplies weighted names and descriptions for the same trait; it does not create another
stable trait ID.

### Active, passive, and equipment behavior

An active mutation may define `cost`, `time`, and kcal, thirst, sleepiness, mana, or stamina
resources, then use current activation or EOC fields for effects. `starts_active` is meaningful only
for an activatable trait. Validate reflex conditions, on/off messages, and talker semantics as EOC
conditions.

`destroys_gear`, `allow_soft_gear`, body-part or armor changes, and enchantments affect worn items,
anatomy, and caches. Acquisition, removal, purification, variant changes, and save reload can all
update cached state; the character-creation screen is insufficient evidence.

### Categories, thresholds, and relation graphs

A mutation category is a registered object governing vitamins, thresholds, primers or mutagens, and
category strength. Trait `prereqs`, `prereqs2`, `threshreq`, `cancels`, `replacements`, and
additions form a directed graph. Check unreachable nodes, cycles, pre/post-threshold substitution,
and instability effects after changing any edge.

Use the current `trait_migration` contract when removing or renaming a public trait. It can replace
a trait or variant or explicitly remove it. Deleting the old JSON ID alone abandons saves and other
Mods.

### Validation

Run the formatter, `make -j2 json-check`, `--check-mods` for the real Mod set, and relevant
`mutation_test` filters. Cover character creation, mutagen or primer use, purification, thresholds,
bad-mutation odds, active cooldowns, insufficient resources, equipment conflicts, enchantment and
cache updates, NPCs, and save reload. Check translated variants, message arguments, and EOC
true/false paths.

Legacy chemistry and probability explanations can drift; use current mutation source and tests for
system behavior.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `e4b74d434588fa10a89e1938e43cf2456f9ce60905f66484f8381769a4db16ab`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/MUTATIONS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/MUTATIONS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/MUTATIONS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
