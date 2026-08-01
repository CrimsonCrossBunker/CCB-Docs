---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: mods.in-repository-policy
title: 'Legacy migration draft: in repository policy'
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
- doc/IN_REPO_MODS.md
- CONTRIBUTING.md
- GOVERNANCE.md
- data/mods/AGENTS.md
- src/mod_manager.cpp
- tools/load_all_mods.sh
source_symbols:
- mod_manager::load_modfile
source_queries: []
source_fingerprint: 0e75c77124cf84a936f3bd2f6e19b29d2e7e067eae2b27963fe90dca28aa828e
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 51386b8d3cb82557243fd7f621aad1a377d2bac476fe9764479544715c0ecff3
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
risk_group: mods
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
search:
  exclude: true
---

# Legacy migration draft: in repository policy

This is the migration draft page for `mods.in-repository-policy`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `mods.in-repository-policy`
- Target: `mods/in-repository-policy.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/mods/in-repository-policy/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| mods.in-repository-policy | doc/IN_REPO_MODS.md | migrate_rewrite | stubbed | b1ee97987589450da70f30ee2feed12c9d18f479 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `0e75c77124cf84a936f3bd2f6e19b29d2e7e067eae2b27963fe90dca28aa828e`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/IN_REPO_MODS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/IN_REPO_MODS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/IN_REPO_MODS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
