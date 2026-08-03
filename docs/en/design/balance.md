---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: design-balance
title: 'Legacy migration draft: balance'
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
- doc/design-balance-lore/GAME_BALANCE.md
- doc/design-balance-lore/design-balance.md
- GOVERNANCE.md
source_symbols: []
source_queries: []
source_fingerprint: 1d0054d7999d75ae681f7fa6317b6ee70b8c6bdd8b86a97507c1edf1f974fb51
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 13fee1d31007d3482845ef6483008b2b839b5f3b753834a8745ee91de1c4a3ce
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- legacy.doc-design-balance-lore-game-balance
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: design
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/balance/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/design/balance/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/balance/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/design/balance/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/design-balance-lore/GAME_BALANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/GAME_BALANCE.md
- path: doc/design-balance-lore/design-balance.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/design-balance.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/GOVERNANCE.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28design-balance%29%3A+&body=Document+ID%3A+design-balance%0ALanguage%3A+en%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: balance

This is the migration draft page for `design-balance`. It records **2** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `legacy.doc-design-balance-lore-game-balance, design-balance`
- Target: `design/balance.md`
- Replacement: design-balance
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| legacy.doc-design-balance-lore-game-balance | doc/design-balance-lore/GAME_BALANCE.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | design-balance |
| design-balance | doc/design-balance-lore/design-balance.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## What balance documentation is for

CCB balance goals help contributors make consistent tradeoffs among verisimilitude, readability,
risk, resource cost, and long-term progression. They do not establish permanent numeric limits for
every value. The old stat, skill, monster, weapon, and resource tables captured reference points at
the time they were written. They can explain intent, but they are not current runtime contracts.
Rebuild the baseline from current JSON, C++, tests, and observed game data before making a change.

### Define the problem first

1. Describe the current player-visible behavior, a repeatable scenario, and the affected stage of
   progression.
2. Locate the loaders, formulas, data objects, and tests that implement it instead of copying
   numbers from a superficially similar entry.
3. Distinguish bug fixes, content calibration, difficulty preferences, and new mechanics. They need
   different evidence and may need different options or compatibility treatment.
4. Consider acquisition, time, noise, carrying cost, durability, damage, recovery, and enemy
   counterplay together. Avoid balancing an ecosystem through one number alone.
5. Compare representative early-, middle-, and late-game scenarios before and after the change,
   including random and extreme cases.

## Balance principles

- Real-world evidence constrains plausible ranges, while the game compresses complex systems into
  mechanics players can understand and operate.
- Powerful tools may remain powerful. Scarcity, supply, time, noise, mass, exposure, and maintenance
  can provide tradeoffs without forcing every option to be equivalent.
- Prefer enemies and equipment that create different decisions over an endless race of larger hit
  point, armor, and damage values.
- Lethal outcomes without warning or reasonable counterplay are rarely meaningful difficulty.
  Hazards should normally expose observable cues and learnable responses.
- Save and mod compatibility are design constraints. Changes to IDs, serialized fields,
  inheritance, or widely reused data require a separate migration assessment.

## Evidence and validation

A design statement can propose direction; it cannot prove that behavior is implemented. A balance
change should cite current source paths and tests, provide reproducible comparison steps, and run
the relevant JSON loading, focused unit tests, or live game scenario. When an old table or example
does not match current data, cite it as a historical snapshot instead of silently turning it into a
new authority.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`; the aggregate source fingerprint is `1d0054d7999d75ae681f7fa6317b6ee70b8c6bdd8b86a97507c1edf1f974fb51`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/design-balance-lore/GAME_BALANCE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/GAME_BALANCE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/GAME_BALANCE.md)
- [`doc/design-balance-lore/design-balance.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/design-balance.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/design-balance.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
