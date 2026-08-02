---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.flags
title: JSON flag direct-definition index
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
- doc/JSON/JSON_FLAGS.md
- src/flag.cpp
- src/flag.h
- data/json/flags.json
- tools/flagdoc/flagdoc.pl
- tools/flagdoc/sections.conf
source_symbols:
- json_flag::load
source_queries: []
source_fingerprint: 3cab8da23ea482c450b9d0f6f2d2f5fb692e10b827e8f0ead7d3f361f1db6001
authority: api-contract
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 6d567e079a34e8d7c27978dba23dbf8a573285ef3038d186afa134e959badb00
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LunaGlaze, LYHGLYTX, Standing-Storm, Mihály Verhás, zihanZheng, Tektolnes,
  RenechCDDA, dumb-kevin, evilbananas, Anton Simakov, thaelina; accepted inventory identities only. Source
  paths and Git history remain authoritative.'
example_validation_ids: []
api_version: legacy-generated-reference-v1
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
search:
  exclude: true
---

# JSON flag direct-definition index

This is the migration draft page for `json.flags`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.flags`
- Target: `reference/json/generated/flags.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/generated/flags/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.flags | doc/JSON/JSON_FLAGS.md | generated_reference | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Generated scope and evidence

This table parses `data/json/flags.json` at the pinned commit and indexes **648** direct `json_flag` definitions. A field is shown only when it exists in JSON. C++-implicit flags, use sites, and resolved behaviour are not inferred, so this is a **partial direct-definition index**, not a complete Schema and not a replacement for `json_flag::load`.

| ID | info | restriction | inherit | conflicts |
| --- | --- | --- | --- | --- |
| ABLATIVE_CHAINMAIL_ARMS | You can use this armor &lt;info&gt;with chainmail&lt;/info&gt; without encumbrance penalty. | Item must be a chainmail compatible armor piece | — | — |
| ABLATIVE_CHAINMAIL_ELBOWS | You can use this armor &lt;info&gt;with chainmail&lt;/info&gt; without encumbrance penalty. | Item must be a chainmail compatible armor piece | — | — |
| ABLATIVE_CHAINMAIL_KNEES | You can use this armor &lt;info&gt;with chainmail&lt;/info&gt; without encumbrance penalty. | Item must be a chainmail compatible armor piece | — | — |
| ABLATIVE_CHAINMAIL_LEGS | You can use this armor &lt;info&gt;with chainmail&lt;/info&gt; without encumbrance penalty. | Item must be a chainmail compatible armor piece | — | — |
| ABLATIVE_CHAINMAIL_TORSO | You can use this armor &lt;info&gt;with chainmail&lt;/info&gt; without encumbrance penalty. | Item must be a chainmail compatible armor piece | — | — |
| ABLATIVE_HELMET | This will hook to a &lt;info&gt;Hub 01 proprietary&lt;/info&gt; helmet connector. | Item must be an armored helmet | — | — |
| ABLATIVE_LARGE | This plate will fit in &lt;info&gt;large&lt;/info&gt; armor pockets. | Item must be a large ablative plate | — | — |
| ABLATIVE_MANTLE | This will hook to a &lt;info&gt;Hub 01 proprietary&lt;/info&gt; mantle connector. | Item must be an armored mantle | — | — |
| ABLATIVE_MEDIUM | This plate will fit in &lt;info&gt;medium&lt;/info&gt; armor pockets. | Item must be a medium ablative plate | — | — |
| ABLATIVE_SKIRT | This will hook to a &lt;info&gt;Hub 01 proprietary&lt;/info&gt; skirt connector. | Item must be an armored skirt | — | — |
| ACID | — | — | — | — |
| ACID_IMMUNE | This gear &lt;good&gt;completely protects&lt;/good&gt; you from &lt;info&gt;acid damage&lt;/info&gt;. | — | — | — |
| ACTIVATE_ON_PLACE | This item will be activated when it is placed in mapgen. | — | — | — |
| ACTIVE_CLOAKING | This gear has &lt;info&gt;cloaking tech&lt;/info&gt; that will &lt;good&gt;make you invisible&lt;/good&gt; when active, at the cost of &lt;info&gt;power from a UPS&lt;/info&gt;. | — | — | — |
| ACT_IN_FIRE | — | — | — | — |
| ACT_ON_RANGED_HIT | — | — | — | — |
| AFS_CS_ARMORY_CARD | ID card granting access to the crashing ship's armory. | — | — | — |
| AFS_CS_EXOBAY_CARD | ID card granting access to the crashing ship's exobay. | — | — | — |
| AFS_CS_LOCKER_CARD | ID card granting access to the crashing ship's locker room. | — | — | — |
| ALARMCLOCK | This gear has an &lt;info&gt;alarm clock&lt;/info&gt; feature. | — | — | — |
| ALCOHOL | — | — | — | — |
| ALCOHOL_STRONG | — | — | — | — |
| ALCOHOL_WEAK | — | — | — | — |
| ALLERGEN_BREAD | — | — | — | — |
| ALLERGEN_CHEESE | — | — | — | — |
| ALLERGEN_DRIED_VEGETABLE | — | — | — | — |
| ALLERGEN_EGG | — | — | — | — |
| ALLERGEN_FRUIT | — | — | — | — |
| ALLERGEN_JUNK | — | — | — | — |
| ALLERGEN_MEAT | — | — | — | — |
| ALLERGEN_MILK | — | — | — | — |
| ALLERGEN_NUT | — | — | — | — |
| ALLERGEN_VEGGY | — | — | — | — |
| ALLERGEN_WHEAT | — | — | — | — |
| ALLERGEN_WOOL | — | — | — | — |
| ALLOWS_BODY_BLOCK | This item &lt;info&gt;won't prevent you from blocking with your body, such as arms or legs&lt;/info&gt; when wielded as a weapon. | — | — | — |
| ALLOWS_GASTROPOD_FOOT | — | — | — | — |
| ALLOWS_LEG_TENTACLES | — | — | — | — |
| ALLOWS_NATURAL_ATTACKS | This clothing won't hinder special attacks that involve &lt;info&gt;mutated or cybernetic anatomy&lt;/info&gt;. | — | — | — |
| ALLOWS_REMOTE_USE | This item can be activated or reloaded from an adjacent tile without picking it up. | — | — | — |
| ALLOWS_TAIL | — | — | — | — |
| ALLOWS_TALONS | — | — | — | — |
| ALL_TERRAIN_NAVIGATION | Allows movement over rough and sharp terrain without penalty. | — | — | — |
| ALWAYS_AIMED | This gun is &lt;good&gt;always fully aimed&lt;/good&gt;. | — | — | — |
| ALWAYS_TWOHAND | &lt;bad&gt;You must&lt;/bad&gt; have two free hands to wield this item. | — | — | — |
| ANDURIL_AR_CARD | You could probably use this to get into a secure Anduril Industries facility. | — | — | — |
| ANIMALDISCORD | The character is disliked by natural animals. | — | — | — |
| ANIMALDISCORD2 | The character is intensely disliked by natural animals. | — | — | — |
| ANIMALEMPATH | The character is liked by natural animals. | — | — | — |
| ANIMALEMPATH2 | The character is intensely liked by natural animals. | — | — | — |
| ANIMAL_PRODUCT | — | — | — | — |
| APPLIANCE | — | — | — | — |
| ARM_PROSTHETIC | — | — | — | — |
| AURA | This is in your &lt;info&gt;outer aura&lt;/info&gt;. | — | — | — |
| BACKBLAST | — | — | — | — |
| BAD_TASTE | This food is &lt;bad&gt;unappetizing&lt;/bad&gt; in a way that &lt;bad&gt;can't be covered up by most cooking&lt;/bad&gt;. | — | — | — |
| BANK_NETWORKED | — | — | — | — |
| BANK_NOTE_SHAPED | — | Item must be shaped like a bank note | — | — |
| BANK_NOTE_STRAP_SHAPED | — | Item must be shaped like a bank note strap | — | — |
| BAROMETER | This gear is equipped with an accurate barometer (which is used to measure atmospheric pressure). | — | — | — |
| BARRICADABLE_DOOR | — | — | — | — |
| BARRICADABLE_DOOR_DAMAGED | — | — | — | — |
| BARRICADABLE_DOOR_REINFORCED | — | — | — | — |
| BARRICADABLE_DOOR_REINFORCED_DAMAGED | — | — | — | — |
| BARRICADABLE_WINDOW | — | — | — | — |
| BARRICADABLE_WINDOW_CURTAINS | — | — | — | — |
| BASH_IMMUNE | This gear &lt;good&gt;completely protects&lt;/good&gt; you from &lt;info&gt;bash damage&lt;/info&gt;. | — | — | — |
| BATTERY_HEAVY | This item fits in items that use tool batteries. | — | — | — |
| BATTERY_LIGHT | This item fits in items that use light batteries. | — | — | — |
| BATTERY_MEDIUM | This item fits in items that use medium batteries. | — | — | — |
| BATTERY_ULTRA_LIGHT | This item fits in items that use ultra-light batteries. | — | — | — |
| BELTED | This gear is &lt;info&gt;strapped&lt;/info&gt; onto you. | — | — | — |
| BELT_CLIP | This item can be &lt;info&gt;clipped onto a belt loop&lt;/info&gt; of the appropriate size. | Item must clip onto a belt loop | — | — |
| BIONIC_ARMOR_INTERFACE | This bionic can provide power to powered armor. | — | — | — |
| BIONIC_FAULTY | This bionic is &lt;bad&gt;faulty&lt;/bad&gt;. | — | — | — |
| BIONIC_FUEL_SOURCE | Contents of this item are used for fueling bionics. | — | — | — |
| BIONIC_GUN | — | — | — | — |
| BIONIC_INSTALLATION_DATA | This item &lt;info&gt;provides&lt;/info&gt; instructions and other required data for several bionics, allowing installation of them with &lt;good&gt;minimal failure chance&lt;/good&gt;. | — | — | — |
| BIONIC_NPC_USABLE | A &lt;good&gt;follower&lt;/good&gt; could &lt;info&gt;make use of this CBM&lt;/info&gt; if installed properly. | — | — | — |
| BIONIC_POWER_SOURCE | This bionic provides power. | — | — | — |
| BIONIC_TOGGLED | — | — | — | — |
| BIONIC_WEAPON | — | — | — | — |
| BIONIC_WEAPON_MELEE | — | — | — | — |
| BIO_IMMUNE | This gear &lt;good&gt;completely protects&lt;/good&gt; you from &lt;info&gt;biological damage&lt;/info&gt;. | — | — | — |
| BIPOD | — | — | — | — |
| BIRD | — | — | — | — |
| BLED | — | — | — | — |
| BLIND | This gear &lt;bad&gt;prevents&lt;/bad&gt; you from &lt;info&gt;seeing&lt;/info&gt; anything. | — | — | — |
| BLOCK_HUGE_ATTACKS | You are capable of blocking attacks from targets of any size | — | — | — |
| BLOCK_SUPERNATURAL_HEALING | — | — | — | — |
| BLOCK_WHILE_WORN | This item can be used to block attacks when worn. | — | — | — |
| BLOODFEEDER | — | — | — | — |
| BOLT_ACTION | This weapon requires you to manually pull and insert cartridge into the chamber using a turn-bolt, which &lt;bad&gt;takes additional time&lt;/bad&gt; and &lt;bad&gt;messes your aim&lt;/bad&gt;.  The penalty is decreased the more experienced with guns you are. | — | — | — |
| BOMB | — | — | — | — |
| BOOT_FINS | This item is attachable to commercial diving boots as fins. | Item must be some kind of fins | — | — |
| BOOT_FINS_CUSTOM | This item is attachable to custom diving boots as fins. | Item must be some kind of custom fins | — | — |
| BRASS_CATCHER | This gun mod catches ejected casings. | — | — | — |
| BULLET_IMMUNE | This gear &lt;good&gt;completely protects&lt;/good&gt; you from &lt;info&gt;bullet damage&lt;/info&gt;. | — | — | — |
| BURNOUT | — | — | — | — |
| BYPRODUCT | — | — | — | — |
| CABLE_SPOOL | — | — | — | — |
| CALORIES_INTAKE | This item enables you to keep track of calorie intake. | — | — | — |
| CALORIE_BURN | This item enables you to keep track of calorie consumption.  Includes CALORIES_INTAKE. | — | — | — |
| CAMERA_PRO | — | — | — | — |
| CANNIBAL | — | — | — | — |
| CANNIBALISM | — | — | — | — |
| CANNOT_ATTACK | — | — | — | — |
| CANNOT_CHANGE_TEMPERATURE | — | — | — | — |
| CANNOT_GAIN_EFFECTS | — | — | — | — |
| CANNOT_GAIN_WEARINESS | You have a seemingly inexhaustible supply of energy. | — | — | — |
| CANNOT_MOVE | — | — | — | — |
| CANNOT_TAKE_DAMAGE | — | — | — | — |
| CANNOT_USE_COMPUTERS | — | — | — | — |
| CANT_HEAL_EVERYONE | This med can't be used by everyone, it requires a special mutation. | — | — | — |
| CANT_WEAR | This armor can't be worn directly. | — | False | — |
| CAN_HAVE_CHARGES | — | — | — | — |
| CAN_USE_IN_DARK | This item can use all of its features in darkness. | — | — | — |
| CARNIVORE_OK | — | — | — | — |
| CASELESS_ROUNDS | Being caseless rounds, these &lt;bad&gt;cannot be disassembled or reloaded&lt;/bad&gt;. | — | — | — |
| CASING | — | — | — | — |
| CATTLE | — | — | — | — |
| CBM | This item is a Compact Bionic Module.  You'll need to &lt;info&gt;use specialized machinery&lt;/info&gt; or &lt;info&gt;ask a surgeon&lt;/info&gt; to install it into your body. | — | — | — |
| CHALLENGE | — | — | — | — |
| CHARGEDIM | — | — | — | — |
| CHIP | A paint chipper can be used to remove paint from this. | — | — | — |
| CHOKE | — | — | — | — |
| CITY_START | — | — | — | — |
| CLIMB_FLYING | You can ascend straight up even with no physical surface to climb on. | — | — | — |
| COIN_SHAPED | — | Item must be shaped like a coin | — | — |
| COLD | — | — | — | — |
| COLD_IMMUNE | This gear &lt;good&gt;completely protects&lt;/good&gt; you from &lt;info&gt;low temperatures&lt;/info&gt;. | — | — | — |
| COLLAPSED_STOCK | This items stock is collapsed it will be hard to shoot with. | — | — | — |
| COLLAPSE_CONTENTS | Contents are hidden by default in inventory view. | — | — | — |
| COLLAPSIBLE_STOCK | — | — | — | — |
| COLLAR | This clothing has a &lt;info&gt;wide collar&lt;/info&gt; that can keep your mouth warm if it is unencumbered. | — | — | — |
| COMBAT_TOGGLEABLE | This item is meant to be toggled during combat. | — | — | — |
| CONCENTRATE | — | — | — | — |
| CONDUCTIVE | — | — | — | — |
| CONSUMABLE | — | — | — | — |
| COOKED | — | — | — | — |
| COOP_CARD | Gives you access to the artisans workshop. | — | — | — |
| CORPSE | — | — | — | — |
| CORROSIVE | — | — | — | — |
| COSPLAY_COSTUME | This clothing is &lt;info&gt;cosplay costume&lt;/info&gt;. | — | — | ["COSPLAY_PROPS"] |
| COSPLAY_PROPS | This item is &lt;info&gt;cosplay prop&lt;/info&gt;. | — | — | ["COSPLAY_COSTUME"] |
| CRAFT_IN_DARKNESS | You can craft at 100% speed in any level of light. | — | — | — |
| CREDIT_CARD_SHAPED | — | Item must be shaped like a credit card | — | — |
| CRUTCHES | — | — | — | — |
| CRYOGENIC_ROT | This item &lt;info&gt;requires specialized cryogenic preservation&lt;/info&gt; and will &lt;bad&gt;spoil rapidly&lt;/bad&gt; even at subzero temperatures. | — | — | — |
| CUSTOM_EXPLOSION | — | — | — | — |
| CUT_HARVEST | — | — | — | — |
| CUT_IMMUNE | This gear &lt;good&gt;completely protects&lt;/good&gt; you from &lt;info&gt;cut damage&lt;/info&gt;. | — | — | — |
| CYLINDER_GRENADE | — | — | — | — |
| DANGEROUS | — | — | — | — |
| DEAF | This gear &lt;bad&gt;prevents&lt;/bad&gt; you from &lt;info&gt;hearing any sounds&lt;/info&gt;. | — | — | ["PARTIAL_DEAF"] |
| DEBUG_ONLY | This is not intended to be visible during normal gameplay.  &lt;bad&gt;Please file a bug report&lt;/bad&gt; unless you are seeing this in the debug menu. | — | — | — |
| DECAYS_IN_AIR | This will eventually &lt;bad&gt;go bad&lt;/bad&gt; if left in the open air too long. | — | — | — |
| DECAY_EXPOSED_ATMOSPHERE | If exposed to the atmosphere, it will &lt;bad&gt;start to go bad&lt;/bad&gt;. | — | — | — |
| DESTROY_ON_CHARGE_USE | — | — | — | — |
| DETERGENT | — | — | — | — |
| DIAMOND | This item has a &lt;good&gt;diamond coating&lt;/good&gt; improving its &lt;info&gt;cutting or piercing damage&lt;/info&gt;. | — | False | — |
| DIGGABLE | A hole can be dug here. | — | — | — |
| DIG_TOOL | While wielded, this item allows you to mine through rocks and other hard obstacles by moving into tiles with them.  Note that automatic mining option should be set to true for this to work. | — | — | — |
| DIMENSIONAL_ANCHOR | — | — | — | — |
| DIRTY | — | — | — | — |
| DISABLE_SIGHTS | — | — | — | — |
| DISCOUNT_VALUE_1 | — | — | — | — |
| DISCOUNT_VALUE_2 | — | — | — | — |
| DISCOUNT_VALUE_3 | — | — | — | — |
| DRACULIN_VENOM | — | — | — | — |
| DROP_ACTION_ONLY_IF_LIQUID | — | — | — | — |
| DURABLE_MELEE | As a weapon, this item is &lt;good&gt;well-made&lt;/good&gt; and will &lt;info&gt;withstand the punishment of combat&lt;/info&gt;. | — | — | ["FRAGILE_MELEE"] |
| EASY_CLEAN | This gun is made of &lt;info&gt;relatively simple parts&lt;/info&gt; which makes powder fouling &lt;good&gt;easier to clean&lt;/good&gt;. | — | — | — |
| EASY_DECONSTRUCT | — | — | — | — |
| EATEN_COLD | This tastes &lt;good&gt;better&lt;/good&gt; while &lt;color_light_cyan&gt;cold&lt;/color&gt;. | — | — | — |
| EATEN_HOT | This tastes &lt;good&gt;better&lt;/good&gt; while &lt;color_red&gt;hot&lt;/color&gt;. | — | — | — |
| EDIBLE_FROZEN | — | — | — | — |
| EFFECT_IMPEDING | — | — | — | — |
| EFFECT_LUA_ON_ADDED | — | — | — | — |
| EFFECT_LUA_ON_REMOVED | — | — | — | — |
| EFFECT_LUA_ON_TICK | — | — | — | — |
| ELECTRIC_IMMUNE | This gear &lt;good&gt;completely protects&lt;/good&gt; you from &lt;info&gt;electric discharges&lt;/info&gt;. | — | — | — |
| ELECTRONIC | — | — | — | — |
| EMP_IMMUNE | This gear &lt;good&gt;completely protects&lt;/good&gt; you from &lt;info&gt;EMP blasts&lt;/info&gt;. | — | — | — |
| ENCUMBRANCE_UPDATE | — | — | — | — |
| ENERGY_SHIELD | This piece of armor is an energy barrier and will break after absorbing a certain amount of damage. | — | — | — |
| ETHEREAL | You feel like you would keep all your items if you somehow became incorporeal. | — | — | — |
| ETHEREAL_ITEM | — | — | — | — |
| EXODII_STRING_DIMENSION_CARD | You could probably use this to open some lock. | — | — | — |
| EXO_ARM_PLATE | This is meant for exoskeleton arm plating. | — | False | — |
| EXO_BOOT_PLATE | This is meant for exoskeleton foot plating. | — | False | — |
| EXO_GLOVE_PLATE | This is meant for exoskeleton arm plating. | — | False | — |
| EXO_HELMET_GADGET | This is meant for helmet-specific gadgets. | — | False | — |
| EXO_HELMET_PLATE | This is meant for exoskeleton helmet plating. | — | False | — |
| EXO_LARGE | This is meant for a large exosuit hardpoint. | — | False | — |
| EXO_LARGE_GADGET | This is meant for large exosuit gadgets, larger than 5 L. | — | False | — |
| EXO_LEG_PLATE | This is meant for exoskeleton leg plating. | — | False | — |
| EXO_MEDIUM_GADGET | This is meant for medium exosuit gadgets, between 1 L and 5 L. | — | False | — |
| EXO_PSU | This is meant for an exosuit PSU hardpoint. | — | False | — |
| EXO_SMALL | This is meant for a small exosuit hardpoint. | — | False | — |
| EXO_SMALL_GADGET | This is meant for small exosuit gadgets, 1 L or less. | — | False | — |
| EXO_TORSO_PLATE | This is meant for exoskeleton torso plating. | — | False | — |
| EXO_UNDERLAYER | This is meant for exosuit underlayers. | — | False | — |
| EXTRA_EFFECTS_FIRST | — | — | — | — |
| EXTRA_PLATING | This item is wearable over some armors as an extra layer of plating. | Item must be some kind of strapped additional plating | — | — |
| E_COMBUSTION | — | — | — | — |
| E_COPIABLE | — | — | — | — |
| E_FILE_COLLECTION | — | — | — | — |
| E_FILE_DEVICE | — | — | — | — |
| E_FILE_DEVICE_UNREAD | — | — | — | — |
| E_STORABLE | — | — | — | — |
| E_STORABLE_EXCLUSIVE | — | — | — | — |
| FAKE_MILL | — | — | — | — |
| FAKE_SMOKE | — | — | — | — |
| FAULT_ON_COMPLETION | — | — | — | — |
| FELINE | — | — | — | — |
| FERTILIZER | — | — | — | — |
| FIELD_DRESS | — | — | — | — |
| FIELD_DRESS_FAILED | — | — | — | — |
| FILTHY | This item is &lt;bad&gt;filthy&lt;/bad&gt;. | — | — | — |
| FIN | This clothing has fins that &lt;good&gt;improve swimming speed&lt;/good&gt;, but &lt;bad&gt;reduce movement speed&lt;/bad&gt; on land. | — | — | — |
| FIRE | This item counts as &lt;color_red&gt;fire&lt;/color&gt; for crafting purposes. | — | — | — |
| FIRESTARTER | This item can start &lt;color_red&gt;fire&lt;/color&gt;. | — | — | — |
| FIREWOOD | This item can serve as a firewood. | — | — | — |
| FIRE_TWOHAND | &lt;bad&gt;You must&lt;/bad&gt; have two free hands to fire this item. | — | — | — |
| FIRING_EXT_POWER | — | — | — | — |
| FIT | — | — | — | — |
| FIX_FARSIGHT | This gear &lt;good&gt;corrects farsightedness&lt;/good&gt;. | — | — | — |
| FIX_NEARSIGHT | This gear &lt;good&gt;corrects nearsightedness&lt;/good&gt;. | — | — | — |
| FLAMING | — | — | — | — |
| FLASH_PROTECTION | — | — | — | — |
| FLAT | — | — | — | — |
| FLAT_TIRE | — | — | — | — |
| FLOTATION | This clothing &lt;info&gt;prevents going underwater&lt;/info&gt; including both &lt;good&gt;drowning&lt;/good&gt; and &lt;bad&gt;diving&lt;/bad&gt;. | — | — | — |
| FOLDED_STOCK | This items stock is folded it will be hard to shoot with. | — | — | — |
| FORAGE_HALLU | — | — | — | — |
| FORAGE_POISON | — | — | — | — |
| FRAGILE | This gear is &lt;bad&gt;fragile&lt;/bad&gt; and &lt;info&gt;won't protect you for long&lt;/info&gt;. | — | False | ["STURDY"] |
| FRAGILE_MELEE | As a weapon, this item is &lt;bad&gt;flimsy&lt;/bad&gt; and &lt;info&gt;won't last long in combat&lt;/info&gt; before breaking apart. | — | — | ["DURABLE_MELEE"] |
| FREEZERBURN | — | — | — | — |
| FREEZE_EFFECTS | — | — | — | — |
| FRESH_GRAIN | — | — | — | — |
| FROM_FROZEN_LIQUID | — | — | — | — |
| FROZEN | — | — | — | — |
| FUNGAL_VECTOR | — | — | — | — |
| GASFILTER_MED | A medium-sized gas mask filter. | — | — | — |
| GASFILTER_SM | A small-sized gas mask filter. | — | — | — |
| GAS_DISCOUNT | — | — | — | — |
| GAS_PROOF | This gear &lt;good&gt;completely protects&lt;/good&gt; you from &lt;info&gt;any gas&lt;/info&gt;. | — | — | — |
| GAS_TANK | Airtight tanks for propane, natural gas, etc. | — | — | — |
| GEMSTONE | This item is a precious gemstone, used for ornamentation.  This is mostly useless post-Cataclysm. | — | — | — |
| GENDER_FLUIDITY | — | — | — | — |
| GENDER_INVARIANCE | — | — | — | — |
| GENE_TECH | — | — | — | — |
| GIBBED | — | — | — | — |
| GNV_EFFECT | — | — | — | — |
| GRENADE | — | Item must be a grenade | — | — |
| HANDS_CANNOT_USE_FIREARMS | — | — | — | — |
| HARD | — | — | — | — |
| HEAD_STRAP_MOUNT | This item is attachable to straps and mountings on some masks and hoods. | Item must be some kind of item that can be attached to straps on masks and hoods | — | — |
| HEARING_PROTECTION | — | — | — | — |
| HEAT_IMMUNE | This gear &lt;good&gt;completely protects&lt;/good&gt; you from &lt;info&gt;high temperatures&lt;/info&gt;. | — | — | — |
| HELMET_AVENTAIL | This item is attachable to metal cap helmets as a face and neck protective layer. | Item must be some kind of chainmail veil | — | — |
| HELMET_BACK_POUCH | This item is attachable in the back of &lt;info&gt;hard hats and helmets&lt;/info&gt; as a counterweight pouch. | Item must be some kind of back pouch | — | — |
| HELMET_EAR_ATTACHMENT | This item is attachable in &lt;info&gt;hard hats and helmets&lt;/info&gt; to cover the ears. | Item must be some kind of ear attachment | — | — |
| HELMET_FACE_SHIELD | This item is attachable in the front of &lt;info&gt;hard hats and helmets&lt;/info&gt; to protect your eyes or face. | Item must be some kind of face shield | — | — |
| HELMET_FRONT_ATTACHMENT | This item is attachable in the front of &lt;info&gt;military helmets&lt;/info&gt;. | Item must be some kind of frontal helmet attachment | — | — |
| HELMET_HEAD_ATTACHMENT | This item is attachable in &lt;info&gt;tactical helmets&lt;/info&gt; as a flashlight. | Item must be some kind of flashlight | — | — |
| HELMET_MANDIBLE_GUARD | This item is attachable as a mandible guard in military &lt;info&gt;helmets&lt;/info&gt; or headgear specifically adapted with rails for attachments. | Item must be some kind of rail-mounted mandible guard | — | — |
| HELMET_MANDIBLE_GUARD_STRAPPED | This item is attachable as a mandible guard in &lt;info&gt;hard hats and helmets&lt;/info&gt;. | Item must be some kind of strapped mandible guard | — | — |
| HELMET_NAPE_PROTECTOR | This item is attachable in &lt;info&gt;hard hats and helmets&lt;/info&gt; as a nape protector. | Item must be some kind of nape protector | — | — |
| HEMOVORE | — | — | — | — |
| HEMOVORE_FUN | — | — | — | — |
| HERITAGE | You have nonhuman ancestry or are not human | — | — | — |
| HIDDEN | You have marked this article to not display a sprite when worn. | — | — | — |
| HIDDEN_HALLU | — | — | — | — |
| HIDDEN_ITEM | — | — | — | — |
| HIDDEN_POISON | — | — | — | — |
| HIDDEN_SPELL | — | — | — | — |
| HIGH_GLARE | — | — | — | — |
| HINT_THE_LOCATION | — | — | — | — |
| HOOD | This clothing has a &lt;info&gt;hood&lt;/info&gt; to keep your head warm if your head is unencumbered. | — | — | — |
| HOSTILE_50 | — | — | — | — |
| HOSTILE_SUMMON | — | — | — | — |
| HOT | — | — | — | — |
| HUNGER_DISRUPTION | You don't know how hungry you are when you are effected by this. | — | — | — |
| HURT_WHEN_WIELDED | — | — | — | — |
| HYGROMETER | This gear is equipped with an accurate hygrometer (which is used to measure humidity). | — | — | — |
| IGNORE_WALLS | — | — | — | — |
| IMPERIAL_ROAD_KEY | — | — | — | — |
| IMPERIAL_ROAD_TRAVELER | — | — | — | — |
| INDUSTRIAL_CARD | You could probably use this to get into a secure industrial facility. | — | — | — |
| INEDIBLE | — | — | — | — |
| INHALED_TOXIN_IMMUNE | You are immune to gaseous toxins | — | — | — |
| INITIAL_PART | — | — | — | — |
| INSENSITIVITY | — | — | — | — |
| INSPIRATIONAL | — | — | — | — |
| INSTALL_DIFFICULT | — | — | — | — |
| INSTANT_BLEED | — | — | — | — |
| INTANGIBLE_ARMOR | — | — | — | — |
| INTEGRATED | This is &lt;info&gt;integrated into the body&lt;/info&gt;. | — | — | — |
| IRRADIATED | This food item has been irradiated, and will spoil 4 times slower. | — | — | — |
| IRREMOVABLE | This item is a component of the gun it is attached to.  It can't be removed without destroying it. | — | False | — |
| IRREPLACEABLE_CONSUMABLE | — | — | — | — |
| IRRITANT_IMMUNE | This gear &lt;good&gt;completely protects&lt;/good&gt; you from &lt;info&gt;skin irritants&lt;/info&gt;. | — | — | — |
| IS_ARMOR | — | — | — | — |
| IS_PET_ARMOR | — | — | — | — |
| IS_UPS | This item provides power to &lt;info&gt;UPS compatible items&lt;/info&gt;. | — | False | — |
| ITEM_BROKEN | This item was broken and &lt;bad&gt;won't activate anymore&lt;/bad&gt;. | — | — | — |
| ITEM_WATERPROOFING | Something is preventing your worn and carried items from being effected by water. | — | — | — |
| JAVELIN | — | — | — | — |
| JETPACK | This item is a jetpack. | — | — | — |
| LASER_SIGHT | Laser sights are invalid when the target position is &lt;bad&gt;too far&lt;/bad&gt; or &lt;bad&gt;too bright&lt;/bad&gt;. | — | — | — |
| LEAK_ALWAYS | — | — | — | — |
| LEAK_DAM | — | — | — | — |
| LEG_PROSTHETIC | — | — | — | — |
| LEVER_ACTION | This weapon uses a manual lever to load each round into the chamber, forcing you to cock the lever after each shot, which &lt;bad&gt;takes additional time&lt;/bad&gt; and &lt;bad&gt;messes your aim&lt;/bad&gt;.  The penalty is decreased the more experienced with guns you are. | — | — | — |
| LEVITATION | Allows movement in open air. | — | — | — |
| LITCIG | — | — | — | — |
| LIXA_MILITARY_CARD | This grants access to locked-down areas of the LIXA facility. | — | — | — |
| LIXA_SCIENCE_CARD | This grants access to the LIXA facility. | — | — | — |
| LIXA_SCIENCE_CARD_2 | This grants access to the experiment chamber of the LIXA facility. | — | — | — |
| LIXA_SCIENCE_CARD_3 | This grants access to the experiment chamber and PPE lockup for the LIXA facility. | — | — | — |
| LOCATION_PRECISE_CLOSEST_CITY | — | — | — | — |
| LOUD | — | — | — | — |
| LUPINE | — | — | — | — |
| MAGICAL | — | — | — | — |
| MAGIC_FOCUS | — | — | — | — |
| MAG_BELT | — | — | — | — |
| MAG_BULKY | This item is &lt;bad&gt;bulky&lt;/bad&gt; and may not fit in all magazine pockets. | Item must be a bulky magazine | — | — |
| MAG_COMPACT | This item has a small profile consistent with a compact magazine. | Item must be a compact magazine | — | — |
| MAG_DESTROY | — | — | — | — |
| MAG_EJECT | — | — | — | — |
| MANUAL_CBM_INSTALLATION | — | — | — | — |
| MC_HAS_DATA | Some of your data is &lt;info&gt;stored&lt;/info&gt; here. | — | — | — |
| MC_MOBILE | Can be used to &lt;info&gt;store data&lt;/info&gt; for other devices. | — | — | — |
| MECH_BAT | — | — | — | — |
| MELTS | This food &lt;neutral&gt;melts when not in a very cold climate&lt;/neutral&gt;, and tastes much &lt;good&gt;better&lt;/good&gt; when &lt;color_light_cyan&gt;frozen&lt;/color&gt;. | — | — | — |
| MESSY | — | — | — | — |
| METHANOL_TANK | This item fits in items that use methanol fuel cells. | — | — | — |
| MILITARY_CARD | You could probably use this to get into a secure military facility. | — | — | — |
| MISSION_ITEM | — | — | — | — |
| MODULE_HOLDER | — | — | — | — |
| MOP | — | — | — | — |
| MORPHIC | This is &lt;info&gt;naturally sized to the body&lt;/info&gt;. | — | — | — |
| MOUNTED_GUN | This weapon is &lt;bad&gt;too unwieldy&lt;/bad&gt; to fire on its own and &lt;info&gt;must be mounted&lt;/info&gt; on a vehicle or furniture (window, table, mound of dirt, etc.) before use. | — | — | — |
| MOUSE | — | — | — | — |
| MUNDANE | This item is designed to have special effects | — | — | — |
| MUSHY | — | — | — | — |
| MUTAGEN_CATALYST | Injecting it will &lt;neutral&gt;jumpstart mutation&lt;/neutral&gt;. | — | — | — |
| MUTAGEN_PRIMER | Injecting it will &lt;neutral&gt;prime your body for mutation&lt;/neutral&gt;. | — | — | — |
| MUTAGEN_SAMPLE | Used in the &lt;neutral&gt;creation of mutagenic drugs&lt;/neutral&gt;. | — | — | — |
| MUTATED_ANATOMY_ONLY | This can only be worn by those with &lt;info&gt;particular mutated anatomy&lt;/info&gt;  | — | — | — |
| MUTE | This gear &lt;bad&gt;prevents&lt;/bad&gt; you from &lt;info&gt;speaking&lt;/info&gt;. | — | — | — |
| MWS_PORTAL_STORM_DATA | This ongoing report has a series of odd recordings, as if the instruments malfunctioned. | — | — | — |
| MYCUS_OK | — | — | — | — |
| MYOPIC_IN_LIGHT_SUPERNATURAL | — | — | — | — |
| MYOPIC_SUPERNATURAL | — | — | — | — |
| NANOFAB_REPAIR | This item has a holographic patch that reflects the light oddly.  It was constructed in a nanofabricator and can be &lt;info&gt;repaired in one&lt;/info&gt;. | — | — | — |
| NANOFAB_TEMPLATE | This item contains a nanofabricator recipe. | — | — | — |
| NANOFAB_TEMPLATE_SINGLE_USE | This template is copy protected and will be &lt;bad&gt;destroyed&lt;/bad&gt; after a single use. | — | — | — |
| NATURAL_UNDERGROUND | — | — | — | — |
| NEEDS_NO_LUBE | — | — | — | — |
| NEEDS_SUNLIGHT | This tool only functions in strong direct sunlight.  It will not work indoors, underground, at night, or in overcast weather. | — | — | — |
| NEEDS_UNFOLD | — | — | — | — |
| NEGATIVE_MONOTONY_OK | — | — | — | — |
| NEVER_JAMS | — | — | — | — |
| NOGIB | — | — | — | — |
| NONCONDUCTIVE | — | — | — | — |
| NON_FOULING | — | — | — | — |
| NON_THRESH | — | — | — | — |
| NORMAL | This gear &lt;info&gt;fits like&lt;/info&gt; normal clothing. | — | — | — |
| NO_AUTO_CONSUME | — | — | — | — |
| NO_BODY_HEAT | The character produces no body heat and is not visible on infrared (for characters only, for monsters use the WARM flag to enable infrared visibility). | — | — | — |
| NO_CLEAN | This item is impossible to clean. | — | — | — |
| NO_CROP_OVERGROWTH | This planting facility can prevent crops from over-ripening and wilting. | — | — | — |
| NO_CVD | — | — | — | — |
| NO_DROP | — | — | — | — |
| NO_FAIL | — | — | — | — |
| NO_HANDS | — | — | — | — |
| NO_INGEST | — | — | — | — |
| NO_LEGS | — | — | — | — |
| NO_MANUAL_ACTIVATION | — | — | — | — |
| NO_PACKED | — | — | — | — |
| NO_PAINT | This vehicle part keeps its own sprite colors and is never tinted by a vehicle color palette. | — | — | — |
| NO_PARASITES | — | — | — | — |
| NO_RELOAD | — | — | — | — |
| NO_REPAIR | — | — | False | — |
| NO_SALVAGE | — | — | — | — |
| NO_STERILE | — | — | — | — |
| NO_TAKEOFF | — | — | — | — |
| NO_TEMP | — | — | — | — |
| NO_TURRET | — | — | — | — |
| NO_UNLOAD | — | — | False | — |
| NO_UNWIELD | — | — | — | — |
| NO_WEAR_EFFECT | This item can be worn, but it &lt;neutral&gt;won't provide any effects&lt;/neutral&gt;. | — | — | — |
| NPC_ACTIVATE | — | — | — | — |
| NPC_ALT_ATTACK | — | — | — | — |
| NPC_SAFE | — | — | — | — |
| NPC_THROWN | — | — | — | — |
| NPC_THROW_NOW | — | — | — | — |
| NUMB | — | — | — | — |
| NUTRIENT_OVERRIDE | — | — | — | — |
| NVG_GREEN | — | — | — | — |
| OBSOLETE | This thing no longer spawns naturally and has been obsoleted. | — | — | — |
| OLD_CURRENCY | This item used to be legal tender before the Cataclysm. | — | — | — |
| OLD_GUN | An old gun, WWII or earlier. | — | — | — |
| ONE_PER_LAYER | &lt;info&gt;Only one&lt;/info&gt; item can be worn on this clothing layer. | — | — | — |
| ONE_STORY_FALL | — | — | — | — |
| ORGANIC | — | — | — | — |
| OUTER | This gear is generally &lt;info&gt;worn over&lt;/info&gt; clothing. | — | — | — |
| OVERHEATS | Continuously firing this weapon will cause it to &lt;bad&gt;overheat&lt;/bad&gt; and &lt;info&gt;can potentially damage it&lt;/info&gt;. | — | — | — |
| OVERSIZE | This clothing is large enough to accommodate &lt;info&gt;abnormally large mutated anatomy&lt;/info&gt;. | — | — | — |
| PADDED | This item has notable padding and will be comfortable worn without clothing under it. | — | — | — |
| PAIN_IMMUNE | — | — | — | — |
| PAIN_NORESIST | — | — | — | — |
| PALS_LARGE | This item will &lt;good&gt;attach directly&lt;/good&gt; to &lt;info&gt;load bearing vests&lt;/info&gt;, taking a &lt;bad&gt;large amount of space&lt;/bad&gt;. | — | — | — |
| PALS_MEDIUM | This item will &lt;good&gt;attach directly&lt;/good&gt; to &lt;info&gt;load bearing vests&lt;/info&gt;, taking an average amount of space. | — | — | — |
| PALS_SMALL | This item will &lt;good&gt;attach directly&lt;/good&gt; to &lt;info&gt;load bearing vests&lt;/info&gt;, taking a &lt;good&gt;small amount of space&lt;/good&gt;. | — | — | — |
| PANORAMIC_INSERT | This item is intended to be inserted behind the visor of a single-lens gas mask. | Item must be able to clip into place within a gas mask that has a single, panoramic eyepiece. | — | — |
| PANORAMIC_OUTSERT | This item is meant to be externally attached to the eyepiece of a single-lens gas mask. | Item must be designed to clip onto the external Lenz brackets of a panoramic-view gas mask. | — | — |
| PAPER_SHAPED | — | Item must be shaped like paper | — | — |
| PAPR_BLOWER | This item functions as a powered air purifying respirator blower. | — | — | — |
| PAPR_MASK | This item functions as a powered air purifying respirator. | — | — | — |
| PARTIAL_DEAF | This gear &lt;good&gt;reduces&lt;/good&gt; the volume of &lt;info&gt;sounds&lt;/info&gt; to a safe level. | — | — | ["DEAF"] |
| PAUSE_INFECTIONS | Infections cannot progress to a fatal stage while you have this flag. | — | — | — |
| PERFECT_LOCKPICK | This item can be used to &lt;info&gt;pick locks&lt;/info&gt; with &lt;good&gt;zero effort&lt;/good&gt;. | — | — | — |
| PERMANENT | — | — | — | — |
| PERPETUAL | — | — | — | — |
| PERSONAL | This is in your &lt;info&gt;personal aura&lt;/info&gt;. | — | — | — |
| PHASE_BACK | — | — | — | — |
| PIT_FILLABLE | — | — | — | — |
| PLACE_RANDOMLY | — | — | — | — |
| PLANTABLE_SEED | You could probably &lt;color_brown&gt;plant&lt;/color&gt; these. | — | — | — |
| PLOWABLE | — | — | — | — |
| POCKETS | This clothing has &lt;info&gt;pockets&lt;/info&gt; to warm your hands when you are wielding nothing. | — | — | — |
| POLEARM | As a weapon, this item needs considerable space to use properly and does 70% of its normal damage to adjacent enemies. | — | — | — |
| PORTAL_PROOF | — | — | — | — |
| POST_UP | This item can be put up on a wall, like a poster. | — | — | — |
| POWERARMOR_COMPATIBLE | This item can be worn simultaneously with power armor. | — | — | — |
| POWERED | — | — | — | — |
| PREDATOR_FUN | — | — | — | — |
| PREFIX_XL | — | — | — | — |
| PREFIX_XS | — | — | — | — |
| PRESERVE_SPAWN_LOC | — | — | — | — |
| PRIMITIVE_RANGED_WEAPON | — | — | — | — |
| PROCESSING | — | — | — | — |
| PROCESSING_RESULT | — | — | — | — |
| PROVIDES_TECHNIQUES | — | — | — | — |
| PSEUDO | — | — | — | — |
| PSEUDOPOD_GRASP | — | — | — | — |
| PSYCHOPATH | — | — | — | — |
| PSYSHIELD_PARTIAL | This gear &lt;good&gt;keeps out&lt;/good&gt; the &lt;info&gt;mind control rays&lt;/info&gt;. | — | — | — |
| PULPED | — | — | — | — |
| PUMP_ACTION | This weapon requires you to manually pull and insert cartridge into the chamber by sliding a handguard, which &lt;bad&gt;takes additional time&lt;/bad&gt; and &lt;bad&gt;messes your aim&lt;/bad&gt;.  The penalty is decreased the more experienced with guns you are. | — | — | — |
| PUMP_RAIL | — | — | — | — |
| PUMP_RAIL_COMPATIBLE | — | — | — | — |
| PUNCTURE_VEHICLE_WHEELS | — | — | — | — |
| QUADRUPED_CROUCH | — | — | — | — |
| QUADRUPED_RUN | — | — | — | — |
| QUARTERED | — | — | — | — |
| RABBIT | — | — | — | — |
| RADIOACTIVE | — | — | — | — |
| RADIOCAR | — | — | — | — |
| RADIOCARITEM | — | — | — | — |
| RADIOSIGNAL_1 | — | — | — | — |
| RADIOSIGNAL_2 | — | — | — | — |
| RADIOSIGNAL_3 | — | — | — | — |
| RADIO_ACTIVATION | — | — | — | — |
| RADIO_CONTAINER | — | — | — | — |
| RADIO_INVOKE_PROC | — | — | — | — |
| RADIO_MOD | — | — | — | — |
| RADIO_MODABLE | — | — | — | — |
| RAD_DETECT | This item can &lt;good&gt;detect&lt;/good&gt; dangerous levels of &lt;info&gt;radiation&lt;/info&gt;. | — | — | — |
| RAD_PROOF | This clothing &lt;good&gt;completely protects&lt;/good&gt; you from &lt;info&gt;radiation&lt;/info&gt;. | — | — | ["RAD_RESIST"] |
| RAD_RESIST | This clothing &lt;good&gt;partially protects&lt;/good&gt; you from &lt;info&gt;radiation&lt;/info&gt;. | — | — | ["RAD_PROOF"] |
| RAD_STERILIZED | Sterilized using radiation, so it's &lt;good&gt;safe to eat&lt;/good&gt;. | — | — | — |
| RAINPROOF | This clothing is designed to keep you &lt;info&gt;dry&lt;/info&gt; in the rain. | — | — | — |
| RAIN_PROTECT | — | — | — | — |
| RAT | — | — | — | — |
| RAW | This food is &lt;info&gt;raw&lt;/info&gt;, and will be &lt;good&gt;more nutritious&lt;/good&gt; if cooked. | — | — | — |
| REACH3 | — | — | — | — |
| REACH_ATTACK | — | — | — | — |
| REBREATHER | — | — | — | — |
| REBREATHER_CART | A filter for a rebreather. | — | — | — |
| RECHARGE | — | — | — | — |
| REDUCED_BASHING | — | — | — | — |
| REDUCED_WEIGHT | — | — | — | — |
| RELIC_PINK | — | — | — | — |
| RELOAD_AND_SHOOT | — | — | — | — |
| RELOAD_EJECT | — | — | — | — |
| RELOAD_ONE | — | — | — | — |
| REMOVED_STOCK | This item has had its stock removed, it will be hard to shoot with. | — | — | — |
| REQUIRES_BALANCE | This gear requires careful balance to use.  Being hit while wearing it could make you &lt;bad&gt;fall down&lt;/bad&gt;. | — | — | — |
| REQUIRES_TINDER | — | — | — | — |
| RESTRICT_HANDS | — | — | — | — |
| REVIVE_SPECIAL | — | — | — | — |
| ROBOFAC_ARM | This item is a Hub 01 ARM exoskeleton.  It requires an implanted XM-ARM interface to function. | — | — | — |
| ROBOFAC_BACK | This item is a Hub 01 BACK exoskeleton.  It requires an implanted XM-LEG interface and it must be worn with ARM and LEG exoskeletons to function. | — | — | — |
| ROBOFAC_LEG | This item is a Hub 01 LEG exoskeleton.  It requires an implanted XM-LEG interface to function. | — | — | — |
| ROBOFAC_LENS_ACCESSORY | This item is an accessory for a Hub 01 LENS helmet, and can only be worn with that helmet. | — | — | — |
| ROBOFAC_LENS_HELMET | This item allows you to wear Hub 01 LENS accessories. | — | — | — |
| ROBOFAC_ROBOT_MEDIUM | A medium drone sold by Hub 01. | — | — | — |
| ROBOFAC_ROBOT_SMALL | A small drone sold by Hub 01. | — | — | — |
| ROBUST_GENETIC | — | — | — | — |
| ROLLER_INLINE | — | — | — | — |
| ROLLER_ONE | — | — | — | — |
| ROLLER_QUAD | — | — | — | — |
| ROOTS2 | The character has roots, which helps with the TREE_COMMUNION mutation. | — | — | — |
| ROOTS3 | The character has extensive roots, which helps with the TREE_COMMUNION mutation. | — | — | — |
| RUBBLE | — | — | — | — |
| SAFECRACK | — | — | — | — |
| SCIENCE_CARD | You could probably use this to get into a secure science facility. | — | — | — |
| SCIENCE_CARD_MAINTENANCE_BLUE | You could probably use this to get into a secured maintenance area. | — | — | — |
| SCIENCE_CARD_MAINTENANCE_GREEN | You could probably use this to get into a science facility. | — | — | — |
| SCIENCE_CARD_MAINTENANCE_YELLOW | You could probably use this to get into a secured maintenance area. | — | — | — |
| SCIENCE_CARD_MEDICAL_RED | You could probably use this to access a secure zone of a facility. | — | — | — |
| SCIENCE_CARD_MUTAGEN_CYAN | You could probably use this to access a secure zone of a facility. | — | — | — |
| SCIENCE_CARD_MUTAGEN_GREEN | You could probably use this to access a secure zone of a facility. | — | — | — |
| SCIENCE_CARD_MUTAGEN_PINK | You could probably use this to access a secure zone of a facility. | — | — | — |
| SCIENCE_CARD_MU_UNIVERSAL | You could probably use this to access a secure zone of a facility. | — | — | — |
| SCIENCE_CARD_SECURITY_BLACK | You could probably use this to get into a secured law enforcement area. | — | — | — |
| SCIENCE_CARD_SECURITY_MAGENTA | You could probably use this to get into a secured law enforcement area. | — | — | — |
| SCIENCE_CARD_SECURITY_YELLOW | You could probably use this to get into a secured law enforcement area. | — | — | — |
| SCIENCE_CARD_TRANSPORT_1 | You could probably use this to get into a science facility. | — | — | — |
| SCIENCE_CARD_VISITOR | You could probably use this to get into a science facility. | — | — | — |
| SEMITANGIBLE | It seems &lt;info&gt;partially intangible&lt;/info&gt;, and can occupy the same space as other things when worn. | — | — | — |
| SHAPESHIFTED_ARMOR | This item is currently &lt;good&gt;part of your form&lt;/good&gt; and &lt;bad&gt;will not protect you&lt;/bad&gt;. | — | — | — |
| SHAPESHIFT_SIZE_HUGE | — | — | — | — |
| SHAPESHIFT_SIZE_LARGE | — | — | — | — |
| SHAPESHIFT_SIZE_SMALL | — | — | — | — |
| SHAPESHIFT_SIZE_TINY | — | — | — | — |
| SHEATH_AXE | This item can &lt;info&gt;fit in an axe sheath&lt;/info&gt; of the appropriate size. | Item must fit in an axe sheath | — | — |
| SHEATH_BOW | This item can &lt;info&gt;fit in a bow sling&lt;/info&gt; of the appropriate size. | Item must fit in a bow sling | — | — |
| SHEATH_GOLF | — | — | — | — |
| SHEATH_KNIFE | This item can &lt;info&gt;fit in a sheath&lt;/info&gt; of the appropriate size. | Item must fit in a sheath | — | — |
| SHEATH_SPEAR | This item can &lt;info&gt;attach to a spear strap&lt;/info&gt; of the appropriate size. | Item must attach to a spear strap | — | — |
| SHEATH_SWORD | This item can &lt;info&gt;fit in a scabbard&lt;/info&gt; of the appropriate size. | Item must fit in a scabbard | — | — |
| SHREDDED | This is a small fragment. | — | — | — |
| SILENT | — | — | — | — |
| SINGLE_ACTION | This weapon requires you to cock the hammer of a firearm manually, which &lt;bad&gt;takes additional time&lt;/bad&gt; and &lt;bad&gt;messes your aim&lt;/bad&gt;.  The penalty is decreased the more experienced with guns you are. | — | — | — |
| SINGLE_USE | This item is removed after use. | — | — | — |
| SKINNED | — | — | — | — |
| SKINTIGHT | This clothing &lt;info&gt;lies close&lt;/info&gt; to the skin. | — | — | — |
| SKIP_HEALTH | — | — | — | — |
| SLEEP_AID | This item provides comfort during sleep. | — | — | — |
| SLEEP_AID_CONTAINER | — | — | — | — |
| SLEEP_IGNORE | — | — | — | — |
| SLOW_WIELD | — | — | — | — |
| SMOKED | — | — | — | — |
| SNOWWALKING | Your movement is not slowed regardless of snow depth. | — | — | — |
| SOFT | — | — | — | — |
| SOLARPACK | — | — | — | — |
| SOLARPACK_ON | — | — | — | — |
| SOMATIC | — | — | — | — |
| SPAWN_ACTIVE | — | — | — | — |
| SPAWN_WITH_DEATH_DROPS | — | — | — | — |
| SPEAR | — | — | — | — |
| SPEEDLOADER | This item can quickly reload rounds into gun or magazine that &lt;info&gt;have enough space&lt;/info&gt;. | — | — | ["SPEEDLOADER_CLIP"] |
| SPEEDLOADER_CLIP | This item can quickly reload rounds into gun or magazine that &lt;info&gt;don't have enough space&lt;/info&gt;. | — | — | ["SPEEDLOADER"] |
| SPLINT | — | — | — | — |
| STAB | — | — | — | — |
| STAB_IMMUNE | This gear &lt;good&gt;completely protects&lt;/good&gt; you from &lt;info&gt;stab damage&lt;/info&gt;. | — | — | — |
| STAR_PLATE | This can be supported by the ryūsei battle kit. | Item must be resonance plate | — | — |
| STAR_SHOULDER | This can be supported by the ryūsei battle kit. | Item must be resonance shoulder | — | — |
| STAR_SKIRT | This can be supported by the ryūsei battle kit. | Item must be resonance skirt | — | — |
| STRICT_HUMANITARIANISM | — | — | — | — |
| STR_DRAW | — | — | — | — |
| STR_RELOAD | — | — | — | — |
| STURDY | This clothing will &lt;good&gt;protect&lt;/good&gt; you from harm and withstand &lt;info&gt;a lot of abuse&lt;/info&gt;. | — | False | ["FRAGILE"] |
| SUFFOCATION_IMMUNE | You are immune to being crowd-crushed | — | — | — |
| SUNBURN_SUPERNATURAL | You burn in the sunlight like a vampire.  Probably because you're a vampire. | — | — | — |
| SUNBURN_SUPERNATURAL_REDUCTION | You burn in the sunlight like a vampire, but not quite as badly. | — | — | — |
| SUN_GLASSES | This clothing keeps the &lt;info&gt;glare&lt;/info&gt; out of your eyes. | — | — | — |
| SUPPORTS_ROOF | A roof can be built above this without other support. | — | — | — |
| SUPPRESS_INVISIBILITY | If you're invisible, now you're not | — | — | — |
| SWIM_GOGGLES | This clothing allows you to &lt;good&gt;see much further&lt;/good&gt; &lt;info&gt;under water&lt;/info&gt;. | — | — | — |
| SWIM_UNDER | Terrain with this flag is treated as having water beneath a covering (e.g. ice); entities may be considered under water for swimming and related mechanics. | — | — | — |
| TACK | — | — | — | — |
| TANGLE | — | — | — | — |
| TARDIS | — | — | — | — |
| TELEPORT_LOCK | — | — | — | — |
| TEMPORARY_SHAPESHIFT | — | — | — | — |
| TEMPORARY_SHAPESHIFT_NO_HANDS | — | — | — | — |
| THERMOMETER | This gear is equipped with an &lt;info&gt;accurate thermometer&lt;/info&gt;. | — | — | — |
| THROW_KEEP_WIELDED | Can be kept wielded while throwing another item, boosting the throw. | — | — | — |
| TIE_UP | — | — | — | — |
| TINDER | — | — | — | — |
| TOBACCO | — | — | — | — |
| TOUGH_FEET | — | — | — | — |
| TOURNIQUET | — | — | — | — |
| TOW_CABLE | — | — | — | — |
| TRADER_AVOID | — | — | — | — |
| TRADER_KEEP | — | — | — | — |
| TRADER_KEEP_EQUIPPED | — | — | — | — |
| TREE | — | — | — | — |
| TREE_COMMUNION_PLUS | You gain greatly enhanced effects from the Mycorrhizal Communion mutation | — | — | — |
| TRUE_SEEING | The character can see through CAMOUFLAGE, NIGHT_INVISIBILITY, or the invisibility effect. | — | — | — |
| TWO_WAY_RADIO | This item can be used to communicate with radio waves. | — | — | — |
| UNBREAKABLE | — | — | — | — |
| UNBREAKABLE_MELEE | — | — | — | — |
| UNDERFED | — | — | — | — |
| UNDERSIZE | — | — | — | — |
| UNDERWATER_GUN | — | — | — | — |
| UNRECOVERABLE | — | — | — | — |
| UNRESTRICTED | This clothing is able to &lt;info&gt;accommodate even mutated anatomy&lt;/info&gt;. | — | — | — |
| URSINE_HONEY | — | — | — | — |
| USES_BIONIC_POWER | — | — | — | — |
| USES_NEARBY_AMMO | — | — | — | — |
| USE_EAT_VERB | — | — | — | — |
| USE_PLAYER_ENERGY | — | — | — | — |
| USE_POWER_WHEN_HIT | This armor &lt;info&gt;expends energy when hit&lt;/info&gt;. | — | — | — |
| USE_UPS | — | — | — | — |
| VARSIZE | — | — | — | — |
| VEHICLE | — | — | — | — |
| VERBAL | — | — | — | — |
| VIEW_PHOTOS | — | — | — | — |
| VIEW_RECIPES | — | — | — | — |
| VINE_RAPPEL | The character can use vines to safely rappel down sheer drops. | — | — | — |
| VOLTMETER | This tool can test for voltage. | — | — | — |
| WAIST | This gear is worn on or around your &lt;info&gt;waist&lt;/info&gt;. | — | — | — |
| WALL | — | — | — | — |
| WATCH | This gear allows to see &lt;info&gt;actual time&lt;/info&gt;. | — | — | — |
| WATERPROOF | This clothing &lt;info&gt;won't let water through&lt;/info&gt;.  Even if you jump into a river. | — | — | — |
| WATERPROOF_GUN | — | — | — | — |
| WATERWALKING | You can walk across the surface of water. | — | — | — |
| WATER_BREAK | This item &lt;bad&gt;will get broken&lt;/bad&gt; by water. | — | — | — |
| WATER_BREAK_ACTIVE | This item &lt;bad&gt;will get broken&lt;/bad&gt; by water if it gets &lt;info&gt;submerged while active&lt;/info&gt;. | — | — | — |
| WATER_DISSOLVE | This item &lt;bad&gt;will get dissolved&lt;/bad&gt; in water. | — | — | — |
| WATER_EXTINGUISH | — | — | — | — |
| WATER_FRIENDLY | This clothing &lt;good&gt;performs well&lt;/good&gt; even when &lt;info&gt;soaking wet&lt;/info&gt;.  This can feel good. | — | — | — |
| WET | — | — | — | — |
| WHIP | — | — | — | — |
| WIND_EXTINGUISH | — | — | — | — |
| WIRED_WALL | — | — | — | — |
| WONDER | — | — | — | — |
| WONT_TRAIN_MARKSMANSHIP | — | — | — | — |
| WRIST_MOUNT_ATTACHMENT | This item is attachable to a proprietary wrist mount. | Item must be some kind of item that can be attached to a proprietary wrist mount | — | — |
| WRITE_MESSAGE | — | — | — | — |
| ZERO_WEIGHT | — | — | — | — |
| ZOOM | This item can be used to &lt;good&gt;better&lt;/good&gt; see &lt;info&gt;things far away&lt;/info&gt;. | — | — | — |
| auto_wield | — | — | — | — |
| furred | This clothing has a fur lining sewn into it to &lt;good&gt;increase&lt;/good&gt; its overall &lt;info&gt;warmth&lt;/info&gt;. | — | — | — |
| kevlar_padded | This gear has Kevlar inserted into strategic locations to &lt;good&gt;increase protection&lt;/good&gt; with some &lt;bad&gt;increase to encumbrance&lt;/bad&gt;. | — | — | — |
| leather_padded | This gear has certain parts padded with leather to &lt;good&gt;increase protection&lt;/good&gt; with moderate &lt;bad&gt;increase to encumbrance&lt;/bad&gt;. | — | — | — |
| no_auto_equip | — | — | — | — |
| steel_padded | This gear has certain parts padded with steel to &lt;good&gt;increase protection&lt;/good&gt; with moderate &lt;bad&gt;increase to encumbrance&lt;/bad&gt;. | — | — | — |
| wooled | This clothing has a wool lining sewn into it to &lt;good&gt;increase&lt;/good&gt; its overall &lt;info&gt;warmth&lt;/info&gt;. | — | — | — |

## History and attribution

Accepted inventory contributors: LunaGlaze, LYHGLYTX, Standing-Storm, Mihály Verhás, zihanZheng, Tektolnes, RenechCDDA, dumb-kevin, evilbananas, Anton Simakov, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `3cab8da23ea482c450b9d0f6f2d2f5fb692e10b827e8f0ead7d3f361f1db6001`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/JSON_FLAGS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_FLAGS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_FLAGS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
