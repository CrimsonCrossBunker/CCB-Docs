---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: how-to.common-tasks
title: 'Legacy migration draft: common tasks'
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
- doc/DEVELOPER_FAQ.md
- src/monstergenerator.cpp
- src/overmap_terrain.cpp
- src/item_factory.cpp
- src/item_armor.cpp
- tests/monster_test.cpp
source_symbols:
- MonsterGenerator::load_monster
- overmap_terrains::load
- itype::load
source_queries: []
source_fingerprint: 51bcfbc2885b30088566d8c5623f1c4b35f924e720d8d11b5c2b3858a7bab9fa
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 775a0d624efe641d6921065485354412da532b158159f8ec9c1fc7607037f5a5
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- contributing.developer-faq
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: architecture
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
search:
  exclude: true
---

# Legacy migration draft: common tasks

This is the migration draft page for `how-to.common-tasks`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `contributing.developer-faq`
- Target: `how-to/common-tasks.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/common-tasks/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| contributing.developer-faq | doc/DEVELOPER_FAQ.md | merge_into | stubbed | b1ee97987589450da70f30ee2feed12c9d18f479 | how-to.common-tasks |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `51bcfbc2885b30088566d8c5623f1c4b35f924e720d8d11b5c2b3858a7bab9fa`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/DEVELOPER_FAQ.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/DEVELOPER_FAQ.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/DEVELOPER_FAQ.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
