## The CCB color system

`color_manager::load_default` establishes color names, pairs, and invert/highlight mappings, while
`data/raw/colors.json` supplies default base RGB values. Common names use `c_foreground`; `h_`
denotes highlighting and `i_` inversion. Some foreground/background combinations also have named
pairs. Query the current color manager for valid names rather than assuming any two names can be
concatenated.

Player-facing strings may use properly closed and nested `<color_name>…</color>` tags. Color must
not be the only semantic channel: disabled, dangerous, and selected states also need text, symbols,
or structure for screen readers and alternative themes. Support for `color` or `bgcolor` in map,
item, and other JSON objects is defined by each loader; it is not uniform across object types.

### User configuration and validation

Users can override base RGB values, and the color manager serializes named custom and inverted
mappings. ImGui styles are a separate configuration path with RGBA values rather than curses pairs.
A theme can replace highlight/invert rules, so code must not depend on the actual RGB of one default
theme.

For a color-contract change, run JSON loading, color consistency, and relevant UI/light tests. Check
default and custom themes, curses and tiles, ImGui, low contrast and color-vision differences,
nested tags, invalid-name fallback, and screen readers. RGB values documented at one source commit
are defaults, not a permanent visual ABI.
