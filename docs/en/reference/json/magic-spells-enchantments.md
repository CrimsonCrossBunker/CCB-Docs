---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.magic-spells-enchantments
title: 'Legacy migration draft: magic spells enchantments'
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
- doc/JSON/MAGIC.md
- src/magic.cpp
- src/magic_enchantment.cpp
- src/magic_type.cpp
- data/json/enchantments.json
- tests/magic_spell_test.cpp
source_symbols:
- spell_type::load
- enchantment::load
- magic_type::load
- spell_migration::load
source_queries: []
source_fingerprint: 05865897c5c912a033dde17275cb850056b9b8ce3a46b2917abea7071cf484bf
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 88cd03f69419899b72d03e4c14bad38b4bf22f52f45571dbcfc140ddd2178827
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LYHGLYTX, Standing-Storm, LunaGlaze, thaelina; accepted inventory identities
  only. Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/magic-spells-enchantments/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/magic-spells-enchantments/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/magic-spells-enchantments/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/magic-spells-enchantments/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/MAGIC.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/MAGIC.md
- path: src/magic.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/magic.cpp
- path: src/magic_enchantment.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/magic_enchantment.cpp
- path: src/magic_type.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/magic_type.cpp
- path: data/json/enchantments.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/enchantments.json
- path: tests/magic_spell_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/magic_spell_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.magic-spells-enchantments%29%3A+&body=Document+ID%3A+json.magic-spells-enchantments%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: magic spells enchantments

This is the migration draft page for `json.magic-spells-enchantments`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.magic-spells-enchantments`
- Target: `reference/json/magic-spells-enchantments.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/magic-spells-enchantments/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.magic-spells-enchantments | doc/JSON/MAGIC.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB Magic, Spell, and Enchantment contracts

This family includes `SPELL`, `magic_type`, `enchantment`, and inline `fake_spell` values used by
other objects. They share some IDs and conditions but have different lifecycles: spells are cast,
magic types provide system defaults, and enchantments are continuously evaluated against an owner
or carrier.

### Minimal spell skeleton

```jsonc
{
  "type": "SPELL",
  "id": "spell_ccb_example",
  "name": "Example pulse",
  "description": "A documentation-only spell.",
  "effect": "attack",
  "shape": "blast",
  "valid_targets": [ "hostile" ],
  "min_damage": 1,
  "damage_increment": 1,
  "max_damage": 5,
  "min_range": 3,
  "max_range": 3,
  "energy_source": "MANA",
  "base_energy_cost": 10,
  "base_casting_time": 100
}
```

Current `spell_type::load` requires `name`, `description`, `effect`, `shape`, and
`valid_targets`. Effects and shapes must exist in native registries. Damage, range, AoE, duration,
pierce, accuracy, energy, and casting time commonly use min, increment, and max values. Expressions
and units come from the owning reader and are not uniformly plain integers.

`caster_condition`, `target_condition`, target species or monster IDs, body parts, and flags jointly
limit valid targets. `extra_effects` or `fake_spell` values chain spells, and consistency checks
detect cycles. WONDER, permanent summons, vitamin energy, touch versus no-hands, and formula
parameters also have specialized checks.

### Magic types, learning, and channels

A `magic_type` can centralize energy, level or XP and failure formulas, cannot-cast flags, failure
cost, and failure EOCs. Level and XP formulas must be paired and have the expected argument counts.
A spell can override magic-type values and can be learned through books, professions or NPCs,
`learn_spells`, and other current entry points.

A channeled spell needs maximum turns, a channel spell, and an end spell. Cover cancellation,
movement, damage, resource exhaustion, interrupt behavior, per-turn energy, and save boundaries.
Multiple projectiles and repeated or random extra spells need performance and recursion review.

### Enchantments

An enchantment may use a named ID or be inline when its caller can supply a stable inline ID. `has`
and `condition` select HELD, WIELD, or WORN and ACTIVE, INACTIVE, ALWAYS, or a dialogue condition.
`values`, skills, custom values, encumbrance, and melee or incoming damage support add and multiply
forms. Mutations, effects, body-part changes, special vision, emitters, hit effects, and intermittent
spells each have separate semantics.

Characters, monsters, and vehicles process only the subsets their implementations consider
relevant. A loadable field is not proof that every carrier applies it; inspect
`is_monster_relevant`, `is_vehicle_relevant`, and call sites.

### Validation

Run the formatter, `make -j2 json-check`, `--check-mods` for the real Mod set, and relevant filters
from `magic_spell_test`, `magic_spell_effect_test`, and `enchantments_test`. Cover level boundaries,
failure and resources, targets and shapes, extra-effect cycles, channel interruption, enchantment
activation, add/multiply ordering, and save reload. Test player, NPC, monster, vehicle, and inline
carriers separately; profile frequent intermittent or area spells.

## History and attribution

Accepted inventory contributors: LYHGLYTX, Standing-Storm, LunaGlaze, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `05865897c5c912a033dde17275cb850056b9b8ce3a46b2917abea7071cf484bf`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/MAGIC.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/MAGIC.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/MAGIC.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
