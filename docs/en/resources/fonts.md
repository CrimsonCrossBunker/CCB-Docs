---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: resources.fonts
title: Fonts
language: en
status: draft
doc_type: reference
audiences:
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- doc/user-guides/FONT_OPTIONS.md
- src/font_loader.cpp
- src/sdl_font.h
source_symbols:
- class Font
source_queries:
- gui_typeface
source_fingerprint: 2a27e0ba73f9ebf7415861a346360263b5a232b4f25250cb0757261f496b779f
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8922eb552ca0384525d024eece39f14ecebad1dd58fdc11c423803d33708d1e1
prerequisites:
- platforms.ui
depends_on:
- resources.translation
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: resources-fonts
risk_level: normal
pending_source_pr: null
stale_reason: null
search:
  exclude: true
---

# Fonts

Fonts cover four distinct presentation roles—terminal/native typeface, ImGui GUI, map, and
overmap—with ordered fallback, glyph coverage, metrics, hinting, antialiasing, and GPU-resource
recovery.

## Authoritative paths

`doc/user-guides/FONT_OPTIONS.md` explains user configuration. `src/font_loader.cpp` defines the
accepted string/object/array forms, hinting values, migration, and mandatory Unifont fallback.
`src/sdl_font.*` owns runtime font instances and glyph/texture caches. Bundled files live under
`data/font/`.

## Configuration contract

`typeface`, `gui_typeface`, `map_typeface`, and `overmap_typeface` may be one path or an ordered
fallback list. Object entries can declare `path`, `hinting`, and `antialiasing`. Preserve the
fallback that supplies missing Unicode glyphs; a Latin-only visual check is insufficient.

## Contributor workflow

Confirm the font's redistribution and embedding license before adding a binary. Record source,
version, author/foundry, license, subset/transformation, and expected role. Do not replace a
font file under the same name without reviewing metrics, coverage, package size, and attribution.

## Validation

Test Latin, Simplified/Traditional Chinese, combining marks, wide characters, symbols, fallback,
line drawing, narrow UI, map/overmap alignment, DPI/scaling, hinting modes, and renderer reset.
Check both SDL2 and SDL3 where texture lifecycle differs.

## Performance and ownership

Font objects own cached glyph textures; renderer recovery releases/rebuilds or lazily repopulates
them. Unbounded glyph/color caches can consume GPU memory. Font paths and metadata persist in
user configuration; GPU resources never do.

## Generated data

Do not commit local font caches or atlases. A deliberately generated subset may be tracked only
with its reproducible generator, source license, Unicode coverage input, and validation.
