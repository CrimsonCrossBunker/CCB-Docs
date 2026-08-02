---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.inventory
title: Inventory subsystem
language: en
status: active
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/inventory.h
- src/inventory.cpp
- src/character_inventory.cpp
- tests/advanced_inventory_test.cpp
source_symbols:
- 'class inventory : public visitable'
source_queries: []
source_fingerprint: 68795ccdc6d58516938058c3abd0f3746c8f3c53290b20d5361c4da21c5cc0ae
authority: source-and-tests
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: ef01bd7cfd6865b84a58bc916ca97dc64bbc88ef325f2072cff48a4a8b24c3f5
prerequisites:
- cpp.items
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
risk_group: cpp-inventory
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/inventory/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/inventory/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/inventory/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/inventory/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: src/inventory.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/inventory.h
- path: src/inventory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/inventory.cpp
- path: src/character_inventory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/character_inventory.cpp
- path: tests/advanced_inventory_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/advanced_inventory_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.inventory%29%3A+&body=Document+ID%3A+cpp.inventory%0ALanguage%3A+en%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Inventory

## Responsibility

`inventory` organizes item stacks for a character or temporary crafting view. It handles
insertion, removal, stacking, inventory letters, pseudo-tools, searches, and cache-backed
queries; it is distinct from pockets and from the inventory UI.

## Entry points

Read `src/inventory.h` and `src/inventory.cpp`; character integration is in
`src/character_inventory.cpp`, temporary crafting views use `form_from_map`/`form_from_zone`,
and presentation belongs to `inventory_ui.cpp`.

## Data ownership

The container owns its `std::list<item>` stacks. A character owns its durable inventory;
temporary inventories may copy or synthesize views, including pseudo-items, and therefore are
not authoritative owners of map or vehicle items.

## Dependencies

Inventory depends on item stacking, visitable traversal, map zones, crafting requirements,
character invlets, and item-location rules.

## Lifecycle

Items are added, restacked, queried, consumed, or removed. Mutators mark ordering and query
caches dirty; temporary crafting inventories are rebuilt from their source scope.

## Invariants

Every item is in exactly one owning container; stack members are actually stackable; invlets
respect assignment policy; and mutators invalidate cached amounts, charges, qualities, and
sorted state.

## Extension points

Add a focused query or mutation only when visitable/item-location APIs cannot express it.
Presentation filters belong in inventory UI; pocket selection policy belongs in pockets.

## Serialization

Inventory is persisted as part of its owning character rather than as an independent global
object. Pseudo-items and query caches are reconstructed and must not become save authority.

## Tests

Use advanced-inventory, temporary crafting inventory, item inventory-color, pickup, and item
location tests. Cache-sensitive changes need a mutation followed by a repeated query.

## Performance

`form_from_map`, restacking, and recursive visits can dominate crafting and UI latency. Use the
bulk-add path only with its documented invlet combinations and preserve source order.

## CCB divergence

CCB contains a bulk insertion path with explicit ordering and invlet constraints. Do not port
inventory optimizations without checking those constraints and CCB performance tests.

## Technical debt

The same type serves durable inventories and synthesized crafting views. Code must keep that
ownership distinction explicit until the roles can be separated safely.
