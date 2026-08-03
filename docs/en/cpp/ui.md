---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.ui
title: Native UI subsystem
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
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/ui_manager.h
- src/ui_manager.cpp
- src/ui_helpers.cpp
- tests/ui_profile_test.cpp
source_symbols:
- class ui_adaptor
source_queries: []
source_fingerprint: 9bcfa9d914370ad89daf4deafe7ab4ea9b47210c646a04e8d33cc977ba378725
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: f0818aa16ebac2c72fc3ea7c0401e2e6f8a7b9c2564202a66165e2d9d9c6e4bb
prerequisites:
- architecture.overview
depends_on:
- cpp.input
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-ui
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/ui/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/ui/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/ui/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/ui/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: src/ui_manager.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/ui_manager.h
- path: src/ui_manager.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/ui_manager.cpp
- path: src/ui_helpers.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/ui_helpers.cpp
- path: tests/ui_profile_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/tests/ui_profile_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.ui%29%3A+&body=Document+ID%3A+cpp.ui%0ALanguage%3A+en%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Native UI

## Responsibility

The native UI layer coordinates a stack of screen regions, resize and redraw invalidation,
curses-compatible windows, SDL/tile rendering, lists, popups, and newer ImGui surfaces.
`ui_adaptor` is the central lifetime and redraw boundary.

## Entry points

Start with `src/ui_manager.h` / `.cpp`, then `ui_helpers`, `uilist`, and the focused screen.
Register `on_screen_resize` and `on_redraw`, set the adaptor's region, and drive it through an
`input_context`.

## Data ownership

A stack-local `ui_adaptor` owns callbacks and membership in the UI stack by RAII. The screen
function owns its windows and view model; render backends own textures/buffers; global `uistate`
stores only intentionally persistent presentation choices.

## Dependencies

UI depends on input contexts, translation, color/font and terminal metrics, render backends,
game view models, Android UI mode, and optional Lua UI/ImGui integration.

## Lifecycle

Constructing an adaptor pushes it, resize establishes geometry, redraw paints only that region,
input may trigger more resize/redraw events, and destruction pops it. Callbacks must not mutate
the adaptor stack during a redraw.

## Invariants

Declared geometry contains all drawing; callbacks obey manager reentrancy rules; the top UI
owns input focus; window sizes use cells unless an absolute pixel API is explicit; and resize
invalidates layout before drawing.

## Extension points

Use a local adaptor and input context for a native screen. Put reusable layout in helpers;
expose data to Lua only through the bounded public API, never by leaking a native UI pointer.

## Serialization

Adaptors, windows, callbacks, and renderer resources are ephemeral. Persist only explicit user
configuration or `uistate` fields, with defaults and tests; reconstruct layout after load.

## Tests

Use UI profile and screen-specific tests, plus resize, narrow-terminal, keyboard, tiles/curses,
Android touch, and Lua-disabled paths where applicable.

## Performance

Redraw runs frequently. Limit invalidated regions, avoid rebuilding expensive view models in
the paint callback, and prevent transparent ImGui layers from leaving stale SDL pixels.

## CCB divergence

CCB combines legacy native screens with project-specific Lua UI, ImGui, and Android HUD paths.
Upstream UI ports must preserve all enabled backend and input-mode boundaries.

## Technical debt

Cell, pixel, curses, SDL, ImGui, and Android abstractions coexist. New screens should keep
geometry explicit and avoid another global redraw or input shortcut.
