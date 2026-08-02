## Your first JSON mapgen

A spawnable location normally spans three contracts: `mapgen` draws reality-bubble tiles,
`overmap_terrain` supplies OMT IDs, display, and flags, and a `city_building`, region setting, or
`overmap_special` decides world placement. Start from a current similar location and follow loaders
and data references. Do not copy stale upstream paths or treat a filename as registration.

### Minimal flow

1. Define overmap-terrain IDs for each ground, floor, basement, and roof level.
2. Add a `"type": "mapgen"` with `om_terrain` bound to the target ID. Multiple implementations for
   one ID participate according to `weight`.
3. In `object`, provide `fill_ter` and fixed-size `rows`, then explain symbols with terrain,
   furniture, palettes, and placement entries. Row count and width must match the mapgen grid; the
   standard single-OMT size comes from current `SEEX`/`SEEY` constants.
4. Register a city location through current `city_building` and region data, or use an
   `overmap_special` for wilderness placement and connections. Align stairs, ladders, downspouts,
   and roof openings across every z-level point.
5. When using regional groundcover or an existing palette, inspect all inherited effects. Editing a
   shared palette can change unrelated locations.

### Content and probability

Terrain and furniture symbols may share a cell; a cell without explicit terrain uses `fill_ter`.
Item, monster, vehicle, NPC, field, trap, and liquid placements each define their own required
fields, chance/repeat behavior, and coordinate semantics. Do not infer one placement type from
another. Vehicle mount origins and rotation require real generation tests. Overmap monster density
and fixed mapgen spawns solve different problems.

### Validation

Run the project JSON formatter, `make -j2 json-check`, the target mod's `--check-mods`, and focused
mapgen tests. Use debug generation on fresh, previously ungenerated OMTs and cover every weighted
variant, four rotations, z-levels, city/special placement, season/region, loot density, and boundary
connection. Inspect terrain under furniture, door/window reachability, roofs and basements, vehicles
near OMT boundaries, lighting, sight, and save/reload. A submap already generated into a save does
not automatically rebuild after JSON changes and is not a valid sample of the new definition.
