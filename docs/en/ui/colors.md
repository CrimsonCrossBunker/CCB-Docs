---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: ui-colors
title: 'Legacy migration draft: colors'
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
- doc/user-guides/COLOR.md
- data/raw/colors.json
- data/raw/color_templates/default.json
- src/color.cpp
- tests/light_color_test.cpp
source_symbols:
- color_manager::load_default
- color_manager::load_custom
source_queries: []
source_fingerprint: aa880955188cf714e451fa318120a59ccac3bb9258529fa8177324bbb4cc1331
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 34b29f4375ae98e77ef7292aff2bde131d64473fd902ee2d6e36745a3620fe28
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
risk_group: ui
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/ui/colors/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/ui/colors/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/ui/colors/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/ui/colors/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/user-guides/COLOR.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/user-guides/COLOR.md
- path: data/raw/colors.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/raw/colors.json
- path: data/raw/color_templates/default.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/raw/color_templates/default.json
- path: src/color.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/color.cpp
- path: tests/light_color_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/light_color_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28ui-colors%29%3A+&body=Document+ID%3A+ui-colors%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: colors

This is the migration draft page for `ui-colors`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `ui-colors`
- Target: `ui/colors.md`
- Replacement: ui-colors
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| ui-colors | doc/user-guides/COLOR.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## The CCB color system

`color_manager::load_default` establishes color names, pairs, and invert/highlight mappings, while
`data/raw/colors.json` supplies default base RGB values. Common names use `c_foreground`; `h_`
denotes highlighting and `i_` inversion. Some foreground/background combinations also have named
pairs. Query the current color manager for valid names rather than assuming any two names can be
concatenated.

Player-facing strings may use properly closed and nested `<color_name>…</color>` tags. Color must
not be the only semantic channel: disabled, dangerous, and selected states also need text, symbols,
or structure for screen readers and alternative themes. Support for `color` or `bgcolor` in map,
item, and other JSON objects is defined by each loader; it is not uniform across object types.

### User configuration and validation

Users can override base RGB values, and the color manager serializes named custom and inverted
mappings. ImGui styles are a separate configuration path with RGBA values rather than curses pairs.
A theme can replace highlight/invert rules, so code must not depend on the actual RGB of one default
theme.

For a color-contract change, run JSON loading, color consistency, and relevant UI/light tests. Check
default and custom themes, curses and tiles, ImGui, low contrast and color-vision differences,
nested tags, invalid-name fallback, and screen readers. RGB values documented at one source commit
are defaults, not a permanent visual ABI.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `aa880955188cf714e451fa318120a59ccac3bb9258529fa8177324bbb4cc1331`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/user-guides/COLOR.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/user-guides/COLOR.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/user-guides/COLOR.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
