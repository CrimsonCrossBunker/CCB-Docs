---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: modding-overview
title: 'Legacy migration draft: overview'
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
- doc/MODDING.md
- src/mod_manager.cpp
- src/init.cpp
- src/game_io.cpp
- build-scripts/get_all_mods.py
source_symbols:
- DynamicDataLoader::load_mod_interaction_files_from_path
- game::load_mod_interaction_data_from_dir
source_queries: []
source_fingerprint: 01df11ed2410a7436b91d317d9a7b0843f550d730255abb4d6c637526c226e9b
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 54105e68a8c09c078e03a6988321b0e6c0a2e35fbb2bee8ea8c5b9c7cb48e1d0
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: SpinosaurusBoat, thaelina; accepted inventory identities only. Source
  paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: mods
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/modding/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/modding/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/modding/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/modding/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/MODDING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/MODDING.md
- path: src/mod_manager.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/mod_manager.cpp
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/init.cpp
- path: src/game_io.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/game_io.cpp
- path: build-scripts/get_all_mods.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/build-scripts/get_all_mods.py
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28modding-overview%29%3A+&body=Document+ID%3A+modding-overview%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: overview

This is the migration draft page for `modding-overview`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `modding-overview`
- Target: `modding/overview.md`
- Replacement: modding-overview
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| modding-overview | doc/MODDING.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## History and attribution

Accepted inventory contributors: SpinosaurusBoat, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `01df11ed2410a7436b91d317d9a7b0843f550d730255abb4d6c637526c226e9b`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/MODDING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/MODDING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/MODDING.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
