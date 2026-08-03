---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: design-steel-crafting
title: 'Legacy migration draft: steel crafting'
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
- doc/design-balance-lore/STEEL_CRAFTING.md
- data/json/materials.json
- data/json/recipes/other/materials.json
- data/json/requirements/materials.json
source_symbols: []
source_queries: []
source_fingerprint: f12dfc5ad874180d9e08feb7e486805f625b52d0e537aa4b23769e04b0b6d35b
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 12613de7270a0ee1fa4b3a42a32656dcdba39c94338a7c23f1883ecf18ae5d8a
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: FarFarLakeSea, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: design
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/steel-crafting/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/design/steel-crafting/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/steel-crafting/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/design/steel-crafting/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/design-balance-lore/STEEL_CRAFTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/STEEL_CRAFTING.md
- path: data/json/materials.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/materials.json
- path: data/json/recipes/other/materials.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/recipes/other/materials.json
- path: data/json/requirements/materials.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/requirements/materials.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28design-steel-crafting%29%3A+&body=Document+ID%3A+design-steel-crafting%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: steel crafting

This is the migration draft page for `design-steel-crafting`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `design-steel-crafting`
- Target: `design/steel-crafting.md`
- Replacement: design-steel-crafting
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| design-steel-crafting | doc/design-balance-lore/STEEL_CRAFTING.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current steel abstraction

CCB uses a small set of material classes to express major differences in impurities, carbon
content, and heat treatment rather than simulating complete metallurgy. Current
`data/json/materials.json` includes `budget_steel`, `lc_steel`, `mc_steel`, `hc_steel`, `ch_steel`,
`qt_steel`, and the legacy-compatible `steel`, among others. That data and its loader define real
IDs, resistances, repair materials, and descriptions. Historical SAE comparisons, skill tables, and
hour counts are design approximations, not recipe contracts.

Low-, medium-, and high-carbon, case-hardened, and quench-tempered categories should create
understandable differences in working, durability, and repair. Harder processes normally require
better heat control, tools, knowledge, time, and risk. The game may compress cooling and batching,
but an advanced steel should not become a cost-free numeric upgrade.

## Writing or migrating recipes

1. Start from current material, item, and recipe IDs and confirm what the target actually uses
   instead of inferring it from a display name.
2. Compare the real process with tool quality, proficiencies, skills, activity time, batches, fuel,
   and components that the game can currently express.
3. Separate stock production, forging, case hardening or quenching and tempering, and repair. Do not
   apply a finished-item treatment to a generic ingot when that process would not fit.
4. Prefer recovery from pre-Cataclysm vehicles, machinery, and goods. A new mining or smelting route
   must show why it is sensible under current setting and technology constraints and not busywork.
5. For upgrades and repairs, inspect `copy-from`, material, `repaired_with`, requirement groups,
   tool energy, batch time, and disassembly results.

Validation includes JSON formatting and loading, recipe reachability, component conservation, batch
scaling, tool energy, failure conditions, repair, and disassembly. Historical tables may explain a
tradeoff, but every concrete skill, time, carbon quantity, or material property must be rechecked in
current data at the pinned commit.

## History and attribution

Accepted inventory contributors: FarFarLakeSea, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `f12dfc5ad874180d9e08feb7e486805f625b52d0e537aa4b23769e04b0b6d35b`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/design-balance-lore/STEEL_CRAFTING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/STEEL_CRAFTING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/STEEL_CRAFTING.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
