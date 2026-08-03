---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.msvc
title: MSVC and vcpkg
language: en
status: active
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
source_symbols: []
source_queries:
- windows-tiles-sounds-x64-msvc
source_fingerprint: d2dbe858dd29b80612d853044debd594adb8e0ffeaf9d473becbc5dd3d2b0d74
authority: build-config
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: de436d260762856faafc61fcc6f466c2b2e07c1d6c8db41648cec2681eda5411
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/msvc/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/msvc/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/msvc/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/msvc/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/CMakePresets.json
- path: build-scripts/MSVC.cmake
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/build-scripts/MSVC.cmake
- path: build-scripts/windows-tiles-sounds-x64-msvc.cmake
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/build-scripts/windows-tiles-sounds-x64-msvc.cmake
- path: .github/workflows/msvc-full-features.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/.github/workflows/msvc-full-features.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.msvc%29%3A+&body=Document+ID%3A+platforms.msvc%0ALanguage%3A+en%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
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

Keep `Release`, `Debug`, and `RelWithDebInfo` artifacts separate. State whether `UseSDL3` is
true or false; the same project can build distinct SDL2 and SDL3 release packages. PDBs must
match the exact binary and commit used for a crash.

## Validation and hygiene

Run configure, build, tests, and package smoke tests in the same architecture. Do not commit
vcpkg trees, generated solutions outside maintained project files, `.vs`, PDBs, local presets,
or signing material. Preserve the first compiler/linker error and the vcpkg logs.
