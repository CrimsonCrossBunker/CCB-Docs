---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.faction-missions
title: 'Legacy migration draft: faction missions'
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
- doc/JSON/FACTION_MISSIONS.md
- src/faction_mission.cpp
- src/faction_camp.cpp
- data/json/faction_missions.json
- tests/faction_camp_test.cpp
source_symbols:
- faction_mission::load
source_queries: []
source_fingerprint: 06cdbc4c15861847dfbef5486ae1b1c427c73774ff0cc485322ff8a7b5e2cd93
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 07cd2c8cff1fd62af5952e2cc9b375bc0dfd18537b0fef94210dc127e353343a
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/faction-missions/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/faction-missions/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/faction-missions/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/faction-missions/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/FACTION_MISSIONS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/FACTION_MISSIONS.md
- path: src/faction_mission.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/faction_mission.cpp
- path: src/faction_camp.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/faction_camp.cpp
- path: data/json/faction_missions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/faction_missions.json
- path: tests/faction_camp_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/faction_camp_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.faction-missions%29%3A+&body=Document+ID%3A+json.faction-missions%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: faction missions

This is the migration draft page for `json.faction-missions`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.faction-missions`
- Target: `reference/json/faction-missions.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/faction-missions/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.faction-missions | doc/JSON/FACTION_MISSIONS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Faction mission data boundary

The `faction_mission` generic factory currently supplies names, descriptions, and display metadata
for basecamp missions. Target selection, NPC dispatch, rewards or risk, and map mutation remain
largely implemented by C++ consumers such as `faction_camp.cpp`. Adding a JSON object does not create
an executable mission system.

### Loader fields

Name and desc are mandatory. Skill, difficulty, risk, activity, time, positions, items_label,
items_possibilities, effects, and footer are optional. Difficulty and risk accept only NONE,
VERY_LOW, LOW, MEDIUM, HIGH, and VERY_HIGH. Activity must exist in the activity-level map or the
loader reports it as invalid.

Time, effects, and item fields are translated descriptions rather than a structured duration, loot
table, or effect program. They must accurately describe the matching hardcoded consumer and cannot
replace consumer tests.

### Adding or changing a mission

Find camp code and unlock conditions that consume the mission ID before editing its display object.
Check positions, real duration, skill training, food or gear transfer, failure and risk, and repeat
semantics. A new data-driven behavior first needs a public execution contract, loader, and tests;
natural-language effects are not instructions.

### Validation

Run formatting, `make -j2 json-check`, and Mod `--check-mods`. In the camp menu, check zero, one, and
multiple-NPC displays, translations, unavailable reasons, departure and return, and repeat missions.
A new ID or behavior needs focused faction-camp tests and prose that agrees with the implementation.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `06cdbc4c15861847dfbef5486ae1b1c427c73774ff0cc485322ff8a7b5e2cd93`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/FACTION_MISSIONS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/FACTION_MISSIONS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/FACTION_MISSIONS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
