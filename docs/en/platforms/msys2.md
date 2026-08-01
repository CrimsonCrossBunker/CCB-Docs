---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.msys2
title: MSYS2 and MinGW
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
last_human_reviewer: Pending human review
source_paths:
- CMakePresets.json
- doc/c++/COMPILING-MSYS.md
- .github/workflows/msvc-full-features.yml
source_symbols: []
source_queries:
- windows-x64
source_fingerprint: 8cd18fa5d699734e435a4a5e4adc4c4e5d73f59fd585323ec6ce56b474c752e9
authority: build-config
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: bc3e58ed87ce480f2925aecac89f9313b9869c581272cfae45131748b7f4ae03
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
search:
  exclude: true
---

# MSYS2 and MinGW

MSYS2 provides the MinGW Windows lane behind the `windows-x64` presets. The selected MSYS2
subsystem, compiler architecture, package set, and shell must agree; mixing MSYS and MinGW
libraries produces misleading configure or runtime failures.

## Contract route

Open a matching MinGW64 environment and inspect the repository presets:

```sh
cmake --list-presets
cmake --preset windows-x64
cmake --build --preset windows-x64
```

Use `windows-tiles-sounds-x64` for the tiles+sound surface. Both are multi-configuration Ninja
presets with `RelWithDebInfo` build presets; do not invent a build directory or configuration
that silently differs from the preset.

## Dependencies and shell boundary

`doc/c++/COMPILING-MSYS.md` describes the ecosystem, while `CMakePresets.json`, CMake configure
errors, and current CI decide the actual contract. Install dependencies for the selected MinGW
architecture. Run MinGW executables from the matching shell and inspect the packaged DLL set
outside the development PATH.

## Validation

- Configure and build the exact preset.
- Run the produced tests for the same configuration.
- For tiles/sound, start from a clean shell and verify renderer, fonts, sound, translations, and
  shader artifacts where SDL3 is enabled.
- Record shell (`MINGW64`), compiler/version, preset, and configuration in the PR.

## Common failures

Wrong-architecture packages, an MSYS compiler before MinGW on `PATH`, stale CMake cache,
missing runtime DLLs, and mixed slash/drive paths are distinct failures. Preserve the first
configure/link error and avoid “fixing” it by copying arbitrary DLLs into the source tree.
