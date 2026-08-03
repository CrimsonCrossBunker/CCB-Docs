---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: design-gameplay
title: 'Legacy migration draft: gameplay'
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
- doc/design-balance-lore/design-gameplay.md
- doc/design-balance-lore/design-balance.md
- GOVERNANCE.md
source_symbols: []
source_queries: []
source_fingerprint: cb2d9706730e3e8a7d418c865a6c42f81c0c455b45ec6330e6ce4b33cd4ad951
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: cc3c3cfcdec1c8143ff595437ce967a21292857443c745ed7dff1e31f18ba9aa
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/gameplay/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/design/gameplay/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/gameplay/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/design/gameplay/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/design-balance-lore/design-gameplay.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/design-balance-lore/design-gameplay.md
- path: doc/design-balance-lore/design-balance.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/design-balance-lore/design-balance.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/GOVERNANCE.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28design-gameplay%29%3A+&body=Document+ID%3A+design-gameplay%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: gameplay

This is the migration draft page for `design-gameplay`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `design-gameplay`
- Target: `design/gameplay.md`
- Replacement: design-gameplay
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| design-gameplay | doc/design-balance-lore/design-gameplay.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## CCB gameplay direction

CCB is an open-world survival game. Its core experience comes from planning with incomplete
information, limited resources, and a changing environment; taking understandable risks; and
dealing with the consequences of those plans. World simulation should support those decisions,
not add unobservable detail solely for the sake of simulation.

### Properties contributors should preserve

- Time, position, noise, weather, carrying capacity, injury, supply, and enemy behavior should form
  connected choices.
- A strong solution may be clearly better than an improvised one, but should have acquisition,
  operation, maintenance, or exposure costs that make sense in the world.
- Separate character knowledge, player knowledge, and interface hints. Danger may surprise, but
  should not depend on arbitrary rules that cannot be learned.
- Failure should normally be traceable to observable decisions. Necessary randomness needs bounded
  outcomes, feedback, and appropriate recovery space.
- Automation and convenience should remove repetition while retaining meaningful route, resource,
  time, and risk decisions.
- NPCs, factions, missions, and world events should interact through shared systems where possible
  instead of creating exceptions for a single script.

## Verisimilitude and abstraction

Verisimilitude determines what is plausible in the world; abstraction selects which details are
worth operating as a player. A contributor may omit electrical parameters, repeated labor, or
invisible microscopic processes while preserving consequences that change strategy. Conversely,
being “more realistic” is not enough to justify a mechanic: explain how a player understands and
responds to it and how it composes with existing systems.

## Intent is not implementation

The legacy design documents mix long-term vision, implementation at the time, and unfinished
ideas. The migrated text retains reusable principles, but every concrete behavior must still be
confirmed in current C++, JSON, Lua registrations, and tests. Proposals should label current
behavior, desired behavior, and possible future direction explicitly. Do not write aspiration as an
existing contract. Governance and merge decisions follow current `GOVERNANCE.md`, not personal
authority statements preserved in old prose.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `cb2d9706730e3e8a7d418c865a6c42f81c0c455b45ec6330e6ce4b33cd4ad951`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/design-balance-lore/design-gameplay.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/design-balance-lore/design-gameplay.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/design-balance-lore/design-gameplay.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
