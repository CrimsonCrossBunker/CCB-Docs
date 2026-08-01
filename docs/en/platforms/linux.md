---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.linux
title: Linux development
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
- Makefile
- CMakePresets.json
- .github/workflows/matrix.yml
- doc/c++/COMPILING.md
source_symbols: []
source_queries:
- linux-x64
source_fingerprint: f9673e31237f2f19406a5b0c87562884840e5e7ef89ef570dd607aebc7926676
authority: build-config
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 4e369a0d5512e76ab86eb50a35d7ef9d9bf57a9c01e655bdaa4c683411f050da
prerequisites:
- platforms.matrix
- build.overview
depends_on:
- validation.testing
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
risk_group: platforms-linux
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/linux/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/linux/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/linux/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/linux/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/Makefile
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/CMakePresets.json
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/.github/workflows/matrix.yml
- path: doc/c++/COMPILING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/doc/c++/COMPILING.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.linux%29%3A+&body=Document+ID%3A+platforms.linux%0ALanguage%3A+en%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Linux development

Linux is the broadest local and CI development lane, but a build result is meaningful only
with its compiler, frontend, SDL version, localization, sound, tests, sanitizer, and build type.

## Authoritative entry points

- `Makefile` defines the native Make feature switches and validation targets.
- `CMakePresets.json` defines `linux-x64`, `linux-tiles-sounds-x64`, and the vcpkg variant.
- `.github/workflows/matrix.yml` records the combinations exercised by current CI.
- `doc/c++/COMPILING.md` is useful background; when it conflicts with the files above, the
  build files win.

## Supported routes

The smallest CMake route is the curses, localized, test-enabled `linux-x64` preset. The
`linux-tiles-sounds-x64` preset adds the graphics and audio dependency surface. Native Make
builds expose the same concerns through `TILES`, `SOUND`, `SDL3`, `LOCALIZE`, `TESTS`, compiler,
sanitizer, and release flags.

```sh
cmake --list-presets
cmake --preset linux-x64
cmake --build --preset linux-x64
```

For a focused native test route, follow the root AGENTS and test matrix rather than copying a
large release command:

```sh
make -j2 tests
./tests/cata_test "<focused filter>"
```

## Validation and artifacts

Report distribution, architecture, compiler/version, Make or CMake, preset/flags, curses or
tiles, SDL2/SDL3, sound, localization, sanitizer, and the exact test filter. Build directories,
`compile_commands.json`, profiler captures, and symbol databases are local or CI artifacts, not
source files to commit.

## Boundaries and caveats

Do not infer Windows or Android support from Linux. SDL3 requires compiled shader artifacts;
SDL2 is still a distinct fallback lane. Package-manager commands in legacy prose age quickly,
so diagnose against configure output and the verified build configuration.
