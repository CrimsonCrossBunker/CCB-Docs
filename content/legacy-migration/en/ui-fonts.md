## Font configuration for the tiled build

The tiled build reads four fallback chains from the user's `fonts.json`: `typeface`,
`gui_typeface`, `map_typeface`, and `overmap_typeface`. Each value may be a path string, an object
with `path`, or an array of those entries. Array order is glyph fallback order. The loader ensures
that `data/font/unifont.ttf` is present as the final fallback.

An object may set `hinting` and `antialiasing`. Current accepted hinting strings are `Auto`,
`NoAuto`, `Default`, `Light`, `None`, and `Bitmap`. An unknown value reports a debug message and
falls back to default; do not copy inconsistent enum lists from old prose. Disabling antialiasing
sets monochrome and mono-hinting flags. Font paths resolve in the runtime environment, and a
distributed package must actually include the file under a compatible font license.

### Migration and validation

`font_loader::load` reads the current configuration. If it does not exist, the loader reads the
legacy/default path and `font_loader::save` writes the canonical object-array form. This write-back
may change representation while preserving selection semantics.

Validate with Latin, simplified and traditional Chinese, combining marks, wide characters, emoji
fallback, and missing glyphs. Cover all four screen roles, DPI/scaling combinations, Bitmap, Light,
and None modes, antialiasing on and off, and missing files. Also inspect ImGui atlas construction,
map-cell dimensions, terminal alignment, memory/startup cost, and license attribution. Successful
JSON parsing alone does not prove a usable font.
