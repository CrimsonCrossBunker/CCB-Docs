---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.ui
title: UI platform matrix
language: en
status: draft
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: Pending human review
source_paths:
- src/ui_manager.h
- src/input_context.cpp
- src/sdltiles.h
- android/app/src/main/java/com/crimsoncrossbunker/cataclysmcb/AndroidUiMode.java
- src/sdltiles.cpp
- data/lua/LUA_FIRST_PLATFORM.md
source_symbols:
- class ui_adaptor
- android_ui_mode::is_new_ui_build()
source_queries: []
source_fingerprint: 16b05f93caea07d5ea0b95749a05d660c6d361a1c1656bc25d3f12a3e471b999
authority: source-and-tests
verified_commit: 7d65b4eff3d92393e659699a312b694f0e72d2cb
verified_at: '2026-10-11'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 349a7f7b769231e70b9b2b7275982033c51fd515d3c2817558a56ceed1a2594f
prerequisites:
- cpp.ui
- cpp.input
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
- android-unit
- lua-contract
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: platforms-ui
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/987
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/ui/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/ui/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/ui/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/ui/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/7d65b4eff3d92393e659699a312b694f0e72d2cb
source_urls:
- path: src/ui_manager.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/src/ui_manager.h
- path: src/input_context.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/src/input_context.cpp
- path: src/sdltiles.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/src/sdltiles.h
- path: android/app/src/main/java/com/crimsoncrossbunker/cataclysmcb/AndroidUiMode.java
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/android/app/src/main/java/com/crimsoncrossbunker/cataclysmcb/AndroidUiMode.java
- path: src/sdltiles.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/src/sdltiles.cpp
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/data/lua/LUA_FIRST_PLATFORM.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.ui%29%3A+&body=Document+ID%3A+platforms.ui%0ALanguage%3A+en%0AVerified+commit%3A+7d65b4eff3d92393e659699a312b694f0e72d2cb%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# UI platform matrix

CCB's UI is one semantic action and view-model layer presented through several rendering and
input routes. Every UI change must name which routes were exercised.

## Routes

| Route | Build/runtime boundary | Evidence to collect |
| --- | --- | --- |
| Curses | terminal cells, terminal colors and keyboard | terminal type/size, locale, key path |
| SDL3 tiles | SDL3 renderer/GPU shader and recovery path | GPU/backend, artifact format, recovery |
| Native UI | `ui_adaptor`, `input_context`, curses-compatible windows | resize/redraw and input actions |
| Lua UI/ImGui | sole Lua Platform v1 and native ImGui integration | Platform v1 contract, actions, native fallback |
| Android | Java HUD/touch/text input plus SDL3 native runtime | device/API, UI mode, orientation, touch |

## Shared invariants

Semantic action IDs remain stable; cell and pixel coordinates are converted at explicit
boundaries; resize establishes layout before redraw; renderer recreation invalidates GPU
resources; translated text and font fallback cannot assume a fixed byte or glyph width; and a
new UI remains operable at narrow sizes.

## Validation matrix

At minimum exercise keyboard navigation, cancel/confirm, resize, narrow viewport, translation,
and the route directly changed. Renderer or coordinate changes cover SDL3 software, OpenGL,
and GPU routes plus Android where platform input differs. Record the SDK, renderer, integer
scale, and viewport; linked SDK identity does not prove device input or audible sound.
Lua UI work also validates the disabled/native fallback build.

## Accessibility and failure evidence

Preserve visible focus, understandable action names, non-color-only state, readable contrast,
and keyboard operation. Capture route, mode, resolution/scale, locale, input device, screenshot
or recording, and the first debug log around a stale frame, bad coordinate, or lost input.

## Generated and local data

Screenshots, recordings, renderer captures, and local UI profiles are evidence artifacts unless
the task explicitly adds a checked fixture. Never commit user keybindings or device-specific
layout state as project defaults without policy review.
