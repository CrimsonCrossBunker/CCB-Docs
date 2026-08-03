---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: build-windows-msys2
title: 'Legacy migration draft: windows msys2'
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
- doc/c++/COMPILING-MSYS.md
- Makefile
- CMakeLists.txt
- .github/workflows/sdl3-matrix.yml
source_symbols: []
source_queries: []
source_fingerprint: 68938c89fa239fbdf111e4c0ab4f278004c226cce9d43e49a1c04248aef44a23
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: e4a7f9d492c61c5fd0975a335d43e05a1f714989c09214d184c0ce574f471f38
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/build/windows-msys2/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/build/windows-msys2/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/build/windows-msys2/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/build/windows-msys2/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/c++/COMPILING-MSYS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/c++/COMPILING-MSYS.md
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/Makefile
- path: CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/CMakeLists.txt
- path: .github/workflows/sdl3-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/.github/workflows/sdl3-matrix.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28build-windows-msys2%29%3A+&body=Document+ID%3A+build-windows-msys2%0ALanguage%3A+en%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: windows msys2

This is the migration draft page for `build-windows-msys2`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `build-windows-msys2`
- Target: `build/windows-msys2.md`
- Replacement: build-windows-msys2
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| build-windows-msys2 | doc/c++/COMPILING-MSYS.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current MSYS2 route

The legacy guide still points at a CleverRaven clone, old Windows releases, and a frozen
pacman package line. CCB contributors work from a CCB fork and treat current MSYS2,
Make/CMake configuration, and Windows CI as authoritative.

### Select a shell and toolchain

On a modern Windows installation, use the 64-bit MinGW or UCRT shell matching the installed
package prefix. Do not mix the plain MSYS shell, MINGW64, and UCRT64 toolchains. Fully update
MSYS2 first, then install dependencies based on the current Makefile/CMake configuration,
the first missing-header error, and CI. Do not preserve version numbers copied from this page.

### CMake preset

The pinned source provides:

```sh
cmake --list-presets
cmake --preset windows-x64
cmake --build --preset windows-x64
```

Use `windows-tiles-sounds-x64` for the Tiles and sound combination. These presets use
Ninja Multi-Config and write to `out/build/<preset>/`; current preset data defines the
configuration and install paths.

### Make entry point

The Makefile still supports `MSYS2=1` and `DYNAMIC_LINKING=1`, with dependencies selected
by Tiles, sound, localization, SDL2/SDL3, and other switches. Do not reuse the old guide's
large command that disables lint and tests as the default validation. Build the target,
then select formatting, JSON, or focused tests from `ai/test-matrix.yml`.

### Runtime and review evidence

- Run the artifact from the same MSYS2 environment and confirm that runtime DLLs resolve.
- Record shell type, compiler, CMake or Make, package prefix, and the complete command.
- Windows CI is merge evidence; Linux or WSL does not replace a native Windows result.
- Release and packaging workflows create distributable artifacts. A local developer build
  is not an official package.

MSYS2 package names and tool versions change, so this page intentionally does not freeze a
complete installation command. Resolve differences through current CI and the official
MSYS2 package database.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`; the aggregate source fingerprint is `68938c89fa239fbdf111e4c0ab4f278004c226cce9d43e49a1c04248aef44a23`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/c++/COMPILING-MSYS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/c%2B%2B/COMPILING-MSYS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/c%2B%2B/COMPILING-MSYS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
