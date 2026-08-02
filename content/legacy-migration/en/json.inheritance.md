## Current CCB JSON inheritance rules

`copy-from` is not an automatic language feature of every JSON object type. Many types use
`generic_factory`, some have specialized implementations, and others do not support it.
For each use, follow the current registration into its loader and confirm the operations
that object actually implements.

### Generic-factory load order

For an object using `generic_factory`, the usual sequence is:

1. With `copy-from`, look for a loaded concrete object or `abstract`.
2. If the base is not loaded, place the child in the deferred queue and retry later.
3. Copy the base, then let the child's loader replace or adjust fields.
4. An `abstract` exists only for inheritance; specifying both `abstract` and a real `id` is an error.
5. Finalization and checks resolve cross-IDs and can find problems not proven during initial loading.

Deferred loading often handles ordering, but does not make an inheritance cycle valid or make
cross-Mod replacement order irrelevant.

### Four modification forms

```jsonc
{
  "type": "ITEM",
  "id": "ccb_example_child",
  "copy-from": "ccb_example_parent",
  "name": { "str": "example child" },
  "relative": { "weight": "50 g" },
  "proportional": { "price": 1.2 },
  "extend": { "flags": [ "WATER_FRIENDLY" ] },
  "delete": { "flags": [ "FRAGILE" ] }
}
```

- A directly specified top-level field normally replaces the inherited value.
- `relative` adds to a base value when its reader supports the operation.
- `proportional` multiplies a base value when its reader supports the operation.
- `extend` and `delete` add or remove members through a supported container reader.

These express intent; they are not guarantees. Using the blocks without `copy-from` is warned
or rejected. An unsupported type, field, or reader may report an error, be ignored, or use
special behavior. Support for `extend` on `ITEM.flags` does not imply support for every array
on every object.

### Abstracts, real objects, and chain depth

Use `abstract` for a stable base that a family of definitions always shares; it is not a real
in-game ID. Prefer one or two narrow inheritance levels. A deep chain makes one base edit
silently affect many objects or Mods and makes save compatibility and balance review harder.
Where a variant mechanism already represents display-only differences, it usually needs no
new inheritance chain.

### Specialized implementations

- `recipe_dictionary::load` performs its own recipe deferral and copy; inline requirements
  add replacement rules.
- An item group can copy only a previously loaded group with the same ID, and its loader reads
  `extend` specially.
- Some objects extend selected containers by default; others support only `copy-from` and not
  all four modification blocks.

Do not maintain a supposedly permanent complete list of supported types. Use the current
object registry to find the registration, then inspect the loader, reader, and tests.

### Review and validation

1. Identify which core or Mod supplies the base, its load order, and stable ID.
2. Confirm whether a direct field replaces, merges, or has specialized semantics.
3. Check the reader for units and ranges used by `relative` or `proportional`.
4. Cover the chain, missing bases, duplicate IDs, and finalization with an existing test or minimal Mod.
5. Run the formatter, `make -j2 json-check`, and `--check-mods` for the actual Mod set.

If implementation evidence cannot prove that a field supports an inheritance operation,
write the complete definition explicitly or add a test first. A quiet load is not proof.
