---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.options
title: 'Legacy migration draft: options'
language: en
status: stale
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
- doc/JSON/OPTIONS.md
- src/options.cpp
- src/options.h
- data/core/external_options.json
- tests/options_test.cpp
source_symbols:
- options_manager::add_external
- options_manager::load
- options_manager::migrateOptionName
source_queries: []
source_fingerprint: dc0f5c048fe806d59c97d86763e1aa730559bde0e6753b81e8cd3d955a99ad24
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8aea7c6b81af836fd95ec6e38a51b220fb4a12271f878ff20416020b53e907e9
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: 'Source paths changed after d32b9cc880a8: doc/JSON/OPTIONS.md, src/options.cpp'
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/options/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/options/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/options/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/options/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/OPTIONS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/OPTIONS.md
- path: src/options.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/options.cpp
- path: src/options.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/options.h
- path: data/core/external_options.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/core/external_options.json
- path: tests/options_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/options_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.options%29%3A+&body=Document+ID%3A+json.options%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: options

This is the migration draft page for `json.options`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.options`
- Target: `reference/json/options.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/options/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.options | doc/JSON/OPTIONS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

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

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `dc0f5c048fe806d59c97d86763e1aa730559bde0e6753b81e8cd3d955a99ad24`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/OPTIONS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/OPTIONS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/OPTIONS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
