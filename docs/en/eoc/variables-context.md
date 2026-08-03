---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: eoc.variables-context
title: EOC variables and context
language: en
status: active
doc_type: reference
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
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8e90cbae7e8c02b7eaa85d8151d686e20feb0dac08e769660feee6034b89c055
prerequisites:
- eoc.overview
depends_on:
- eoc.talkers
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/eoc/variables-context/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/variables-context/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/eoc/variables-context/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/variables-context/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28eoc.variables-context%29%3A+&body=Document+ID%3A+eoc.variables-context%0ALanguage%3A+en%0AVerified+commit%3A+d49367845e6cd725d5ca56d171b610047d64592d%0A%0ADescribe+the+documentation+problem%3A%0A
---

# EOC variables and context

The machine inventories prove that the common variable parser recognizes these scopes:

| Scope | Boundary |
| --- | --- |
| `u_val` | A variable name associated with alpha routing; the prefix does not prove a concrete talker type |
| `npc_val` | A variable name associated with beta routing; also historical naming |
| `global_val` | The global variable namespace |
| `var_val` | An indirect variable reference |
| `context_val` | A context value passed through the current EOC/dialogue call chain |

The inventories also prove use of value helpers including `value_or_var`, `value_or_var_pair`,
`dbl_or_var`, `duration_or_var`, `str_or_var`, `translation_or_var`, and `eoc_math`. They do not
prove that every condition or effect accepts every scope or value type.

## Context discipline

- Treat `context_val` as a call protocol: writer and reader must agree on name, type, and lifetime.
- Before nesting an EOC, check whether the call interface forwards variables; do not assume every
  effect propagates context automatically.
- For EVENT EOCs, inspect how event fields map into context before consuming a key.
- Prefix mod variables stably to avoid collisions with core or other mods in global scope.
- Validate expression, string interpolation, and structured variable-object parser paths separately.

The handler-level variable contract remains `unclassified` for 272 of 275 conditions and all 306
effects. `known_global_scopes` in generated reference is a global parser capability, not a
per-key allowlist.
