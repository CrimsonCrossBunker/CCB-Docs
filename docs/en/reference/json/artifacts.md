---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.artifacts
title: 'Legacy migration draft: artifacts'
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
- doc/JSON/ARTIFACTS.md
- src/relic.cpp
- src/relic.h
- data/json/artifact/relic_procgen_data.json
- data/json/artifact/premade_artifacts.json
source_symbols:
- relic_procgen_data::load
- relic_procgen_data::generation_rules::load
- relic_charge_template::load
source_queries: []
source_fingerprint: ad2b5a81653c650736c14c7353edf81b77620c498c521c6ccdcb628e6b7c3fc5
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 2c568666bb67a6bf85682a86b7fc1f8427ba1b5aa2d64e34da1bcc858e1ebd73
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
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/artifacts/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/artifacts/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/artifacts/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/artifacts/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/ARTIFACTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/ARTIFACTS.md
- path: src/relic.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/relic.cpp
- path: src/relic.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/relic.h
- path: data/json/artifact/relic_procgen_data.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/artifact/relic_procgen_data.json
- path: data/json/artifact/premade_artifacts.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/artifact/premade_artifacts.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.artifacts%29%3A+&body=Document+ID%3A+json.artifacts%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: artifacts

This is the migration draft page for `json.artifacts`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.artifacts`
- Target: `reference/json/artifacts.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/artifacts/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.artifacts | doc/JSON/ARTIFACTS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Relics and procedural artifacts

An artifact combines a base item with relic data. Premade relics and `relic_procgen_data` are distinct
paths. A procgen dataset supplies weighted base items, charge templates, active spells, passive
enchantment values, and type weights. Generation rules set power budget, attribute limit, negative
power allowance, and resonance.

### Procgen lists

Every weighted entry requires weight. A passive entry requires an enchantment value type and may set
minimum, maximum, increment, power per increment, and ench_has. An active entry requires spell_id and
may set levels, power, and ench_has. Item entries require item and type-weight entries require a
usable value. Dataset checks validate active spells but do not prove balance, item suitability, or
that every enchantment consumer is meaningful.

### Charges

A charge template contains range and power objects for max_charges, charges, and charges_per_use,
plus recharge_type and time. Generation clamps starting charges to the maximum and selects time from
the range. The current procgen-template loader does not read the historical `recharge_condition`
field. That member exists on generated runtime charge information and must not be presented as this
JSON input contract.

Take recharge-type and ench_has enums from `relic.cpp`. Multiple generated active spells share one
activation charge cost. Verify how their activation requirements combine with the current generator.

### Power, resonance, and validation

Power is a generator selection budget, not automatic balance proof. A resonant generation rule feeds
final power into current resonance runtime; thresholds, effects, and lore are behavior and design
contracts and cannot be copied from stale prose.

Run formatting, `make -j2 json-check`, and Mod `--check-mods`. Generate many samples with a fixed RNG
seed and inspect empty weighted lists, invalid spells or items, charge bounds, positive and negative
budgets, activation positions, save reload, and resonance. Generator changes need deterministic
distribution and consistency tests.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `ad2b5a81653c650736c14c7353edf81b77620c498c521c6ccdcb628e6b7c3fc5`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/ARTIFACTS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/ARTIFACTS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/ARTIFACTS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
