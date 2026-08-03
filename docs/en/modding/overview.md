---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: modding-overview
title: 'Legacy migration draft: overview'
language: en
status: active
doc_type: explanation
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 365
last_human_reviewer: LYHGLYTX
source_paths:
- doc/MODDING.md
- src/mod_manager.cpp
- src/init.cpp
- src/game_io.cpp
- build-scripts/get_all_mods.py
source_symbols:
- DynamicDataLoader::load_mod_interaction_files_from_path
- game::load_mod_interaction_data_from_dir
source_queries: []
source_fingerprint: 78825cff7acafad971dcbdd1262f871807cb1fee06c58572e8139c94c760608c
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 7706ed082a805dbf55f0fc6885328f2703931da84af41cf5c114cb2d36053a6b
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: SpinosaurusBoat, thaelina; accepted inventory identities only. Source
  paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: mods
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/modding/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/modding/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/modding/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/modding/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/MODDING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/MODDING.md
- path: src/mod_manager.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/mod_manager.cpp
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/init.cpp
- path: src/game_io.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/game_io.cpp
- path: build-scripts/get_all_mods.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/build-scripts/get_all_mods.py
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28modding-overview%29%3A+&body=Document+ID%3A+modding-overview%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: overview

This is the migration draft page for `modding-overview`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `modding-overview`
- Target: `modding/overview.md`
- Replacement: modding-overview
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| modding-overview | doc/MODDING.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

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

## History and attribution

Accepted inventory contributors: SpinosaurusBoat, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `78825cff7acafad971dcbdd1262f871807cb1fee06c58572e8139c94c760608c`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/MODDING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/MODDING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/MODDING.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
