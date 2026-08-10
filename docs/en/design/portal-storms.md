---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: design-portal-storms
title: 'Legacy migration draft: portal storms'
language: en
status: stale
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
- doc/design-balance-lore/PORTAL_STORM_BALANCE_AND_DESIGN.md
- src/game.cpp
- data/json/effects_on_condition/nether_eocs/portal_storm_effect_on_condition.json
- data/json/mapgen/portal_storm.json
- tests/widget_test.cpp
source_symbols:
- game::portal_storm_query
source_queries: []
source_fingerprint: 9370cc17f5eae8733866149bd28406ce50826f277aa6633dd233c94277c5892a
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 04e3c7876a24ba14b903dd7b2d03fa29da655ff9985625215d5d4b97a7856800
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
stale_reason: 'Source paths changed after d32b9cc880a8: src/game.cpp'
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/portal-storms/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/design/portal-storms/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/portal-storms/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/design/portal-storms/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/design-balance-lore/PORTAL_STORM_BALANCE_AND_DESIGN.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/design-balance-lore/PORTAL_STORM_BALANCE_AND_DESIGN.md
- path: src/game.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/game.cpp
- path: data/json/effects_on_condition/nether_eocs/portal_storm_effect_on_condition.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/effects_on_condition/nether_eocs/portal_storm_effect_on_condition.json
- path: data/json/mapgen/portal_storm.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/mapgen/portal_storm.json
- path: tests/widget_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/widget_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28design-portal-storms%29%3A+&body=Document+ID%3A+design-portal-storms%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: portal storms

This is the migration draft page for `design-portal-storms`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `design-portal-storms`
- Target: `design/portal-storms.md`
- Replacement: design-portal-storms
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| design-portal-storms | doc/design-balance-lore/PORTAL_STORM_BALANCE_AND_DESIGN.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## The role of a portal storm

A portal storm is anomalous weather and an interdimensional collision that changes a player's
plans, not a scheduled boss fight. It should create unease, disruption, and compound pressure, but
must not depend on unwarned damage to kill a character or force every player to sleep through it.
Sound shelter should matter, while a prepared character may choose to travel at genuine risk rather
than with guaranteed safety.

### Passive and active pressure

- **Passive effects** express worlds colliding: anomalous entities, obstacles, sensory interference,
  or temporary environmental changes. They should not actively hunt the player or spend the
  attention resource known as `ire`.
- **Active effects** express malicious entities noticing an exposed character. They may track,
  sabotage, or force route changes, but need the appropriate trigger and an `ire` cost so pressure
  does not stack without bound.
- A themed storm need not reuse identical resource names, but must still explain what is ambient,
  what can target a character, and how a player observes and reduces risk.

Current first-party data still registers `EOC_PORTAL_EFFECTS_PASSIVE` and
`EOC_PORTAL_EFFECTS_ACTIVE` in
`data/json/effects_on_condition/nether_eocs/portal_storm_effect_on_condition.json`. The EOC chain,
related mapgen, and calling code define actual weights, conditions, variables, and effects; this
page does not freeze their numeric values.

## Content review checklist

Limit repeated messages and effect frequency so sound, visuals, and behavior convey the anomaly.
Cover indoor and outdoor boundaries, underground areas and vehicles, sight, sleep and activity
interruptions, NPCs, different senses, save/reload, and repeated storms over time. A new EOC needs
condition, `ire` accounting, failure-path, and repeat-execution validation plus JSON/EOC loading and
focused tests. Long-term ideas such as localized trackable storms or additional themes remain
possible directions, not claims about current implementation.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `9370cc17f5eae8733866149bd28406ce50826f277aa6633dd233c94277c5892a`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/design-balance-lore/PORTAL_STORM_BALANCE_AND_DESIGN.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/design-balance-lore/PORTAL_STORM_BALANCE_AND_DESIGN.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/design-balance-lore/PORTAL_STORM_BALANCE_AND_DESIGN.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
