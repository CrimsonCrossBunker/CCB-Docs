---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json-armor-design
title: 'Legacy migration draft: armor design'
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
- doc/design-balance-lore/ARMOR_BALANCE_AND_DESIGN.md
- src/item_armor.cpp
- src/item_factory.cpp
- data/json/items/armor/torso_armor.json
- tests/item_test.cpp
source_symbols: []
source_queries: []
source_fingerprint: 0d4468c16850762127afe9408b887ea90675b4ce26263150a1e4b8d4f36fc759
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 2ccd806d61f39bddc37ddad016969bb3fc0bd584d09b6bbbd4ad0fb2d1ee3e54
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/armor-design/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/armor-design/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/armor-design/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/armor-design/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/design-balance-lore/ARMOR_BALANCE_AND_DESIGN.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/ARMOR_BALANCE_AND_DESIGN.md
- path: src/item_armor.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/item_armor.cpp
- path: src/item_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/item_factory.cpp
- path: data/json/items/armor/torso_armor.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/items/armor/torso_armor.json
- path: tests/item_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/item_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json-armor-design%29%3A+&body=Document+ID%3A+json-armor-design%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: armor design

This is the migration draft page for `json-armor-design`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json-armor-design`
- Target: `json/armor-design.md`
- Replacement: json-armor-design
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json-armor-design | doc/design-balance-lore/ARMOR_BALANCE_AND_DESIGN.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Armor JSON design and review

Armor combines the item contract with `islot_armor`. Every `armor` portion requires `covers` and can
set coverage, melee, ranged, or vitals coverage, sublocations, encumbrance, materials, layers,
breathability, and environmental protection independently. Top-level fields and inheritance are then
applied to portions, so review the expanded result.

### Geometry, materials, and wearing

`specifically_covers` restricts coverage to sub-bodyparts. Without sublocation data, covering a
parent bodypart covers its subparts. `sided` lets an instance move between left and right. Layers
control clothing conflicts on shared locations; do not replace the current layer enum and runtime
checks with an arbitrary flag or historical table.

A portion material requires type, allows `covered_by_mat` only from 1 through 100, and uses thickness
for that material layer. The loader still accepts the old string-material form but marks it as legacy;
prefer auditable per-portion materials for new content. Real mass, thickness, material, coverage, and
joint mobility drive balance. Do not falsify physical properties to reach a desired defense value.

### Encumbrance, pockets, and ablative armor

Encumbrance may be one value, an empty/full pair, or use a volume modifier. Pocket modifiers,
rigidity, and contents affect the result. An insert in an ablative pocket remains an armor item; audit
its flag restriction, coverage, direct-wearing boundary, and damage or transformation together.

### Minimum-complexity principle

Ordinary clothing should express only the portions it needs. Add advanced materials, per-subpart
layers, special coverage, relic effects, or transforms only for a player-visible distinction. The old
prose's “complete flag list” is not authoritative; the flag registry and consumers are.

### Validation

Start from a current comparable first-party armor and inspect item info, layering conflicts, full and
empty pockets, sides, melee and ranged attacks, and ablative damage. Run formatting,
`make -j2 json-check`, Mod `--check-mods`, and focused item or armor tests for new boundaries. Balance
numbers also need Responsible-human review of their research sources.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `0d4468c16850762127afe9408b887ea90675b4ce26263150a1e4b8d4f36fc759`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/design-balance-lore/ARMOR_BALANCE_AND_DESIGN.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/ARMOR_BALANCE_AND_DESIGN.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/ARMOR_BALANCE_AND_DESIGN.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
