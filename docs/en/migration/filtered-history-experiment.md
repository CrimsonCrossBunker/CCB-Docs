---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: migration.filtered-history-experiment
title: Filtered-history experiment
language: en
status: draft
doc_type: explanation
audiences:
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 365
last_human_reviewer: Pending human review
source_paths:
- doc/migration/markdown-inventory.yml
- doc/migration/history-assessment.md
source_symbols: []
source_queries: []
source_fingerprint: 11ee34ef59bec5c932234a2249ad178c7b65b05f748c83530c4b49a4b0d3eb14
authority: historical
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
search:
  exclude: true
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
