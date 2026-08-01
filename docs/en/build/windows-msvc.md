---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: build-windows-msvc
title: 'Legacy migration draft: windows msvc'
language: en
status: draft
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
last_human_reviewer: Pending human review
source_paths:
- doc/c++/COMPILING-CMAKE-VCPKG.md
- CMakeLists.txt
- CMakePresets.json
- build-scripts/x64-windows-static.cmake
- .github/workflows/msvc-full-features.yml
- doc/c++/COMPILING-VS-VCPKG.md
- build-scripts/windows-tiles-sounds-x64-msvc.cmake
source_symbols: []
source_queries: []
source_fingerprint: 67ae130a01e46324ef41c87a392ce88719218f4d66dd72ea896d4a6cd8d82c98
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8d4a95ffb429c23a4f9c779018a9fcb0fb06b22acd77ae340be3a626e61724e9
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- legacy.doc-c-compiling-cmake-vcpkg
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina, Maleclypse, dumb-kevin; accepted inventory identities only.
  Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: build
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/build/windows-msvc/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/build/windows-msvc/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/build/windows-msvc/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/build/windows-msvc/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/c++/COMPILING-CMAKE-VCPKG.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c++/COMPILING-CMAKE-VCPKG.md
- path: CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/CMakeLists.txt
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/CMakePresets.json
- path: build-scripts/x64-windows-static.cmake
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/build-scripts/x64-windows-static.cmake
- path: .github/workflows/msvc-full-features.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/.github/workflows/msvc-full-features.yml
- path: doc/c++/COMPILING-VS-VCPKG.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c++/COMPILING-VS-VCPKG.md
- path: build-scripts/windows-tiles-sounds-x64-msvc.cmake
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/build-scripts/windows-tiles-sounds-x64-msvc.cmake
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28build-windows-msvc%29%3A+&body=Document+ID%3A+build-windows-msvc%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: windows msvc

This is the migration draft page for `build-windows-msvc`. It records **2** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `legacy.doc-c-compiling-cmake-vcpkg, build-windows-msvc`
- Target: `build/windows-msvc.md`
- Replacement: build-windows-msvc
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| legacy.doc-c-compiling-cmake-vcpkg | doc/c++/COMPILING-CMAKE-VCPKG.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | build-windows-msvc |
| build-windows-msvc | doc/c++/COMPILING-VS-VCPKG.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## History and attribution

Accepted inventory contributors: thaelina, Maleclypse, dumb-kevin. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `67ae130a01e46324ef41c87a392ce88719218f4d66dd72ea896d4a6cd8d82c98`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/c++/COMPILING-CMAKE-VCPKG.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/COMPILING-CMAKE-VCPKG.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/COMPILING-CMAKE-VCPKG.md)
- [`doc/c++/COMPILING-VS-VCPKG.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/COMPILING-VS-VCPKG.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/COMPILING-VS-VCPKG.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
