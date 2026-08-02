## Tileset authoring and composition

CCB distributions use compositing tilesets: individual PNG sprites, tile-entry JSON,
`tile_info.json`, and `tileset.txt` are converted by `tools/gfx_tools/compose.py` into tilesheets and
`tile_config.json`. Runtime-readable fields remain defined by the tiles loader; compose only
validates and transforms the source format it understands.

### Source layout and tile entries

A tile entry maps one or more game-entity `id` values to `fg` and `bg` sprite roots. It may use
rotations, weighted variants, `multitile`/`additional_tiles`, seasonal, gender, and item-variant
names, plus contextual layering. Terrain/furniture connections and rotation also depend on
`connect_groups`, `connects_to`, and `rotates_to` in game JSON. A tileset cannot create those runtime
relationships. Inventory hardcoded overlay and animation IDs from current `cata_tiles.cpp` and call
sites; a historical hand-maintained list can be incomplete.

`tile_info.json` describes default and per-sheet sprite sizes, offsets, pixel scale, sheet width,
and filler/fallback/exclusion behavior. Duplicate sprite roots, filler ordering, and cross-directory
references affect the result, so keep names unambiguous and review compose warnings.
`layering.json` contexts, item/field variants, offsets, and layers form a separate runtime contract.

### Composition, distribution, and validation

Current CI uses a command shaped like:

```sh
python3 tools/gfx_tools/compose.py --use-all --obsolete-fillers \
  --feedback CONCISE --format-json --loglevel INFO SOURCE DEST
```

Take actual flags from `compose.py --help`; options such as `--only-json`, `--fail-fast`, and palette
conversion change output or diagnostics. Compose into a temporary destination, review unused,
missing, and duplicate sprites plus generated JSON and image dimensions, then load it in a tiled
build. Test rotation, multitiles, fallback, zoom, seasons, overlays, and layering. Use
`decompose.py` only to convert an old indexed tileset, then manually organize its generated names
and directories.

Every artwork needs a redistributable license and traceable attribution; successful composition is
not license approval. `.github/workflows/compose-tilesets.yml` defines the current packaging matrix.
External tileset-repository content is not a CCB runtime contract, so pin and review its source and
revision.
