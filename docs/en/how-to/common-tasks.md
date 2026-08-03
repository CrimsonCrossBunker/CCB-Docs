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
translation_source_fingerprint: 5acb20890aac2502fa29ce71a3d06e2e3b162734a9f7c39384543f973b6853c6
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/how-to/common-tasks/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/common-tasks/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/how-to/common-tasks/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/common-tasks/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/DEVELOPER_FAQ.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/DEVELOPER_FAQ.md
- path: src/monstergenerator.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/monstergenerator.cpp
- path: src/overmap_terrain.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/overmap_terrain.cpp
- path: src/item_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/item_factory.cpp
- path: src/item_armor.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/item_armor.cpp
- path: tests/monster_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tests/monster_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28how-to.common-tasks%29%3A+&body=Document+ID%3A+how-to.common-tasks%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
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

## Current contribution routes

The old FAQ's instructions around `omdata.h`, large `switch` statements,
`player::activate_bionic`, and direct `iuse` registration are not current procedures.
Start from the loader for the data type, a neighbouring first-party JSON example, and
the relevant tests. Only then decide whether a C++ extension is actually required.

### Add or change a monster

1. Find a similar `MONSTER` definition under `data/json/` or the target Mod and copy the
   smallest working example.
2. Use a globally unique ID. Update the relevant monster group if the monster should
   spawn naturally; adding the type alone does not place it in the world.
3. Reuse item groups for drops and prefer existing JSON actors or EOC capabilities for
   special attacks. Change native registration only when the public data contract cannot
   represent the behaviour.
4. Run JSON formatting and loading checks, then the narrowest applicable filter from
   `tests/monster_test.cpp`.

`MonsterGenerator::load_monster` delegates definitions to the monster factory. Later
consistency checks also validate species, harvest data, ammunition, and referenced IDs,
so successful JSON parsing does not prove that a definition is complete.

### Add an overmap terrain or building

1. Decide whether the change is an overmap terrain, an overmap special, or mapgen; these
   are different layers.
2. Select a current example from `data/json/overmap/`, the target Mod, and adjacent mapgen
   definitions.
3. Declare orientation, connection, city placement, or wilderness-special relationships
   that the feature needs.
4. Run JSON loading plus the relevant mapgen or overmap tests. Do not copy the legacy
   hard-coded enum and `draw_map` switch procedure.

`overmap_terrains::load` feeds a factory, and later consistency checks resolve mapgen IDs
and spawn groups. Validate both overmap placement and the mapgen it selects.

### Add an item, armour, or use action

1. Start from the current object type and a neighbouring definition. Confirm `copy-from`,
   required fields, and defaults.
2. For armour, review pockets, coverage, materials, layers, and hit-location semantics.
   The protection sequence in the legacy FAQ is not a stable formula.
3. Prefer an existing use action, EOC, or Lua API. Add a native action only when a public
   contract cannot express the behaviour, and update registration, tests, and documentation
   impact together.
4. Run JSON formatting, loading, ID checks, and the affected focused test.

`itype::load` reads mass, volume, length, prices, and subtype slots before later factory
finalization and checks. Follow the whole load lifecycle instead of relying on one example.

### Minimum pre-PR loop

- Use the nearest `AGENTS.md` and `ai/test-matrix.yml` to select the narrowest validation.
- Fill Documentation impact, Related CCB-Docs PR, Affected documentation IDs, Generated
  reference impact, and Responsible human.
- Record the commands, platform, and actual results. Explain skipped checks; do not hide a
  focused failure behind an unrelated full test run.
- If a public Schema, LuaLS declaration, registration, or generated inventory changes,
  regenerate the reference and inspect the diff.

Continue with [common tasks](../getting-started/common-tasks.md), the
[JSON overview](../json/overview.md), the [EOC overview](../eoc/overview.md), and
the [testing strategy](../validation/testing.md).

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `51bcfbc2885b30088566d8c5623f1c4b35f924e720d8d11b5c2b3858a7bab9fa`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/DEVELOPER_FAQ.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/DEVELOPER_FAQ.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/DEVELOPER_FAQ.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
