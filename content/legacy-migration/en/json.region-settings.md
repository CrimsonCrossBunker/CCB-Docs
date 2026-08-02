## Current CCB region-settings structure

Region settings determine default terrain, ground cover, forests, rivers, lakes and oceans,
cities, road connections, highways, map extras, weather, and feature-flag filters for new
overmaps. They are not one open-ended object: multiple `region_settings_*` object types load
through separate factories and the main `region_settings` composes them by ID.

### Main region

The main object reads default OMT and ground cover, mandatory cities, weather, forest, river,
lake, ocean, highway, ravine, connections, map extras, terrain or furniture replacements, and
switches for roads, railways, specials, and neighbour connections. A valid region with
`id: "default"` must exist or finalization reports it.

Do not infer component fields from a legacy table. For example, the current
`region_settings_city` requires `city_size`, while forest, highway, lake, and map-extra
collections each have their own readers, defaults, and stable IDs.

### Extension and replacement

```jsonc
{
  "type": "region_settings",
  "id": "default",
  "copy-from": "default",
  "feature_flag_settings": {
    "extend": { "blacklist": [ "CCB_EXCLUDED" ] }
  }
}
```

Concrete `copy-from` and extension support depends on that field's reader. Same-ID Mod patches
depend on load order and can replace each other when several Mods alter the default region. A
new region is often easier to review than an implicit change to every world, but still needs
a world-selection entry and correct dimension or layout references.

### Cities, extras, and feature flags

City weighted lists reference OMTs or specials. Radius, size, and spacing affect distribution
but do not guarantee that every candidate can be placed. A map-extra collection combines a
chance with registered extra IDs and weights. Feature blacklists and whitelists combine with
overmap location flags; over-restricting them can leave empty candidates or broken networks.

A region change affects only overmaps that have not been generated. Explored regions are not
rebuilt. Document visual, resource, or road changes separately for new worlds or areas and for
already generated parts of old saves.

### Validation

Run the formatter, `make -j2 json-check`, and `--check-mods` for the actual Mod set. Generate
complete overmaps from several seeds, recording the selected region, and inspect cities and
roads, forests and water, specials, extras, weather, and feature filters. Load an old world and
cross into a new overmap to check boundaries and connections.

See [overmap](overmap.md) for OMT and special relationships and [mapgen](mapgen.md) for local generation.
