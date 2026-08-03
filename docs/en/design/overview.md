---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: design-overview
title: 'Legacy migration draft: overview'
language: en
status: active
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
last_human_reviewer: LYHGLYTX
source_paths:
- doc/design-balance-lore/design-doc.md
- doc/design-balance-lore/design-gameplay.md
- doc/design-balance-lore/design-user-experience.md
- GOVERNANCE.md
source_symbols: []
source_queries: []
source_fingerprint: 2e899b0038baf37c21a3b183ee8fdfc2f10745766a4385c4db0fd3621ddeb6ef
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: f648640c91c73b044dbc539fe538833d6f14b3b685ae5afa327317b0a6280fe0
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
risk_group: design
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/design/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/design/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/design-balance-lore/design-doc.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/design-doc.md
- path: doc/design-balance-lore/design-gameplay.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/design-gameplay.md
- path: doc/design-balance-lore/design-user-experience.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/design-user-experience.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/GOVERNANCE.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28design-overview%29%3A+&body=Document+ID%3A+design-overview%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: overview

This is the migration draft page for `design-overview`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `design-overview`
- Target: `design/overview.md`
- Replacement: design-overview
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| design-overview | doc/design-balance-lore/design-doc.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | design-overview |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## How to use design documentation

Design documentation explains why CCB favors a kind of experience, which questions a proposal must
answer, and which tradeoffs matter when systems conflict. It does not replace runtime, data-format,
or governance authorities. Source and tests define concrete behavior; schemas, declarations,
registrations, and generated inventories define JSON, Lua, and API contracts; current governance
files define project decisions.

### Minimum proposal structure

1. **Problem:** describe the current player experience and a reproducible scenario before assuming
   a solution.
2. **Goals and non-goals:** state the desired outcome and the boundaries that will not change.
3. **Current state:** list entry points, data ownership, lifecycle, tests, and CCB differences from
   upstream.
4. **Approach and alternatives:** compare player visibility, complexity, performance,
   maintainability, and compatibility.
5. **Migration risk:** inspect saves, mods, IDs, serialization, localization, platforms, and
   generated content.
6. **Acceptance:** provide runnable commands, scenarios, and rollback conditions.

## Decision boundaries

Numbers, file paths, people, and unimplemented mechanics in legacy design prose are historical
context only. Revalidate them against the current default branch before carrying them into a new
proposal. Resolve conflicting directions through Issues, pull requests, and the current maintainer
governance process. No old statement by one person permanently overrides repository governance.

## CCB and upstream

Upstream material can explain shared history and portable approaches, but CCB has its own runtime
differences, content direction, compatibility requirements, and governance. A proposal should name
the source revision, compare both current implementations, and port only what still applies to CCB.
If prose conflicts with a current contract, mark the page stale and repair the documentation rather
than changing the implementation to fit an obsolete explanation.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `2e899b0038baf37c21a3b183ee8fdfc2f10745766a4385c4db0fd3621ddeb6ef`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/design-balance-lore/design-doc.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/design-doc.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/design-doc.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
