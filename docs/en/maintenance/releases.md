---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: maintenance.releases
title: Release maintenance
language: en
status: active
doc_type: how-to
audiences:
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- CONTRIBUTING.md
- doc/RELEASE_PROCESS.md
- .github/workflows/release.yml
- .github/workflows/release-android-bundle.yaml
source_symbols: []
source_queries: []
source_fingerprint: e20c16c43878b2fd175b9287b26b0340655df5724554fe0985cf74441118045d
authority: build-config
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: b257834293240b817b77b6d8244f0484ff475e9215a6a56f402f0c7f90db9d29
prerequisites:
- platforms.matrix
- validation.testing
depends_on:
- governance.security-license
redirect_from: []
supersedes:
- legacy.doc-release-diff
- legacy.doc-release-process
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/maintenance/releases/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/maintenance/releases/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/maintenance/releases/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/maintenance/releases/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/CONTRIBUTING.md
- path: doc/RELEASE_PROCESS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/RELEASE_PROCESS.md
- path: .github/workflows/release.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/.github/workflows/release.yml
- path: .github/workflows/release-android-bundle.yaml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/.github/workflows/release-android-bundle.yaml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28maintenance.releases%29%3A+&body=Document+ID%3A+maintenance.releases%0ALanguage%3A+en%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Release maintenance

Release behaviour is defined by the current workflows and repository settings,
not by an old checklist copied from an upstream release. Treat historical
release prose as input to review until every command is confirmed.

## Before a release

- select and record the exact source commit and version identity;
- require stable default-branch checks for intended platforms and feature sets;
- review save, data, Lua API, mod, translation, packaging, and security impact;
- confirm third-party licenses, attributions, and release-note provenance;
- generate documentation and API snapshots from the same source commit;
- verify signing and publishing credentials through protected environments,
  never through repository files or logs.

## Artifacts and verification

For every artifact record platform, architecture/ABI, build type, feature
options, source commit, workflow run, checksums, and signing state. Test install
or extraction and one startup/load path. Android APK/AAB, Windows packages, and
Linux artifacts are distinct evidence.

Large Doxygen output, compile databases, indexes, profiles, and symbol databases
remain CI/release artifacts rather than tracked source. Retention and backups
must include a restore test, not only successful upload.

## After publication

Publish release notes, API changelog, known compatibility issues, documentation
snapshot, and rollback or hotfix route. Confirm download links and the player
entry point. A failed or partially published release is recorded explicitly;
do not silently replace an artifact under the same identity.
