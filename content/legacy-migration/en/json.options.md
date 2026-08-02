## Game options and external options

CCB options are not one JSON registry. Menu options are primarily registered by
`options_manager::add_options`. Hidden external options come from `data/core/external_options.json`
and mod data, then `options_manager::add_external` creates internal entries with a type and default.
Saved global values come from `config/options.json`; world values come from the world directory and
may override the corresponding world option.

Only registered options are meaningful when saved values are read. `options_manager::deserialize`
passes old names and values through `migrateOptionName` and `migrateOptionValue`, skips explicitly
removed legacy entries, and then sets the current entry. External options are always hidden by
default. `get_value_type` defines the basic supported types, including bool, int, float, int_map,
string_select, and string_input. Treat the historical loading-order description as guidance, not a
permanent ABI; verify the current startup, world-load, and mod-loader paths.

Moving a menu option to an external option must preserve old-save behavior. The historical `stub`
technique prevents an external definition from replacing an already selected value, but its exact
fields and ordering must be checked against the current loader and `external_options.json`. Test
defaults, global/world precedence, old name and value migrations, unknown and removed entries, mod
load order, and save/reload. Keep user-facing guidance aligned with the menu tooltip.
