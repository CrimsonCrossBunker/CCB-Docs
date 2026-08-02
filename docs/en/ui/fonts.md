---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: ui-fonts
title: 'Legacy migration draft: fonts'
language: en
status: draft
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
last_human_reviewer: Pending human review
source_paths:
- doc/user-guides/FONT_OPTIONS.md
- data/fontdata.json
- src/font_loader.cpp
- src/sdl_font.cpp
source_symbols:
- font_loader::load
- font_loader::save
source_queries: []
source_fingerprint: 8efffabac0938483250479a7eeb7d30df373704e07ee9b82ec9bcfca51392efd
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: b8be2fb8a289d316c8b45eee51e67745791b4bef30d39ed88c796ac1ec4102f5
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/ui/fonts/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/ui/fonts/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/ui/fonts/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/ui/fonts/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/user-guides/FONT_OPTIONS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/user-guides/FONT_OPTIONS.md
- path: data/fontdata.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/fontdata.json
- path: src/font_loader.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/font_loader.cpp
- path: src/sdl_font.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/sdl_font.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28ui-fonts%29%3A+&body=Document+ID%3A+ui-fonts%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: fonts

This is the migration draft page for `ui-fonts`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `ui-fonts`
- Target: `ui/fonts.md`
- Replacement: ui-fonts
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| ui-fonts | doc/user-guides/FONT_OPTIONS.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Font configuration for the tiled build

The tiled build reads four fallback chains from the user's `fonts.json`: `typeface`,
`gui_typeface`, `map_typeface`, and `overmap_typeface`. Each value may be a path string, an object
with `path`, or an array of those entries. Array order is glyph fallback order. The loader ensures
that `data/font/unifont.ttf` is present as the final fallback.

An object may set `hinting` and `antialiasing`. Current accepted hinting strings are `Auto`,
`NoAuto`, `Default`, `Light`, `None`, and `Bitmap`. An unknown value reports a debug message and
falls back to default; do not copy inconsistent enum lists from old prose. Disabling antialiasing
sets monochrome and mono-hinting flags. Font paths resolve in the runtime environment, and a
distributed package must actually include the file under a compatible font license.

### Migration and validation

`font_loader::load` reads the current configuration. If it does not exist, the loader reads the
legacy/default path and `font_loader::save` writes the canonical object-array form. This write-back
may change representation while preserving selection semantics.

Validate with Latin, simplified and traditional Chinese, combining marks, wide characters, emoji
fallback, and missing glyphs. Cover all four screen roles, DPI/scaling combinations, Bitmap, Light,
and None modes, antialiasing on and off, and missing files. Also inspect ImGui atlas construction,
map-cell dimensions, terminal alignment, memory/startup cost, and license attribution. Successful
JSON parsing alone does not prove a usable font.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `8efffabac0938483250479a7eeb7d30df373704e07ee9b82ec9bcfca51392efd`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/user-guides/FONT_OPTIONS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/user-guides/FONT_OPTIONS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/user-guides/FONT_OPTIONS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
