---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: pr-review-guide
title: 'Legacy migration draft: pr review'
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
- doc/reviewing_PR_guide.md
- CONTRIBUTING.md
- GOVERNANCE.md
- .github/pull_request_template.md
source_symbols: []
source_queries: []
source_fingerprint: e5ceb52246d59389382a552d90cbda3849e690eac4e606cce311555304fa8c68
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: e360a3cc0be225a07bdd7b01db1c5bc0a0bbffd4e5a1fbd4b01d8d7d806f4864
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: governance
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/pr-review/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/pr-review/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/pr-review/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/pr-review/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/reviewing_PR_guide.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/reviewing_PR_guide.md
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/CONTRIBUTING.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/GOVERNANCE.md
- path: .github/pull_request_template.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/.github/pull_request_template.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28pr-review-guide%29%3A+&body=Document+ID%3A+pr-review-guide%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: pr review

This is the migration draft page for `pr-review-guide`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `pr-review-guide`
- Target: `contributing/pr-review.md`
- Replacement: pr-review-guide
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| pr-review-guide | doc/reviewing_PR_guide.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current PR review checklist

Review establishes that a change solves the stated problem and agrees with CCB contracts,
compatibility policy, and maintenance policy. The legacy guide's fixed line thresholds and
upstream people or Discord roles are not CCB's permission model. Size is a review-risk
signal, not a merge rule.

### Read the scope first

- Does the description explain the problem, solution, alternatives, actual tests, and
  residual risk?
- Does the diff contain only work needed for the outcome, without unrelated formatting,
  refactors, generated output, or local files?
- Are commits and stacked PRs split by dependency with an exact merge order?
- Does the Responsible human understand the final diff instead of merely supplying a name?

### Compare authoritative sources

1. Check runtime claims against source and tests.
2. Check JSON, Lua, and API claims against Schemas, LuaLS, registrations, and generated
   inventories.
3. Check build commands against CI, CMake, Makefile, Gradle, and repository validators.
4. Check contribution and governance claims against `AGENTS.md`, `CONTRIBUTING.md`, and
   `GOVERNANCE.md`.
5. If CCB-Docs conflicts, mark and repair stale prose; prose does not override a contract.

### Review risk

- Do save serialization, stable IDs, Mod/Lua APIs, Android/desktop differences, and upstream
  divergence have migrations or compatibility plans?
- Is gameplay or balance supported by reviewable reasoning and sources?
- Are external code, data, images, sound, or text license-compatible and attributed?
- Did a generator update generated files, and is the generated diff stable?
- Are documentation IDs, the related CCB-Docs PR, and generated-reference impact complete?

### Validation evidence

Run the narrowest test that can demonstrate the failure first. Distinguish an actual pass,
not run, an environment blocker, and a flaky or master failure unrelated to the diff. Do not
change assertions merely because CI is red, and do not call a failure unrelated without logs.

### Approval and merge boundary

A Bot cannot approve its own PR and PRs are not auto-merged. Before requiring non-author
approval, confirm at least two active, willing, permissioned human reviewers. A permissioned
human decides whether to merge only after conversations, Draft state, stack dependencies,
and final source pins are resolved.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `e5ceb52246d59389382a552d90cbda3849e690eac4e606cce311555304fa8c68`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/reviewing_PR_guide.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/reviewing_PR_guide.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/reviewing_PR_guide.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
