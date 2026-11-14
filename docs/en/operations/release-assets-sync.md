---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: operations.release-assets-sync
title: 'Draft: Android sound and translation release archive'
language: en
status: draft
doc_type: how-to
audiences:
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 60
last_human_reviewer: Pending human review
source_paths:
- .github/workflows/release.yml
- .github/workflows/matrix.yml
source_symbols: []
source_queries:
- publish-translations
- Android x64 New UI
- clang++-22
- g++-16
source_fingerprint: 654aa06af56cd828a6c7cbe22d369d4d481f5c289b43000be487cb4abd98de06
authority: build-config
verified_commit: 34200a2ffcdaaf925cf2381bf900d2c753cd1a6c
verified_at: '2026-11-14'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8e73ee7a18624c5587638586e4f16ac31f8765fced8cfb51293ca51ea1ceb6ef
prerequisites:
- operations.releases
- platforms.android
depends_on:
- maintenance.releases
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
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/operations/release-assets-sync/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/operations/release-assets-sync/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/operations/release-assets-sync/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/operations/release-assets-sync/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c
source_urls:
- path: .github/workflows/release.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c/.github/workflows/release.yml
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c/.github/workflows/matrix.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28operations.release-assets-sync%29%3A+&body=Document+ID%3A+operations.release-assets-sync%0ALanguage%3A+en%0AVerified+commit%3A+34200a2ffcdaaf925cf2381bf900d2c753cd1a6c%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Draft: Android sound and translation release archive

CCB #993 introduced the translation archive and Android sound entries. Local tool checks cover the matrix and archive commands. Android builds, device playback and actual Release uploads still require release acceptance.

The later Android packaging change removed the bundled soundpack entries from Android x64, Android x64 New UI and Android x32 in Experimental Release. Device playback and signing are separate release checks.

After translations finish, a separate step packages the `translations` artifact as `ccb-translations-<timestamp>.tar.gz` and uploads to the actual `tag_name` returned by release creation. Experimental uses timestamp tags; Candidate and Stable retain their version tags. This extra archive does not replace platform installers.

Reruns do not overwrite an existing archive. Inspect precise provenance, logs and asset state if upload fails or the asset already exists; do not silently substitute another translation build.

Five regression tests cover newly extracted strings, cumulative macOS alias columns, a real tar archive and mocked uploads for three release channels. Mocked uploads only record commands. Final acceptance must check the source SHA, workflow run, all installers and actual Release assets.

Adapted from CDDA #88516, #88789, #88791 and #88836. Source commits retain original authors and provenance. Responsible human: LYHGLYTX.

The CI matrix uses Clang 14 and checks Clang 22 and GCC 16 on Ubuntu 26.04. It retains Lua, railroad and advanced-inventory checks and the single-job GCC memory limit, with explicit compiler packages. The recorded matrix check verified parsing.
