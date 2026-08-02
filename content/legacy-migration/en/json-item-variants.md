## Item aesthetic variants

An item's `variants` are presentations of one itype, not separate gameplay items. Each entry requires
a stable `id` and may override name, description, symbol, color, or ASCII picture. `weight` defaults
to one, `append` controls description appending, and `expand_snippets` controls expansion at
generation. Finalization inherits a missing name or description from the base item.

This `itype_variant_data` contract is unrelated to C++'s `cata_variant` typed-value container. Their
names are similar, so documentation, tests, and source symbols must identify the correct one.

### Scope

A variant expresses visual, naming, or prose differences only. It cannot change mass, damage,
nutrition, armor, pockets, recipes, or other gameplay statistics. Use a separate itype, inheritance,
a snippet or conditional name, or another fitting structure for gameplay differences. Many tiny
variants impose translation and tileset cost; every entry needs a recognizable, plausible use.

Variant IDs can appear in item instances, spawns, migrations, and serialization. Before deleting or
renaming one, inspect save compatibility and migrations. Also inspect the expanded result when
copy-from clears or replaces variants.

### Validation

Run formatting, `make -j2 json-check`, and Mod `--check-mods`, then generate every weighted variant.
Check default inheritance, translation plurals, symbols, colors, ASCII art, snippet expansion,
tileset fallback, save round trips, and old-ID migration. `tests/cata_variant_test.cpp` does not test
item variants; use focused item-name, spawn, or serialization tests.
