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
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: c1071ebee5db7c6a0c45e8cf701bb02438657b970592421fb31e0c5bbfe22e3d
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/obsoletion-and-migration/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/obsoletion-and-migration/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/obsoletion-and-migration/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/obsoletion-and-migration/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/JSON/OBSOLETION_AND_MIGRATION.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/OBSOLETION_AND_MIGRATION.md
- path: src/item_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/item_factory.cpp
- path: src/effect.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/effect.cpp
- path: src/savegame_json.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/savegame_json.cpp
- path: data/json/obsoletion_and_migration_0.J/migration_items.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/obsoletion_and_migration_0.J/migration_items.json
- path: data/json/obsoletion_and_migration_0.J/eocs.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/obsoletion_and_migration_0.J/eocs.json
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/init.cpp
- path: src/magic.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/magic.cpp
- path: src/proficiency.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/proficiency.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.obsoletion-and-migration%29%3A+&body=Document+ID%3A+json.obsoletion-and-migration%0ALanguage%3A+en%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
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

## Choosing obsoletion and migration

There is no universal migration covering every JSON type. First identify whether an old ID belongs
to items, traits, terrain or furniture, overmap terrain, vehicle parts, effects, spells, Mods, or
another registry. Use that loader's registered migration object. If no loader exists, retain the old
ID or compatibility shim, or implement and test non-behavioral migration support; do not invent a
Schema contract.

### Item `MIGRATION`

Current item migration accepts one or more old `id` values and may set `replace`, `variant`,
`from_variant`, flags, charges, contents, sealed state, and `reset_item_vars`. `replace` cannot equal
the old ID. A variant migration matches only that old variant. Contents that do not fit a normal
container enter a dedicated migration pocket instead of being silently lost.

```jsonc
{
  "type": "MIGRATION",
  "id": "old_item_id",
  "replace": "new_item_id"
}
```

The replacement type must exist when loading and finalizing. Counts, charges, pockets, item
variables, damage, ownership, and sealed state may all need fixtures; changing one ID is not proof
of a complete migration.

### Other registries and Mods

CCB currently registers migrations for traits, bionics, proficiencies, terrain or furniture, fields,
vehicle parts, traps, effects, overmap terrain or specials, camps, spells, global variables, and
Mods, among others. Their fields and abilities differ. `mod_migration` uses an old `id` plus
`new_id`, or a translated `removal_reason` when removed; the target Mod must be valid.

`obsolete: true` generally controls new-content selection and does not rewrite every saved
reference. Retention windows, replacements, release notes, and removed-ID tests remain necessary.

### Validation

Load each real old fixture with current code, inspect migrated objects and nested contents plus map,
character, and world state, then save and load again to prove idempotence and no duplicated
resources. Run formatting, `make -j2 json-check`, `--check-mods`, and owning subsystem tests. Cover
missing targets, chains and cycles, old and new Mods together, and the release boundary for eventual
migration removal.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`; the aggregate source fingerprint is `4061a49a916458a30b17a18ae14969ab456a694b47ee87fef9ac0d7a08a6d979`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/OBSOLETION_AND_MIGRATION.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/OBSOLETION_AND_MIGRATION.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/OBSOLETION_AND_MIGRATION.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
