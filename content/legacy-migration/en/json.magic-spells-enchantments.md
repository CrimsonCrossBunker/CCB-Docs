## Current CCB Magic, Spell, and Enchantment contracts

This family includes `SPELL`, `magic_type`, `enchantment`, and inline `fake_spell` values used by
other objects. They share some IDs and conditions but have different lifecycles: spells are cast,
magic types provide system defaults, and enchantments are continuously evaluated against an owner
or carrier.

### Minimal spell skeleton

```jsonc
{
  "type": "SPELL",
  "id": "spell_ccb_example",
  "name": "Example pulse",
  "description": "A documentation-only spell.",
  "effect": "attack",
  "shape": "blast",
  "valid_targets": [ "hostile" ],
  "min_damage": 1,
  "damage_increment": 1,
  "max_damage": 5,
  "min_range": 3,
  "max_range": 3,
  "energy_source": "MANA",
  "base_energy_cost": 10,
  "base_casting_time": 100
}
```

Current `spell_type::load` requires `name`, `description`, `effect`, `shape`, and
`valid_targets`. Effects and shapes must exist in native registries. Damage, range, AoE, duration,
pierce, accuracy, energy, and casting time commonly use min, increment, and max values. Expressions
and units come from the owning reader and are not uniformly plain integers.

`caster_condition`, `target_condition`, target species or monster IDs, body parts, and flags jointly
limit valid targets. `extra_effects` or `fake_spell` values chain spells, and consistency checks
detect cycles. WONDER, permanent summons, vitamin energy, touch versus no-hands, and formula
parameters also have specialized checks.

### Magic types, learning, and channels

A `magic_type` can centralize energy, level or XP and failure formulas, cannot-cast flags, failure
cost, and failure EOCs. Level and XP formulas must be paired and have the expected argument counts.
A spell can override magic-type values and can be learned through books, professions or NPCs,
`learn_spells`, and other current entry points.

A channeled spell needs maximum turns, a channel spell, and an end spell. Cover cancellation,
movement, damage, resource exhaustion, interrupt behavior, per-turn energy, and save boundaries.
Multiple projectiles and repeated or random extra spells need performance and recursion review.

### Enchantments

An enchantment may use a named ID or be inline when its caller can supply a stable inline ID. `has`
and `condition` select HELD, WIELD, or WORN and ACTIVE, INACTIVE, ALWAYS, or a dialogue condition.
`values`, skills, custom values, encumbrance, and melee or incoming damage support add and multiply
forms. Mutations, effects, body-part changes, special vision, emitters, hit effects, and intermittent
spells each have separate semantics.

Characters, monsters, and vehicles process only the subsets their implementations consider
relevant. A loadable field is not proof that every carrier applies it; inspect
`is_monster_relevant`, `is_vehicle_relevant`, and call sites.

### Validation

Run the formatter, `make -j2 json-check`, `--check-mods` for the real Mod set, and relevant filters
from `magic_spell_test`, `magic_spell_effect_test`, and `enchantments_test`. Cover level boundaries,
failure and resources, targets and shapes, extra-effect cycles, channel interruption, enchantment
activation, add/multiply ordering, and save reload. Test player, NPC, monster, vehicle, and inline
carriers separately; profile frequent intermittent or area spells.
