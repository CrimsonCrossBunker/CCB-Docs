---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.item-groups
title: 'Legacy migration draft: item groups'
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
- doc/JSON/ITEM_SPAWN.md
- src/item_factory.cpp
- src/item_group.cpp
- data/json/itemgroups/Food/food.json
- tests/item_group_test.cpp
- tests/item_spawn_test.cpp
source_symbols:
- Item_factory::load_item_group
- item_group::load_item_group
- Item_spawn_data::relic_generator::load
source_queries: []
source_fingerprint: 396e03a55ee867b47adbf915b320f8fe9c67208316db94fbab24608855f051be
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 9de57bfabed9db72864e41733bf2882c7da839aaa04facd7b26c50310cb8df15
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: dumb-kevin, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/item-groups/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/item-groups/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/item-groups/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/item-groups/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/JSON/ITEM_SPAWN.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/ITEM_SPAWN.md
- path: src/item_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/item_factory.cpp
- path: src/item_group.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/item_group.cpp
- path: data/json/itemgroups/Food/food.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/itemgroups/Food/food.json
- path: tests/item_group_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tests/item_group_test.cpp
- path: tests/item_spawn_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tests/item_spawn_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.item-groups%29%3A+&body=Document+ID%3A+json.item-groups%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: item groups

This is the migration draft page for `json.item-groups`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.item-groups`
- Target: `reference/json/item-groups.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/item-groups/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.item-groups | doc/JSON/ITEM_SPAWN.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB item-group contract

An `item_group` describes what to spawn; it is not an item definition.
`Item_factory::load_item_group` reads named groups, while `item_group::load_item_group` can
also read anonymous inline groups in monster drops, recipe byproducts, and similar fields.
Referenced item, group, container, and event values must be loaded stable IDs.

### Collection and distribution

```jsonc
{
  "type": "item_group",
  "id": "ccb_example_supplies",
  "subtype": "distribution",
  "entries": [
    { "item": "water_clean", "prob": 70 },
    { "item": "bandages", "prob": 30 }
  ]
}
```

- A `distribution` treats entry `prob` values as relative weights and makes one distribution choice.
- A `collection` evaluates entries independently; `prob` is the percentage chance to include one.
- The old or omitted subtype is treated as a distribution. New data should state its intent.

An entry uses `item` for an item and `group` for another group. `items` and `groups` are
shortcuts for simple IDs and probabilities. Use full `entries` objects for damage, charges,
count, containers, events, faults, variants, or variables. If shortcut arrays and `entries`
are both present, all of them are added; they are not deduplicated.

### Containers, ammunition, and recursion

Group-level `ammo` and `magazine` values are percentage chances used for guns, tools, and
magazines. Explicit entry modifiers such as `charges` can change default loading behaviour.
`container-item`, `container-group`, sealing, and overflow rules affect nesting and capacity.
A multi-magazine-well item cannot distribute one ambiguous `charges` value across its wells;
test it against the current loader and real item definition.

Nested groups can create deep chains. Bad recursion, an empty distribution, or a missing ID
may only become visible during loading or generation. Keep hierarchies shallow and use tests
around `item_group::items_from` for structural invariants rather than only probabilities.

### Extending an existing group from a Mod

The current implementation allows an item group to `copy-from` only a previously loaded group
with the **same ID**, then add entries through `extend`:

```jsonc
{
  "type": "item_group",
  "id": "ccb_example_supplies",
  "copy-from": "ccb_example_supplies",
  "subtype": "distribution",
  "extend": {
    "entries": [ { "item": "aspirin", "prob": 10 } ]
  }
}
```

A same-ID definition without `copy-from` rebuilds or replaces the group; it does not append
implicitly. Load order and Mod dependencies are therefore contractual. Do not assume that
same-ID patches from two Mods can be reordered.

### Inline groups and validation

Some fields accept a group ID, inline object, or entry array. An inline group receives an
internal unique ID and cannot be referenced elsewhere, which suits a one-off drop or
byproduct. Its default subtype is supplied by the calling loader; check that field before
copying an array from another context.

Run the JSON formatter and loader, ID checks, and `--check-mods`. Add focused coverage for
important drops, including empty results, container overflow, charges or magazines, event
gates, and possible recursion. One Debug-menu sample does not prove probability behaviour.

## History and attribution

Accepted inventory contributors: dumb-kevin, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `396e03a55ee867b47adbf915b320f8fe9c67208316db94fbab24608855f051be`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/ITEM_SPAWN.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/ITEM_SPAWN.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/ITEM_SPAWN.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
