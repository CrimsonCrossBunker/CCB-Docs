## Current JSON style and validation

Two-space indentation, stable field layout, short inline arrays, and wrapped long structures
are determined by the repository formatter. Do not guess formatting from a legacy example
or use a generic formatter across whole files. CCB's formatter parses the project's JSON
dialect and emits project style.

### Formatting entry points

CI runs the complete JSON style check with:

```sh
make style-all-json-parallel RELEASE=1
```

For a small set of locally changed, checked files, use:

```sh
make style-json
```

The Makefile's `JSON_FORMATTER_BIN` selects the platform artifact, such as
`tools/format/json_formatter.cgi` or `.exe`. Do not depend on the legacy external web
formatter.

### Semantic validation

```sh
make -j2 json-check
```

Formatting proves layout only; `json-check` also exercises loading. Changes to stable IDs,
`copy-from`, EOCs, item groups, mapgen, or Mod dependencies require the relevant ID,
loader, or focused tests as well. An object type with incomplete Schema coverage is not
valid merely because an editor reports no error.

### Editing principles

- Format only files needed by the PR and inspect every extra formatter change.
- Use neighbouring first-party definitions for field order and actual usage, while treating
  the loader as authoritative for required fields and defaults.
- `//` comments and project extensions are not standard JSON; avoid tools that delete them.
- Run the owner generator instead of editing a generated inventory by hand.
- Record formatter and loading checks, the Mod set, and every skipped check in the PR.

See the [JSON overview](../json/overview.md) and
[inheritance and copy-from](../json/inheritance-copy-from.md).
