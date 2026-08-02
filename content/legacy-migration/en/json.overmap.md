## Current CCB overmap data relationships

Overmap data is split across related object types. `overmap_terrain` defines OMT types and
display or connection properties; `overmap_special` composes one or more OMTs under placement
constraints; `overmap_connection` joins linear networks such as roads and subways; mapgen then
builds local maps for the OMTs. A mismatched ID at any layer may appear only during worldgen.

### Overmap terrain and mapgen

A terrain's stable ID can finalize into rotated or linear variants, while mapgen uses its
mapgen ID. Consistency checks report an OMT with neither mapgen nor uniform terrain and validate
static spawn groups. Review a new terrain's:

- name, symbol, colour, vision, and flags;
- rotation, `LINEAR` behavior, and connection directions;
- mapgen ID, uniform terrain, and roof or underground relationships;
- monster density, extras, and location flags;
- compatibility of a released ID with mission targets, saves, and Mods.

Do not hand-build directional suffixes and assume every matcher treats them alike. Where a
field supports exact, type, subtype, prefix, or contains matching, use its current
`ot_match_type` implementation.

### Overmap specials

A fixed special composes OMTs through `overmaps` and connections; a mutable special uses a
different generation model. `occurrences` is mandatory for a real `overmap_special`. City size
or distance, locations, flags, priority, rotation, and connections jointly decide placement.
A special that fits an empty test world is not guaranteed to fit among cities, roads, other
specials, and regional blacklists.

A special can bind an inline EOC, parameters, spawns, and mapgen. Test multi-tile coordinates,
rotation centres, z-levels, and connection endpoints together. Migrating a released special
ID requires the current migration object and a save test.

### Connections and regions

An `overmap_connection` defines connectable terrains and rules. Region settings select the
intra-city and inter-city road, trail, sewer, subway, and rail connections. Changing a
connection or regional reference can reshape newly generated overmaps without rewriting
existing ones, creating old-versus-new save differences.

### Validation

Run the formatter, `make -j2 json-check`, `--check-mods` for the actual Mod set, and relevant
`overmap_test` cases. Generate multiple seeds and regions and inspect special occurrences,
rotation, roads, boundaries, z-levels, mission targets, and no-placement outcomes. Load an old
save for every released ID change.

See [mapgen](mapgen.md) for local tile layout and
[region settings](region-settings.md) for large-scale distribution.
