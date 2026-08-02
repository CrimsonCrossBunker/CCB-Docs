## Current CCB Mod model

A CCB Mod is a data package with `MOD_INFO`. The runtime first resolves available Mods,
dependencies, and conflicts, then loads JSON in the order stored by the world. Matching
`mod_interactions/` data is loaded only after ordinary data. JSON, EOC, and Lua may coexist,
but each remains governed by its loader, Schema, registrations, or Lua v5 contract.

### Minimal layout

```text
ccb_example/
├── modinfo.json
├── items.json
└── lua/
    └── manifest.json   # only when the Mod uses Lua
```

```jsonc
[
  {
    "type": "MOD_INFO",
    "id": "ccb_example",
    "name": "CCB Example",
    "authors": [ "Example author" ],
    "maintainers": [ "github-account" ],
    "description": "A small example Mod.",
    "category": "content",
    "dependencies": [ "dda" ]
  }
]
```

The `id` is a stable identity used by world Mod lists, dependencies, interaction directories,
and source tracking; changing it is not a display-text cleanup. Current `MOD_INFORMATION` also
reads `path`, `version`, `conflicts`, `core`, `obsolete`, `loading_images`, and
`disable_other_loading_screens`. Do not copy an old field table: check
`mod_manager::load_modfile` and a nearby first-party `modinfo.json`. A Mod cannot depend on
itself, and `#` is not a legal Mod ID character.

### Data, dependencies, and load order

Ordinary JSON is found recursively under the Mod path, `mod_interactions` is deferred, and
`lua/manifest.json` is not sent to the JSON object loader. `dependencies` names Mods that must
load first; `conflicts` prevents incompatible combinations. Dependencies establish availability
and order, but do not migrate referenced IDs or replace explicit compatibility content.

Split files by domain, not an assumed file load order. A forward reference is valid only where
the owning loader supports it. Published item, terrain, EOC, Lua service, and other IDs can enter
saves or other Mods; inspect obsoletion or migration support and old-world loading before removal
or renaming.

### Choose the expression layer

- Prefer JSON for static content, recipes, maps, and registered objects.
- Prefer EOC for conditions, effects, event chains, and dialogue flow.
- Use Lua for dynamic logic exposed by the public Lua v5 contract, with exact capabilities.
- Change C++ only when the public data contracts cannot express a capability the project will maintain.

### Minimal validation loop

1. Format changed JSON with the repository formatter and run `make -j2 json-check`.
2. With a built game, run `./cataclysm-tiles --check-mods ccb_example` (the binary name depends on the build).
3. Cover EOC true/false, talkers, context, and repetition; run Lua manifest, syntax, coverage, and example checks.
4. Create, save, and reload a world, then test the actual dependency and conflict combinations.
5. Record commands, platform, Mod set, failures, and skipped checks in the PR. Loading is not balance or save-compatibility proof.

Continue with [Mod compatibility](compatibility.md), [Mod localization](localization.md), and
the [in-repository Mod policy](../mods/in-repository-policy.md).
