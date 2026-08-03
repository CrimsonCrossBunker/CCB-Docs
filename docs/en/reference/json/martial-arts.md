---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.martial-arts
title: 'Legacy migration draft: martial arts'
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
- doc/JSON/MARTIALART_JSON.md
- src/martialarts.cpp
- src/martialarts.h
- data/json/martialarts.json
- tests/martial_art_test.cpp
source_symbols:
- martialart::load
- ma_technique::load
- ma_buff::load
- attack_vector::load
source_queries: []
source_fingerprint: 2dae37d80a7a5118d1ba3e4e39e6e061160fc23beaa6e745832bb491a88d3d62
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: d1fae3685a2aac9b2884292d435301ccf5b8e193c742ce2aca5302580fe166e5
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/martial-arts/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/martial-arts/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/martial-arts/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/martial-arts/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/JSON/MARTIALART_JSON.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/MARTIALART_JSON.md
- path: src/martialarts.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/martialarts.cpp
- path: src/martialarts.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/martialarts.h
- path: data/json/martialarts.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/martialarts.json
- path: tests/martial_art_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tests/martial_art_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.martial-arts%29%3A+&body=Document+ID%3A+json.martial-arts%0ALanguage%3A+en%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: martial arts

This is the migration draft page for `json.martial-arts`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.martial-arts`
- Target: `reference/json/martial-arts.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/martial-arts/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.martial-arts | doc/JSON/MARTIALART_JSON.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB Martial Arts object graph

Martial arts are not one JSON object. The runtime separately registers `attack_vector`,
`weapon_category`, `technique`, `martial_art`, and buffs. A style references techniques and
weapons or categories, then applies buffs or EOCs at combat events.

### Styles and techniques

A `martial_art` needs a stable `id`, `name`, `description`, and `initiate`. `autolearn` contains
skill and level pairs; `primary_skill`, `learn_difficulty`, `teachable`, `weapons`, and
`weapon_category` govern learning and eligible weapons. Validate `strictly_melee` and related
limits through both UI and actual selection logic.

A `technique` currently requires at least `name` and normally provides player/NPC messages and
`attack_vectors`. Critical, counter, disarm, knockback, AoE, repeat, condition, requirement, and
bonus data jointly determine candidacy and execution. Consistency checking reports an ordinary
attack technique without an attack vector; defensive, dummy, grab-break, and miss-recovery types
are exceptions.

### Attack vectors, requirements, and buffs

An `attack_vector` describes weapon or limb use, contact area, limb HP, encumbrance, armor bonus,
and required or forbidden limb flags. It is not just an animation label: selected limbs and contact
affect eligibility, damage, and tests.

A style can attach buffs and inline EOCs at static, move, pause, hit, attack, dodge, block, get-hit,
miss, critical, and kill events. Buffs define duration, stacks, persistence, dodge or block, bonuses,
and requirements. Each event has different actors, weapons, targets, and frequency; an EOC must not
assume a beta talker always exists.

Requirements combine skills, weapon damage, weapon categories, buffs, and character flags. Holding
an allowed weapon does not prove a technique passes limb, condition, ammo, range, or cooldown gates.

### Design and validation

1. Start from the closest first-party style graph and preserve ID prefixes and translated messages.
2. Run the formatter, `make -j2 json-check`, and `--check-mods` for the actual Mod set.
3. Run `martial_art_test` for weapon categories, limb substitution, HP, encumbrance, conditions,
   sweep, stun, and knockback.
4. In game, cover unarmed use, every weapon class, injury and high encumbrance, NPCs, criticals,
   counters, and every buff or EOC event.
5. Record DPS, hit and defense changes, stacks, and trigger frequency. Loading does not disprove
   infinite stacking or forced loops.

Legacy bonus strings and flag lists can drift. Use current loaders and consistency checks for exact
enums and bounds.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`; the aggregate source fingerprint is `2dae37d80a7a5118d1ba3e4e39e6e061160fc23beaa6e745832bb491a88d3d62`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/MARTIALART_JSON.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/MARTIALART_JSON.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/MARTIALART_JSON.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
