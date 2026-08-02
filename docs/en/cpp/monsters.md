---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.monsters
title: Monsters subsystem
language: en
status: draft
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
- src/monster.h
- src/monster.cpp
- src/monstergenerator.cpp
- tests/monster_test.cpp
source_symbols:
- 'class monster : public Creature'
source_queries: []
source_fingerprint: d32869f17e7e85b671a83a09a3b196638df5130c32eba07b8ced8fccce8118b1
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 2b25c242a79a9761e70ba5092154a44fbbb3694bf164138f53376c512c37ca5b
prerequisites:
- cpp.creatures
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
risk_group: cpp-monsters
risk_level: normal
pending_source_pr: null
stale_reason: null
search:
  exclude: true
---

# Monsters

## Responsibility

`monster` is the concrete non-character creature. It combines a `mtype` definition with
runtime health, movement plans, faction/attitude state, special attacks, inventory and
equipment-like state, destinations, and death behavior.

## Entry points

Begin at `src/monster.h` and `src/monster.cpp`. Static monster definitions and attacks enter
through `monstergenerator`; AI helpers and special attacks live in their focused files; active
instances are indexed by `creature_tracker`.

## Data ownership

The instance owns mutable monster state and references immutable `mtype` data. The tracker
indexes it; the map owns terrain; overmap groups may own deferred population records rather
than this loaded instance.

## Dependencies

Monsters depend on `Creature`, monster type registries, factions, paths, map fields, effects,
special-attack actors, items, overmap population, and save JSON.

## Lifecycle

A monster is generated or loaded, placed into the tracker, plans and acts each turn, may move
between reality bubbles and overmap representation, then dies or unloads into owning world
state.

## Invariants

The `mtype_id` resolves; plans use valid coordinate spaces; tracker position stays synchronized;
special attacks are registered; and unload/load cannot duplicate either an instance or its
inventory.

## Extension points

Prefer monster JSON and registered attack actors. Native AI belongs in focused helpers with a
deterministic test; add a new virtual or hard-coded type check only when data cannot represent
the rule.

## Serialization

`monster::serialize` / `deserialize` live in `savegame_json.cpp`; overmap serialization covers
deferred groups and stored monsters. New fields need safe defaults across both loaded and
unloaded forms.

## Tests

Use monster behavior, attack, vision, stairs, deterministic AI, overmap, and save-sensitive
tests. Fix the RNG seed for plan/attack regressions.

## Performance

Pathfinding, target selection, visibility, and special-attack evaluation scale with active
population. Keep deterministic caches scoped and avoid a full creature scan per monster.

## CCB divergence

Monster data, AI, and overmap handling are common upstream-port hotspots. CCB behavior must be
validated with its own JSON and tests; matching IDs do not prove matching semantics.

## Technical debt

Runtime AI, type data, and persistence still have cross-file coupling. New work should expose a
measurable policy boundary instead of adding another ad-hoc state flag.
