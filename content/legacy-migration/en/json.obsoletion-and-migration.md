## Choosing obsoletion and migration

There is no universal migration covering every JSON type. First identify whether an old ID belongs
to items, traits, terrain or furniture, overmap terrain, vehicle parts, effects, spells, Mods, or
another registry. Use that loader's registered migration object. If no loader exists, retain the old
ID or compatibility shim, or implement and test non-behavioral migration support; do not invent a
Schema contract.

### Item `MIGRATION`

Current item migration accepts one or more old `id` values and may set `replace`, `variant`,
`from_variant`, flags, charges, contents, sealed state, and `reset_item_vars`. `replace` cannot equal
the old ID. A variant migration matches only that old variant. Contents that do not fit a normal
container enter a dedicated migration pocket instead of being silently lost.

```jsonc
{
  "type": "MIGRATION",
  "id": "old_item_id",
  "replace": "new_item_id"
}
```

The replacement type must exist when loading and finalizing. Counts, charges, pockets, item
variables, damage, ownership, and sealed state may all need fixtures; changing one ID is not proof
of a complete migration.

### Other registries and Mods

CCB currently registers migrations for traits, bionics, proficiencies, terrain or furniture, fields,
vehicle parts, traps, effects, overmap terrain or specials, camps, spells, global variables, and
Mods, among others. Their fields and abilities differ. `mod_migration` uses an old `id` plus
`new_id`, or a translated `removal_reason` when removed; the target Mod must be valid.

`obsolete: true` generally controls new-content selection and does not rewrite every saved
reference. Retention windows, replacements, release notes, and removed-ID tests remain necessary.

### Validation

Load each real old fixture with current code, inspect migrated objects and nested contents plus map,
character, and world state, then save and load again to prove idempotence and no duplicated
resources. Run formatting, `make -j2 json-check`, `--check-mods`, and owning subsystem tests. Cover
missing targets, chains and cycles, old and new Mods together, and the release boundary for eventual
migration removal.
