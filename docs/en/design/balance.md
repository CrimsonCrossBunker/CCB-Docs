---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: design-balance
title: 'Legacy migration draft: balance'
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
- doc/design-balance-lore/GAME_BALANCE.md
- doc/design-balance-lore/design-balance.md
- GOVERNANCE.md
source_symbols: []
source_queries: []
source_fingerprint: 1d0054d7999d75ae681f7fa6317b6ee70b8c6bdd8b86a97507c1edf1f974fb51
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: df81506bc82134bb6081d97530d94c5e6fb3d040826c9830291b9b58de441a7a
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- legacy.doc-design-balance-lore-game-balance
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
search:
  exclude: true
---

# Legacy migration draft: balance

This is the migration draft page for `design-balance`. It records **2** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `legacy.doc-design-balance-lore-game-balance, design-balance`
- Target: `design/balance.md`
- Replacement: design-balance
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| legacy.doc-design-balance-lore-game-balance | doc/design-balance-lore/GAME_BALANCE.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | design-balance |
| design-balance | doc/design-balance-lore/design-balance.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `1d0054d7999d75ae681f7fa6317b6ee70b8c6bdd8b86a97507c1edf1f974fb51`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/design-balance-lore/GAME_BALANCE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/GAME_BALANCE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/GAME_BALANCE.md)
- [`doc/design-balance-lore/design-balance.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/design-balance.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/design-balance.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
