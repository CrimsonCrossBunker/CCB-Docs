---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.recipes-and-disassembly
title: 'Legacy migration draft: recipes and disassembly'
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
- doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md
- src/recipe.cpp
- src/recipe_dictionary.cpp
- data/json/recipes/armor/other.json
- data/json/uncraft/ammo/10mm.json
- tests/recipe_steps_test.cpp
source_symbols:
- recipe::load
- recipe_dictionary::load
- recipe_dictionary::load_uncraft
source_queries: []
source_fingerprint: 74b3b7fdb8eed201e742fece7ebf19c59fa8f6dfd65fa21b6584d07c1cee067e
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: f0e57fe37e00ec8a5783f145412fb540d18aaf6193ca526078b9d90fedf02571
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: Anton Simakov, RenechCDDA, dobbry-vechur, dumb-kevin, thaelina; accepted
  inventory identities only. Source paths and Git history remain authoritative.'
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

# Legacy migration draft: recipes and disassembly

This is the migration draft page for `json.recipes-and-disassembly`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.recipes-and-disassembly`
- Target: `reference/json/recipes-and-disassembly.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/recipes-and-disassembly/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.recipes-and-disassembly | doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## History and attribution

Accepted inventory contributors: Anton Simakov, RenechCDDA, dobbry-vechur, dumb-kevin, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `74b3b7fdb8eed201e742fece7ebf19c59fa8f6dfd65fa21b6584d07c1cee067e`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
