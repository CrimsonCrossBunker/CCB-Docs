---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: build.overview
title: Building CCB
language: en
status: draft
doc_type: how-to
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
- android/gradlew
- android/build.gradle
- .github/workflows/matrix.yml
source_symbols: []
source_queries: []
source_fingerprint: d1a51672bd4739e5b0051c192091e672288cdc557e3919d08b04fb44b05c952f
authority: build-config
verified_commit: 2c899a3db790e11a6ff44d91f319064b1ee65d2a
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 2a5adc64a79b2cb017b29f11abb46a6685a76fc1949b56ccc9616d1b25e9eda8
prerequisites:
- architecture.project-map
depends_on:
- platforms.matrix
- validation.quickstart
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cmake-configure
- cpp-format
- cpp-tests
- json-load
- android-unit
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: build
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/560
stale_reason: null
search:
  exclude: true
---

# Building CCB

Current Makefile, CMake, Gradle, and CI definitions are authoritative for build
behaviour. This page explains entry points and choices. Recheck the owning file
before copying a command because dependencies and feature flags can evolve.

## Choose a build system

| Scenario | Preferred entry | Scope |
| --- | --- | --- |
| Fast Linux development | `make` | Shares entry points with formatting, JSON, and tests |
| Cross-platform, IDE, or clangd | CMake preset | Use `cmake --list-presets` to inspect current presets |
| Windows MSYS2 | Maintained Windows CMake preset or MSYS2 flow | Validate in that shell; Linux results do not prove Windows |
| MSVC | vcpkg/MSVC instructions and CI | Compiler, dependency, and warning differences require MSVC evidence |
| Android | `android/gradlew` | Requires SDK/NDK; signing and release credentials stay outside Git |

For this documentation review, the following command was actually run on Linux
at source commit `2c899a3db790e11a6ff44d91f319064b1ee65d2a`:

```sh
# validation: cmake-configure
cmake --list-presets
```

It listed `linux-x64`, Linux tiles/sounds variants, and Windows MSYS2 presets.
That verifies preset discovery only; it does not claim a completed compile.

## Common entry points

```sh
# validation: cpp-format
make astyle-check

# validation: cpp-tests
make -j2 tests
./tests/cata_test "<focused filter>"

# validation: json-load
make -j2 json-check

# validation: cmake-configure
cmake --preset linux-x64
```

From `android/`:

```sh
# validation: android-unit
./gradlew test
./gradlew assembleDebug
```

These are authoritative entry-point examples, not results from this docs build.
Record the platform, dependency set, result, and every skipped check. This site
does not substitute for real Windows, MSVC, or Android validation.

## Configuration boundaries

- `CATA_ENABLE_LUA_UI` is enabled by default in CCB Make, CMake, and Android
  configuration.
- Android uses SDL3. Desktop generally uses SDL2; desktop SDL3 CI is gated by
  `CCB_DESKTOP_SDL3_ENABLED`. Do not infer one platform from another.
- Tiles, sound, localization, and Lua affect dependencies or artifacts. State
  the exact combination in the pull request.
- CMake builds must be out-of-tree. Large indexes, Doxygen HTML, ctags, and
  compilation databases are local or CI artifacts, not committed files.

## Diagnose a build failure

1. Preserve the complete command, first failed target, and compiler or Gradle
   version.
2. Classify the failure as configuration, dependency/download, compile, link,
   resource copy, or test.
3. Compare the same platform and feature combination with CI, not only the last
   error line.
4. Clean only an explicitly identified build directory; never delete a worktree
   or untracked user data.
5. Rerun the failed target, then validate the affected subsystem.

See the [platform matrix](../platforms/matrix.md) and
[validation quickstart](../validation/quickstart.md) for narrower routing.
