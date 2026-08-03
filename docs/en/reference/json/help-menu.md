---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.help-menu
title: 'Legacy migration draft: help menu'
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
- doc/JSON/HELP_MENU.md
- src/help.cpp
- src/help.h
- data/core/help.json
source_symbols:
- help::load
- help::load_object
source_queries: []
source_fingerprint: f183f3f25cca04b29131aec235909008cdcd84abbf61c36866f607c9fb1595c4
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8c2d790827fc56b5aa13090c5e7fc03bad2937e0680f7170a2f641a345d8ad0a
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/help-menu/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/help-menu/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/help-menu/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/help-menu/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/HELP_MENU.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/HELP_MENU.md
- path: src/help.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/help.cpp
- path: src/help.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/help.h
- path: data/core/help.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/core/help.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.help-menu%29%3A+&body=Document+ID%3A+json.help-menu%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: help menu

This is the migration draft page for `json.help-menu`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.help-menu`
- Target: `reference/json/help-menu.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/help-menu/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.help-menu | doc/JSON/HELP_MENU.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Help-menu JSON

A `"type": "help"` object defines a scrollable help topic. Core topics live in
`data/core/help.json`, while mods may supply their own. `help::load` delegates to
`help::load_object`, which groups topics by source and appends each source in load order.

Each object must provide an integer `order`, a translatable `name`, and a `messages` array of
translatable strings. The order only has to be unique within one source, so separate mods may each
start at zero. The current loader rejects duplicate orders. Core help must be placed in the core JSON
directory rather than presented as an ordinary mod source.

Messages may use color tags and `<press_ACTION_ID>` keybinding tags. `<DRAW_NOTE_COLORS>` and
`<HELP_DRAW_DIRECTIONS>` are special placeholders handled in `help.cpp`. Take action IDs from the
current input registrations instead of guessing from old screenshots or upstream prose. For a new
topic, check translation extraction, narrow-terminal wrapping, tiled and terminal presentation,
topic order, and JSON loading.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `f183f3f25cca04b29131aec235909008cdcd84abbf61c36866f607c9fb1595c4`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/HELP_MENU.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/HELP_MENU.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/HELP_MENU.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
