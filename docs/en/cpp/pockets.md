---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.pockets
title: Item pockets subsystem
language: en
status: draft
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
- src/item_pocket.h
- src/item_pocket.cpp
- src/savegame_json.cpp
- tests/item_pocket_test.cpp
source_symbols:
- class item_pocket
source_queries: []
source_fingerprint: 98aacfc7461dbd18a5fe0cd9f77e9c1af844e04a471e409a529f998891e695b1
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 15058334dbe3ae0dbae6295a3e42f60413af03077ce74702b078e9eb348cd07f
prerequisites:
- cpp.items
depends_on:
- cpp.inventory
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-pockets
risk_level: normal
pending_source_pr: null
stale_reason: null
search:
  exclude: true
---

# Item pockets

## Responsibility

`item_pocket` enforces storage constraints for one compartment: type, volume, weight, length,
liquid/gas sealing, ammo compatibility, flags, priorities, whitelists, and nested contents.

## Entry points

Start with `src/item_pocket.h` and `src/item_pocket.cpp`; parent orchestration is in
`item_contents.cpp`, save code is in `savegame_json.cpp`, and insertion behavior is exercised
by `tests/item_pocket_test.cpp`.

## Data ownership

A pocket owns the items placed in it plus favorite settings and pocket runtime state. Static
capacity/configuration comes from pocket data on the parent item's type.

## Dependencies

It depends on item dimensions and phases, units, ammo types, item locations, parent contents,
characters performing moves, and JSON pocket definitions.

## Lifecycle

Pockets are built from item type data, receive and remove items, seal or unseal, update favorite
settings, and serialize with the parent item. Parent conversion can migrate or spill contents.

## Invariants

Insertion must return a meaningful `contain_code`; capacity and phase constraints hold after
every mutation; an item has one owner; recursive containment cannot create a cycle; sealed
state agrees with pocket capability.

## Extension points

Add a constraint to the centralized containment checks and expose a diagnostic reason. New
preference behavior belongs in `favorite_settings`; do not special-case it in inventory UI.

## Serialization

`item_pocket`, favorite settings, and pocket data deserialize in `savegame_json.cpp`. Missing
fields need stable defaults, and migrations must preserve or explicitly reject contents.

## Tests

Cover each new success and failure code, nested pockets, liquids, weight/volume limits,
whitelist precedence, sealing, and a serialization round trip.

## Performance

Autopickup and inventory organization evaluate many pockets. Keep acceptance checks allocation
free where practical and avoid repeatedly walking nested contents.

## CCB divergence

Pocket rules are a save- and mod-facing contract. Treat upstream pocket changes as migrations,
and verify CCB JSON definitions and tests rather than assuming the same constraints.

## Technical debt

Containment, preference policy, and serialization meet in one broad type. New code should keep
pure feasibility checks separate from mutations and UI decisions.
