---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: design-user-experience
title: 'Legacy migration draft: user experience'
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
- doc/design-balance-lore/design-user-experience.md
- doc/USER_INTERFACE_AND_ACCESSIBILITY.md
- src/options.cpp
source_symbols: []
source_queries: []
source_fingerprint: c48c4c006650195f1034263cc5e9b25a072b994966ca12dc6ab7f2777250c761
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: dd9ed99d0e45082a7c701ac2d242db90427adeac37dea2aa8869d230802dc9b8
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
risk_group: design
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/user-experience/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/design/user-experience/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/user-experience/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/design/user-experience/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/design-balance-lore/design-user-experience.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/design-user-experience.md
- path: doc/USER_INTERFACE_AND_ACCESSIBILITY.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/USER_INTERFACE_AND_ACCESSIBILITY.md
- path: src/options.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/options.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28design-user-experience%29%3A+&body=Document+ID%3A+design-user-experience%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: user experience

This is the migration draft page for `design-user-experience`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `design-user-experience`
- Target: `design/user-experience.md`
- Replacement: design-user-experience
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| design-user-experience | doc/design-balance-lore/design-user-experience.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## CCB user-experience goals

CCB is a top-down, grid-based, action-time-driven open-world survival game with character and tiles
rendering across desktop and Android targets. Its depth should come from interacting world systems
and multiple problem-solving approaches, not from fighting the interface. Games cited by the legacy
page and its “DDA” name are historical background; confirm current product identity, platforms, and
features in CCB README, build configuration, source, and tests.

### Depth must be understandable

- Before a decision consumes time or resources or exposes a character, show the relevant
  information where practical. Afterward, provide feedback that lets the player locate the cause.
- Automate repetition while preserving real choices about route, equipment, risk, priority, and
  retreat.
- Keep actions discoverable, cancellable, and focus-safe with keyboard, touch, narrow windows,
  scaling, and translated text.
- Color, ASCII glyphs, sound, or pointer position cannot be the only semantics. Supply text or
  structure for screen readers, high-contrast users, and play without audio.
- Let players learn complex systems progressively. Defaults show information needed for the current
  task and advanced detail may expand, but contracts should not be permanently hidden.

## Designing a flow

Write down the player goal, entry point, shortest successful path, cancel and failure paths, and save
boundary first. Inspect the input context, activity system, messages, help, options, and
`ui_adaptor` or ImGui lifecycle involved. Do not use a new global option to conceal an unclear
default flow; every option expands the testing and maintenance matrix.

Validate curses and tiles, keyboard and Android touch, resizing, narrow windows, long translations,
color themes, screen-reader mode, interruption and resumption, save/reload, and invalid input. A
pattern borrowed from another game is a candidate, not a substitute for current CCB usability and
accessibility evidence.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `c48c4c006650195f1034263cc5e9b25a072b994966ca12dc6ab7f2777250c761`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/design-balance-lore/design-user-experience.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/design-user-experience.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/design-user-experience.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
