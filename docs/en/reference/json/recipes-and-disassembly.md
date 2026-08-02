---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.recipes-and-disassembly
title: 'Legacy migration draft: recipes and disassembly'
language: en
status: active
doc_type: explanation
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 365
last_human_reviewer: Pending human review
source_paths:
- doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md
- src/recipe.cpp
- src/recipe_dictionary.cpp
- data/json/recipes/armor/other.json
- data/json/uncraft/ammo/10mm.json
- tests/recipe_steps_test.cpp
source_symbols:
- recipe::load
- recipe_dictionary::load
- recipe_dictionary::load_uncraft
source_queries: []
source_fingerprint: 74b3b7fdb8eed201e742fece7ebf19c59fa8f6dfd65fa21b6584d07c1cee067e
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 2dada06bcfe6ca4152d3d42677bff2200a4621a5948dc0775078923457a01a2e
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: Anton Simakov, RenechCDDA, dobbry-vechur, dumb-kevin, thaelina; accepted
  inventory identities only. Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/recipes-and-disassembly/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/recipes-and-disassembly/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/recipes-and-disassembly/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/recipes-and-disassembly/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md
- path: src/recipe.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/recipe.cpp
- path: src/recipe_dictionary.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/recipe_dictionary.cpp
- path: data/json/recipes/armor/other.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/recipes/armor/other.json
- path: data/json/uncraft/ammo/10mm.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/uncraft/ammo/10mm.json
- path: tests/recipe_steps_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/recipe_steps_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.recipes-and-disassembly%29%3A+&body=Document+ID%3A+json.recipes-and-disassembly%0ALanguage%3A+en%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: recipes and disassembly

This is the migration draft page for `json.recipes-and-disassembly`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.recipes-and-disassembly`
- Target: `reference/json/recipes-and-disassembly.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/recipes-and-disassembly/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.recipes-and-disassembly | doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB recipe and disassembly model

Recipes are registered by `recipe_dictionary` and passed to `recipe::load`. The current
loader distinguishes `recipe`, `uncraft`, `practice`, and `nested_category`. They share some
fields but differ in ID construction, mandatory fields, learning, and result semantics. Do
not turn a crafting example into a valid uncraft merely by changing `type`.

### Regular crafting recipe

```jsonc
{
  "type": "recipe",
  "result": "ccb_example_part",
  "category": "CC_OTHER",
  "subcategory": "CSC_OTHER_PARTS",
  "skill_used": "fabrication",
  "difficulty": 1,
  "time": "10 m",
  "activity_level": "LIGHT_EXERCISE",
  "autolearn": true,
  "qualities": [ { "id": "HAMMER", "level": 1 } ],
  "components": [ [ [ "scrap", 2 ] ] ]
}
```

A regular recipe normally derives its recipe ID from `result`; `variant` or `id_suffix`
changes the final ID. `category` and `subcategory` are mandatory display classifications
for regular recipes. Loader code defines which other fields inherit, default, or have ranges.

### Nested requirement semantics

`components`, `tools`, and `qualities` contain groups that must all be satisfied; entries
within a group can be alternatives. `using` references a named `requirement` with a multiplier
and is suitable for reusable combinations such as soldering or welding. Bracket depth encodes
AND and OR, so wrong nesting can change resource requirements without being invalid JSON.
For a complex recipe, check:

- whether alternatives really are OR choices;
- quantities, charges, and `LIST` requirement multipliers;
- how `NO_RECOVER` and `UNRECOVERABLE` affect disassembly recovery;
- whether overlapping alternatives make craftability calculation too complex.

### Step recipes

A recipe with `steps` defines per-step tools, qualities, proficiencies, time, and activity.
The current loader forbids root-level `tools`, `qualities`, `proficiencies`,
`batch_time_factors`, `time`, or `activity_level` on a step recipe, and rejects an empty
`steps` array. Root `using` and components have dedicated aggregation behavior. Run the
recipe-step tests whenever inheritance or step structure changes.

### Uncraft and reversible recipes

```jsonc
{
  "type": "uncraft",
  "result": "ccb_example_part",
  "time": "5 m",
  "activity_level": "LIGHT_EXERCISE",
  "components": [ [ [ "scrap", 1 ] ] ]
}
```

An `uncraft` enters a separate dictionary and is marked as a reversible disassembly. A regular
recipe with `reversible: true` derives a disassembly from crafting data; the object form can
override disassembly time. The current loader explicitly rejects a reversible recipe with
`byproducts` or `byproduct_group`. A disassembly review must also check conservation of mass,
result counts, sensible tools, differences between world-spawned and player-crafted items,
and duplicate disassembly definitions for one result.

### Inheritance and loading

`recipe_dictionary::load` defers a recipe whose `copy-from` base has not appeared, copies the
base when available, then calls `recipe::load`. Inline requirements are rebuilt, and steps,
tools or components, and `using` have specialized inheritance rules. Do not assume recipe
inheritance behaves exactly like generic `ITEM` inheritance.

### Validation checklist

1. Confirm the result, recipe ID, categories, and every item, skill, quality, and requirement ID.
2. Run the JSON formatter and `make -j2 json-check`.
3. Run relevant `recipe_steps_test` cases for step or `copy-from` changes.
4. For a Mod, run `--check-mods` with the real Mod set to verify dependencies and load order.
5. In a focused test or game, inspect craftability, batch time, results and byproducts,
   disassembly recovery, and conservation of mass.

A successful load proves that the structure is readable, not that a recipe cannot duplicate
resources, become unreachable, or break balance.

## History and attribution

Accepted inventory contributors: Anton Simakov, RenechCDDA, dobbry-vechur, dumb-kevin, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `74b3b7fdb8eed201e742fece7ebf19c59fa8f6dfd65fa21b6584d07c1cee067e`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
