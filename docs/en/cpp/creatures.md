---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.creatures
title: Creatures subsystem
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
- src/creature.h
- src/creature.cpp
- src/creature_tracker.cpp
- tests/creature_test.cpp
source_symbols:
- 'class Creature : public viewer'
source_queries: []
source_fingerprint: dfe4c194a3da180d38dbc01dccf160ef9f66900266cb4d9d89febec6d2925cdb
authority: source-and-tests
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: f235b42e3c694abbbf01554bdb9d2fd81d66ffe74955f3b5e975dceb3716f395
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
risk_group: cpp-creatures
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/creatures/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/creatures/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/creatures/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/creatures/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: src/creature.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/creature.h
- path: src/creature.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/creature.cpp
- path: src/creature_tracker.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/creature_tracker.cpp
- path: tests/creature_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/creature_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.creatures%29%3A+&body=Document+ID%3A+cpp.creatures%0ALanguage%3A+en%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Creatures

## Responsibility

`Creature` is the polymorphic base for characters and monsters. It defines position, senses,
combat-facing stats, damage, effects, movement, visibility, attitude hooks, and viewer behavior
shared by all live actors.

## Entry points

Read `src/creature.h` and `src/creature.cpp`; effect integration is covered by creature-effect
tests, while spatial indexing and lookup enter through `creature_tracker`.

## Data ownership

A creature owns base actor state and its effect map. Concrete subclasses own type-specific
state. The map owns terrain, while `creature_tracker` indexes active creature instances without
becoming their gameplay owner.

## Dependencies

The base depends on coordinates, map visibility, fields, effects, damage types, factions,
events, and virtual behavior supplied by `Character` or `monster`.

## Lifecycle

Concrete actors are constructed, positioned and registered, updated by simulation, may move
between submaps, receive effects/damage, die, and are removed from tracking by their owner.

## Invariants

Tracked position and actual position agree; a live actor is not duplicated in the tracker;
effect keys and durations remain valid; and virtual type predicates match the concrete object.

## Extension points

Put truly shared actor behavior in `Creature`; otherwise implement in the concrete class.
Publish cross-actor changes through existing events and IDs rather than adding type checks.

## Serialization

The base provides shared loading helpers, but concrete `Character` and `monster` paths own
their durable records. Tracker indexes and visibility caches are reconstructed.

## Tests

Use creature, creature-in-field, creature-effect, vision, combat, and subclass tests. Movement
changes must assert both map occupancy and tracker lookup.

## Performance

Visibility, effect processing, distance checks, and tracker queries are hot. Avoid virtual-call
fan-out over every creature and repeated map lookups inside nested loops.

## CCB divergence

CCB's creature behavior is defined by this source and tests, including its current field and
effect semantics. Upstream algorithms require deterministic regression evidence before porting.

## Technical debt

The base exposes a large virtual surface shared by semantically different actors. Prefer
capability-oriented helpers and events over another broad virtual when extending it.
