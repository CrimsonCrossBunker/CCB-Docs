---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.proficiencies-index
title: Proficiency direct-definition index
language: en
status: draft
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
- doc/JSON/PROFICIENCY_LIST.md
- src/proficiency.cpp
- data/json/proficiencies/misc.json
- data/json/proficiencies/proficiency_categories.json
- data/mods/Magiclysm/proficiencies.json
source_symbols:
- proficiency::load
- proficiency_category::load
source_queries: []
source_fingerprint: 73dd5825970a152d2af8ae47a76c3fa9ae8e57cef9ffaa47ec9b70740fdd2395
authority: api-contract
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 0eeaff66ac726d8e2883b7b3fe9cbeac414ae62fe2d74426b75697299a9bb6ca
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: legacy-generated-reference-v1
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/generated/proficiencies/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/generated/proficiencies/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/generated/proficiencies/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/generated/proficiencies/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/JSON/PROFICIENCY_LIST.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/PROFICIENCY_LIST.md
- path: src/proficiency.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/proficiency.cpp
- path: data/json/proficiencies/misc.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/proficiencies/misc.json
- path: data/json/proficiencies/proficiency_categories.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/proficiencies/proficiency_categories.json
- path: data/mods/Magiclysm/proficiencies.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/mods/Magiclysm/proficiencies.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.proficiencies-index%29%3A+&body=Document+ID%3A+json.proficiencies-index%0ALanguage%3A+en%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Proficiency direct-definition index

This is the migration draft page for `json.proficiencies-index`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.proficiencies-index`
- Target: `reference/json/generated/proficiencies.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/generated/proficiencies/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.proficiencies-index | doc/JSON/PROFICIENCY_LIST.md | generated_reference | stubbed | b1ee97987589450da70f30ee2feed12c9d18f479 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Generated scope and evidence

The pinned inputs contain **50** proficiency objects and **21** categories. Only direct JSON fields are listed. Other mods, resolved inheritance, and recipe use sites are outside this generator, so the index is explicitly **partial**.

### Categories

| ID | name | description |
| --- | --- | --- |
| prof_alchemy | Alchemy | Proficiencies for working with the elements and transforming substances. |
| prof_archery | Archery | Proficiencies for all things bow and arrows.  Includes knowledge and experience of making and modifying bows, as well as archery form and posture. |
| prof_athletics | Athletics | Proficiencies for various athletic activities. |
| prof_butchering | Butchering | Proficiencies for carving and proper dressing of meat and skin of animals. |
| prof_chem | Applied Science | Proficiencies for scientific understanding and working with certain chemicals and substances. |
| prof_combat | Weapons Proficiencies | Proficiencies for various weapons. |
| prof_devices | Device Manipulation | Proficiencies for lockpicking, cracking safes, and general tinkering. |
| prof_druidic_shifting | Shapeshifting | Proficiencies for involving druidic transformation into the forms of animals. |
| prof_electronic | Electronics | Proficiencies for building and maintaining electronics and powered devices. |
| prof_firstaid | Health Care | Proficiencies for treating injuries and general health care knowledge. |
| prof_food | Food Handling | Proficiencies for cooking and food preparation, as well as experience with food handling tools. |
| prof_gunmaking | Projectile Weaponry | Proficiencies for creating and modifying projectile weapons. |
| prof_magic_casting | Spellcraft | Proficiencies that help with casting of magical spells. |
| prof_mechanic | Mechanics | Proficiencies for building and maintaining vehicles, engines, and similar equipment. |
| prof_misc_craft | Miscellaneous Crafts | Proficiencies for various domain-specific crafts. |
| prof_smithing | Metalworking | Proficiencies for welding, casting and shaping metal. |
| prof_survival | Wilderness | Proficiencies for surviving out in the wild. |
| prof_tailoring | Fabrics and Tailoring | Proficiencies for sewing, binding and mending fabrics and clothing materials. |
| prof_vehicles | Vehicles | Proficiencies for driving, piloting, and general vehicle operations. |
| prof_weakpoint | Weakpoint | Proficiencies that help target weak points on specific creatures. |
| prof_woodworking | Woodworking | Proficiencies for creating and modifying wood-based crafts. |

### Proficiencies

| ID | name | category | time_to_learn | required_proficiencies |
| --- | --- | --- | --- | --- |
| prof_alchemy | Alchemy | prof_alchemy | 8 h | — |
| prof_almetallurgy | Almetallurgy | prof_alchemy | 4 h | ["prof_alchemy", "prof_metalworking"] |
| prof_appliance_repair | General Appliance Repair | prof_mechanic | 8 h | — |
| prof_basketweaving | Basketweaving | prof_misc_craft | 6 h | — |
| prof_botanical_enchantment | Mystic Horticulture | prof_alchemy | 10 h | — |
| prof_bowyery | Bowyery | prof_archery | 10 h | — |
| prof_carving | Carving | prof_survival | 10 h | — |
| prof_druid_basis_of_transformation | Basis of Druidic Transformation | prof_druidic_shifting | 1 h | — |
| prof_druid_transformation_bear | Form Mastery (Forest King) | prof_druidic_shifting | 16 h | ["prof_druid_basis_of_transformation"] |
| prof_druid_transformation_cougar | Form Mastery (Stalking Hunter) | prof_druidic_shifting | 16 h | ["prof_druid_basis_of_transformation"] |
| prof_druid_transformation_deer | Form Mastery (Swift Runner) | prof_druidic_shifting | 16 h | ["prof_druid_basis_of_transformation"] |
| prof_druid_transformation_raven | Form Mastery (Soaring Wings) | prof_druidic_shifting | 16 h | ["prof_druid_basis_of_transformation"] |
| prof_fletching | Fletching | prof_archery | 8 h | — |
| prof_gem_setting | Gem Setting | prof_misc_craft | 10 h | ["prof_fine_metalsmithing", "prof_redsmithing"] |
| prof_glassblowing | Glassblowing | prof_misc_craft | 8 h | — |
| prof_golemancy_basic | Basic Golemancy | prof_alchemy | 4 h | — |
| prof_handloading | Handloading | prof_gunmaking | 8 h | — |
| prof_knapping | Basic Knapping | prof_survival | 8 h | — |
| prof_knapping_speed | Speed Knapping | prof_survival | 12 h | ["prof_knapping"] |
| prof_leatherworking_dragon | Dragon leather working | prof_tailoring | 6 h | ["prof_leatherworking"] |
| prof_magic_channel_apprentice | Apprentice Channeling | prof_magic_casting | 16 h | ["prof_magic_channel_beginner"] |
| prof_magic_channel_beginner | Novice Channeling | prof_magic_casting | 8 h | — |
| prof_magic_channel_master | Master Channeling | prof_magic_casting | 32 h | ["prof_magic_channel_apprentice"] |
| prof_magic_conveyance_apprentice | Apprentice Conveyance | prof_magic_casting | 16 h | ["prof_magic_conveyance_beginner"] |
| prof_magic_conveyance_beginner | Novice Conveyance | prof_magic_casting | 8 h | — |
| prof_magic_conveyance_master | Master Conveyance | prof_magic_casting | 32 h | ["prof_magic_conveyance_apprentice"] |
| prof_magic_enervation_apprentice | Apprentice Enervation | prof_magic_casting | 16 h | ["prof_magic_enhancement_beginner"] |
| prof_magic_enervation_beginner | Novice Enervation | prof_magic_casting | 8 h | — |
| prof_magic_enervation_master | Master Enervation | prof_magic_casting | 32 h | ["prof_magic_enhancement_apprentice"] |
| prof_magic_enhancement_apprentice | Apprentice Enhancement | prof_magic_casting | 16 h | ["prof_magic_enhancement_beginner"] |
| prof_magic_enhancement_beginner | Novice Enhancement | prof_magic_casting | 8 h | — |
| prof_magic_enhancement_master | Master Enhancement | prof_magic_casting | 32 h | ["prof_magic_enhancement_apprentice"] |
| prof_magic_evocation_apprentice | Apprentice Evocation | prof_magic_casting | 16 h | ["prof_magic_evocation_beginner"] |
| prof_magic_evocation_beginner | Novice Evocation | prof_magic_casting | 8 h | — |
| prof_magic_evocation_master | Master Evocation | prof_magic_casting | 32 h | ["prof_magic_evocation_apprentice"] |
| prof_magic_restoration_apprentice | Apprentice Restoration | prof_magic_casting | 16 h | ["prof_magic_conveyance_beginner"] |
| prof_magic_restoration_beginner | Novice Restoration | prof_magic_casting | 8 h | — |
| prof_magic_restoration_master | Master Restoration | prof_magic_casting | 32 h | ["prof_magic_conveyance_apprentice"] |
| prof_magic_summon_apprentice | Apprentice Conjuration | prof_magic_casting | 16 h | ["prof_magic_summon_beginner"] |
| prof_magic_summon_beginner | Novice Conjuration | prof_magic_casting | 8 h | — |
| prof_magic_summon_master | Master Conjuration | prof_magic_casting | 32 h | ["prof_magic_summon_apprentice"] |
| prof_magic_transformation_apprentice | Apprentice Transformation | prof_magic_casting | 16 h | ["prof_magic_conveyance_beginner"] |
| prof_magic_transformation_beginner | Novice Transformation | prof_magic_casting | 8 h | — |
| prof_magic_transformation_master | Master Transformation | prof_magic_casting | 32 h | ["prof_magic_conveyance_apprentice"] |
| prof_plasticworking | Plastic Working | prof_misc_craft | 6 h | — |
| prof_plumbing | Plumbing | prof_mechanic | 8 h | — |
| prof_pottery | Pottery | prof_misc_craft | 6 h | — |
| prof_pottery_glazing | Pottery Glazing | prof_misc_craft | 5 h | — |
| prof_scaleworking_dragon | Dragon scale working | prof_tailoring | 12 h | ["prof_leatherworking_dragon"] |
| prof_weapon_enchanting | Enchanting | prof_alchemy | 12 h | — |

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`; the aggregate source fingerprint is `73dd5825970a152d2af8ae47a76c3fa9ae8e57cef9ffaa47ec9b70740fdd2395`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/PROFICIENCY_LIST.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/PROFICIENCY_LIST.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/PROFICIENCY_LIST.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
