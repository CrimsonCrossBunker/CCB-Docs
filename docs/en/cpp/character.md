---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.character
title: Character subsystem
language: en
status: active
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/character.h
- src/character.cpp
- src/savegame_json.cpp
- tests/character_modifier_test.cpp
source_symbols:
- 'class Character : public Creature, public visitable'
source_queries: []
source_fingerprint: 676ea9eea3a0095c2353bc1fbe964fd5d5ffdae4ac45f2f8a40f5b242b51e0c1
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 18981a2c728ee2086cc0f845397786036da299f213159c1a0587ff087c5379b4
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
risk_group: cpp-character
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/character/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/character/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/character/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/character/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: src/character.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/character.h
- path: src/character.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/character.cpp
- path: src/savegame_json.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/savegame_json.cpp
- path: tests/character_modifier_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/tests/character_modifier_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.character%29%3A+&body=Document+ID%3A+cpp.character%0ALanguage%3A+en%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Character

## Responsibility

`Character` is the shared native model for human-like actors. It layers stats, body state,
traits, skills, needs, equipment, inventory access, crafting knowledge, and activities on top
of `Creature`; `avatar` and NPC implementations supply the concrete save boundary.

## Entry points

Start at `class Character` in `src/character.h`, then follow the focused
`character_*.cpp` translation unit for the behavior being changed. `initialize`, turn
processing, inventory visits, effect handling, and the pure virtual `serialize` /
`deserialize` boundary are the main integration points.

## Data ownership

The instance owns character-specific mutable state and durable identifiers. It visits rather
than globally owns map and vehicle objects; item ownership is mediated by worn, wielded, and
inventory containers. Static definitions such as traits and professions are ID-backed data.

## Dependencies

`Character` depends on `Creature`, item and pocket traversal, effects, activities, recipes,
mutations, map coordinates, and save JSON. Callers must not bypass those owners' invariants.

## Lifecycle

Construction establishes an uninitialized actor, `initialize` fills defaults, the game loop
updates derived state and activities, and a concrete subclass saves or loads the actor. Actor
conversion and NPC control require identity and ownership to remain coherent.

## Invariants

Character IDs become stable once assigned; base stats and body parts must agree with derived
caches; inventory mutation must invalidate the relevant caches; and position-dependent work
must use the correct coordinate space and current `map`.

## Extension points

Add narrowly scoped behavior in the matching `character_*.cpp`, reuse ID registries for new
data, and add virtual behavior only when both avatar and NPC semantics are defined. Prefer
JSON, EOC, or a supported Lua surface for content-only extensions.

## Serialization

`Character` declares the contract but concrete subclasses serialize it. Durable field changes
must be traced through `src/savegame_json.cpp`, legacy/default handling, and save
compatibility; ephemeral caches should remain explicitly non-serialized.

## Tests

Use focused character, crafting, effect, inventory, mutation, and save/world tests. A change
to derived values needs assertions before and after cache invalidation, not only construction.

## Performance

Turn processing is hot. Avoid repeated whole-inventory visits, registry lookups, and broad
cache rebuilds; preserve the existing invalidation boundaries and measure large inventories.

## CCB divergence

This page asserts no blanket equivalence with an upstream `Character`. CCB retains legacy EOC
and mod-facing state such as `kill_xp`; every upstream port must be checked against CCB's
current save, activity, and Lua boundaries.

## Technical debt

The header records an ongoing, piecewise migration of player logic into `Character`, leaving
many getters, setters, and wide dependencies. New work should reduce coupling locally without
combining that cleanup with behavior changes.
