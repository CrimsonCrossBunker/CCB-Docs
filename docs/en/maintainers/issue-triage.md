---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: maintainers.issue-triage
title: 'Legacy migration draft: issue triage'
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
- doc/ISSUE_TRIAGE.md
- ISSUES.md
- GOVERNANCE.md
- .github/ISSUE_TEMPLATE/bug_report.yml
- .github/ISSUE_TEMPLATE/feature_proposal.yml
- .github/labeler.yml
source_symbols: []
source_queries: []
source_fingerprint: 0f1b70d5d11df0526e5494b437c0b12f938d7be646c80980f7236642b3054adc
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 47d479b09803b82e23c34c99404f7a4a6b3aa891a71207427295ab013b6ac2ed
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/maintainers/issue-triage/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/maintainers/issue-triage/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/maintainers/issue-triage/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/maintainers/issue-triage/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/ISSUE_TRIAGE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/ISSUE_TRIAGE.md
- path: ISSUES.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/ISSUES.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/GOVERNANCE.md
- path: .github/ISSUE_TEMPLATE/bug_report.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/.github/ISSUE_TEMPLATE/bug_report.yml
- path: .github/ISSUE_TEMPLATE/feature_proposal.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/.github/ISSUE_TEMPLATE/feature_proposal.yml
- path: .github/labeler.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/.github/labeler.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28maintainers.issue-triage%29%3A+&body=Document+ID%3A+maintainers.issue-triage%0ALanguage%3A+en%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: issue triage

This is the migration draft page for `maintainers.issue-triage`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `maintainers.issue-triage`
- Target: `maintainers/issue-triage.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/maintainers/issue-triage/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| maintainers.issue-triage | doc/ISSUE_TRIAGE.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current issue-triage workflow

Triage turns reports into actionable work; its purpose is not to close issues quickly.
Confirm the repository and version, then distinguish defects, features, mechanics or
balance, JSON content, performance, documentation, and upstream sync. Current Issue Forms,
`ISSUES.md`, `LABELS.md`, and governance policy define the categories.

### First pass

1. Search open and closed CCB issues for duplicates and newer evidence.
2. Record the exact CCB commit or release, platform, build type, SDL backend, Mod list, and
   save origin.
3. Check reproduction steps, expected and actual results, logs, and a minimal example. Ask
   one specific, answerable question when evidence is missing.
4. Identify vulnerabilities, credentials, or private data and route them through the private
   process in `SECURITY.md`.
5. Apply subsystem, confirmation, and priority labels only when evidence supports them.
   Labels do not promise a schedule.

### Risk order

- crashes, save or map data loss, irreversible compatibility breakage, and security issues
  come first;
- player item or character loss, severe regressions, and blocking UI problems follow;
- ordinary defects, performance, and usability are ranked by impact and reproducibility;
- a small content request or unexplained number change is not automatically a confirmed bug.

Behaviour that matches current design but is undesirable is normally a feature or balance
proposal. Behaviour that violates a current contract or design is a bug. Record uncertainty
instead of replacing source, tests, or design policy with a personal expectation.

### Reproduction, closure, and reopening

A triager may reproduce a report, but does not owe a complete debugging session for every
issue. After a reasonable information request, an issue without reproducible evidence may
be closed with an explanation. Duplicate, out-of-scope, superseded, or rejected outcomes
also need a clear reason. New logs, a minimal save, or reproduction on a new version are
reasonable grounds to reopen.

### Hand off to implementation

An implementer should comment with intended scope and open a Draft PR. The PR links the
issue, names a Responsible human, and records validation and documentation impact. Do not
invent an owner, CODEOWNERS entry, or review team while triaging.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`; the aggregate source fingerprint is `0f1b70d5d11df0526e5494b437c0b12f938d7be646c80980f7236642b3054adc`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/ISSUE_TRIAGE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/ISSUE_TRIAGE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/ISSUE_TRIAGE.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
