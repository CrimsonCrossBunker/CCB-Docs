---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.monster-special-attacks
title: 'Legacy migration draft: monster special attacks'
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
last_human_reviewer: Pending human review
source_paths:
- doc/JSON/MONSTER_SPECIAL_ATTACKS.md
- src/monstergenerator.cpp
- src/monstergenerator.h
- data/json/monster_special_attacks/monster_attacks.json
- tests/monster_attack_test.cpp
source_symbols:
- MonsterGenerator::load_monster_attack
- mattack_actor::load
source_queries: []
source_fingerprint: b4670a309a41ffe2bd452359a1f19f61ab7653d62acbb8582b4a245c78736492
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 37ea54fc1bc8b70dbdf6102f2ba706cfa53de70b2836f8f1fcc5d9bfc6a82beb
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/monster-special-attacks/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/monster-special-attacks/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/monster-special-attacks/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/monster-special-attacks/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/JSON/MONSTER_SPECIAL_ATTACKS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/JSON/MONSTER_SPECIAL_ATTACKS.md
- path: src/monstergenerator.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/monstergenerator.cpp
- path: src/monstergenerator.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/monstergenerator.h
- path: data/json/monster_special_attacks/monster_attacks.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/monster_special_attacks/monster_attacks.json
- path: tests/monster_attack_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/monster_attack_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.monster-special-attacks%29%3A+&body=Document+ID%3A+json.monster-special-attacks%0ALanguage%3A+en%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: monster special attacks

This is the migration draft page for `json.monster-special-attacks`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.monster-special-attacks`
- Target: `reference/json/monster-special-attacks.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/monster-special-attacks/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.monster-special-attacks | doc/JSON/MONSTER_SPECIAL_ATTACKS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Monster special-attack contract

`special_attacks` is an ordered capability set on a `MONSTER`. An entry may use legacy
`[ native_name, cooldown ]` syntax for a registered C++ attack or an actor object with `type` and
`id`. Actor types, fields, and behavior come from `MonsterGenerator::init_attack`,
`mattack_actors.cpp`, and tests.

### Identity, cooldowns, and conditions

Repeated actor subtypes on one monster need distinct `id` values; otherwise loading reports a
duplicate and retains only the last definition. A cooldown can use current fixed or expression forms.
Whether a failed condition, missing target, or missing resource consumes cooldown depends on the
actor call path and needs implementation-specific tests.

Leap, melee or bite, gun, spell, grab, and summon actors have different required members. For
example, leap requires `max_range` while gun reads `gun_type`, ranges or modes, targeting, and ammo.
Do not apply one actor's field table to another. A `condition` normally gets the monster as alpha;
beta availability depends on how that actor constructs its dialogue.

### Inheritance and side effects

The Monster `copy-from` reader supports replacement or deletion, with names and `id` values
determining the result. Self or target effects, fields, spawns, sounds, messages, ammo, item, and
spell IDs must exist. Attacks can mutate maps, cross z-levels, grab body parts, or establish targeting
state; failure paths must clean up state.

### Validation

Run formatting, `make -j2 json-check`, `--check-mods` for the real Mod, and relevant
`monster_attack_test`, `mondefense_test`, and actor tests. Cover no target, invisible targets,
minimum and maximum range, obstacles, cooldowns, empty ammo, false conditions, player/NPC/monster
targets, save reload, and duplicate actor IDs. Profile frequent path searches, AoE, spawn, and field
actors.

## History and attribution

Accepted inventory contributors: Maleclypse, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `b4670a309a41ffe2bd452359a1f19f61ab7653d62acbb8582b4a245c78736492`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/MONSTER_SPECIAL_ATTACKS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/MONSTER_SPECIAL_ATTACKS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/MONSTER_SPECIAL_ATTACKS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
