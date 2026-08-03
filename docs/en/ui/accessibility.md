---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: ui-accessibility
title: 'Legacy migration draft: accessibility'
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
- doc/USER_INTERFACE_AND_ACCESSIBILITY.md
- src/options.cpp
- src/newcharacter.cpp
- src/player_difficulty.cpp
source_symbols:
- SCREEN_READER_MODE
source_queries: []
source_fingerprint: 512e14575d0545351f6fd8681a91825b993934d608585186f39da929e79d4405
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 3658d11bffce36601c4ebbafdc5e66515bfcb3048cac1ff6fd12b794a6c7780c
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/ui/accessibility/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/ui/accessibility/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/ui/accessibility/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/ui/accessibility/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/USER_INTERFACE_AND_ACCESSIBILITY.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/USER_INTERFACE_AND_ACCESSIBILITY.md
- path: src/options.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/options.cpp
- path: src/newcharacter.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/newcharacter.cpp
- path: src/player_difficulty.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/player_difficulty.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28ui-accessibility%29%3A+&body=Document+ID%3A+ui-accessibility%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: accessibility

This is the migration draft page for `ui-accessibility`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `ui-accessibility`
- Target: `ui/accessibility.md`
- Replacement: ui-accessibility
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| ui-accessibility | doc/USER_INTERFACE_AND_ACCESSIBILITY.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## UI and accessibility contracts

CCB contains curses/tiled windows, `ui_adaptor`, and ImGui UIs at the same time. Before changing a
screen, identify its redraw, resize, input, and focus paths instead of assuming every screen has
migrated to one framework. `ui_adaptor` manages redraw, resize, and final terminal cursor placement;
an ImGui-backed screen uses `cataimgui::window` to wrap the corresponding lifecycle.

### Screen-reader mode

`SCREEN_READER_MODE` is a current interface option and defaults to off. `src/newcharacter.cpp` and
`src/player_difficulty.cpp` show how supported screens switch layouts. It is not a global transform
that automatically makes every UI accessible; support is implemented and verified per screen.

A screen reader cannot reliably communicate information expressed only through color, so disabled,
dangerous, and changed states also need text or structure. Place the final terminal cursor at the
most important current content. Scrolling lists and changes above the cursor can steal the reading
position. In reader mode, a list-with-details screen should prefer the selected entry plus its detail
instead of a simultaneously scrolling full list. Visual columns, ASCII borders, and color must not
be the only semantics.

### Implementation and validation

Preserve cursor or focus after redraw and resize; use `ui_adaptor::set_cursor` or `disable_cursor`
where appropriate. Test normal and `SCREEN_READER_MODE`, curses and tiles, keyboard navigation,
narrow windows, dynamic content, long translated strings, and high-contrast themes. Record the
software, platform, and scenario for real screen-reader testing. Screenshots and automated contrast
checks do not replace spoken reading-order tests.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `512e14575d0545351f6fd8681a91825b993934d608585186f39da929e79d4405`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/USER_INTERFACE_AND_ACCESSIBILITY.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/USER_INTERFACE_AND_ACCESSIBILITY.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/USER_INTERFACE_AND_ACCESSIBILITY.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
