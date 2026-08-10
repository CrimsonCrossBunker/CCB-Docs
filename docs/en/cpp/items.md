---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.items
title: Items subsystem
language: en
status: stale
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- mod-author
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/item.h
- src/item.cpp
- src/item_contents.cpp
- tests/item_test.cpp
source_symbols:
- 'class item : public visitable'
source_queries: []
source_fingerprint: d6d1953d58c7bdcbcabe63f1ef7104c6ff3a8d3d10f70119bf957f7d0e6f0201
authority: source-and-tests
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: db589b513ee116296c0ea65bf66e9e63ee7fcde871406c28f875881a0e2023d8
prerequisites:
- architecture.overview
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-items
risk_level: normal
pending_source_pr: null
stale_reason: 'Source paths changed after d32b9cc880a8: src/item.cpp'
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/items/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/items/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/items/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/items/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: src/item.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/item.h
- path: src/item.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/item.cpp
- path: src/item_contents.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/item_contents.cpp
- path: tests/item_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/item_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.items%29%3A+&body=Document+ID%3A+cpp.items%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Items

## Responsibility

`item` represents one runtime item instance: type identity, charges, damage, flags, variables,
active state, craft state, unique ID, and nested `item_contents`. Static `itype` definitions
are created by `item_factory`; they are not copied into each instance.

## Entry points

Begin with `class item` in `src/item.h`. Use the focused `item_*.cpp` file for naming, armor,
gun/tool/ammo, activation, degradation, or transformation behavior; creation enters through
`item_factory` and persistence through `src/savegame_json.cpp`.

## Data ownership

An item owns its instance fields and contents. Containers own child items through pockets;
`item_location` is a relocatable reference, not ownership. `itype_id` resolves immutable
definition data in the factory.

## Dependencies

Items depend on type registries, pockets, units, flags, use actors, recipes, effects, and the
map/character/vehicle container that currently holds them.

## Lifecycle

Items are spawned from a type, may activate, transform, split, stack, move between owners, and
eventually be consumed or destroyed. `safe_reference` and persistent `item_uid` cover distinct
identity needs and must not be conflated.

## Invariants

Type pointers and IDs agree; nested contents satisfy pocket constraints; stacking compares all
state that affects equivalence; charge-counted items follow their quantity rules; and moves do
not leave stale locations or duplicate UIDs.

## Extension points

Add content through item JSON and existing use actors where possible. Native behavior belongs
in the focused item component, with loader, formatter, save compatibility, and tests updated
together.

## Serialization

`item::serialize` / `deserialize` and `item_contents` persistence live in
`src/savegame_json.cpp`. New fields need defaults for old saves; derived caches and safe
references are not durable state.

## Tests

Select item, contents, pocket, stacking, name, spawn, location, or activation tests according
to the invariant changed. Round-trip any durable instance field.

## Performance

Item visits and name/info generation multiply across large inventories. Avoid recursive scans,
string formatting, or factory lookup in hot predicates when a scoped cached value exists.

## CCB divergence

CCB item JSON and runtime state may intentionally lag, port, or extend upstream contracts.
Compare loaders, save fields, and tests before importing an upstream item change.

## Technical debt

`item` remains a broad type split across many translation units. Keep new features in existing
components and resist adding another cross-cutting flag or unversioned variable convention.
