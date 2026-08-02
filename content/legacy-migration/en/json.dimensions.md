## Dimension definitions and switching

A `dimension` object reads only `region_layout`; finalization reports an invalid reference and falls
back to `default`. Runtime stores non-main dimension world data in the save's dimension area and
switches the currently loaded data during travel. This is not a remote API for arbitrary map reads
or writes in an unloaded dimension.

### Data and EOC boundaries

A new dimension needs a valid `dimension_region_layout` and its region settings. The current layout
implementation supports only UNIFORM, so verify the implementation boundary in the layout page.

`u_travel_to_dimension` performs the switch. `npc_travel_radius` defaults to zero and its filter to
`all`; the consumer evaluates both to select accompanying NPCs. `item_travel_radius` defaults to -1,
meaning no item transfer, while `target_location` can change the collection and placement center.
A vehicle option also exists. Take fields, defaults, and accepted filters from the EOC registry and
`talk_effect_fun::f_travel_to_dimension`; historical snippets are examples only.

`clear_dimension` removes that dimension's persistent world data, so re-entering generates it again.
This loses its map, items, vehicles, monsters, NPCs, and other state. It is a destructive authoring
operation, not routine teleport cleanup.

### Safe workflow

Capture required location variables before travel, switch dimensions, then run mapgen updates or
teleport against the now-loaded dimension. Do not reuse bubble coordinates after the old dimension
is unloaded or assume equal coordinates identify the same place across dimensions.

Run formatting, `make -j2 json-check`, and Mod `--check-mods`. In a disposable world, cover first
creation, round trips, save reload, NPC, item, and vehicle boundaries, invalid-layout fallback, and
regeneration after clear. Never test `clear_dimension` on a valuable save.
