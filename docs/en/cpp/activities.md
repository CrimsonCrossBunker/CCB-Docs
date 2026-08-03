---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.activities
title: Activities subsystem
language: en
status: active
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
- src/player_activity.h
- src/activity_actor.h
- src/activity_actor.cpp
- tests/activity_tracker_test.cpp
source_symbols:
- class activity_actor
source_queries: []
source_fingerprint: 8a0b60ebcca4a10e9695716c3962cd5192ef75b64eb2be044c6f323f6aa9e101
authority: source-and-tests
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 17895565fe1a2250932afd4b8c8594f9f562f3e02c9d6aa4fa53eff5395b7355
prerequisites:
- cpp.character
depends_on: []
redirect_from: []
supersedes:
- cpp-activities
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-activities
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/activities/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/activities/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/activities/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/activities/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: src/player_activity.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/player_activity.h
- path: src/activity_actor.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/activity_actor.h
- path: src/activity_actor.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/activity_actor.cpp
- path: tests/activity_tracker_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/activity_tracker_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.activities%29%3A+&body=Document+ID%3A+cpp.activities%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Activities

## Responsibility

Activities represent work that spans moves or turns. `player_activity` stores scheduling,
progress, targets, values, resume state, and an optional polymorphic `activity_actor`; actor
implementations own behavior for start, turn, finish, cancellation, and serialization.

## Entry points

Read `src/player_activity.h`, `src/activity_actor.h`, their implementations, and the focused
`activity_actor_definitions.h`. Legacy handlers remain in `activity_handlers`; scheduling and
backlog behavior use `activity_tracker`.

## Data ownership

A `Character` owns current and queued activity state through its tracker. `player_activity`
owns a cloneable actor and stable item locations/targets, not the target items or map tiles
themselves.

## Dependencies

Activities depend on characters, item locations, coordinates, activity type definitions,
inventory validity, movement points, UI interruption, events, and save JSON.

## Lifecycle

An activity is constructed and assigned, its actor `start`s once, `do_turn` advances it,
interruption may suspend/cancel it, compatible work can resume, and `finish` or cancellation
cleans up before the tracker advances.

## Invariants

Actor type equals activity ID; clone preserves concrete behavior; targets remain checked before
use; move totals and remaining work stay coherent; cancellation performs required cleanup; and
resume compares only compatible actors.

## Extension points

New long-running behavior should be an `activity_actor` with a registered deserializer. Keep UI
selection outside the actor and put durable execution inputs inside it; avoid adding another
legacy handler.

## Serialization

`player_activity` serializes in `savegame_json.cpp`; each actor must serialize its custom data
and register the matching deserializer. Add defaults or migration for old actor payloads.

## Tests

Use activity tracker/scheduling tests plus focused behavior tests. Cover start, one turn,
completion, cancellation, suspension/resume, invalid targets, cloning, and save round trip.

## Performance

Activities execute every turn and may validate inventory. Actors that can safely manage
invalid-item cleanup should use the documented override to avoid expensive repeated scans.

## CCB divergence

CCB retains a mixture of actor and legacy activity paths. An upstream actor port must match the
current CCB ID mapping, save payload, interruption, and inventory rules.

## Technical debt

Legacy handlers and actor-based activities coexist. Migrate one behavior at a time with save
compatibility; do not renumber or silently reinterpret legacy IDs.
