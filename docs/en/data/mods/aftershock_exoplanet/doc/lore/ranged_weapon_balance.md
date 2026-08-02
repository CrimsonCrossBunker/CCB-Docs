---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: mods.aftershock-exoplanet.balance.ranged-weapons
title: Aftershock ranged-weapon balance input index
language: en
status: active
doc_type: generated-api
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
- data/mods/aftershock_exoplanet/doc/lore/ranged_weapon_balance.md
- data/mods/aftershock_exoplanet/modinfo.json
- data/mods/aftershock_exoplanet/items/weapons.json
- data/mods/aftershock_exoplanet/itemgroups/weapons/energy_gun_groups.json
- data/mods/aftershock_exoplanet/itemgroups/weapons/balistic_gun_groups.json
source_symbols: []
source_queries: []
source_fingerprint: c6ecee98014d5659798ef3185754b5e43308e35dd06ca9ef9275f76093217f53
authority: api-contract
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 2a4a6cf756800edee7da3a6d83e488edf8b17c083a0ca2348a8528b8881e7b54
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: Mihály Verhás, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: legacy-generated-reference-v1
deprecated: false
deprecation_replacement: null
risk_group: mods
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/data/mods/aftershock_exoplanet/doc/lore/ranged_weapon_balance/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/data/mods/aftershock_exoplanet/doc/lore/ranged_weapon_balance/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/data/mods/aftershock_exoplanet/doc/lore/ranged_weapon_balance/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/data/mods/aftershock_exoplanet/doc/lore/ranged_weapon_balance/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: data/mods/aftershock_exoplanet/doc/lore/ranged_weapon_balance.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/mods/aftershock_exoplanet/doc/lore/ranged_weapon_balance.md
- path: data/mods/aftershock_exoplanet/modinfo.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/mods/aftershock_exoplanet/modinfo.json
- path: data/mods/aftershock_exoplanet/items/weapons.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/mods/aftershock_exoplanet/items/weapons.json
- path: data/mods/aftershock_exoplanet/itemgroups/weapons/energy_gun_groups.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/mods/aftershock_exoplanet/itemgroups/weapons/energy_gun_groups.json
- path: data/mods/aftershock_exoplanet/itemgroups/weapons/balistic_gun_groups.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/mods/aftershock_exoplanet/itemgroups/weapons/balistic_gun_groups.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28mods.aftershock-exoplanet.balance.ranged-weapons%29%3A+&body=Document+ID%3A+mods.aftershock-exoplanet.balance.ranged-weapons%0ALanguage%3A+en%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Aftershock ranged-weapon balance input index

This is the migration draft page for `mods.aftershock-exoplanet.balance.ranged-weapons`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `mods.aftershock-exoplanet.balance.ranged-weapons`
- Target: `data/mods/aftershock_exoplanet/doc/lore/ranged_weapon_balance.md`
- Replacement: —
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| mods.aftershock-exoplanet.balance.ranged-weapons | data/mods/aftershock_exoplanet/doc/lore/ranged_weapon_balance.md | generated_reference | stubbed | — | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Generated scope and evidence

The pinned inputs contain **18** direct `ITEM` definitions and **37** `item_group` objects. The table does not resolve `copy-from`, normalize units, or derive final DPS after ammunition, attachments, skills, and runtime formulas. It is a **partial balance input index**, not a balance result.

### Direct item definitions

| ID | name | subtypes | skill | range | dispersion | damage | copy-from |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TANK | Tankbot Main Gun | ["GUN"] | launcher | — | 60 | — | — |
| afs_bio_whip_weapon | monofilament whip | — | — | — | — | — | — |
| afs_bionic_rocket | deployed grenade launcher | ["GUN"] | launcher | — | 290 | — | — |
| afs_energy_saber_off | CE-4 "The Claw" (Non-Lethal) | ["TOOL"] | — | — | — | — | — |
| afs_energy_saber_on | CE-4 "The Claw" (Lethal) | ["TOOL"] | — | — | — | — | afs_energy_saber_off |
| afs_freeze_gauntlet | psychrophile handling gloves | ["ARMOR", "ARTIFACT"] | — | — | — | — | — |
| afs_hardlight_longbow | Alien lune | ["GUN"] | archery | 30 | 80 | {"amount": 50, "armor_penetration": 15, "damage_type": "heat"} | — |
| afs_hydraulic_gauntlet | hydraulic gauntlet | ["ARMOR"] | — | — | — | — | — |
| afs_titanium_bat | titanium bat | — | — | — | — | — | bat_metal |
| afs_toxic_knife | neurotoxic knife | ["TOOL"] | — | — | — | — | — |
| aza_sword | Aztlani hunting sword | ["TOOL"] | — | — | — | — | — |
| azabow_off | Aztlani bow | ["ARMOR", "GUN"] | — | 25 | 1000 | {"amount": 17, "damage_type": "stab"} | compbow |
| azabow_on | Aztlani bow (active) | ["GUN"] | — | — | — | — | azabow_off |
| ceramic_knife | bodyguard knife | ["TOOL"] | — | — | — | — | — |
| golf_club | golf club | — | — | — | — | — | golf_club |
| scrapbow | salvage bow | ["ARMOR", "GUN"] | — | 14 | 850 | {"amount": 12, "damage_type": "stab"} | compositebow |
| scrapcrossbow | salvage crossbow | ["GUN"] | rifle | 22 | 325 | {"amount": 16, "damage_type": "stab"} | — |
| trident | trident | — | — | — | — | — | — |

### Item groups

| ID | subtype | items count | entries count | ammo | magazine |
| --- | --- | --- | --- | --- | --- |
| afs_any_ballistic_ammo | distribution | 3 | 0 | — | — |
| afs_any_ballistic_gun | distribution | 2 | 0 | — | — |
| afs_any_ballistic_h_ammo | distribution | 3 | 0 | 100 | 100 |
| afs_any_ballistic_h_gun | distribution | 2 | 0 | 100 | 100 |
| afs_any_ballistic_h_mag | distribution | 2 | 0 | 100 | 100 |
| afs_any_ballistic_m_ammo | distribution | 6 | 0 | 100 | 100 |
| afs_any_ballistic_m_gun | distribution | 8 | 0 | 100 | 100 |
| afs_any_ballistic_m_mag | distribution | 3 | 0 | 100 | 100 |
| afs_any_ballistic_mag | distribution | 3 | 0 | — | — |
| afs_any_ballistic_s_ammo | distribution | 3 | 0 | 100 | 100 |
| afs_any_ballistic_s_gun | distribution | 2 | 0 | 100 | 100 |
| afs_any_ballistic_s_mag | distribution | 2 | 0 | 100 | 100 |
| afs_any_civilian_ballistic_ammo | distribution | 3 | 0 | — | — |
| afs_any_energy_gun | distribution | 3 | 0 | — | — |
| afs_any_energy_mag | distribution | 3 | 0 | — | — |
| afs_any_laser_gun | distribution | 2 | 0 | — | — |
| afs_any_laser_h_gun | distribution | 2 | 0 | 100 | 100 |
| afs_any_laser_mag | distribution | 4 | 0 | 100 | — |
| afs_any_laser_s_gun | distribution | 3 | 0 | 100 | 100 |
| afs_any_plasma_gun | distribution | 2 | 0 | 100 | 100 |
| afs_any_plasma_mag | distribution | 2 | 0 | 100 | — |
| afs_any_voltaic_gun | distribution | 3 | 0 | 100 | 100 |
| afs_any_voltaic_mag | distribution | 1 | 0 | 100 | — |
| afs_civilian_ballistic_gun | distribution | 2 | 0 | — | — |
| afs_civilian_ballistic_h_ammo | distribution | 1 | 0 | 100 | 100 |
| afs_civilian_ballistic_m_ammo | distribution | 5 | 0 | 100 | 100 |
| afs_civilian_ballistic_m_gun | distribution | 4 | 0 | 100 | 100 |
| afs_civilian_ballistic_s_ammo | distribution | 2 | 0 | 100 | 100 |
| afs_civilian_ballistic_s_gun | distribution | 2 | 0 | 100 | 100 |
| afs_civilian_energy_gun | distribution | 2 | 0 | — | — |
| afs_civilian_energy_mag | distribution | 2 | 0 | — | — |
| afs_civilian_laser_gun | distribution | 2 | 0 | 100 | 100 |
| afs_civilian_laser_mag | distribution | 2 | 0 | 100 | — |
| afs_civilian_voltaic_gun | distribution | 1 | 0 | 100 | 100 |
| afs_explosive_pumped_laser_s | collection | 0 | 2 | — | — |
| afs_shotgun_gunmod | distribution | 1 | 0 | — | — |
| afs_swat_emp | distribution | 1 | 0 | — | — |

## History and attribution

Accepted inventory contributors: Mihály Verhás, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `c6ecee98014d5659798ef3185754b5e43308e35dd06ca9ef9275f76093217f53`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`data/mods/aftershock_exoplanet/doc/lore/ranged_weapon_balance.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/mods/aftershock_exoplanet/doc/lore/ranged_weapon_balance.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/data/mods/aftershock_exoplanet/doc/lore/ranged_weapon_balance.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
