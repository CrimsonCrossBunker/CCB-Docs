## Terrain, furniture, and bashing contracts

Terrain and furniture `bash` objects share fields loaded by `map_common_bash_info`, followed by
replacement fields from `map_ter_bash_info` or `map_furn_bash_info`. CCB stores unfinished bash
damage on the map tile. Reaching the active `str_max` value, including a blocked or supported
variant, replaces the object and clears accumulated damage.

### Strength and damage profiles

`str_min` is the armor threshold applied to each damage type and `str_max` is the object's effective
HP. `damage_to()` applies the selected `bash_damage_profile` multiplier to each weapon damage type,
subtracts the threshold from each result, and accumulates only positive values. During finalization,
valid damage types omitted by the profile receive that type's `bash_conversion_factor`. The default
profile explicitly names bash and receives all other valid types through finalization.

The historical statement that HP equals `str_max - str_min` is therefore no longer accurate. Do not
predict results from character strength or one bash number alone: weapon damage composition,
profile, blocked or supported state, and existing map damage all affect destruction.

### Common fields and replacements

- `profile` references a `bash_damage_profile` and defaults to `default`.
- `str_min_blocked`/`str_max_blocked` and `str_min_supported`/`str_max_supported` are conditional
  replacements.
- `items`, `sound*`, `hit_field`, `destroyed_field`, `explosive`, and tent or collapse fields control
  side effects.
- Terrain must provide `ter_set`; `ter_set_bashed_from_above` defaults to it.
- Furniture may omit `furn_set`, which defaults to `f_null`.

Use the three loaders for requiredness and defaults rather than inferring a contract from occurrence
counts in existing JSON.

### Changes and validation

A new profile must use valid damage types and non-negative multipliers and pass factory finalization
and checks. For a terrain or furniture `bash` change, inspect replacement IDs, item groups, field
spawns, bashing from above, support or blocking, and accumulated-damage reset together. Run the JSON
formatter and `make -j2 json-check`, then add a focused `tests/map_bash_test.cpp` case for behavioral
changes. Mod combinations also need a real `--check-mods` run.
