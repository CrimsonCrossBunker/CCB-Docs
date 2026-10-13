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
source_symbols: []
source_queries:
- publish-translations
- Android x64 New UI
source_fingerprint: 4fa639b456b9891e4b9f50a601c47e9cb4c81220d20139062366d1507c1907bd
authority: build-config
verified_commit: b4342dc18797c4097f0dc275f61e420bb5887a4a
verified_at: '2026-10-13'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 505a9971715fc641229ddff68985b6bacb6922f28d437e014c85af365be3f46b
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/993
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/operations/release-assets-sync/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/operations/release-assets-sync/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/operations/release-assets-sync/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/operations/release-assets-sync/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/b4342dc18797c4097f0dc275f61e420bb5887a4a
source_urls:
- path: .github/workflows/release.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b4342dc18797c4097f0dc275f61e420bb5887a4a/.github/workflows/release.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28operations.release-assets-sync%29%3A+&body=Document+ID%3A+operations.release-assets-sync%0ALanguage%3A+en%0AVerified+commit%3A+b4342dc18797c4097f0dc275f61e420bb5887a4a%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Draft: Android sound and translation release archive

This page accompanies unmerged CCB PR #993. Local tool checks cover the matrix and archive commands. Android builds, device playback and actual Release uploads still require release acceptance.

The Experimental Release matrix sets `sound: 1` for Android x64, Android x64 New UI and Android x32. A matrix flag does not prove playback or signature validation.

After translations finish, a separate step packages the `translations` artifact as `ccb-translations-<timestamp>.tar.gz` and uploads to the actual `tag_name` returned by release creation. Experimental uses timestamp tags; Candidate and Stable retain their version tags. This extra archive does not replace platform installers.

Reruns do not overwrite an existing archive. Inspect precise provenance, logs and asset state if upload fails or the asset already exists; do not silently substitute another translation build.

Five regression tests cover newly extracted strings, cumulative macOS alias columns, a real tar archive and mocked uploads for three release channels. Mocked uploads only record commands. Final acceptance must check the source SHA, workflow run, all installers and actual Release assets.

Adapted from CDDA #88516, #88789, #88791 and #88836. Source commits retain original authors and provenance. Responsible human: LYHGLYTX.
