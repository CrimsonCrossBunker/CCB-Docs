---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.npcs-dialogue
title: 'Legacy migration draft: npcs and dialogue'
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
- doc/JSON/NPCs.md
- src/npc.cpp
- src/npc_class.cpp
- src/npctalk.cpp
- data/json/npcs/missiondef.json
- tests/npc_talk_test.cpp
source_symbols:
- npc_template::load
- npc_class::load
- json_talk_topic::load
source_queries: []
source_fingerprint: c3ae69403c9d1063bb5329654dab7a0ba1529549923508a5620387a10823bb73
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: cf67a987c080d954bbd86810dcb20b259a21e20a23deea85866dcd5d4f1ae102
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: Killa-bite, Standing-Storm, Maleclypse, LunaGlaze, 李诗琪, Anton Simakov,
  Tektolnes, RenechCDDA, thaelina; accepted inventory identities only. Source paths and Git history remain
  authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: eoc
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/eoc/npcs-and-dialogue/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/npcs-and-dialogue/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/eoc/npcs-and-dialogue/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/npcs-and-dialogue/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/JSON/NPCs.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/NPCs.md
- path: src/npc.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/npc.cpp
- path: src/npc_class.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/npc_class.cpp
- path: src/npctalk.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/npctalk.cpp
- path: data/json/npcs/missiondef.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/npcs/missiondef.json
- path: tests/npc_talk_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tests/npc_talk_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.npcs-dialogue%29%3A+&body=Document+ID%3A+json.npcs-dialogue%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: npcs and dialogue

This is the migration draft page for `json.npcs-dialogue`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.npcs-dialogue`
- Target: `reference/eoc/npcs-and-dialogue.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/npcs-and-dialogue/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.npcs-dialogue | doc/JSON/NPCs.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## History and attribution

Accepted inventory contributors: Killa-bite, Standing-Storm, Maleclypse, LunaGlaze, 李诗琪, Anton Simakov, Tektolnes, RenechCDDA, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `c3ae69403c9d1063bb5329654dab7a0ba1529549923508a5620387a10823bb73`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/NPCs.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/NPCs.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/NPCs.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
