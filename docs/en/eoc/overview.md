---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: eoc.overview
title: EOC contracts and lifecycle
language: en
status: active
doc_type: explanation
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 60
last_human_reviewer: LYHGLYTX
source_paths:
- data/reference/json/ccb_eoc_conditions.json
- data/reference/json/ccb_eoc_effects.json
- tools/json_api/contract-inventory.schema.json
- tools/json_api/generate_contracts.py
- tools/json_api/test_generate_contracts.py
- src/condition.cpp
- src/npctalk.cpp
- src/effect_on_condition.cpp
- src/effect_on_condition.h
- tests/eoc_test.cpp
- doc/JSON/EFFECT_ON_CONDITION.md
source_symbols: []
source_queries: []
source_fingerprint: 104d655e889b5071282102d8ebd64521a5dbdc36ad6c7a6b6daacdd6e00e8689
authority: api-contract
verified_commit: 71f403ecea0dcf16be8fe93c661acbe2a4906cc6
verified_at: '2026-08-09'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 6ade8b771f3f8e8fda9e53cded6b0c1893f6023f1cd6a65c7be38ffa2b8f1146
prerequisites:
- json.overview
depends_on:
- reference.eoc-conditions
- reference.eoc-effects
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; parser registrations, inventories, and tests remain authoritative.
example_validation_ids: []
api_version: contract-inventory-v1
deprecated: false
deprecation_replacement: null
risk_group: eoc
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/eoc/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/eoc/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/71f403ecea0dcf16be8fe93c661acbe2a4906cc6
source_urls:
- path: data/reference/json/ccb_eoc_conditions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/data/reference/json/ccb_eoc_conditions.json
- path: data/reference/json/ccb_eoc_effects.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/data/reference/json/ccb_eoc_effects.json
- path: tools/json_api/contract-inventory.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/tools/json_api/contract-inventory.schema.json
- path: tools/json_api/generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/tools/json_api/generate_contracts.py
- path: tools/json_api/test_generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/tools/json_api/test_generate_contracts.py
- path: src/condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/src/condition.cpp
- path: src/npctalk.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/src/npctalk.cpp
- path: src/effect_on_condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/src/effect_on_condition.cpp
- path: src/effect_on_condition.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/src/effect_on_condition.h
- path: tests/eoc_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/tests/eoc_test.cpp
- path: doc/JSON/EFFECT_ON_CONDITION.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/doc/JSON/EFFECT_ON_CONDITION.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28eoc.overview%29%3A+&body=Document+ID%3A+eoc.overview%0ALanguage%3A+en%0AVerified+commit%3A+71f403ecea0dcf16be8fe93c661acbe2a4906cc6%0A%0ADescribe+the+documentation+problem%3A%0A
---

# EOC contracts and lifecycle

An EOC (effect on condition) combines condition parsing, effect parsing, and a trigger lifecycle.
The machine inventories currently index [275 condition keys](../reference/eoc-conditions.md) and
[310 effect keys](../reference/eoc-effects.md). Registration coverage is complete while
handler-level parameter classification remains incomplete.

## The `effect_on_condition` object

The source inventory classifies this object's fields as `partial`:

- `id` has explicit mandatory evidence.
- `eoc_type` is optional; the loader follows activation by default without `recurrence`, and the
  recurring rules when `recurrence` exists.
- `condition`, `deactivate_condition`, `effect`, and `false_effect` are read behind presence branches.
- `global` and `run_for_npcs` default to `false`.
- `required_event` is mandatory only inside the `EVENT` branch; do not describe it as mandatory
  for every EOC.

Lifecycle types come from `effect_on_condition.h/.cpp`: `ACTIVATION`, `RECURRING`,
`AVATAR_DEATH`, `NPC_DEATH`, `PREVENT_DEATH`, and `EVENT`. Each receives talkers and context from
different trigger paths, which must be checked in the corresponding source and tests.

## Parser boundaries

- Conditions use first-matching-parser dispatch. An unknown object condition throws `JsonError`;
  an unknown string condition becomes a predicate that returns false.
- Effect containers accept a string, object, or array and also use first-match dispatch; an unknown
  effect throws `JsonError`.
- Only the logical `and`, `or`, and `not` condition keys are fully classified; the other 272 are
  `partial`.
- All 310 effect keys are `partial`. This does not mean they are unusable. It means parameters,
  defaults, nesting, talkers, variables, or context do not yet have complete source classification.

Continue with [talker routing](talkers.md), [variables and context](variables-context.md), and
[nesting](nesting.md), then build a minimal validation chain with the
[complete example mod](../mods/complete-json-eoc-mod.md).
