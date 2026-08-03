---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json-widgets
title: 'Legacy migration draft: widgets'
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
- doc/WIDGETS.md
- src/widget.cpp
- src/widget.h
- tests/widget_test.cpp
- data/json/ui/layout.json
source_symbols:
- widget::load_widget
- widget::load
source_queries: []
source_fingerprint: e2ec68ecbb94f6857d18bcb011f940e6ac2b0525364fed1d5346b482f4836fb3
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 74e083259ed3dd408364a9cb0629e9325147a2fcb892cec032b4a271e0052a79
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/widgets/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/widgets/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/widgets/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/widgets/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/WIDGETS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/WIDGETS.md
- path: src/widget.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/widget.cpp
- path: src/widget.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/widget.h
- path: tests/widget_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/widget_test.cpp
- path: data/json/ui/layout.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/ui/layout.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json-widgets%29%3A+&body=Document+ID%3A+json-widgets%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: widgets

This is the migration draft page for `json-widgets`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json-widgets`
- Target: `json/widgets.md`
- Replacement: json-widgets
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json-widgets | doc/WIDGETS.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## JSON widgets and sidebar layouts

A `"type": "widget"` object enters `generic_factory<widget>` through `widget::load_widget`; its
fields are read by `widget::load`. A widget can display a number, graph, or text directly, or combine
other widgets as a `layout` or `sidebar`. Reusable definitions live under `data/json/ui/`, and a mod
can add or inherit widgets through the same factory.

### Core fields

Every object needs a unique `id`. `style` defaults to `number`; common values are `number`, `graph`,
`text`, `layout`, and `sidebar`. `label`, `description`, `width`, `height`, `text_align`,
`label_align`, `separator`, `padding`, and `flags` control presentation. A `sidebar` must explicitly
provide `separator` and `padding`. A layout references child IDs in `widgets` and arranges them as
`"columns"` or `"rows"`. Do not infer defaults solely from the historical prose: use
`widget::load` and `widget.h`.

A numeric or text widget binds a `widget_var` through `var`. Body-part variables additionally need
`bodypart` or `bodyparts`. `var: "custom"` requires `custom_var.value` and a two-to-four-element
`range`; its entries may be integers, variable objects, or math expressions. Graph `symbols`,
`fill`, color breaks, and clauses determine the output. Invalid enums, references, and ranges should
surface during load or consistency checks.

### Inheritance and validation

Widgets use the generic factory, so the project's normal `copy-from`, `extend`, and `delete`
semantics apply. Extending a shared `id` affects every layout that references it; inspect current UI
JSON before replacing a common component.

Run the JSON formatter and loader plus the widget cases in `tests/widget_test.cpp`. Cover numbers,
graph fills, colors and clauses, nested row/column layouts, narrow widths, body parts, custom ranges,
and mod extension. Recheck field lists, variable enums, and actual defaults against
`src/widget.cpp` and `src/widget.h`.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `e2ec68ecbb94f6857d18bcb011f940e6ac2b0525364fed1d5346b482f4836fb3`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/WIDGETS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/WIDGETS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/WIDGETS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
