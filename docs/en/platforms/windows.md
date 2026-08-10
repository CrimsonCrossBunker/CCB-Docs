---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.windows
title: Windows development
language: en
status: stale
doc_type: explanation
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
- .github/workflows/msvc-full-features.yml
- doc/c++/COMPILING.md
- build-scripts/MSVC.cmake
source_symbols: []
source_queries:
- windows-x64
source_fingerprint: 2bfa57d79840fe27622bf1d9d9c2fe5a47388ec0797adbb80ddc9a9a070f1e74
authority: build-config
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 0d041a17d3cafee4a5a57d3aa8a5ac7894acc2dba06bcfc7ae00d6c8479fbaa3
prerequisites:
- platforms.matrix
- build.overview
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
stale_reason: 'Source paths changed after d32b9cc880a8: .github/workflows/msvc-full-features.yml'
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/windows/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/windows/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/windows/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/windows/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/CMakePresets.json
- path: .github/workflows/msvc-full-features.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/workflows/msvc-full-features.yml
- path: doc/c++/COMPILING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c++/COMPILING.md
- path: build-scripts/MSVC.cmake
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/build-scripts/MSVC.cmake
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.windows%29%3A+&body=Document+ID%3A+platforms.windows%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Windows development

Windows has two maintained compiler environments with different dependency, shell, path, and
artifact behavior: MSYS2/MinGW and native MSVC/vcpkg. Choose one before diagnosing a build.

## Route selection

| Route | Contract entry | Strength | Main boundary |
| --- | --- | --- | --- |
| MSYS2/MinGW | `windows-x64` or `windows-tiles-sounds-x64` preset | Unix-like shell and Ninja | MSYS2 package/runtime DLL set |
| MSVC/vcpkg | `windows-x64-msvc` or `windows-tiles-sounds-x64-msvc` preset | Matches the Windows CI compiler lane | Visual Studio, vcpkg triplet and configuration |
| ClangCL | `windows-tiles-sounds-x64-clang-cl` preset | Compiler diagnostics/time traces | Inherits the MSVC/vcpkg dependency model |

Use `CMakePresets.json`, `.github/workflows/msvc-full-features.yml`, and the applicable toolchain
files as authority. Legacy compilation prose is context, not proof that a package or command is
still supported.

## Shared checklist

1. Name the shell: PowerShell, cmd, MSYS2 MinGW64, or another environment.
2. Name architecture, compiler, generator, preset, configuration, SDL version, tiles/sound,
   localization, tests, and static/dynamic linking.
3. Keep source and build paths short enough for the selected tools and quote paths with spaces.
4. Run the preset's configure and build stages in the same environment.
5. Test the packaged directory, not only an executable beside development DLLs.

## Artifacts and diagnostics

Do not commit Visual Studio output, vcpkg installations, local CMake user presets, DLL staging,
PDBs, crash dumps, or credentials. PDBs, logs, package manifests, and dumps can be uploaded as
restricted CI/release artifacts when needed for diagnosis.

## Cross-platform boundary

Windows path encoding, console/SDL input, DLL discovery, and renderer recovery differ from
Linux. A WSL build is a Linux binary and does not validate native Windows packaging.
