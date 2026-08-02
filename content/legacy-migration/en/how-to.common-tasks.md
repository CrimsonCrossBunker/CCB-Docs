## Current contribution routes

The old FAQ's instructions around `omdata.h`, large `switch` statements,
`player::activate_bionic`, and direct `iuse` registration are not current procedures.
Start from the loader for the data type, a neighbouring first-party JSON example, and
the relevant tests. Only then decide whether a C++ extension is actually required.

### Add or change a monster

1. Find a similar `MONSTER` definition under `data/json/` or the target Mod and copy the
   smallest working example.
2. Use a globally unique ID. Update the relevant monster group if the monster should
   spawn naturally; adding the type alone does not place it in the world.
3. Reuse item groups for drops and prefer existing JSON actors or EOC capabilities for
   special attacks. Change native registration only when the public data contract cannot
   represent the behaviour.
4. Run JSON formatting and loading checks, then the narrowest applicable filter from
   `tests/monster_test.cpp`.

`MonsterGenerator::load_monster` delegates definitions to the monster factory. Later
consistency checks also validate species, harvest data, ammunition, and referenced IDs,
so successful JSON parsing does not prove that a definition is complete.

### Add an overmap terrain or building

1. Decide whether the change is an overmap terrain, an overmap special, or mapgen; these
   are different layers.
2. Select a current example from `data/json/overmap/`, the target Mod, and adjacent mapgen
   definitions.
3. Declare orientation, connection, city placement, or wilderness-special relationships
   that the feature needs.
4. Run JSON loading plus the relevant mapgen or overmap tests. Do not copy the legacy
   hard-coded enum and `draw_map` switch procedure.

`overmap_terrains::load` feeds a factory, and later consistency checks resolve mapgen IDs
and spawn groups. Validate both overmap placement and the mapgen it selects.

### Add an item, armour, or use action

1. Start from the current object type and a neighbouring definition. Confirm `copy-from`,
   required fields, and defaults.
2. For armour, review pockets, coverage, materials, layers, and hit-location semantics.
   The protection sequence in the legacy FAQ is not a stable formula.
3. Prefer an existing use action, EOC, or Lua API. Add a native action only when a public
   contract cannot express the behaviour, and update registration, tests, and documentation
   impact together.
4. Run JSON formatting, loading, ID checks, and the affected focused test.

`itype::load` reads mass, volume, length, prices, and subtype slots before later factory
finalization and checks. Follow the whole load lifecycle instead of relying on one example.

### Minimum pre-PR loop

- Use the nearest `AGENTS.md` and `ai/test-matrix.yml` to select the narrowest validation.
- Fill Documentation impact, Related CCB-Docs PR, Affected documentation IDs, Generated
  reference impact, and Responsible human.
- Record the commands, platform, and actual results. Explain skipped checks; do not hide a
  focused failure behind an unrelated full test run.
- If a public Schema, LuaLS declaration, registration, or generated inventory changes,
  regenerate the reference and inspect the diff.

Continue with [common tasks](../getting-started/common-tasks.md), the
[JSON overview](../json/overview.md), the [EOC overview](../eoc/overview.md), and
the [testing strategy](../validation/testing.md).
