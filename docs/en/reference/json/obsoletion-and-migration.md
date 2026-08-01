---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.obsoletion-and-migration
title: 'Legacy migration draft: obsoletion and migration'
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
- doc/JSON/OBSOLETION_AND_MIGRATION.md
- src/item_factory.cpp
- src/effect.cpp
- src/savegame_json.cpp
- data/json/obsoletion_and_migration_0.J/migration_items.json
- data/json/obsoletion_and_migration_0.J/eocs.json
- src/init.cpp
- src/magic.cpp
- src/proficiency.cpp
source_symbols:
- effect_migration::load
- ter_furn_migrations::load
- spell_migration::load
- proficiency_migration::load
source_queries: []
source_fingerprint: 4061a49a916458a30b17a18ae14969ab456a694b47ee87fef9ac0d7a08a6d979
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 77f2b5617a060b0744280d9fcb218c93ca3ba05cb3dec71e1f75ea12422bce00
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
search:
  exclude: true
---

# Legacy migration draft: obsoletion and migration

This is the migration draft page for `json.obsoletion-and-migration`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.obsoletion-and-migration`
- Target: `reference/json/obsoletion-and-migration.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/obsoletion-and-migration/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.obsoletion-and-migration | doc/JSON/OBSOLETION_AND_MIGRATION.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `4061a49a916458a30b17a18ae14969ab456a694b47ee87fef9ac0d7a08a6d979`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/OBSOLETION_AND_MIGRATION.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/OBSOLETION_AND_MIGRATION.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/OBSOLETION_AND_MIGRATION.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
