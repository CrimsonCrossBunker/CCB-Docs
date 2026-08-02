---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.region-layout
title: 'Legacy migration draft: region layout'
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
- doc/JSON/REGION_LAYOUT.md
- src/overmap_worldgen.cpp
- src/overmap_worldgen.h
- data/json/region_settings/region_settings/dimensions/dimension_regions.json
source_symbols:
- dimension_region_layout::load
source_queries: []
source_fingerprint: f2a802108a8d9ac03af482ec4deb5d436ba86695b03917b2e1ccdf8cffea0f7e
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 1c194e366ba74060d8a07fb8da9cc25a62468731e3176a6d1e7be310b84706d5
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LYHGLYTX, Anton Simakov; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/region-layout/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/region-layout/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/region-layout/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/region-layout/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/JSON/REGION_LAYOUT.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/REGION_LAYOUT.md
- path: src/overmap_worldgen.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/overmap_worldgen.cpp
- path: src/overmap_worldgen.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/overmap_worldgen.h
- path: data/json/region_settings/region_settings/dimensions/dimension_regions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/region_settings/region_settings/dimensions/dimension_regions.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.region-layout%29%3A+&body=Document+ID%3A+json.region-layout%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: region layout

This is the migration draft page for `json.region-layout`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.region-layout`
- Target: `reference/json/region-layout.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/region-layout/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.region-layout | doc/JSON/REGION_LAYOUT.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## History and attribution

Accepted inventory contributors: LYHGLYTX, Anton Simakov. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `f2a802108a8d9ac03af482ec4deb5d436ba86695b03917b2e1ccdf8cffea0f7e`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/REGION_LAYOUT.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/REGION_LAYOUT.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/REGION_LAYOUT.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
