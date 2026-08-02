## Help-menu JSON

A `"type": "help"` object defines a scrollable help topic. Core topics live in
`data/core/help.json`, while mods may supply their own. `help::load` delegates to
`help::load_object`, which groups topics by source and appends each source in load order.

Each object must provide an integer `order`, a translatable `name`, and a `messages` array of
translatable strings. The order only has to be unique within one source, so separate mods may each
start at zero. The current loader rejects duplicate orders. Core help must be placed in the core JSON
directory rather than presented as an ordinary mod source.

Messages may use color tags and `<press_ACTION_ID>` keybinding tags. `<DRAW_NOTE_COLORS>` and
`<HELP_DRAW_DIRECTIONS>` are special placeholders handled in `help.cpp`. Take action IDs from the
current input registrations instead of guessing from old screenshots or upstream prose. For a new
topic, check translation extraction, narrow-terminal wrapping, tiled and terminal presentation,
topic order, and JSON loading.
