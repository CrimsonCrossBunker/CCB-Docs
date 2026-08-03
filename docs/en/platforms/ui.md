---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.ui
title: UI platform matrix
language: en
status: active
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
source_symbols:
- class ui_adaptor
- android_ui_mode::is_new_ui_build()
source_queries: []
source_fingerprint: 4f2ee856289cb1352882870efe2efd69335a90b9e51750df07c43205fa0b2c12
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8e5535d38d8ae267597a3fd6a545d71f480bcb4a173599d1ee3e5f4aee0c0ace
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/ui/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/ui/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/ui/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/ui/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: src/ui_manager.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/ui_manager.h
- path: src/input_context.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/input_context.cpp
- path: src/sdltiles.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/sdltiles.h
- path: android/app/src/main/java/com/crimsoncrossbunker/cataclysmcb/AndroidUiMode.java
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/android/app/src/main/java/com/crimsoncrossbunker/cataclysmcb/AndroidUiMode.java
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.ui%29%3A+&body=Document+ID%3A+platforms.ui%0ALanguage%3A+en%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
---

# UI platform matrix

CCB's UI is one semantic action and view-model layer presented through several rendering and
input routes. Every UI change must name which routes were exercised.

## Routes

| Route | Build/runtime boundary | Evidence to collect |
| --- | --- | --- |
| Curses | terminal cells, terminal colors and keyboard | terminal type/size, locale, key path |
| SDL2 tiles | fallback desktop renderer and SDL2 input/audio | OS, renderer, scale, font, device |
| SDL3 tiles | SDL3 renderer/GPU shader and recovery path | GPU/backend, artifact format, recovery |
| Native UI | `ui_adaptor`, `input_context`, curses-compatible windows | resize/redraw and input actions |
| Lua UI/ImGui | capability-gated Lua pages and native ImGui integration | manifest, API v5, native fallback |
| Android | Java HUD/touch/text input plus SDL3 native runtime | device/API, UI mode, orientation, touch |

## Shared invariants

Semantic action IDs remain stable; cell and pixel coordinates are converted at explicit
boundaries; resize establishes layout before redraw; renderer recreation invalidates GPU
resources; translated text and font fallback cannot assume a fixed byte or glyph width; and a
new UI remains operable at narrow sizes.

## Validation matrix

At minimum exercise keyboard navigation, cancel/confirm, resize, narrow viewport, translation,
and the route directly changed. Renderer or coordinate changes need SDL2/SDL3 and Android where
those branches differ. Lua UI work also validates the disabled/native fallback build.

## Accessibility and failure evidence

Preserve visible focus, understandable action names, non-color-only state, readable contrast,
and keyboard operation. Capture route, mode, resolution/scale, locale, input device, screenshot
or recording, and the first debug log around a stale frame, bad coordinate, or lost input.

## Generated and local data

Screenshots, recordings, renderer captures, and local UI profiles are evidence artifacts unless
the task explicitly adds a checked fixture. Never commit user keybindings or device-specific
layout state as project defaults without policy review.
