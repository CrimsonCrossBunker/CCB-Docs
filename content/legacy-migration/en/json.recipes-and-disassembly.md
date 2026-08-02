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
