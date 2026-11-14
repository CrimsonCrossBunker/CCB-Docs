---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.upstream-authoring-notes
title: 'Draft: upstream JSON documentation corrections'
language: en
status: draft
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
- src/iuse_actor.cpp
- src/recipe.cpp
- src/item_factory.cpp
source_symbols:
- molle_attach_actor::load
- molle_detach_actor::load
- batch_savings::deserialize
source_queries:
- ignore_sheet_thickness
- cover_melee
- batch_time_factors
source_fingerprint: b2484fe56acbc5d5ada896e3263c50e2ffd68595c3c2e31aec525a15f97ce116
authority: api-contract
verified_commit: 6a0c46788f43ef37269cd742e0a6147b4f55e96e
verified_at: '2026-10-14'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 5affaa285f4be6bfb8755a893b375006ecbb0ccb1d90db51801a0124c6f2a220
prerequisites:
- reference.json-object-types
depends_on: []
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/upstream-authoring-notes/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/upstream-authoring-notes/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/upstream-authoring-notes/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/upstream-authoring-notes/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/6a0c46788f43ef37269cd742e0a6147b4f55e96e
source_urls:
- path: src/iuse_actor.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/6a0c46788f43ef37269cd742e0a6147b4f55e96e/src/iuse_actor.cpp
- path: src/recipe.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/6a0c46788f43ef37269cd742e0a6147b4f55e96e/src/recipe.cpp
- path: src/item_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/6a0c46788f43ef37269cd742e0a6147b4f55e96e/src/item_factory.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.upstream-authoring-notes%29%3A+&body=Document+ID%3A+json.upstream-authoring-notes%0ALanguage%3A+en%0AVerified+commit%3A+6a0c46788f43ef37269cd742e0a6147b4f55e96e%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Draft: CCB adaptations of upstream JSON documentation corrections

This page adapts upstream documentation additions and corrections against already-merged CCB source. It does not change runtime rules. Examples are field fragments for complete item or recipe definitions. The page remains a draft.

## MOLLE actions

`attach_molle` requires `size`, the total available MOLLE space. Both actions read optional `moves`, but neither current `use` implementation uses that configured value. Do not infer a 300-move operation from the examples. These are separate definitions: do not repeat the `use_action` key in one JSON object.

```json
{"use_action": {"type": "attach_molle", "size": 10, "moves": 300}}
```

```json
{"use_action": {"type": "detach_molle", "moves": 300}}
```

## Linear batch time

Separate `mode`, `setup` and `max` with commas. `"mode": "linear": "setup"` is invalid JSON. `max` controls when setup cost is applied again, rather than prohibiting larger batches.

```json
{"batch_time_factors": {"mode": "linear", "setup": "12 m", "max": 20}}
```

## Armor materials and coverage

Use JSON boolean `true` for `ignore_sheet_thickness`, not string `"true"`. `coverage`, `cover_melee`, `cover_ranged` and `cover_vitals` belong to body-part entries inside `armor`. Material `covered_by_mat` is a separate material coverage value.

```json
{"armor": [{"covers": ["torso"], "coverage": 95, "cover_melee": 95,
  "cover_ranged": 50, "cover_vitals": 5,
  "material": [{"type": "plastic", "covered_by_mat": 15,
    "thickness": 0.8, "ignore_sheet_thickness": true}]}]}
```

Sources and attribution: CDDA #88587: Proflig; CDDA #88632: dynst; CDDA #88852: OromisElf; CDDA #88866: OromisElf. Original authors and change intent are retained here, with examples checked against CCB loaders. Responsible human: LYHGLYTX.
