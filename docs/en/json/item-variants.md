---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json-item-variants
title: 'Legacy migration draft: item variants'
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
- doc/design-balance-lore/VARIANTS.md
- src/item_factory.cpp
- src/cata_variant.h
- tests/cata_variant_test.cpp
- data/json/artifact/artifact_item_types.json
source_symbols:
- cata_variant
source_queries: []
source_fingerprint: e6e11f897a5007543af3b70f38cedacdaf86f49f07ddb66b0692ee403e21915b
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: cb7c8dd702ae925ea80a72e4cbd48392f0ff1778ce0e7bb7a068085065d779b7
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
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/item-variants/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/item-variants/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/item-variants/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/item-variants/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/design-balance-lore/VARIANTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/design-balance-lore/VARIANTS.md
- path: src/item_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/item_factory.cpp
- path: src/cata_variant.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/cata_variant.h
- path: tests/cata_variant_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/cata_variant_test.cpp
- path: data/json/artifact/artifact_item_types.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/artifact/artifact_item_types.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json-item-variants%29%3A+&body=Document+ID%3A+json-item-variants%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: item variants

This is the migration draft page for `json-item-variants`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json-item-variants`
- Target: `json/item-variants.md`
- Replacement: json-item-variants
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json-item-variants | doc/design-balance-lore/VARIANTS.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

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

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `e6e11f897a5007543af3b70f38cedacdaf86f49f07ddb66b0692ee403e21915b`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/design-balance-lore/VARIANTS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/design-balance-lore/VARIANTS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/design-balance-lore/VARIANTS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
