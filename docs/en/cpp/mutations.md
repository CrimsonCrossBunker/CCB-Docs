---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.mutations
title: Mutations subsystem
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
- src/mutation.h
- src/mutation.cpp
- src/mutation_data.cpp
- tests/mutation_test.cpp
source_symbols:
- struct mutation_branch
source_queries: []
source_fingerprint: eb2d2057e6b418e5c330673786e0225fd459e9ddbb88eed4f36fcbda0999a62f
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 2aadbb74e5fdcf96f4c4b7ce41f07df7bd791454e4507658cdf854cd5b387e8e
prerequisites:
- cpp.character
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
risk_group: cpp-mutations
risk_level: normal
pending_source_pr: null
stale_reason: null
search:
  exclude: true
---

# Mutations

## Responsibility

The mutation subsystem defines mutation types and branches, prerequisites and conflicts,
categories, variants, enchantments, attacks, body changes, activation, acquisition, removal,
and how traits modify a character.

## Entry points

Read `src/mutation.h`, `src/mutation.cpp`, and `src/mutation_data.cpp`. JSON loads into
`mutation_branch` and related registries; character application and UI live in focused mutation
and character files.

## Data ownership

Registries own immutable mutation definitions. A `Character` owns acquired trait state,
variants, activation and charges; caches derived from traits belong to the character and must
be invalidated through normal mutation APIs.

## Dependencies

Mutations depend on JSON IDs, body parts, enchantments, effects, vitamins, items, martial arts,
spells, character stats, events, and save migration.

## Lifecycle

Definitions load, check, and finalize; mutation selection resolves prerequisites/conflicts and
category rules; character state applies or removes the trait; active mutations process costs;
the result persists with the character.

## Invariants

Referenced IDs resolve; prerequisite/conflict graphs remain valid; trait state and derived
body/stat caches agree; activation costs cannot underflow; and variant identity survives save
round trips.

## Extension points

Prefer mutation JSON, EOC, enchantment, and existing mutation effects. Native code is warranted
only for a reusable behavior not expressible by data, with graph validation and character tests.

## Serialization

Definitions deserialize from data; acquired traits and their state serialize in the character
save. New durable state needs defaults and migration for old trait representations.

## Tests

Use mutation tests plus character modifier, body, enchantment, vitamin, effect, and save-related
tests. Cover acquire/remove symmetry and every prerequisite/conflict edge changed.

## Performance

Trait-derived calculations occur in character update and UI paths. Invalidate narrow caches
when the mutation set changes instead of rescanning every definition each turn.

## CCB divergence

CCB mutation data and legacy mod IDs are compatibility boundaries. Upstream mutations require
dependency-graph, body-part, and save review against the CCB data set.

## Technical debt

Mutation effects span data, character caches, UI, and hard-coded hooks. New work should migrate
reusable behavior toward declarative contracts without silently changing existing traits.
