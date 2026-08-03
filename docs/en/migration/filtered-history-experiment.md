---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: migration.filtered-history-experiment
title: Filtered-history experiment
language: en
status: active
doc_type: explanation
audiences:
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 365
last_human_reviewer: LYHGLYTX
source_paths:
- doc/migration/markdown-inventory.yml
- doc/migration/history-assessment.md
source_symbols: []
source_queries: []
source_fingerprint: cf5cd52677add7164774c34104c2d497d1bc57876339a9ed8d65f4a201baa2ea
authority: historical
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 996eb67a61f7df858a29a9f97946e328b2e9428c152b5772a45e8ab96e7c7e33
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB migration experiment; no repository history was imported.
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: migration-history
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/migration/filtered-history-experiment/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/migration/filtered-history-experiment/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/migration/filtered-history-experiment/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/migration/filtered-history-experiment/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/migration/markdown-inventory.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/migration/markdown-inventory.yml
- path: doc/migration/history-assessment.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/migration/history-assessment.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28migration.filtered-history-experiment%29%3A+&body=Document+ID%3A+migration.filtered-history-experiment%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Filtered-history experiment

## Result

A temporary, isolated `git-filter-repo` experiment was run for the selected
final paths. The filtered repository was neither imported into nor pushed to
CCB-Docs.

| Measure | Result |
| --- | ---: |
| Selected final paths | 111 |
| Self-contained repository size | 14 MiB |
| Commits | 1351 |
| Author identities | 226 |
| Final paths | 111 |
| Rename records | 0 |
| `git fsck` | passed |

## Decision

The experiment is self-contained and passes `git fsck`, but it preserved no
auditable rename records and an import would couple migration pages to
game-repository history. This phase therefore imports neither the whole game
history nor the filtered repository. Every page retains CCB source URLs,
source commits, sanitized contributors, and license data. A later import
requires Responsible-human review of author mappings, rename semantics, and
licensing.

The experiment used Git objects and explicit paths only. It did not traverse
`obj-lua/` or another untracked build cache.
