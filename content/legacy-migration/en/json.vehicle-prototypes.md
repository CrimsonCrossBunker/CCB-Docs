## Vehicle prototype contract

A `vehicle` prototype spawns a stock vehicle; the resulting vehicle uses a different save
representation. Its generic factory owns `id`, `parts` is the core structure, and `name`, `items`,
`zones`, and `color_palette` are optional. `blueprint` is currently consumed only for compatibility
and does not drive spawning.

### Parts and installation order

Each part group requires `x`, `y`, and `parts`. An element may be a `vpart_id` string or an object
with `part`; the object can also set 0–100 `ammo`, `ammo_types`, `ammo_qty`, `fuel`, and `tools`.
`part#variant` is split at the last `#` in either form.

Array order is installation order and must satisfy in-game prerequisites for frames, mounts, wheels,
engines, turrets, and stacking. Multiple groups may append at one coordinate, but cannot bypass
installation rules. Limited copy-from applies the parent first and appends parts, items, and zones;
inspect the expanded result rather than only the child object.

### Items, zones, and export

An item spawn requires `x`, `y`, and 0–100 `chance`; it may set `items`, `item_groups`, `magazine`,
and `ammo`. An item may be a string or `{ "id", "variant" }`. A zone requires type, x, and y and may
have name or filter. It is placed only when the vehicle has a faction owner.

The debug exporter can produce parts, selected turret, fuel, and tool state, simple cargo items,
zones, and a visual blueprint. It leaves placeholder ID and name values and does not guarantee a
round trip for complex containers or comestibles. Format and review its output manually.

### Validation

Run formatting, `make -j2 json-check`, and target-Mod `--check-mods`. Spawn a complex prototype in
game and inspect refresh, installation order, cargo, owned zones, and palettes. Changes to export or
fields need a `tests/vehicle_export_test.cpp` case that serializes and reloads equivalent data.
