---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: testing-manual
title: 'Legacy migration draft: manual playtesting'
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
- doc/TESTING_YOUR_CHANGES.md
- tests/AGENTS.md
- Makefile
- CMakeLists.txt
- .github/workflows/matrix.yml
source_symbols: []
source_queries: []
source_fingerprint: 7badd83cf8a19d410f0d2183cacd6b564d381a8f96a17b6bc332b2cc5b003988
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 953d5a01bbdeed5ffe83fea0186dc1ca4d46b711b352f85d609081e11e13acde
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
risk_group: testing
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/testing/manual-playtesting/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/testing/manual-playtesting/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/testing/manual-playtesting/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/testing/manual-playtesting/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/TESTING_YOUR_CHANGES.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/TESTING_YOUR_CHANGES.md
- path: tests/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/AGENTS.md
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/Makefile
- path: CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/CMakeLists.txt
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/.github/workflows/matrix.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28testing-manual%29%3A+&body=Document+ID%3A+testing-manual%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: manual playtesting

This is the migration draft page for `testing-manual`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `testing-manual`
- Target: `testing/manual-playtesting.md`
- Replacement: testing-manual
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| testing-manual | doc/TESTING_YOUR_CHANGES.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | testing-manual |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Evidence-based manual playtesting

Automated checks prove formatting, loading, and encoded invariants. A non-trivial gameplay, UI, or
content change also needs manual validation in a CCB binary matching the source commit. State the
observable risks first and build the smallest scenarios; a few minutes of unguided play is not
evidence that a change was tested.

### Preparation and records

- Use a dedicated test world and character. Record commit, build flags, platform, mod set, seed,
  options, and save origin.
- Format and load JSON first. Compile the affected C++ target and run the focused test before play.
- Ensure binary and data come from the same commit. Restart or reload according to the actual loader
  lifecycle; returning to the main menu does not refresh every registry.
- Preserve reproduction steps, expected and actual results, logs, screenshots or short video, and
  cover normal, failure, and important boundary paths.

The debug menu can spawn items or monsters, edit map/overmap data, advance time, teleport, or call
subsystem entry points, but debug spawning can skip part of natural-generation context. Test a
monster-definition change on newly spawned instances. Growth, evolution, and offscreen processing
need unload/reload and time advancement. Test mapgen on fresh OMTs with direction, z-level, and region
coverage. EOC, Lua, save migration, and multiplayer need their real entry paths.

Remove debug-only state afterward and do not commit test saves, logs, or generated artifacts. A PR
must separate locally executed checks, CI coverage, and work not run. One successful manual run does
not replace a deterministic regression test; a bug fix still needs the narrowest automated case
that failed on the old implementation.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `7badd83cf8a19d410f0d2183cacd6b564d381a8f96a17b6bc332b2cc5b003988`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/TESTING_YOUR_CHANGES.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/TESTING_YOUR_CHANGES.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/TESTING_YOUR_CHANGES.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
