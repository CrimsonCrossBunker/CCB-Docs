## Dimension region layouts

`dimension_region_layout` selects the `region_settings` used by overmaps in a dimension. Its loader
requires `generation_mode`, but the pinned CCB switch creates a generator only for `UNIFORM`.
Appearance in a JSON enum or header does not make another mode usable.

### Currently supported mode

`UNIFORM` is dynamic and requires `uniform_region`. As each overmap is first requested, its generator
maps that coordinate to the same region. All current first-party entries in
`dimension_regions.json` also use this mode.

The header retains MANUAL_VORONOI, RANDOM, EIGHTHS, static-layout types, and part of their base
infrastructure, but the loader has no corresponding cases. Do not publish Mods using those values or
treat unwired `generated_bounds_*` and `layout_out_of_bounds` fields as public JSON contracts. A new
mode needs deserialization, a generator, factory finalization and checks, and tests—not only an enum
value.

### ID chain and validation

The layout's `uniform_region` must be valid region settings, and `dimension.region_layout` then
references the layout. Inspect the complete dimension → layout → region settings → overmap
generation chain.

Run formatting, `make -j2 json-check`, and complete `--check-mods`, then create a new world or
dimension and generate several overmaps. A new generator needs deterministic-seed, boundary, save
reload, and invalid-ID fallback tests. Region-layout changes can alter newly generated worlds, so the
PR must state their compatibility impact.
