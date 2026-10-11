---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.msvc
title: MSVC and vcpkg
language: en
status: draft
doc_type: how-to
audiences:
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: Pending human review
source_paths:
- CMakePresets.json
- build-scripts/MSVC.cmake
- build-scripts/windows-tiles-sounds-x64-msvc.cmake
- .github/workflows/msvc-full-features.yml
- msvc-full-features/Cataclysm.Cpp.props
- msvc-full-features/vcpkg.json
- build-scripts/windist.ps1
source_symbols: []
source_queries:
- windows-tiles-sounds-x64-msvc
source_fingerprint: b5bd59ffe6061a3c7818da7be3ad88b95755843829de165a1801b5a2650c5ad0
authority: build-config
verified_commit: 7d65b4eff3d92393e659699a312b694f0e72d2cb
verified_at: '2026-10-11'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: d759f841a8e8f174ae8a4820487c8073ccda3010120bb90a008ed86465bf2003
prerequisites:
- platforms.windows
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cmake-configure
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: platforms-windows
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/987
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/msvc/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/msvc/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/msvc/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/msvc/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/7d65b4eff3d92393e659699a312b694f0e72d2cb
source_urls:
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/CMakePresets.json
- path: build-scripts/MSVC.cmake
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/build-scripts/MSVC.cmake
- path: build-scripts/windows-tiles-sounds-x64-msvc.cmake
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/build-scripts/windows-tiles-sounds-x64-msvc.cmake
- path: .github/workflows/msvc-full-features.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/.github/workflows/msvc-full-features.yml
- path: msvc-full-features/Cataclysm.Cpp.props
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/msvc-full-features/Cataclysm.Cpp.props
- path: msvc-full-features/vcpkg.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/msvc-full-features/vcpkg.json
- path: build-scripts/windist.ps1
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/build-scripts/windist.ps1
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.msvc%29%3A+&body=Document+ID%3A+platforms.msvc%0ALanguage%3A+en%0AVerified+commit%3A+7d65b4eff3d92393e659699a312b694f0e72d2cb%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# MSVC and vcpkg

The MSVC lane uses Visual Studio 2022, static vcpkg dependencies, repository toolchain files,
and explicit multi-configuration CMake or the maintained `msvc-full-features` solution.

## CMake preset route

In a Visual Studio developer environment with `VCPKG_ROOT` pointing to a valid checkout:

```powershell
cmake --preset windows-tiles-sounds-x64-msvc
cmake --build --preset windows-tiles-sounds-x64-msvc
ctest --preset windows-tiles-sounds-x64-msvc
```

`build-scripts/MSVC.cmake`, `build-scripts/windows-tiles-sounds-x64-msvc.cmake`, the vcpkg
manifest/triplet, and `CMakePresets.json` jointly define this route. The simpler
`windows-x64-msvc` preset covers a curses/test configuration.

## CI parity

`.github/workflows/msvc-full-features.yml` is authoritative for the default Windows CI lane,
including Visual Studio version, vcpkg commit/triplet, localization artifact, ccache wrapper,
solution targets, and test invocation. Local success with different dependency revisions is
useful but is not CI parity.

## Feature and configuration boundaries

Keep `Release`, `Debug`, and `RelWithDebInfo` artifacts separate. Graphical projects
select the vcpkg SDL3 feature and `UseSDL3=true`; disabling this backend is rejected.
Curses projects remain available. Windows archives include the required mpg123 DLLs
and copyright alongside the binary. PDBs must match the exact binary and crash commit.

## Validation and hygiene

Run configure, build, tests, and package smoke tests in the same architecture. Do not commit
vcpkg trees, generated solutions outside maintained project files, `.vs`, PDBs, local presets,
or signing material. Preserve the first compiler/linker error and the vcpkg logs.
