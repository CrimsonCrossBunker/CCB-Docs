---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.items
title: 'Legacy migration draft: items'
language: en
status: stale
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
last_human_reviewer: LYHGLYTX
source_paths:
- doc/JSON/ITEM.md
- src/item_factory.cpp
- src/item_factory.h
- data/json/items/generic.json
- data/json/items/classes/gun.json
- tests/item_test.cpp
source_symbols:
- itype::load
- items::load
- islot_comestible::deserialize
source_queries: []
source_fingerprint: 8c6c2be386b3355ef5417fc38ec2aec753b5e70c63f0c5ed32d1276368406906
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: cba127e56f71350f0eed28cf4cae7557fd01aa8cd32cef2e60d57d16dc5e40f9
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LunaGlaze, Standing-Storm, zihanZheng, Anton Simakov, EArias, RenechCDDA,
  dumb-kevin, thaelina; accepted inventory identities only. Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: 'Source paths changed after d32b9cc880a8: data/json/items/generic.json'
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/items/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/items/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/items/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/items/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/ITEM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/ITEM.md
- path: src/item_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/item_factory.cpp
- path: src/item_factory.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/item_factory.h
- path: data/json/items/generic.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/items/generic.json
- path: data/json/items/classes/gun.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/items/classes/gun.json
- path: tests/item_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/item_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.items%29%3A+&body=Document+ID%3A+json.items%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: items

This is the migration draft page for `json.items`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.items`
- Target: `reference/json/items/index.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/items/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.items | doc/JSON/ITEM.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB item JSON model

CCB loads pickupable entities through `"type": "ITEM"`. `itype::load` reads common fields,
then `subtypes` determines whether armour, tool, gun, ammunition, and other slots are read.
The legacy field list is a navigation aid, not a contract. Required fields, defaults, ranges,
and combinations come from the current loader, registrations, tests, and the
[JSON object-type index](../index.md).

### Minimal definition and stable IDs

```jsonc
{
  "type": "ITEM",
  "id": "ccb_example_part",
  "name": { "str": "example part" },
  "description": "A component used by the documentation example.",
  "symbol": ";",
  "color": "light_gray",
  "weight": "100 g",
  "volume": "250 ml",
  "price": "1 USD",
  "price_postapoc": "10 cent",
  "material": [ "steel" ]
}
```

An `id` is a long-lived reference used by saves, recipes, item groups, EOCs, and Mods. Do
not rename a released ID merely for tidiness. If replacement is necessary, check the
migration or obsoletion mechanism and save compatibility first. Player-visible `name` and
`description` values must be translatable; an ID is not display text.

### Subtypes and slots

The current `itype::load_slots` recognizes `ARMOR`, `TOOL`, `PET_ARMOR`, `GUN`, `GUNMOD`,
`AMMO`, `MAGAZINE`, `COMESTIBLE`, `BOOK`, `BIONIC_ITEM`, `TOOLMOD`, `ENGINE`, `WHEEL`,
`SEED`, `BREWABLE`, `COMPOSTABLE`, `MILLING`, and `ARTIFACT`. An ammunition definition,
for example, declares its slot explicitly:

```jsonc
{
  "type": "ITEM",
  "id": "ccb_example_round",
  "copy-from": "223",
  "subtypes": [ "AMMO" ],
  "name": { "str_sp": "example round" },
  "ammo_type": "223"
}
```

- `subtypes` controls which slot fields this definition reads. Do not omit a child's intent
  merely because its parent has a slot.
- `PET_ARMOR` and `ARMOR` cannot be declared together. `GUNMOD` already loads the tool-mod
  slot and cannot be combined with `TOOLMOD`.
- Other compatible subtypes may be combined, but each slot can add mandatory fields and
  finalization checks.

### Common fields and inheritance

Common fields cover dimensions and mass, prices, materials, display, melee or thrown data,
flags, qualities, use actions, pockets, variants, and variables. Do not infer every field
from one example: some use unit strings, some read stable IDs, and some have dedicated
readers.

`copy-from` first copies a base definition. A directly specified top-level field replaces
its value; supported container fields may use `extend` or `delete`; supported numeric or
special objects may use `relative` or `proportional`. These operations are not a universal
schema for every field. See [inheritance](../inheritance.md) and choose a current neighbour
with the same subtype as an example.

### Change and validation sequence

1. Confirm `type`, `subtypes`, field shapes, and ID references in nearby first-party data.
2. Check `itype::load` and the relevant slot `deserialize` method for requirements and ranges.
3. Format only changed files and inspect every extra formatter diff.
4. Run `make -j2 json-check`; add focused pocket, use-action, recipe, or save-ID tests when relevant.
5. For a Mod, run `--check-mods` with the actual Mod set and record untested platforms or interactions.

Formatting alone does not prove loader, ID, or gameplay relationships. Where Schema coverage
is incomplete, the source loader and tests win.

## History and attribution

Accepted inventory contributors: LunaGlaze, Standing-Storm, zihanZheng, Anton Simakov, EArias, RenechCDDA, dumb-kevin, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `8c6c2be386b3355ef5417fc38ec2aec753b5e70c63f0c5ed32d1276368406906`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/ITEM.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/ITEM.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/ITEM.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
