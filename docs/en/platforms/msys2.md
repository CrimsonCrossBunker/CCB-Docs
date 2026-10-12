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
- Makefile
- msvc-full-features/vcpkg.json
- tools/build_shaders.py
source_symbols: []
source_queries:
- windows-x64
source_fingerprint: e0d575911300ee3881e0b77aa62a39685e5cf7524a82f55ae2a5088bb4ea7cd9
authority: build-config
verified_commit: 75f90e0741588679986b2867923e8a500678cd86
verified_at: '2026-10-12'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 438403074a5c48398e9616f9de1eb24d61926e32f53d1b27425896490302d2dd
prerequisites:
- platforms.windows
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; MSYS notes adapted from CDDA PR 88588 (Matthew Richmond) and PR 88664 (mqrause).
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/msys2/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/msys2/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/msys2/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/msys2/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/75f90e0741588679986b2867923e8a500678cd86
source_urls:
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/75f90e0741588679986b2867923e8a500678cd86/CMakePresets.json
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/75f90e0741588679986b2867923e8a500678cd86/Makefile
- path: msvc-full-features/vcpkg.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/75f90e0741588679986b2867923e8a500678cd86/msvc-full-features/vcpkg.json
- path: tools/build_shaders.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/75f90e0741588679986b2867923e8a500678cd86/tools/build_shaders.py
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.msys2%29%3A+&body=Document+ID%3A+platforms.msys2%0ALanguage%3A+en%0AVerified+commit%3A+75f90e0741588679986b2867923e8a500678cd86%0A%0ADescribe+the+documentation+problem%3A%0A
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

SDL3 tiles builds also require `glslangValidator` to compile shader artifacts. Install
`mingw-w64-ucrt-x86_64-glslang` and check that the UCRT64 shell can find the tool.
Use UCRT64 packages for SDL3 image, font and sound dependencies as well; curses
builds do not need shader tools.

```sh
command -v gcc g++ glslangValidator
cmake --preset windows-tiles-sounds-x64 -DUSE_SDL3=ON
```

## Validation

- Configure and build the exact preset.
- Run the produced tests for the same configuration.
- For tiles/sound, start from a clean shell and verify renderer, fonts, sound, translations, and
  shader artifacts where SDL3 is enabled.
- Record shell (`UCRT64`), compiler/version, preset, and configuration in the PR.

## Common failures

Wrong-architecture packages, an MSYS compiler before MinGW on `PATH`, stale CMake cache,
missing runtime DLLs, and mixed slash/drive paths are distinct failures. Preserve the first
configure/link error and avoid “fixing” it by copying arbitrary DLLs into the source tree.
