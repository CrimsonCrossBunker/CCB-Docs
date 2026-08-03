---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: operations.releases
title: Release operations
language: en
status: active
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
- .github/workflows/release-android-bundle.yaml
- doc/RELEASE_PROCESS.md
- build-scripts/generate-release-notes.js
source_symbols: []
source_queries:
- workflow_dispatch
source_fingerprint: 9b2686c6179dcc7fd3710b82931aa8b4061b7911ee1a4c4b670d0e265034702c
authority: build-config
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 968e8122bf55cc278a9f3c5c45d8fbeedfea0f436185c719787a5f53e02533fc
prerequisites:
- operations.packaging
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/operations/releases/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/operations/releases/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/operations/releases/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/operations/releases/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: .github/workflows/release.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/.github/workflows/release.yml
- path: .github/workflows/release-android-bundle.yaml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/.github/workflows/release-android-bundle.yaml
- path: doc/RELEASE_PROCESS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/doc/RELEASE_PROCESS.md
- path: build-scripts/generate-release-notes.js
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/build-scripts/generate-release-notes.js
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28operations.releases%29%3A+&body=Document+ID%3A+operations.releases%0ALanguage%3A+en%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Release operations

CCB's experimental release workflow is triggered by relevant pushes to `master` and supports
manual dispatch. It creates timestamped prerelease metadata, release notes from Git history,
and a GitHub release, then coordinates platform/data artifacts such as translations, tilesets,
shaders, desktop packages, and Android bundles.

## Authority and sequencing

`.github/workflows/release.yml` and `.github/workflows/release-android-bundle.yaml` define the
actual jobs, permissions, dependencies, artifact names, and triggers. `doc/RELEASE_PROCESS.md`
provides background. Always inspect the workflow at the release commit before operating it.

1. Confirm the target commit and default-branch CI state.
2. Confirm translations, shader/tiles generation, version metadata, and platform build inputs.
3. Trigger only the intended workflow/event; do not rerun unrelated old commits.
4. Monitor every dependent job and preserve the run URL/logs.
5. Compare release target SHA, notes range, tags, checksums, artifact set, signatures, and smoke
   test results before announcing the release.

## Failure handling

A created GitHub release does not prove every artifact succeeded. If a downstream job fails,
state exactly which artifacts are absent or superseded; repair the workflow/input in a PR and
rerun deliberately. Never upload a locally improvised replacement under a trusted release name.

## Security and permissions

Release tokens/signing material stay in GitHub secrets or protected environments. Human review
is required for workflow, permission, signing, and destination changes. Current broad permissions
are a security-review target; documentation must not claim least privilege until settings and
workflow scopes demonstrate it.

## Records and rollback

Retain release commit, tag, run IDs, artifact checksums, toolchain/dependency revisions, signing
identity, Responsible human, known issues, and supersession/rollback decision. Prefer publishing
a corrected/superseding release to silently replacing artifacts.

## Validation

Smoke-test each distributed platform from the published artifact and verify data, mods, Lua,
translations, graphics/audio, save/load, and upgrade behavior. Archive matching symbols and the
documentation/API snapshot needed to diagnose that exact release.
