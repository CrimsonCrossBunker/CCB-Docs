---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.npc-factions
title: 'Legacy migration draft: npc factions'
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
- doc/JSON/FACTIONS.md
- src/faction.cpp
- src/faction.h
- data/json/npcs/factions.json
- tests/faction_price_rules_test.cpp
source_symbols:
- faction_template::load
source_queries: []
source_fingerprint: 4286ef41984cda33091800af8d905c278d43fb2e7037271da4169486e94cfc75
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a7316547f229ed816e820ee74dfe65f69f16f26324ca92ab8e906af89051461c
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/npc-factions/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/npc-factions/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/npc-factions/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/npc-factions/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/JSON/FACTIONS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/FACTIONS.md
- path: src/faction.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/faction.cpp
- path: src/faction.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/faction.h
- path: data/json/npcs/factions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/npcs/factions.json
- path: tests/faction_price_rules_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tests/faction_price_rules_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.npc-factions%29%3A+&body=Document+ID%3A+json.npc-factions%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: npc factions

This is the migration draft page for `json.npc-factions`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.npc-factions`
- Target: `reference/json/npc-factions.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/npc-factions/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.npc-factions | doc/JSON/FACTIONS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## NPC-faction contract

A `FACTION` template is loaded by `faction_template` and later instantiated as a world faction.
The current constructor requires `id`, `name`, `description`, `likes_u`, `respects_u`,
`known_by_u`, `size`, `power`, and `wealth`. Trust, food, currency, price rules, claims, monster
faction, relations, and epilogues are additional contracts.

### Identity, relations, and economy

Faction IDs enter NPCs, dialogue, missions, camps, EOCs, and saves. Display names translate, but IDs
must not be casually renamed. `relations` is a directional bitset keyed by target faction ID; A's
kill, watch, or share relation to B does not guarantee the reverse relation. Validate every target
and relation flag against current registrations.

A `currency` also creates a price rule. Rules can match current item-group criteria and set markup,
premium, fixed adjustment, or price. Trading still depends on NPC, supply, skills, and other systems;
one item is insufficient evidence.

### World state and compatibility

A template initializes a new faction. A save may contain changed likes, respect, trust, wealth, food,
and membership. Editing the template does not migrate an existing world. Before removing or renaming
an ID, design save migration and update every cross-object reference.

Epilogue snippets, monster factions, currency or item groups, and mission IDs need consistency
checks. `known_by_u`, limited-area claims, and lone-wolf behavior need scenario tests.

### Validation

Run formatting, `make -j2 json-check`, `--check-mods`, and faction price, mission, camp, and NPC
dialogue tests. Cover directional relations, theft or attacks, pricing, food and wealth, epilogues,
new and old worlds, Mod combinations, and missing target IDs.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `4286ef41984cda33091800af8d905c278d43fb2e7037271da4169486e94cfc75`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/FACTIONS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/FACTIONS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/FACTIONS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
