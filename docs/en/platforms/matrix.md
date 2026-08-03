---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.matrix
title: Platform matrix
language: en
status: active
doc_type: reference
audiences:
- new-contributor
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- Makefile
- CMakePresets.json
- android/app/build.gradle
- .github/workflows/matrix.yml
- .github/workflows/msvc-full-features.yml
- .github/workflows/sdl3-matrix.yml
source_symbols: []
source_queries: []
source_fingerprint: 2a6efabfbc826b7cca9419407c9012f679512feeab0cdd4e9d56a99edde67dd4
authority: build-config
verified_commit: 2c899a3db790e11a6ff44d91f319064b1ee65d2a
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8ae2dc2c8738c0cbf41d337f70d7c7796755182f4eea9bf39c0d40447c4a623f
prerequisites:
- build.overview
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cmake-configure
- android-unit
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: platforms
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/560
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/matrix/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/matrix/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/matrix/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/matrix/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/2c899a3db790e11a6ff44d91f319064b1ee65d2a
source_urls:
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/Makefile
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/CMakePresets.json
- path: android/app/build.gradle
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/android/app/build.gradle
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/.github/workflows/matrix.yml
- path: .github/workflows/msvc-full-features.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/.github/workflows/msvc-full-features.yml
- path: .github/workflows/sdl3-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/.github/workflows/sdl3-matrix.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.matrix%29%3A+&body=Document+ID%3A+platforms.matrix%0ALanguage%3A+en%0AVerified+commit%3A+2c899a3db790e11a6ff44d91f319064b1ee65d2a%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Platform matrix

CCB supports several build environments, but support evidence is specific to a
toolchain and feature combination. A successful Linux build is not evidence for
Windows, MSVC, or Android.

| Platform | Maintained entry point | Important boundary | Minimum useful evidence |
| --- | --- | --- | --- |
| Linux | Make or `linux-x64` CMake preset | Desktop uses SDL2 by default | Configure/build plus focused tests |
| WSL | Linux toolchain inside WSL | Filesystem and graphics integration differ from native Linux | Name WSL version and filesystem location |
| Windows MSYS2 | Windows MSYS2 CMake presets | Package names, shell quoting, and DLL packaging | Preset configure/build on MSYS2 |
| Windows MSVC | vcpkg/MSVC flow and MSVC CI | Compiler diagnostics and dependency model differ | MSVC workflow or equivalent local build |
| Android | Gradle wrapper and native CMake build | Android uses SDL3 and ABI-specific artifacts | Gradle tests; name variant and ABI for APK/AAB |

Inspect available presets rather than copying an old preset name:

```sh
# validation: cmake-configure
cmake --list-presets
```

## Feature combinations

Tiles, sound, localization, tests, Lua UI, compiler, and build type are part of
the platform identity. Report them in a pull request. CCB's desktop SDL3 jobs
are experimental and gated by `CCB_DESKTOP_SDL3_ENABLED`; Android's use of SDL3
does not change the desktop default.

## What this page does not claim

This page records supported entry points found in Make, CMake presets, Gradle,
and CI at the verified source commit. It does not claim that every matrix cell
was run during the documentation build. Release maintainers must confirm the
actual default-branch checks and artifacts for the release commit.

See [Building CCB](../build/overview.md) for commands and
[testing strategy](../validation/testing.md) for risk-based expansion.
