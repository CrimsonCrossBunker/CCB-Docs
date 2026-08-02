---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json-item-pricing
title: 'Legacy migration draft: item pricing'
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
- doc/design-balance-lore/POSTAPOC_PRICE_GUIDE.md
- src/faction.cpp
- tests/faction_price_rules_test.cpp
- data/json/npcs/factions.json
source_symbols: []
source_queries: []
source_fingerprint: 6e687bb603c8a92394e06cdc39e80d341da61ee4daeac7c98fab49da2017137b
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 9ef954f62e96a4b00e62d5c429c4e1a703850629b848cb635f1c05cd7ea2c5b5
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
risk_group: design
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/item-pricing/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/item-pricing/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/item-pricing/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/item-pricing/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/design-balance-lore/POSTAPOC_PRICE_GUIDE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/POSTAPOC_PRICE_GUIDE.md
- path: src/faction.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/faction.cpp
- path: tests/faction_price_rules_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tests/faction_price_rules_test.cpp
- path: data/json/npcs/factions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/npcs/factions.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json-item-pricing%29%3A+&body=Document+ID%3A+json-item-pricing%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: item pricing

This is the migration draft page for `json-item-pricing`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json-item-pricing`
- Target: `json/item-pricing.md`
- Replacement: json-item-pricing
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json-item-pricing | doc/design-balance-lore/POSTAPOC_PRICE_GUIDE.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Item prices and trade rules

`price` is the old-world or baseline price and `price_postapoc` is the post-Cataclysm trade baseline;
both use non-negative money units. An NPC quote is not a direct display of either value. Item count,
charges or stack size, contents, trade direction, NPC adjustments, faction or personal price rules,
and currency can all change it.

### Faction rules

A faction `price_rules` entry uses item, group, and related matchers and may set `markup`, `premium`,
`fixed_adj`, or a fixed `price`. The consumer searches from the end and uses the first matching rule.
An NPC personal rule can override the faction rule. Declaring `currency` also adds an equivalent rule
for that currency.

Historical currency anchors, fixed price bands, and a “no item above this limit” statement are balance
advice, not loader or trade-code constraints. Price against current CCB faction data, comparable
items, and the real trade UI, and explain availability, utility, consumption rate, replaceability,
and the target faction.

### Charges and contents

For count-by-charges items, fixed rule prices and base item prices account for stack size or charges.
Loaded magazines, ammo, and container contents may also contribute. Do not treat a whole-stack JSON
price as one charge or compensate for the same factor in item, group, and faction rules.

### Validation

Run formatting, `make -j2 json-check`, and Mod `--check-mods`. A new rule needs NPC-buying and
NPC-selling cases, currency, conditional matching, personal override, charged stacks, and contents in
`tests/faction_price_rules_test.cpp`. A Responsible human reviews balance; tests prove only that the
calculation follows the contract.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `6e687bb603c8a92394e06cdc39e80d341da61ee4daeac7c98fab49da2017137b`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/design-balance-lore/POSTAPOC_PRICE_GUIDE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/POSTAPOC_PRICE_GUIDE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/POSTAPOC_PRICE_GUIDE.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
