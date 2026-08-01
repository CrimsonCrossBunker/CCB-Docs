---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.avatar
title: Avatar subsystem
language: en
status: draft
doc_type: reference
audiences:
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/avatar.h
- src/avatar.cpp
- src/savegame_json.cpp
- tests/new_character_test.cpp
source_symbols:
- 'class avatar : public Character'
source_queries: []
source_fingerprint: baff9146ea4183f1cf2e0de2ace20b9a1fbd1c5d6f5ea61d8fb9247021285d12
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: bb72d2a0ebdb8ba5fbd91491ebc59b2d83acd5be495cbf92ce2e24cf4e10897a
prerequisites:
- cpp.character
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
risk_group: cpp-avatar
risk_level: normal
pending_source_pr: null
stale_reason: null
search:
  exclude: true
---

# Avatar

## Responsibility

`avatar` is the concrete, player-controlled `Character`. It adds character creation,
templates, player identity, map memory, control transfer, UI-facing state, and the top-level
player serialization used by a world save.

## Entry points

Read `src/avatar.h` and `src/avatar.cpp`; creation and player commands continue through
`newcharacter.cpp` and `avatar_action.cpp`. `avatar::serialize`, `avatar::deserialize`,
`save_map_memory`, and `control_npc` define high-risk boundaries.

## Data ownership

The avatar owns player-only state and a stable save ID. It owns map-memory data through its
memory object, but references the current map, world, creatures, and UI services managed by
their respective systems.

## Dependencies

It depends on `Character`, world/save services, map memory, input and UI state, missions,
factions, and character-creation registries. Player actions must use normal map and activity
interfaces rather than mutate distant state directly.

## Lifecycle

An avatar is created or loaded, initialized for its character type, attached to a world, and
updated as the controlled actor. `control_npc` deliberately swaps control while preserving the
old actor as an NPC.

## Invariants

There is one controlled avatar context; its save ID must remain stable; map memory must use
absolute coordinates; and control transfer must not duplicate character IDs or item ownership.

## Extension points

Add player-only commands in `avatar_action.cpp`, creation policy in the creation flow, and UI
state only when it cannot live in a local adaptor. Shared actor behavior belongs in
`Character`, not in `avatar`.

## Serialization

`src/savegame_json.cpp` implements the concrete player record. Explicitly non-serialized UI
state, including the zone-sort viewport lock, must stay reconstructible after load.

## Tests

Use new-character tests plus focused tests for the shared subsystem touched. Save-sensitive
changes need a load of missing/old fields and a round trip, not merely a JSON snapshot.

## Performance

Avoid placing full-world queries or repeated map-memory scans in player-turn or redraw paths.
Cache only with a clear invalidation event.

## CCB divergence

CCB has player-facing UI and Lua integration that may not exist or may differ upstream. Port
avatar changes by behavior and save fields, never by assuming class-name parity.

## Technical debt

Player-only state still spans creation, game, UI, and save translation units. Prefer small,
testable moves toward explicit services rather than expanding global avatar access.
