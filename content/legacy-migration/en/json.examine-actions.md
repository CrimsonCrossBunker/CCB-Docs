## Terrain and furniture examine actions

`examine_action` accepts a registered hardcoded string, a JSON examine actor, or an array mixing
both. The current map in `iexamine_functions_from_string` defines string registrations. An unknown
name reports an error and falls back to `none`; the historical hand-written list is not complete.

### Actor contracts

- `appliance_convert` requires item and optionally sets furniture or terrain. Finalization validates
  the item, terrain, furniture, and appliance vpart.
- `cardreader` requires flags, success_msg, and redundant_msg. The mapgen_id route is exclusive with
  radius plus terrain or furniture changes; query, hacking, card consumption, and monster despawn
  also have combination constraints.
- `effect_on_conditions` loads named or inline EOCs in order. Its dialogue has the examiner as u,
  null npc, and `this` furniture ID plus `pos` context.
- `mortar` requires ammo and range and may use condition, aim or flight variables, and completion
  EOCs. Completion also supplies `this`, `pos`, and `target`.

The top-level actor type selects the concrete loader. Do not copy fields across actors or infer
mandatory members and defaults from occurrence counts.

### Design boundary

Reference an existing hardcoded action when it matches. Prefer an actor or EOC for configurable
composition. A new hardcoded string or actor type changes a public contract and needs registration,
loader and finalization, JSON inventory, bilingual documentation, and tests together. An EOC must
define talkers, context variables, repeat behavior, and map-bubble boundaries.

### Validation

Run formatting, `make -j2 json-check`, Mod `--check-mods`, and examine a focused fixture. Cover
missing items, cards, or ammo; cancelled queries; repeat use; invalid IDs; hacking and mapgen paths;
EOC context; and save reload in `tests/iexamine_test.cpp`. Successful parsing alone is insufficient.
