---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: eoc.nesting
title: Nesting EOC conditions and effects
language: en
status: draft
doc_type: how-to
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
source_fingerprint: f52b67e59b777a2d203f58ddaef85d38aa06ac0792196b54e829681279e2f594
authority: api-contract
verified_commit: d49367845e6cd725d5ca56d171b610047d64592d
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 4e8fdd81409a1c292a8d63686520b06e3357687cfa09c99965a731e0090d96d3
prerequisites:
- eoc.overview
depends_on:
- eoc.variables-context
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/566
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/eoc/nesting/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/nesting/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/eoc/nesting/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/nesting/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d49367845e6cd725d5ca56d171b610047d64592d
source_urls:
- path: data/reference/json/ccb_eoc_conditions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d49367845e6cd725d5ca56d171b610047d64592d/data/reference/json/ccb_eoc_conditions.json
- path: data/reference/json/ccb_eoc_effects.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d49367845e6cd725d5ca56d171b610047d64592d/data/reference/json/ccb_eoc_effects.json
- path: tools/json_api/contract-inventory.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d49367845e6cd725d5ca56d171b610047d64592d/tools/json_api/contract-inventory.schema.json
- path: tools/json_api/generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d49367845e6cd725d5ca56d171b610047d64592d/tools/json_api/generate_contracts.py
- path: tools/json_api/test_generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d49367845e6cd725d5ca56d171b610047d64592d/tools/json_api/test_generate_contracts.py
- path: src/condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d49367845e6cd725d5ca56d171b610047d64592d/src/condition.cpp
- path: src/npctalk.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d49367845e6cd725d5ca56d171b610047d64592d/src/npctalk.cpp
- path: src/effect_on_condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d49367845e6cd725d5ca56d171b610047d64592d/src/effect_on_condition.cpp
- path: src/effect_on_condition.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d49367845e6cd725d5ca56d171b610047d64592d/src/effect_on_condition.h
- path: tests/eoc_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d49367845e6cd725d5ca56d171b610047d64592d/tests/eoc_test.cpp
- path: doc/JSON/EFFECT_ON_CONDITION.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d49367845e6cd725d5ca56d171b610047d64592d/doc/JSON/EFFECT_ON_CONDITION.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28eoc.nesting%29%3A+&body=Document+ID%3A+eoc.nesting%0ALanguage%3A+en%0AVerified+commit%3A+d49367845e6cd725d5ca56d171b610047d64592d%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Nesting EOC conditions and effects

Nesting is constrained first by container shape and then by the individual handler.

## Proven general rules

- Conditions enter object or string parser paths. `and` and `or` accept arrays; `not` accepts one
  object or string. These three logical keys have completely classified nesting contracts.
- An effect container may be a string, object, or array.
- Both parser families use first-match dispatch. Do not put multiple competing condition/effect
  keys in one dispatch object.
- Beyond the three logical conditions, handler parameters, defaults, and nesting support are mostly
  unclassified; follow the source links in generated reference.

## Minimal structure

The documentation example mod uses one activation EOC:

```json
{
  "type": "effect_on_condition",
  "id": "EOC_CCB_DOCS_HELLO",
  "eoc_type": "ACTIVATION",
  "condition": { "math": [ "1 == 1" ] },
  "effect": [ { "u_message": "The CCB Docs example EOC ran." } ]
}
```

Both `math` and `u_message` are registered, but their current contracts are `partial`. The example
check proves registration, the maintained fixture shape, and JSON parsing; the real CCB loader
remains the final validation layer.

Add complex nesting one layer at a time: validate leaf conditions/effects, then add
`and`/`or`/`not` or `if`/`then`/`else`, and only then add variable passing and talker swapping. Keep
a minimal EOC that reproduces failures at each layer.
