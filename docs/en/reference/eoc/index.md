---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: eoc.reference
title: 'Legacy migration draft: eoc'
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
- doc/JSON/EFFECT_ON_CONDITION.md
- src/effect_on_condition.cpp
- src/condition.cpp
- src/npctalk.cpp
- data/json/effects_on_condition/example_eocs.json
- tests/npc_talk_test.cpp
source_symbols:
- effect_on_condition::load
- effect_on_conditions::load
- conditional_t::conditional_t
source_queries: []
source_fingerprint: 836e4deb077ab0b5c5a2cfb9efb2ec0b95b8c58a163d733bcd2ede0a9ca2363a
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 91a37b8413beefba55c8e53e5557e7db4ae2100b4ec2f467d3049cf8f383c712
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: zihanZheng, LunaGlaze, Anton Simakov, Maleclypse, GuardianDll, thaelina;
  accepted inventory identities only. Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: eoc
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/eoc/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/eoc/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/JSON/EFFECT_ON_CONDITION.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/EFFECT_ON_CONDITION.md
- path: src/effect_on_condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/effect_on_condition.cpp
- path: src/condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/condition.cpp
- path: src/npctalk.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/npctalk.cpp
- path: data/json/effects_on_condition/example_eocs.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/effects_on_condition/example_eocs.json
- path: tests/npc_talk_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tests/npc_talk_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28eoc.reference%29%3A+&body=Document+ID%3A+eoc.reference%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: eoc

This is the migration draft page for `eoc.reference`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `eoc.reference`
- Target: `reference/eoc/index.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| eoc.reference | doc/JSON/EFFECT_ON_CONDITION.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## History and attribution

Accepted inventory contributors: zihanZheng, LunaGlaze, Anton Simakov, Maleclypse, GuardianDll, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `836e4deb077ab0b5c5a2cfb9efb2ec0b95b8c58a163d733bcd2ede0a9ca2363a`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/EFFECT_ON_CONDITION.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/EFFECT_ON_CONDITION.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/EFFECT_ON_CONDITION.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
