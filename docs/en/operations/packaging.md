---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: operations.packaging
title: Packaging
language: en
status: stale
doc_type: how-to
audiences:
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: Pending human review
source_paths:
- .github/workflows/release.yml
- .github/workflows/release-android-bundle.yaml
- build-scripts/windist.ps1
- Makefile
source_symbols: []
source_queries:
- Experimental Release
source_fingerprint: 9b918f82112a662be47c58bb3000b480f8061242242ffbe820c702729ba5f321
authority: build-config
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a517c91c633dea4acc9e1d492c333d8f5be8b148ab981b63ac2b46b1d72db68b
prerequisites:
- platforms.matrix
- validation.testing
depends_on:
- resources.translation
- resources.tiles
- resources.fonts
- resources.sound
- resources.shaders
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: release
risk_level: high
pending_source_pr: null
stale_reason: 'Source paths changed after d32b9cc880a8: .github/workflows/release-android-bundle.yaml,
  .github/workflows/release.yml, Makefile'
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/operations/packaging/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/operations/packaging/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/operations/packaging/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/operations/packaging/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: .github/workflows/release.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/workflows/release.yml
- path: .github/workflows/release-android-bundle.yaml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/workflows/release-android-bundle.yaml
- path: build-scripts/windist.ps1
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/build-scripts/windist.ps1
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/Makefile
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28operations.packaging%29%3A+&body=Document+ID%3A+operations.packaging%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Packaging

Packaging assembles a built executable with the exact data, graphics, translations, shaders,
libraries, licenses, launcher/support files, and platform metadata needed to run outside a
developer checkout. A successful compile is not a successful package.

## Authoritative entry points

Use the current release workflows, `Makefile` install/package targets, Gradle Android bundle
tasks, and platform helpers under `build-scripts/`. `build-scripts/windist.ps1` owns Windows
distribution staging; Android Gradle owns APK/AAB contents; release jobs own final artifact names
and uploads.

## Reproducible inputs

Record source commit/tag, toolchain and dependency revisions, feature flags (curses/tiles,
SDL2/SDL3, sound, localization, Lua), architecture/ABI, build type, translation artifact, shader
artifact, and asset source. Never package arbitrary files from an unclean development directory.

## Platform checks

- Linux: inspect dynamic dependencies or the intended static set, data paths, executable bits,
  desktop/icon metadata, and archive extraction.
- Windows: test outside the developer PATH, check DLL/PDB pairing and path case/encoding.
- Android: check variant/ABI, manifest, assets/native libraries, version code/name, signature,
  install/upgrade, and launch on a device.

## Smoke test

Extract or install into a clean location; launch; create/load a world; verify JSON/Mod loading,
Lua API availability for the intended build, translation, fonts, tiles, sound, shader variants,
save/write paths, and a clean shutdown. Report every feature omitted intentionally.

## Security and licensing

Signing keys, passwords, service tokens, and local certificates remain outside tracked files and
logs. Include required licenses/attributions and a source/commit reference. Scan the final
artifact, not only the source checkout, for accidental credentials or local paths.

## Artifact policy

Do not commit packages, build directories, symbols, or generated shader/translation outputs
unless a checked generated-file policy says otherwise. Upload packages and matching symbols as
CI/release artifacts with documented retention and restoration.
