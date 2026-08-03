---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: lore-factions
title: 'Legacy migration draft: factions'
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
- doc/design-balance-lore/lore-factions.md
- data/json/npcs/factions.json
- src/faction.cpp
- tests/monfactions_test.cpp
source_symbols: []
source_queries: []
source_fingerprint: 2d848c39599906582312af97e6f3698a2062240e8d2aff0162dcec0d4970ee90
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 4b2e25ce8422108548502687e642110bf929b3280084d6dc9391ec05b333c510
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
risk_group: lore
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/lore/factions/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/lore/factions/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/lore/factions/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/lore/factions/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/design-balance-lore/lore-factions.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/lore-factions.md
- path: data/json/npcs/factions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/npcs/factions.json
- path: src/faction.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/faction.cpp
- path: tests/monfactions_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/monfactions_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28lore-factions%29%3A+&body=Document+ID%3A+lore-factions%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: factions

This is the migration draft page for `lore-factions`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `lore-factions`
- Target: `lore/factions.md`
- Replacement: lore-factions
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| lore-factions | doc/design-balance-lore/lore-factions.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Separate design from current implementation

The legacy faction page mixes implemented groups, empty sections, future mission concepts, and
author speculation. It is not a current game-status inventory. First-party faction IDs and base
relations, currency, food, wealth, and epilogue data come from `data/json/npcs/factions.json` and the
`faction` loader. NPCs, dialogue, missions, mapgen, and tests determine whom a player can actually
meet and how they behave. Mark conflicting prose stale and repair it from those sources.

## Faction writing template

A faction page or proposal should distinguish at least:

- **Identity and origin:** how members formed and which facts are player-visible or backstage
  spoilers.
- **Structure and scale:** leadership, membership, dependencies, and geographic reach, labeling a
  number as implemented data or narrative estimate.
- **Goals and limits:** immediate needs, long-term direction, and what the group cannot or will not
  do.
- **Relations:** attitudes toward the player, human groups, mutation or augmentation, and non-human
  powers, including conditions that change them.
- **Bases and economy:** real locations, currency, sources of goods, production capacity, and supply
  bottlenecks.
- **Missions and development:** current mission IDs and dialogue entry points, planned content, and
  stages that alter world or save state.

The Blob, Mycus, triffids, netherum, Exodii, Yrax, and mi-go need not follow a human-state model.
Preserve their different perception, timescale, communication, and values instead of making an
incommunicable power suddenly use ordinary barter or moral language merely to supply a quest.

## Validation

For a faction change, inspect stable IDs, `copy-from`, relation symmetry, monster faction, currency,
price rules, food, epilogues, NPC classes, dialogue talkers, missions, and mapgen references. Run
JSON/EOC loading, duplicate and invalid-ID checks, and relevant faction or monster-faction tests;
exercise first discovery, hostility changes, trade, mission stages, and save/reload in game. Keep
unimplemented diplomacy, bases, and endings draft instead of presenting them as current features.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `2d848c39599906582312af97e6f3698a2062240e8d2aff0162dcec0d4970ee90`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/design-balance-lore/lore-factions.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/lore-factions.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/lore-factions.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
