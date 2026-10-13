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
- src/CMakeLists.txt
- tools/agent/test_shader_cmake_graph.py
source_symbols: []
source_queries: []
source_fingerprint: b6c9fb6600de97d5f52c1ceb26a11e7b1600e5bfb16dcc237b1591e91b8b71ed
authority: api-contract
verified_commit: eb8bfeabd8748176cc33aa2329b634d17bb61885
verified_at: '2026-10-14'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a376cdd4479fcfbe8bec83cde870e045bd0e0178d79ff408bc63b358b25d1e89
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/1000
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/sdl3-render-sync/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/sdl3-render-sync/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/sdl3-render-sync/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/sdl3-render-sync/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/eb8bfeabd8748176cc33aa2329b634d17bb61885
source_urls:
- path: src/cata_tiles.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/cata_tiles.cpp
- path: src/cata_shader.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/cata_shader.cpp
- path: src/pixel_minimap.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/pixel_minimap.cpp
- path: src/sdl_font.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/sdl_font.cpp
- path: src/sdltiles.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/sdltiles.cpp
- path: src/level_cache.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/level_cache.h
- path: src/smooth_lighting.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/smooth_lighting.cpp
- path: data/shaders/lit_sample.glsl
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/data/shaders/lit_sample.glsl
- path: src/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/CMakeLists.txt
- path: tools/agent/test_shader_cmake_graph.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/tools/agent/test_shader_cmake_graph.py
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.sdl3-render-sync%29%3A+&body=Document+ID%3A+cpp.sdl3-render-sync%0ALanguage%3A+en%0AVerified+commit%3A+eb8bfeabd8748176cc33aa2329b634d17bb61885%0A%0ADescribe+the+documentation+problem%3A%0A
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

Matching game and test binaries built successfully on combined branch #1000 with Clang 23, Release, C++17, SDL3, tiles, sound, zh_CN and the sole Lua Platform v1. The valid scope contains 992 cases: the broad run passed 991 and exposed a sight-cache setup assumption in one visible-NPC fixture. After correcting that fixture, 528 combined Lua and vision cases passed 86,021 assertions. Six integration regressions passed 2,567 assertions. These are results from bounded runs, not a claim that one process passed all 992 cases.

The new binary passed independent loading checks for core and all 18 affected non-obsolete Mods (19 identities total), including MoM dimension and Xedra data. Loading does not establish every new gameplay path, old-save compatibility, actual GPUs, all desktop platforms or Android device acceptance.

Software paths and simulated GPU recovery tests are part of the combined regression scope. DXIL, MSL, actual GPUs, mobile devices and benchmark scenarios remain unverified. No frame-rate improvement is promised here.

Windows vcpkg builds use packaged glslangValidator and shadercross tools. Shared GLSL changes trigger recompilation, requested spv/dxil/msl formats are honored, and fragment/vertex sources retain their stages. Four CMake command-graph tests passed, covering tool paths with spaces, SPIR-V prerequisites, format selection and non-vcpkg builds. This does not establish local Windows DXIL/MSL compilation.

Responsible human: LYHGLYTX.
