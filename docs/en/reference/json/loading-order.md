---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.loading-order
title: 'Legacy migration draft: loading order'
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
- data/json/LOADING_ORDER.md
- doc/JSON/JSON_LOADING_ORDER.md
- src/filesystem.cpp
- src/init.cpp
- src/game_io.cpp
source_symbols:
- DynamicDataLoader::load_data_from_path
- DynamicDataLoader::load_all_from_json
- DynamicDataLoader::finalize_loaded_data
source_queries: []
source_fingerprint: 76dd27431585e4cc4b2992f167b23a7fdc7391e59fa2114a464a1b454b659976
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 061ca2c81f1ae161fc0c185b26b05d5f97afed8f6cf97f5855710ad1e9d16b9d
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- legacy.data-json-loading-order
- legacy.doc-json-json-loading-order
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/loading-order/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/loading-order/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/loading-order/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/loading-order/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: data/json/LOADING_ORDER.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/LOADING_ORDER.md
- path: doc/JSON/JSON_LOADING_ORDER.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_LOADING_ORDER.md
- path: src/filesystem.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/filesystem.cpp
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/init.cpp
- path: src/game_io.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/game_io.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.loading-order%29%3A+&body=Document+ID%3A+json.loading-order%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: loading order

This is the migration draft page for `json.loading-order`. It records **2** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `legacy.data-json-loading-order, legacy.doc-json-json-loading-order`
- Target: `reference/json/loading-order.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/loading-order/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| legacy.data-json-loading-order | data/json/LOADING_ORDER.md | merge_into | stubbed | 5f23722ff28c5cc552baa0422b32b1f10fd890fa | json.loading-order |
| legacy.doc-json-json-loading-order | doc/JSON/JSON_LOADING_ORDER.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | json.loading-order |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## JSON loading phases and order

CCB calls loaders for active Mods in dependency order already resolved for the world. Within one
path, `get_files_from_path(..., recursive=true)` discovers JSON breadth-first and uses current
filesystem sorting within a directory. Ordinary Mod loading excludes `mod_interactions`; matching
interaction content is a later pass after all ordinary content.

### Safe dependencies

Rely on explicit Mod dependencies, documented generic-factory deferred loading, and finalization
owned by a loader. Do not treat file names or directory depth as a universal forward-reference API.
Some handlers require targets during parsing while others retain string IDs until consistency
checking. Inspect the specific handler.

Historical `data/json` layout used depth for relationships such as skills, professions, and
scenarios. New code should prefer explicit factory or loader handling. Moving a file into a
subdirectory can change parse order and break content relying on accidental ordering; treat it as a
high-risk JSON change.

### Mods and interactions

`dependencies` determines active-Mod order. Ordinary content must parse after declared dependencies.
`mod_interactions/<target-id>/` loads in the later pass with source `base#target`. It cannot repair
an earlier ordinary-file exception and does not support nested multi-target directories.

### Validation

Run formatting, `make -j2 json-check`, and `--check-mods` for the complete dependency combination.
For order-sensitive changes, add a minimal fixture covering parent and child order, missing
dependencies, two-Mod overrides, interactions, and finalization. Also exercise packaged path and
case behavior through target-platform CI rather than only a development checkout.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `76dd27431585e4cc4b2992f167b23a7fdc7391e59fa2114a464a1b454b659976`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`data/json/LOADING_ORDER.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/LOADING_ORDER.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/LOADING_ORDER.md)
- [`doc/JSON/JSON_LOADING_ORDER.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_LOADING_ORDER.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_LOADING_ORDER.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
