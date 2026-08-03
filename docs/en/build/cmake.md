---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: build-cmake
title: 'Legacy migration draft: cmake'
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
- doc/c++/COMPILING-CMAKE.md
- CMakeLists.txt
- CMakePresets.json
- build-scripts/CMakeUserPresets.json.in
source_symbols: []
source_queries: []
source_fingerprint: 4d3be77600ca22667ed79ea09c70d03334c0813da303c207a403273d99d77733
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 4e33ea8120a73f3bb371aaebd3003cecdba0091dad79669a9480f7ccbb313bf1
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/build/cmake/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/build/cmake/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/build/cmake/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/build/cmake/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/c++/COMPILING-CMAKE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c++/COMPILING-CMAKE.md
- path: CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/CMakeLists.txt
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/CMakePresets.json
- path: build-scripts/CMakeUserPresets.json.in
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/build-scripts/CMakeUserPresets.json.in
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28build-cmake%29%3A+&body=Document+ID%3A+build-cmake%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: cmake

This is the migration draft page for `build-cmake`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `build-cmake`
- Target: `build/cmake.md`
- Replacement: build-cmake
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| build-cmake | doc/c++/COMPILING-CMAKE.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CMake route

The repository's `CMakePresets.json` is authoritative for preset names, generators,
output directories, and default feature combinations. The old statements that CMake is
unofficial, that SDL DLLs should be downloaded manually, and that an in-tree `build/`
directory is acceptable are obsolete. CCB CI uses CMake, while builds remain out of tree.

### Discover and configure

Start at the repository root:

```sh
cmake --list-presets
cmake --preset linux-x64
```

The pinned source defines `linux-x64`, `linux-tiles-sounds-x64`, and Windows MSYS2 and
MSVC presets. Output defaults to `out/build/<preset>/`. If the local list is empty or a
target preset is absent, inspect platform conditions, the generator, and the toolchain
instead of combining commands from the legacy guide.

### Build and override options

```sh
cmake --build --preset linux-x64
```

Use `-DNAME=VALUE` for a temporary override only after confirming that `CMakeLists.txt`
still defines the option. Tiles, sound, localization, Lua, SDL2/SDL3, and sanitizers alter
dependencies and artifacts, so record the preset and every override. Do not commit local
`CMakeUserPresets.json`, absolute paths, vcpkg roots, or generated build trees.

### Validate and diagnose

1. Preserve the first configure error, not only the final build failure.
2. Record CMake, compiler, Ninja or MSBuild, and dependency versions.
3. Remove only the explicit `out/build/<preset>/` directory when a clean configure is
   necessary; never clean the source tree or untracked user files.
4. Configure again and build the affected target. Run the focused test from the preset's
   output when tests are affected.

`cmake --list-presets` was actually checked on Linux for this documentation stack.
Windows preset availability and compilation are evidenced by the Windows CI jobs; a Linux
result does not replace them. See [building CCB](overview.md) and the
[platform matrix](../platforms/matrix.md).

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `4d3be77600ca22667ed79ea09c70d03334c0813da303c207a403273d99d77733`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/c++/COMPILING-CMAKE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/COMPILING-CMAKE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/COMPILING-CMAKE.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
