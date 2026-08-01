---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.effects
title: Effects subsystem
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
- src/effect.h
- src/effect.cpp
- src/effect_source.cpp
- tests/effect_test.cpp
source_symbols:
- class effect_type
source_queries: []
source_fingerprint: 9583fe6bb89626c7369d25b1a4678344f8815cc1352d8dfbfa374ffa2b2d498b
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 9a7e38d9eeb4f372357100947d6addddc2eaa4b17a718be5d562334f6ec65fdc
prerequisites:
- cpp.creatures
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
- json-load
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-effects
risk_level: normal
pending_source_pr: null
stale_reason: null
search:
  exclude: true
---

# Effects

## Responsibility

The effect subsystem defines timed status types and per-creature effect instances: duration,
intensity, body-part scope, source, modifiers, messages, immunity, removal, and migration of
renamed effect IDs.

## Entry points

Read `src/effect.h`, `src/effect.cpp`, and `src/effect_source.*`. Static JSON enters
`effect_type`; a creature's `effects_map` stores instances; EOC integration is a separate
contract in `effect_on_condition`.

## Data ownership

The registry owns `effect_type` definitions. Each `Creature` owns its `effects_map`; an
`effect` references a type and owns instance duration, intensity, body scope, and source data.

## Dependencies

Effects depend on IDs, body parts, damage and character modifiers, events, messages, immunity
rules, EOC, source serialization, and creature turn processing.

## Lifecycle

Types load and finalize; an instance is added or refreshed, processed each turn, changes
intensity or duration, fires relevant behavior, and expires or is explicitly removed/migrated.

## Invariants

Type IDs resolve; duration and intensity respect type bounds; body-scoped keys do not collide;
source data remains valid; removal does not invalidate an active iteration; migrations are
acyclic and preserve old saves.

## Extension points

Prefer effect JSON, modifiers, and EOC hooks. Add native behavior only when it is reusable and
cannot be declared, then centralize it and test immunity, add, process, and remove paths.

## Serialization

Effect instances and `effect_source` serialize in the save layer; definitions load from JSON.
New fields need defaults, and an ID rename needs an explicit `effect_migration`.

## Tests

Use effect and creature-effect tests plus focused character/monster tests. Cover duration and
intensity edges, body parts, immunity, sources, removal during processing, and round trips.

## Performance

Every active creature processes effects. Keep per-turn work proportional to active instances,
avoid repeated type lookups/formatting, and do not rebuild the whole map for one changed effect.

## CCB divergence

CCB effect definitions and EOC use may differ from upstream despite shared IDs. Port both data
and native semantics only after checking migrations, saves, and CCB tests.

## Technical debt

Effects mix declarative modifiers with native special cases. Prefer explicit, testable data or
event hooks and track any remaining hard-coded ID behavior as compatibility debt.
