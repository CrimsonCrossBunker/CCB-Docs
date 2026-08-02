## Current CCB item-group contract

An `item_group` describes what to spawn; it is not an item definition.
`Item_factory::load_item_group` reads named groups, while `item_group::load_item_group` can
also read anonymous inline groups in monster drops, recipe byproducts, and similar fields.
Referenced item, group, container, and event values must be loaded stable IDs.

### Collection and distribution

```jsonc
{
  "type": "item_group",
  "id": "ccb_example_supplies",
  "subtype": "distribution",
  "entries": [
    { "item": "water_clean", "prob": 70 },
    { "item": "bandages", "prob": 30 }
  ]
}
```

- A `distribution` treats entry `prob` values as relative weights and makes one distribution choice.
- A `collection` evaluates entries independently; `prob` is the percentage chance to include one.
- The old or omitted subtype is treated as a distribution. New data should state its intent.

An entry uses `item` for an item and `group` for another group. `items` and `groups` are
shortcuts for simple IDs and probabilities. Use full `entries` objects for damage, charges,
count, containers, events, faults, variants, or variables. If shortcut arrays and `entries`
are both present, all of them are added; they are not deduplicated.

### Containers, ammunition, and recursion

Group-level `ammo` and `magazine` values are percentage chances used for guns, tools, and
magazines. Explicit entry modifiers such as `charges` can change default loading behaviour.
`container-item`, `container-group`, sealing, and overflow rules affect nesting and capacity.
A multi-magazine-well item cannot distribute one ambiguous `charges` value across its wells;
test it against the current loader and real item definition.

Nested groups can create deep chains. Bad recursion, an empty distribution, or a missing ID
may only become visible during loading or generation. Keep hierarchies shallow and use tests
around `item_group::items_from` for structural invariants rather than only probabilities.

### Extending an existing group from a Mod

The current implementation allows an item group to `copy-from` only a previously loaded group
with the **same ID**, then add entries through `extend`:

```jsonc
{
  "type": "item_group",
  "id": "ccb_example_supplies",
  "copy-from": "ccb_example_supplies",
  "subtype": "distribution",
  "extend": {
    "entries": [ { "item": "aspirin", "prob": 10 } ]
  }
}
```

A same-ID definition without `copy-from` rebuilds or replaces the group; it does not append
implicitly. Load order and Mod dependencies are therefore contractual. Do not assume that
same-ID patches from two Mods can be reordered.

### Inline groups and validation

Some fields accept a group ID, inline object, or entry array. An inline group receives an
internal unique ID and cannot be referenced elsewhere, which suits a one-off drop or
byproduct. Its default subtype is supplied by the calling loader; check that field before
copying an array from another context.

Run the JSON formatter and loader, ID checks, and `--check-mods`. Add focused coverage for
important drops, including empty results, container overflow, charges or magazines, event
gates, and possible recursion. One Debug-menu sample does not prove probability behaviour.
