---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: design-batteries-electricity
title: 'Legacy migration draft: batteries electricity'
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
- doc/design-balance-lore/batteries_and_electricity.md
- data/json/items/battery.json
- data/json/vehicleparts/battery.json
- src/vehicle_part.cpp
- tests/battery_mod_test.cpp
source_symbols: []
source_queries: []
source_fingerprint: b3069bfcdaf5049a556adec6f61a4d44916319fd2acaf3a4bfb77ba468d5fdc0
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: d6228a69b65e05b3d6777edb7824ea753861e7d54740960687a009b2b363a4d6
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/batteries-electricity/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/design/batteries-electricity/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/batteries-electricity/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/design/batteries-electricity/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/design-balance-lore/batteries_and_electricity.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/batteries_and_electricity.md
- path: data/json/items/battery.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/items/battery.json
- path: data/json/vehicleparts/battery.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/vehicleparts/battery.json
- path: src/vehicle_part.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/vehicle_part.cpp
- path: tests/battery_mod_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tests/battery_mod_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28design-batteries-electricity%29%3A+&body=Document+ID%3A+design-batteries-electricity%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: batteries electricity

This is the migration draft page for `design-batteries-electricity`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `design-batteries-electricity`
- Target: `design/batteries-electricity.md`
- Replacement: design-batteries-electricity
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| design-batteries-electricity | doc/design-balance-lore/batteries_and_electricity.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Boundaries of the electricity model

CCB deliberately does not simulate a complete electrical circuit. Power for handheld devices is
primarily abstracted as capacity, consumption, and a compatible battery class. Voltage, current,
series or parallel cells, and physical connectors are normally not exposed. This tradeoff lets a
player reason about runtime, carried energy, and resupply instead of wiring. When a high-draw device
really needs a restriction, express it through an existing visible contract rather than assuming an
unregistered electrical simulation.

## Current data representation

Battery cells are represented by `MAGAZINE` objects in item data. Battery ammunition categories,
capacity, default contents, and flags describe stored energy. A tool with a replaceable battery
accepts one through a `MAGAZINE_WELL` pocket. Ammo restrictions, adaptors, flags, relevant code, and
tests jointly define actual compatibility. `data/json/items/battery.json` is one entry point for
current first-party battery data, whose range now extends beyond the old table, including special
or atomic cells. The historical table is therefore not a complete inventory.

Large vehicle storage and handheld tool batteries are not one interchangeable interface. Trace the
current item, pocket, ammo, vehicle-part registrations, and tests separately before changing either
side; do not infer compatibility from display names.

## Adding or calibrating a device

1. Estimate an order of magnitude from credible real runtime and power evidence, and record the
   conditions. Manufacturer best-case advertising is not a direct test value.
2. Choose the closest existing battery class and combine its capacity with device consumption to
   obtain a reasonable runtime. Do not add types merely to reproduce multiple physical cells.
3. Inspect the tool pocket, ammo restrictions, default battery, supported adaptors, charging paths,
   and insertion and removal behavior.
4. Cover empty, partial, full, incompatible, adapted, save/reload, and charging boundaries.
5. Run JSON loading and focused battery tests. Record mod and documentation impact when a public
   JSON field or compatibility relationship changes.

Short-lived or high-draw real devices warrant tighter estimates; low-draw devices with ample
capacity tolerate wider approximations. The goal is credible runtime and clear player decisions,
not apparently precise electrical parameters that the runtime does not implement.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `b3069bfcdaf5049a556adec6f61a4d44916319fd2acaf3a4bfb77ba468d5fdc0`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/design-balance-lore/batteries_and_electricity.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/batteries_and_electricity.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/batteries_and_electricity.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
