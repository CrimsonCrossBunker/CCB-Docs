## Current CCB Mutation contract

`mutation` objects are loaded by the `mutation_branch` factory. Current
`mutation_branch::load` requires `name`, `description`, and `points`. Activation, categories,
thresholds, equipment conflicts, and EOCs are separate systems layered onto one stable trait ID.

### Basic definition

```jsonc
{
  "type": "mutation",
  "id": "TRAIT_CCB_EXAMPLE",
  "name": { "str": "Example adaptation" },
  "description": "A documentation-only example.",
  "points": 1,
  "starting_trait": false,
  "purifiable": true,
  "category": [ "MUTCAT_CCB_EXAMPLE" ]
}
```

`points` is character-creation and valuation data, not mutation-selection weight.
`starting_trait`, `random_start_allowed`, `valid`, and `purifiable` govern different entry points.
`variants` supplies weighted names and descriptions for the same trait; it does not create another
stable trait ID.

### Active, passive, and equipment behavior

An active mutation may define `cost`, `time`, and kcal, thirst, sleepiness, mana, or stamina
resources, then use current activation or EOC fields for effects. `starts_active` is meaningful only
for an activatable trait. Validate reflex conditions, on/off messages, and talker semantics as EOC
conditions.

`destroys_gear`, `allow_soft_gear`, body-part or armor changes, and enchantments affect worn items,
anatomy, and caches. Acquisition, removal, purification, variant changes, and save reload can all
update cached state; the character-creation screen is insufficient evidence.

### Categories, thresholds, and relation graphs

A mutation category is a registered object governing vitamins, thresholds, primers or mutagens, and
category strength. Trait `prereqs`, `prereqs2`, `threshreq`, `cancels`, `replacements`, and
additions form a directed graph. Check unreachable nodes, cycles, pre/post-threshold substitution,
and instability effects after changing any edge.

Use the current `trait_migration` contract when removing or renaming a public trait. It can replace
a trait or variant or explicitly remove it. Deleting the old JSON ID alone abandons saves and other
Mods.

### Validation

Run the formatter, `make -j2 json-check`, `--check-mods` for the real Mod set, and relevant
`mutation_test` filters. Cover character creation, mutagen or primer use, purification, thresholds,
bad-mutation odds, active cooldowns, insufficient resources, equipment conflicts, enchantment and
cache updates, NPCs, and save reload. Check translated variants, message arguments, and EOC
true/false paths.

Legacy chemistry and probability explanations can drift; use current mutation source and tests for
system behavior.
