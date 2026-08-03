---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platform-matrix
title: 'Legacy migration draft: compiler support'
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
- doc/c++/COMPILER_SUPPORT.md
- CMakeLists.txt
- .github/workflows/matrix.yml
- .github/workflows/msvc-full-features.yml
source_symbols: []
source_queries: []
source_fingerprint: a734b905bc9c70e7a29cf52f31cacb22a1c0eb476f68e854f490e750a0c99409
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: cb6a6d9019dc544108a69a9b3799a21436e9adfc787a8f85904e3cf3391944fd
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
risk_group: build
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/compiler-support/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/compiler-support/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/compiler-support/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/compiler-support/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/c++/COMPILER_SUPPORT.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/c++/COMPILER_SUPPORT.md
- path: CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/CMakeLists.txt
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/.github/workflows/matrix.yml
- path: .github/workflows/msvc-full-features.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/.github/workflows/msvc-full-features.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platform-matrix%29%3A+&body=Document+ID%3A+platform-matrix%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: compiler support

This is the migration draft page for `platform-matrix`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `platform-matrix`
- Target: `platforms/compiler-support.md`
- Replacement: platform-matrix
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| platform-matrix | doc/c++/COMPILER_SUPPORT.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Executable evidence defines support

Compiler support is not a permanent version table. At the pinned CCB commit, `CMakeLists.txt`
requires C++17. Actual support comes from default-branch CI, build scripts, and release toolchains
maintainers can reproduce. Distribution, Xcode market-share, and external links in the legacy page
age quickly and cannot override current workflows.

At the source commit verified by this page, the General build matrix covers:

- a basic clang 13 curses build and test on Ubuntu;
- clang 18 with tiles and ASan on Ubuntu;
- GCC 9 curses/LTO and tiles, sound, CMake, and UBSan combinations on Ubuntu;
- GCC 14 curses and Lua API on Ubuntu;
- macOS 15 and Apple Clang 17 with tiles, sound, and SDL2;
- an Android arm64 build-only job; and
- a separate Windows workflow on windows-2022 using MSVC, pinned CMake and vcpkg, and full tests.

These describe CI at that commit. They do not promise arbitrary older or newer toolchains, and a
build-only target has not thereby run tests.

## Change and validation

Choose the nearest platform CMake preset, Make or Gradle route, or MSVC entry point and record OS,
architecture, compiler, standard library, generator, SDL, tiles, sound, localization, Lua,
sanitizer, and build type. Linux success does not replace Windows, macOS, or Android evidence. A
cross-build does not prove launch, dependency packaging, or input on the target.

Before raising a minimum or using a new library feature, update the matrix so the oldest and newest
supported toolchains compile it, then update prose. Inspect release packaging, third-party
dependencies, and cache keys, and make a check required only after stable default-branch success.
External links help locate tools but are not support promises; repository jobs and configuration
are the evidence.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `a734b905bc9c70e7a29cf52f31cacb22a1c0eb476f68e854f490e750a0c99409`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/c++/COMPILER_SUPPORT.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/c%2B%2B/COMPILER_SUPPORT.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/c%2B%2B/COMPILER_SUPPORT.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
