---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.matrix
title: Platform matrix
language: en
status: draft
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
- .github/workflows/release.yml
- .github/actions/setup-sdl3-stack-macos/action.yml
source_symbols: []
source_queries: []
source_fingerprint: 3af89901fb085d31b24e3b4ddf1bf2bbc90275acb78acafff4d1cce77922e6e2
authority: build-config
verified_commit: 7d65b4eff3d92393e659699a312b694f0e72d2cb
verified_at: '2026-10-11'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 479d980e5f008a8893ca4c1282505d3488c96fd9c25c4412bb29beb7bb85002f
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/987
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/matrix/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/matrix/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/matrix/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/matrix/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/7d65b4eff3d92393e659699a312b694f0e72d2cb
source_urls:
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/Makefile
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/CMakePresets.json
- path: android/app/build.gradle
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/android/app/build.gradle
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/.github/workflows/matrix.yml
- path: .github/workflows/msvc-full-features.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/.github/workflows/msvc-full-features.yml
- path: .github/workflows/sdl3-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/.github/workflows/sdl3-matrix.yml
- path: .github/workflows/release.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/.github/workflows/release.yml
- path: .github/actions/setup-sdl3-stack-macos/action.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/.github/actions/setup-sdl3-stack-macos/action.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.matrix%29%3A+&body=Document+ID%3A+platforms.matrix%0ALanguage%3A+en%0AVerified+commit%3A+7d65b4eff3d92393e659699a312b694f0e72d2cb%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Platform matrix

CCB supports several build environments, but support evidence is specific to a
toolchain and feature combination. A successful Linux build is not evidence for
Windows, MSVC, or Android.

| Platform | Maintained entry point | Important boundary | Minimum useful evidence |
| --- | --- | --- | --- |
| Linux | Make or `linux-x64` CMake preset | Graphical builds require SDL3 >= 3.4.0 | Configure/build plus focused tests |
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

Tiles, sound, localization, tests, Lua Platform v1, compiler, and build type are part of
the platform identity. All graphical lanes use SDL3; the standard Linux and macOS
matrix and MSVC workflow exercise this backend without an opt-in repository variable.
The Release matrix retains ten packages: Windows 2, Linux 3, macOS 2, and Android 3.
Manual matrix/MSVC runs with `package_artifacts=true` validate installable artifacts
without publishing a Release; `run_tests` separately controls broad native test execution.

## What this page does not claim

This page records supported entry points found in Make, CMake presets, Gradle,
and CI at the verified source commit. It does not claim that every matrix cell
was run during the documentation build. Release maintainers must confirm the
actual default-branch checks and artifacts for the release commit.

See [Building CCB](../build/overview.md) for commands and
[testing strategy](../validation/testing.md) for risk-based expansion.
