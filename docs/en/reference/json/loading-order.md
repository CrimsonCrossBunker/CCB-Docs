---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.loading-order
title: 'Legacy migration draft: loading order'
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
- data/json/LOADING_ORDER.md
- doc/JSON/JSON_LOADING_ORDER.md
- src/filesystem.cpp
- src/init.cpp
- src/game_io.cpp
source_symbols:
- DynamicDataLoader::load_data_from_path
- DynamicDataLoader::load_all_from_json
- DynamicDataLoader::finalize_loaded_data
source_queries: []
source_fingerprint: f0979275d95b5694a34e200e0c493b395e64c987686d4ae7488c44253f01d92e
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 31e74e42f3aeea3d2d71dd4176c2fdfa7cc4d630d80617fa94a157c936d3f7ea
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- legacy.data-json-loading-order
- legacy.doc-json-json-loading-order
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

# Legacy migration draft: loading order

This is the migration draft page for `json.loading-order`. It records **2** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `legacy.data-json-loading-order, legacy.doc-json-json-loading-order`
- Target: `reference/json/loading-order.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/loading-order/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| legacy.data-json-loading-order | data/json/LOADING_ORDER.md | merge_into | stubbed | 5f23722ff28c5cc552baa0422b32b1f10fd890fa | json.loading-order |
| legacy.doc-json-json-loading-order | doc/JSON/JSON_LOADING_ORDER.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | json.loading-order |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `f0979275d95b5694a34e200e0c493b395e64c987686d4ae7488c44253f01d92e`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`data/json/LOADING_ORDER.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/LOADING_ORDER.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/LOADING_ORDER.md)
- [`doc/JSON/JSON_LOADING_ORDER.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_LOADING_ORDER.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_LOADING_ORDER.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
