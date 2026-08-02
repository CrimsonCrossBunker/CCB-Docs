## Current CCB item JSON model

CCB loads pickupable entities through `"type": "ITEM"`. `itype::load` reads common fields,
then `subtypes` determines whether armour, tool, gun, ammunition, and other slots are read.
The legacy field list is a navigation aid, not a contract. Required fields, defaults, ranges,
and combinations come from the current loader, registrations, tests, and the
[JSON object-type index](../index.md).

### Minimal definition and stable IDs

```jsonc
{
  "type": "ITEM",
  "id": "ccb_example_part",
  "name": { "str": "example part" },
  "description": "A component used by the documentation example.",
  "symbol": ";",
  "color": "light_gray",
  "weight": "100 g",
  "volume": "250 ml",
  "price": "1 USD",
  "price_postapoc": "10 cent",
  "material": [ "steel" ]
}
```

An `id` is a long-lived reference used by saves, recipes, item groups, EOCs, and Mods. Do
not rename a released ID merely for tidiness. If replacement is necessary, check the
migration or obsoletion mechanism and save compatibility first. Player-visible `name` and
`description` values must be translatable; an ID is not display text.

### Subtypes and slots

The current `itype::load_slots` recognizes `ARMOR`, `TOOL`, `PET_ARMOR`, `GUN`, `GUNMOD`,
`AMMO`, `MAGAZINE`, `COMESTIBLE`, `BOOK`, `BIONIC_ITEM`, `TOOLMOD`, `ENGINE`, `WHEEL`,
`SEED`, `BREWABLE`, `COMPOSTABLE`, `MILLING`, and `ARTIFACT`. An ammunition definition,
for example, declares its slot explicitly:

```jsonc
{
  "type": "ITEM",
  "id": "ccb_example_round",
  "copy-from": "223",
  "subtypes": [ "AMMO" ],
  "name": { "str_sp": "example round" },
  "ammo_type": "223"
}
```

- `subtypes` controls which slot fields this definition reads. Do not omit a child's intent
  merely because its parent has a slot.
- `PET_ARMOR` and `ARMOR` cannot be declared together. `GUNMOD` already loads the tool-mod
  slot and cannot be combined with `TOOLMOD`.
- Other compatible subtypes may be combined, but each slot can add mandatory fields and
  finalization checks.

### Common fields and inheritance

Common fields cover dimensions and mass, prices, materials, display, melee or thrown data,
flags, qualities, use actions, pockets, variants, and variables. Do not infer every field
from one example: some use unit strings, some read stable IDs, and some have dedicated
readers.

`copy-from` first copies a base definition. A directly specified top-level field replaces
its value; supported container fields may use `extend` or `delete`; supported numeric or
special objects may use `relative` or `proportional`. These operations are not a universal
schema for every field. See [inheritance](../inheritance.md) and choose a current neighbour
with the same subtype as an example.

### Change and validation sequence

1. Confirm `type`, `subtypes`, field shapes, and ID references in nearby first-party data.
2. Check `itype::load` and the relevant slot `deserialize` method for requirements and ranges.
3. Format only changed files and inspect every extra formatter diff.
4. Run `make -j2 json-check`; add focused pocket, use-action, recipe, or save-ID tests when relevant.
5. For a Mod, run `--check-mods` with the actual Mod set and record untested platforms or interactions.

Formatting alone does not prove loader, ID, or gameplay relationships. Where Schema coverage
is incomplete, the source loader and tests win.
