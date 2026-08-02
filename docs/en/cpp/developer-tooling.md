---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: developer-tooling
title: 'Legacy migration draft: developer tooling'
language: en
status: draft
doc_type: explanation
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 365
last_human_reviewer: Pending human review
source_paths:
- doc/c++/DEVELOPER_TOOLING.md
- build-scripts/clang-tidy-run.sh
- build-scripts/ci-iwyu-run.py
- .github/workflows/clang-tidy.yml
- .github/workflows/iwyu.yml
source_symbols: []
source_queries: []
source_fingerprint: 71d889bd30bafd07c041e9d131a9381325bce710155ffaeb9c5b11c336bd282d
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: b2db43ba1123c06d1a46de5ac6919fc31a8dd7dccece7395b41c87ed131be004
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: dumb-kevin, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/developer-tooling/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/developer-tooling/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/developer-tooling/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/developer-tooling/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/c++/DEVELOPER_TOOLING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c++/DEVELOPER_TOOLING.md
- path: build-scripts/clang-tidy-run.sh
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/build-scripts/clang-tidy-run.sh
- path: build-scripts/ci-iwyu-run.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/build-scripts/ci-iwyu-run.py
- path: .github/workflows/clang-tidy.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/.github/workflows/clang-tidy.yml
- path: .github/workflows/iwyu.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/.github/workflows/iwyu.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28developer-tooling%29%3A+&body=Document+ID%3A+developer-tooling%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: developer tooling

This is the migration draft page for `developer-tooling`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `developer-tooling`
- Target: `cpp/developer-tooling.md`
- Replacement: developer-tooling
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| developer-tooling | doc/c++/DEVELOPER_TOOLING.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## History and attribution

Accepted inventory contributors: dumb-kevin, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `71d889bd30bafd07c041e9d131a9381325bce710155ffaeb9c5b11c336bd282d`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/c++/DEVELOPER_TOOLING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/DEVELOPER_TOOLING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/DEVELOPER_TOOLING.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
