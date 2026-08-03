---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.monsters
title: 'Legacy migration draft: monsters'
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
- doc/JSON/MONSTERS.md
- src/monstergenerator.cpp
- src/monstergenerator.h
- data/json/monsters/zed-classic.json
- tests/monster_test.cpp
source_symbols:
- MonsterGenerator::load_monster
- mtype::load
- species_type::load
- mon_flag::load
source_queries: []
source_fingerprint: 9d69264687ff03d74f53d9ef417e4d15e8e797b45e100aa8c52209022a738d43
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: f9304afa2dbefb3c066e174917caca8ae8761bdc8c0b4c13e65b0123a2d5d88b
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: Maleclypse, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/monsters/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/monsters/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/monsters/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/monsters/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/MONSTERS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/MONSTERS.md
- path: src/monstergenerator.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/monstergenerator.cpp
- path: src/monstergenerator.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/monstergenerator.h
- path: data/json/monsters/zed-classic.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/monsters/zed-classic.json
- path: tests/monster_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/monster_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.monsters%29%3A+&body=Document+ID%3A+json.monsters%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: monsters

This is the migration draft page for `json.monsters`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.monsters`
- Target: `reference/json/monsters.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/monsters/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.monsters | doc/JSON/MONSTERS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB Monster contract

`MONSTER` is passed by `MonsterGenerator::load_monster` to a generic factory and interpreted by
`mtype::load` for fields, inheritance, and bounds. A legacy field table is only historical evidence;
the current loader, first-party JSON, and `tests/monster_test.cpp` are the contract.

### Minimal definition and identity

```jsonc
{
  "type": "MONSTER",
  "id": "mon_ccb_example",
  "name": { "str": "example creature" },
  "description": "A creature used by documentation.",
  "default_faction": "wildlife",
  "symbol": "e",
  "color": "light_green",
  "material": [ "flesh" ],
  "species": [ "MAMMAL" ],
  "volume": "62500 ml",
  "weight": "80 kg",
  "hp": 40,
  "speed": 90
}
```

The `id` is a stable reference used by spawn groups, mapgen, missions, EOCs, and saves. Current
loading requires `name`, `default_faction`, and `symbol`. Read `mtype::load` for numeric bounds,
units, and defaults; example values are not balance recommendations.

Defining a monster does not make it appear. Natural placement normally also needs a monster group,
mapgen or static spawn, event, or EOC. Species, faction, material, harvest, death-drop, and item-group
fields must reference actual registered IDs.

### Behavior composition

- `flags`, anger/fear/placate triggers, vision, path settings, and move skills control common AI.
- `special_attacks` may name a registered native attack or use current actor objects. Repeated
  subtypes need distinct `id` values or the loader reports replacement.
- Named `weakpoint_sets` merge first and inline `weakpoints` override matching entries last; deletion
  has dedicated semantics.
- `armor`, `melee_damage`, `attack_effs`, `emit_fields`, and death functions have their own contracts.
- Upgrades, reproduction, revive/zombify/fungalize, and corpse, egg, or baby IDs affect long lifecycles.

`copy-from` inherits only what the factory supports. `extend`, `delete`, `relative`, and
`proportional` are not interchangeable for every field; armor, weakpoints, and special attacks have
specialized readers.

### Validation

Run the formatter, `make -j2 json-check`, and `--check-mods` for the real Mod set. Run the relevant
`monster_test` filter and inspect spawning, faction behavior, paths, attack cooldowns, drops, death,
upgrade or reproduction, and save reload across multiple seeds. Performance review should include
frequent special attacks, pathfinding, field emission, and large groups.

A valid combination is not necessarily playable. Review HP, speed, armor, damage, spawn weight, and
loot as one balance and regression surface.

## History and attribution

Accepted inventory contributors: Maleclypse, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `9d69264687ff03d74f53d9ef417e4d15e8e797b45e100aa8c52209022a738d43`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/MONSTERS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/MONSTERS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/MONSTERS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
