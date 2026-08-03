---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.input
title: Input subsystem
language: en
status: active
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
- src/input.h
- src/input.cpp
- src/input_context.h
- src/input_context.cpp
source_symbols:
- class input_manager
- class input_context
source_queries: []
source_fingerprint: 517e97772085ae0bdf4e750e8d5007318066d896a10d97db1bf19d1d0df6e8fb
authority: source-and-tests
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 3bdd53fc0ad79269644357795cb27552b94730daf07b899cc3ef4cb450d7dd94
prerequisites:
- architecture.overview
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-input
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/input/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/input/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/input/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/input/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: src/input.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/input.h
- path: src/input.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/input.cpp
- path: src/input_context.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/input_context.h
- path: src/input_context.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/input_context.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.input%29%3A+&body=Document+ID%3A+cpp.input%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Input

## Responsibility

`input_manager` loads and stores physical bindings and normalizes keyboard, mouse, gamepad,
touch/backend events. `input_context` registers semantic actions for one UI and resolves an
event into an action, including help, conflicts, timeout, directions, and text input.

## Entry points

Read `src/input.h`, `src/input.cpp`, `src/input_context.h`, and `src/input_context.cpp`. Initialize
the manager once, construct a named context, register every accepted action, then call
`handle_input` and branch on the returned action ID.

## Data ownership

The global manager owns loaded binding maps and backend key-name mappings. A local context owns
its registered action set and transient input mode; UI code owns the meaning and resulting
state transition.

## Dependencies

Input depends on platform event backends, keybinding JSON, translation of action names, UI
mode, options, SDL/curses codes, Android mode, and optional Lua UI routing.

## Lifecycle

Defaults and user overrides load at startup; a UI creates and configures a context; backend
events normalize and resolve; the context is destroyed; changed global mappings can be saved.

## Invariants

Action IDs are stable strings; every handled action is registered; context overrides fall back
according to manager policy; portable key names round trip; and timeout/edit modes reset when
their context exits.

## Extension points

Add a semantic action to the narrowest context and update default bindings/data. Platform
backends should emit normalized `input_event`s, not hard-code gameplay commands.

## Serialization

Bindings are user configuration written by `input_manager::save`, not world-save state. Local
contexts, queued events, timeouts, and focus are ephemeral.

## Tests

Exercise the affected UI plus binding load/save, conflict, fallback, portable-name, mouse/touch,
and backend mode behavior. Manual checks must name the platform and input device.

## Performance

Input handling is latency-sensitive. Avoid rescanning all actions per event, blocking work in a
redraw callback, and unnecessary polling outside the manager's timeout model.

## CCB divergence

CCB routes input across native, Lua UI, Android new UI, and legacy modes. An upstream binding or
context port must preserve action IDs and all enabled routing branches.

## Technical debt

Global mappings and multiple platform code systems make implicit assumptions easy. New code
should use portable names and semantic actions rather than raw key integers.
