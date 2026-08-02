## Current CCB Monster contract

`MONSTER` is passed by `MonsterGenerator::load_monster` to a generic factory and interpreted by
`mtype::load` for fields, inheritance, and bounds. A legacy field table is only historical evidence;
the current loader, first-party JSON, and `tests/monster_test.cpp` are the contract.

### Minimal definition and identity

```jsonc
{
  "type": "MONSTER",
  "id": "mon_ccb_example",
  "name": { "str": "example creature" },
  "description": "A creature used by documentation.",
  "default_faction": "wildlife",
  "symbol": "e",
  "color": "light_green",
  "material": [ "flesh" ],
  "species": [ "MAMMAL" ],
  "volume": "62500 ml",
  "weight": "80 kg",
  "hp": 40,
  "speed": 90
}
```

The `id` is a stable reference used by spawn groups, mapgen, missions, EOCs, and saves. Current
loading requires `name`, `default_faction`, and `symbol`. Read `mtype::load` for numeric bounds,
units, and defaults; example values are not balance recommendations.

Defining a monster does not make it appear. Natural placement normally also needs a monster group,
mapgen or static spawn, event, or EOC. Species, faction, material, harvest, death-drop, and item-group
fields must reference actual registered IDs.

### Behavior composition

- `flags`, anger/fear/placate triggers, vision, path settings, and move skills control common AI.
- `special_attacks` may name a registered native attack or use current actor objects. Repeated
  subtypes need distinct `id` values or the loader reports replacement.
- Named `weakpoint_sets` merge first and inline `weakpoints` override matching entries last; deletion
  has dedicated semantics.
- `armor`, `melee_damage`, `attack_effs`, `emit_fields`, and death functions have their own contracts.
- Upgrades, reproduction, revive/zombify/fungalize, and corpse, egg, or baby IDs affect long lifecycles.

`copy-from` inherits only what the factory supports. `extend`, `delete`, `relative`, and
`proportional` are not interchangeable for every field; armor, weakpoints, and special attacks have
specialized readers.

### Validation

Run the formatter, `make -j2 json-check`, and `--check-mods` for the real Mod set. Run the relevant
`monster_test` filter and inspect spawning, faction behavior, paths, attack cooldowns, drops, death,
upgrade or reproduction, and save reload across multiple seeds. Performance review should include
frequent special attacks, pathfinding, field emission, and large groups.

A valid combination is not necessarily playable. Review HP, speed, armor, damage, spawn weight, and
loot as one balance and regression surface.
