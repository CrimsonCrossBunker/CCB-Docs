## Current CCB mapgen model

Mapgen turns one or more overmap terrains (OMTs) into map tiles, furniture, items, creatures,
and other content. A `mapgen` performs initial generation, `nested_mapgen` supplies reusable
chunks, and `update_mapgen` changes an existing map. They share palette and placing syntax but
have different size, background, and lifecycle rules.

### Standalone mapgen

```jsonc
{
  "type": "mapgen",
  "om_terrain": "ccb_example_oter",
  "weight": 1000,
  "object": {
    "fill_ter": "t_grass",
    "rows": [
      "                        "
    ]
  }
}
```

A normal OMT is generally 24 by 24; the example omits the remaining rows and is not directly
loadable. `om_terrain` can name one ID, several IDs, or an OMT grid. In grid form, row dimensions
also expand in blocks of 24. Multiple mapgens for one OMT are selected by `weight`; zero disables
that variant.

`mapgen_function_json::setup_internal` permits `fill_ter`, `predecessor_mapgen`, or
`fallback_predecessor_mapgen` to provide a background. Without one, every character in `rows`
must have a terrain definition in a local or referenced palette. Do not use a space to hide
undefined terrain.

### Rows, palettes, and placings

Mappings for `terrain`, `furniture`, fields, items, monsters, vehicles, traps, computers, zones,
and other entries connect row characters to placings. A named `palette` requires an ID and can
reference other palettes; loops are reported. Parameters and dynamic mapgen values expand the
possible results, so validate every possible ID rather than only the default.

Coordinate placings and character rows can coexist. In a multi-OMT mapgen, random coordinate
ranges must not accidentally cross OMT boundaries. Rotation, mirroring, linear-terrain suffixes,
and multiple z-levels change direction semantics and need structural tests.

### Nested and update mapgen

A `nested_mapgen` requires a positive square `mapgensize` and can replace a region of a parent
mapgen while reusing palettes. An `update_mapgen` needs no fill or row background: it loads an
existing map and applies placings for missions, EOCs, or post-processing. An update is not
automatically idempotent; repeated execution can duplicate items or NPCs, remove structures,
or change a saved map.

Handle an update's target OMT, offset, rotation, and verification failures. Initial worldgen
success does not prove that the same update is safe for an old save.

### Validation

1. Cross-check overmap-terrain and mapgen IDs, special rotation, and connections.
2. Run the formatter, `make -j2 json-check`, and `--check-mods` for the actual Mod set.
3. Run `mapgen_function_test`, plus `mapgen_post_process_test` for post-processing changes.
4. Inspect every variant, rotation, neighbour, z-level, palette parameter, and boundary character.
5. For an update, test first and repeated execution, an old save, missing targets, and occupied maps.

New contributors can start with the [mapgen tutorial](../../tutorials/json-mapgen/beginner.md).
This page defines current loader boundaries, not a substitute for checking source fields.
