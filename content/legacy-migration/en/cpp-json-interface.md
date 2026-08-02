## CCB C++ JSON interface

First distinguish three jobs: loading human-authored game data, reading program-written old saves,
and writing new saves. They share `JsonValue`, `JsonArray`, `JsonObject`, `JsonMember`, and
`JsonOut`, but have different compatibility policies. Game data has factory inheritance; save data
must recognize old formats and must not treat `copy-from` as a save mechanism.

### Read and write basics

`JsonValue` tests and reads scalars or becomes an object or array. `JsonObject` accesses named
members, `JsonArray` iterates or consumes positions, and `JsonMember` preserves both key and value.
Prefer `read` and existing deserializers or readers instead of reimplementing type dispatch.

After a type implements `T::serialize( JsonOut & ) const` or a free `serialize`,
`JsonOut::write` and `member` can compose it. Implement the corresponding `deserialize` for reads.
The emitted form is a compatibility contract: before renaming, removing, or changing a field type,
retain an old-format reader and round-trip plus frozen-fixture tests.

### Game-data loaders

A generic factory manages IDs, `copy-from`, deferred loading, finalization, and consistency checks.
An object's `load` normally uses:

- `mandatory( jo, was_loaded, name, member[, reader] )` for values required on first definition;
- `optional( jo, was_loaded, name, member[, reader], default )` for an explicit first-load default;
- typed readers for shorthand, units, IDs, containers, and supported inheritance operations.

Put the default in the `optional` call rather than relying only on header initialization.
`was_loaded` preserves a parent's value when the child omits a member. Passing false incorrectly
erases inherited state; passing true incorrectly can skip first-definition requirements.

`extend` and `delete`, `relative`, and `proportional` are all opt-in. Container readers often support
the first pair; numeric operations depend on the type and reader. A field resembling a vector or
integer is not proof that every patch form is supported.

### Errors and strictness

Let `JsonObject` or the reader throw at a specific member so file, line, column, and member context
survive. Do not call `allow_omitted_members` broadly for “compatibility”; reserve it for deliberate
forwarding or ignored-object boundaries. Run finalization and consistency checking after parsing
because cross-ID failures and cycles often appear only there.

### Validation

For game data, run formatting, `make -j2 json-check`, `--check-mods` for the actual Mod set, and
object-focused tests. For save data, test current write-to-read round trips, frozen old fixtures,
missing and added fields, and malformed input. Compile every target using a changed public header
and confirm diagnostics retain source context.
