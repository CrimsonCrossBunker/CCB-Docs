---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: eoc.talkers
title: EOC talkers and alpha/beta routing
language: en
status: draft
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
source_fingerprint: f52b67e59b777a2d203f58ddaef85d38aa06ac0792196b54e829681279e2f594
authority: api-contract
verified_commit: a038c765568fc47a58ef8c523b2722d416f5f61c
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 633c116b8ceb25994926cb0d914dc6f0b5623695fae7fddbefd46996ec0cf860
prerequisites:
- eoc.overview
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/566
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/eoc/talkers/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/talkers/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/eoc/talkers/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/talkers/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/a038c765568fc47a58ef8c523b2722d416f5f61c
source_urls:
- path: data/reference/json/ccb_eoc_conditions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/a038c765568fc47a58ef8c523b2722d416f5f61c/data/reference/json/ccb_eoc_conditions.json
- path: data/reference/json/ccb_eoc_effects.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/a038c765568fc47a58ef8c523b2722d416f5f61c/data/reference/json/ccb_eoc_effects.json
- path: tools/json_api/contract-inventory.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/a038c765568fc47a58ef8c523b2722d416f5f61c/tools/json_api/contract-inventory.schema.json
- path: tools/json_api/generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/a038c765568fc47a58ef8c523b2722d416f5f61c/tools/json_api/generate_contracts.py
- path: tools/json_api/test_generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/a038c765568fc47a58ef8c523b2722d416f5f61c/tools/json_api/test_generate_contracts.py
- path: src/condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/a038c765568fc47a58ef8c523b2722d416f5f61c/src/condition.cpp
- path: src/npctalk.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/a038c765568fc47a58ef8c523b2722d416f5f61c/src/npctalk.cpp
- path: src/effect_on_condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/a038c765568fc47a58ef8c523b2722d416f5f61c/src/effect_on_condition.cpp
- path: src/effect_on_condition.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/a038c765568fc47a58ef8c523b2722d416f5f61c/src/effect_on_condition.h
- path: tests/eoc_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/a038c765568fc47a58ef8c523b2722d416f5f61c/tests/eoc_test.cpp
- path: doc/JSON/EFFECT_ON_CONDITION.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/a038c765568fc47a58ef8c523b2722d416f5f61c/doc/JSON/EFFECT_ON_CONDITION.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28eoc.talkers%29%3A+&body=Document+ID%3A+eoc.talkers%0ALanguage%3A+en%0AVerified+commit%3A+a038c765568fc47a58ef8c523b2722d416f5f61c%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# EOC talkers and alpha/beta routing

EOC conditions and effects operate on alpha/beta talkers in a dialogue context. Historical key
names commonly use `u_` and `npc_` for those routing directions, but a prefix does not prove that
the object is necessarily the player avatar or an ordinary NPC. Events, items, monsters, map
locations, and nested calls can construct other talker combinations.

## How the inventory preserves unknowns

The condition inventory marks 235 keys `legacy_alpha_beta_alias` and 40 `unknown`; the effect
inventory has 161 and 145 respectively. `legacy_alpha_beta_alias` proves only a registration alias
group. It is never a classification of the concrete runtime talker type.

Before using a key:

1. Locate its parser or handler in the condition/effect registry.
2. Read how the handler obtains alpha and beta from `dialogue`.
3. Read the call site that triggers the EOC and constructs that dialogue.
4. If a call swaps talkers or nests another EOC, test both routing directions.
5. Do not document a key as “player-only” or “NPC-only” from its prefix alone.

## Failure modes

- Alpha or beta is absent or does not support the requested interface.
- An EVENT resolves its focus entity differently from the author's assumption.
- A parent EOC passes context to a child but not the expected talker.
- An alias works in one routing direction while tests omit the other.

Generated references expose the talker classification deliberately. A concrete compatibility
claim belongs in the contract only after the handler, call site, and tests prove it together.
