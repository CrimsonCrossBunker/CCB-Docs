---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.sdl3-render-sync
title: 'Draft: SDL3 rendering synchronization'
language: en
status: draft
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- mod-author
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: Pending human review
source_paths:
- src/cata_tiles.cpp
- src/cata_shader.cpp
- src/pixel_minimap.cpp
- src/sdl_font.cpp
- src/sdltiles.cpp
- src/level_cache.h
- src/smooth_lighting.cpp
- data/shaders/lit_sample.glsl
source_symbols: []
source_queries: []
source_fingerprint: 4de63a674cc4587ddef63bf9fcf379e1d65b46d42b793a428eaddfad1410890a
authority: api-contract
verified_commit: 7c964d3c9047216fffbefc602218da86c2781049
verified_at: '2026-10-14'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 19f4ab0c610d25f7944c6ffd8b630695478361e2c082212b00a96d16f471f002
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- lua-contract
api_version: '1'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/sdl3-render-sync/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/sdl3-render-sync/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/sdl3-render-sync/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/sdl3-render-sync/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/7c964d3c9047216fffbefc602218da86c2781049
source_urls:
- path: src/cata_tiles.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7c964d3c9047216fffbefc602218da86c2781049/src/cata_tiles.cpp
- path: src/cata_shader.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7c964d3c9047216fffbefc602218da86c2781049/src/cata_shader.cpp
- path: src/pixel_minimap.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7c964d3c9047216fffbefc602218da86c2781049/src/pixel_minimap.cpp
- path: src/sdl_font.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7c964d3c9047216fffbefc602218da86c2781049/src/sdl_font.cpp
- path: src/sdltiles.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7c964d3c9047216fffbefc602218da86c2781049/src/sdltiles.cpp
- path: src/level_cache.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7c964d3c9047216fffbefc602218da86c2781049/src/level_cache.h
- path: src/smooth_lighting.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7c964d3c9047216fffbefc602218da86c2781049/src/smooth_lighting.cpp
- path: data/shaders/lit_sample.glsl
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7c964d3c9047216fffbefc602218da86c2781049/data/shaders/lit_sample.glsl
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.sdl3-render-sync%29%3A+&body=Document+ID%3A+cpp.sdl3-render-sync%0ALanguage%3A+en%0AVerified+commit%3A+7c964d3c9047216fffbefc602218da86c2781049%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Draft: SDL3 rendering synchronization

This page describes an unmerged rendering branch depending on CCB #987's SDL3 backend. Original authors and upstream #88716, #88880, #88720, #88318, #88754, #88873 and #88888 are retained.

## Preserved CCB behavior

Simulation remains the map-memory writer; rendering reads it without reinstating per-frame memory sweeps. RenderPrep retains sparse row caches, layer sidecars and one combined dynamic refresh. Atlas reload checks include Lua sprite generations. Android input wakeups and fit-to-screen boundaries remain.

The minimap batches changed chunk pixels and critter beacons while keeping CCB chunk and composed-texture caches. Text uses shared glyph pages, shelf allocation and quad batches, with software bitmap fallback. Tint and smooth lighting use SDL3 shaders while preserving recovery and present-repair boundaries.

Painted or diagonal vehicle sprites currently retain classic geometry to preserve CCB paint. This is a compatibility limitation, not complete new-lighting coverage of every sprite.

## Acceptance limits

The owning generator compiled 10 SPIR-V shaders. Syntax checks passed 39 affected source/test translation units. Avatar and level_cache layouts changed, so linking new files against old engine objects cannot establish matching-build acceptance.

Combined compilation and software rendering regression are in progress. DXIL, MSL, actual GPUs, mobile devices and benchmark scenarios remain unverified. No frame-rate improvement is promised here.

Responsible human: LYHGLYTX.
