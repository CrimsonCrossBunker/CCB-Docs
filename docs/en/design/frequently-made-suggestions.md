---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: design.frequently-made-suggestions
title: 'Legacy migration draft: frequently made suggestions'
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
- doc/FREQUENTLY_MADE_SUGGESTIONS.md
- GOVERNANCE.md
- README.md
source_symbols: []
source_queries: []
source_fingerprint: 1ce8e96664cf785d8ebe4739b45940e2ccf0febc6b7e53ec213b0fa807e34ef7
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 4ce36a9c5056a35d5e2db3eef731b86239dec6ccdcd4b8dfb4b47439373295ed
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LunaGlaze, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: design
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/frequently-made-suggestions/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/design/frequently-made-suggestions/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/frequently-made-suggestions/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/design/frequently-made-suggestions/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/FREQUENTLY_MADE_SUGGESTIONS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/FREQUENTLY_MADE_SUGGESTIONS.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/GOVERNANCE.md
- path: README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/README.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28design.frequently-made-suggestions%29%3A+&body=Document+ID%3A+design.frequently-made-suggestions%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: frequently made suggestions

This is the migration draft page for `design.frequently-made-suggestions`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `design.frequently-made-suggestions`
- Target: `design/frequently-made-suggestions.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/design/frequently-made-suggestions/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| design.frequently-made-suggestions | doc/FREQUENTLY_MADE_SUGGESTIONS.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## This is not a live feature-status table

The legacy “frequently made suggestions” page mixed years of feature status, personal opinion,
upstream links, and specific numbers. Its answers only describe discussion at the time; they do not
prove that CCB currently implements, is developing, rejects, or permits something only in a mod.
Reconfirm status in current source, Issues, pull requests, roadmaps, and maintainer decisions.
`GOVERNANCE.md`, not old descriptions of individuals or hostile wording, governs the project.

## Quick check before proposing something

1. Search current CCB Issues, pull requests, source registrations, and CCB-Docs to confirm that the
   problem remains and no implementation is already in progress.
2. Describe the player need and a reproducible scenario instead of supplying only a feature name or
   asking for a vote.
3. Explain interaction with setting, design principles, platforms, performance, saves, and mod
   compatibility.
4. Compare smaller approaches: can existing EOC, JSON, or Lua express it; is it suitable for a
   first- or third-party mod; does it require new runtime capability?
5. List maintenance cost, including UI, localization, test matrix, data migration, generated
   content, and a long-term owner.
6. If you intend to implement it, open a scoped design Issue first, then prepare the smallest PR and
   validation evidence after receiving direction feedback.

## Recurring decision principles

- One existing exception does not prove another should be added; old content may itself need repair.
- Real-world feasibility does not prove that one post-Cataclysm character can perform a task with
  available tools, knowledge, time, and acceptable risk.
- An option is not free: every branch expands code, documentation, localization, compatibility, and
  testing obligations.
- A content suggestion is often strongest as a working JSON or mod prototype, but the prototype
  still needs compatible licensing, provenance, and project fit.
- Technical difficulty is not permanent rejection, and desire is not a roadmap promise. Record
  dependencies, the current gap, and a verifiable next step.

When an answer affects project policy or many players, current maintainers decide through a
reviewable Issue or pull request. The page should link that decision and applicable commit and
become stale when its sources change instead of freezing one conversation forever.

## History and attribution

Accepted inventory contributors: LunaGlaze, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `1ce8e96664cf785d8ebe4739b45940e2ccf0febc6b7e53ec213b0fa807e34ef7`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/FREQUENTLY_MADE_SUGGESTIONS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/FREQUENTLY_MADE_SUGGESTIONS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/FREQUENTLY_MADE_SUGGESTIONS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
