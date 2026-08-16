---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.cookbook.items
title: Items and Pockets Cookbook
language: en
status: active
doc_type: tutorial
audiences:
- mod-author
- api-user
- experienced-contributor
- maintainer
owners:
- CCB Lua API maintainers
reviewers:
- Documentation reviewers
- Lua API reviewers
review_interval_days: 60
last_human_reviewer: LYHGLYTX
source_paths:
- data/lua/README.md
- data/lua/manifest.schema.json
- data/lua/types/ccb_api_v5.d.lua
- data/lua/reference/ccb_public_api_v5.json
- data/lua/reference/ccb_public_api_v5_coverage.json
- tools/lua_api/README.md
source_symbols:
- Lua Mod API v5
source_queries: []
source_fingerprint: 30a19e6cbd8c6709ac5ccda80fe349e9459ddaccd8d3dc96507ee282c17f48cb
authority: api-contract
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a72760fa18c5e8777dd154d3157780468424dec30614b3b5569e143bbf693b25
prerequisites:
- architecture.overview
depends_on: []
redirect_from: []
supersedes:
- lua.v5.overview
license: CC-BY-SA-3.0
attribution: CCB contributors; generated contract and source paths at the verified commit.
example_validation_ids: []
api_version: '5'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/cookbook/items/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/cookbook/items/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/cookbook/items/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/cookbook/items/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: data/lua/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/README.md
- path: data/lua/manifest.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/manifest.schema.json
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/types/ccb_api_v5.d.lua
- path: data/lua/reference/ccb_public_api_v5.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/reference/ccb_public_api_v5.json
- path: data/lua/reference/ccb_public_api_v5_coverage.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/reference/ccb_public_api_v5_coverage.json
- path: tools/lua_api/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/lua_api/README.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.cookbook.items%29%3A+&body=Document+ID%3A+api.lua.cookbook.items%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Pure-Lua Items and Pockets Cookbook

In **CCB Lua 0.1**, Mod authors can define in-game items, weapons, armor, and nested pocket containers directly in Lua using modern object-oriented and dataflow APIs without relying on legacy JSON files.

---

## 1. Core Concepts & Lifecycle

In CCB, item definitions feature the following characteristics:
1. **Pure Code Registration**: Register item prototypes in your Mod's `main.lua` or submodules via `game.items.register()`.
2. **Pocket Container Architecture**: Single-layer inventories are completely replaced by nested Pocket trees with volume, weight, length, and sealing constraints.
3. **Dynamic Property Computation**: Item weight, volume, and encumbrance are calculated recursively at runtime, allowing dynamic state mutation and attachments.

---

## 2. Tutorial 1: Defining a Tactical Melee Weapon

The following example shows how to define a high-frequency vibrating blade with custom damage types and special callbacks:

```lua
-- mods/tactical_weapons/items/vibro_blade.lua
local items = {}

function items.register_weapons()
    game.items.register({
        id = "ccb_vibro_blade",
        name = "High-frequency Tactical Blade",
        description = "A lightweight titanium dagger equipped with a micro ultrasonic generator capable of slicing through heavy armor.",
        weight = 850, -- grams (g)
        volume = 750, -- milliliters (ml)
        price = 4500, -- cents
        category = "weapons",
        material = { "titanium", "plastic" },
        symbol = "/",
        color = "light_cyan",
        
        -- Melee combat stats
        melee = {
            damage = {
                cut = 28,      -- Cut damage
                pierce = 14,   -- Pierce damage
                bash = 4,      -- Bash damage
            },
            attack_cost = 75, -- Action points (AP) cost per attack
            to_hit = 2,       -- Accuracy bonus
        },
        
        -- Weapon tags & flags
        flags = {
            "SHEATH_KNIFE",      -- Can be holstered in standard sheaths
            "UNBREAKABLE_MELEE", -- High durability
            "CONDUCTIVE",        -- Conducts electricity
        },
        
        -- Custom item action callback
        on_use = function(character, item)
            game.add_msg("info", "You click the button on the hilt. The blade emits a faint high-frequency hum.")
            return true
        end
    })
end

return items
```

---

## 3. Tutorial 2: Defining a Modular Tactical Chest Rig (Pocket Container Tree)

Every container in CCB consists of one or more `pockets`. Each pocket independently specifies **max volume, max weight, opening size, and fluid sealing**:

```lua
function items.register_backpack()
    game.items.register({
        id = "ccb_tactical_rig",
        name = "Modular Tactical Chest Rig",
        description = "A modular chest rig designed for quick magazine draws, featuring a main pouch, utility pouches, and a sealed hydration pocket.",
        weight = 1200,
        volume = 2000,
        category = "armor",
        symbol = "[",
        color = "dark_gray",
        
        -- Armor stats (covers torso)
        armor = {
            covers = { "torso" },
            coverage = 65,      -- 65% torso coverage
            encumbrance = 12,   -- Encumbrance value
            warmth = 5,         -- Warmth
            protection = {
                cut = 8,
                bash = 6,
                ballistic = 12, -- Ballistic resistance
            }
        },
        
        -- Multi-pocket Container Architecture
        pockets = {
            -- 1. Main compartment
            {
                pocket_type = "CONTAINER",
                max_contains_volume = 12000, -- 12 Liters
                max_contains_weight = 15000, -- 15 kg
                max_item_length = 450,       -- Max length constraint (mm)
                rigid = false,               -- Non-rigid (expands when filled)
            },
            -- 2. Quick-draw Magazine Pouch
            {
                pocket_type = "CONTAINER",
                max_contains_volume = 1500,
                max_contains_weight = 2000,
                moves = 30,                  -- Quick draw moves (50% faster than main pouch)
                item_restriction = { "magazine", "ammo" }, -- Only magazines and ammo
            },
            -- 3. Watertight Hydration Bladder
            {
                pocket_type = "CONTAINER",
                max_contains_volume = 3000,  -- 3 Liters liquid
                watertight = true,           -- 100% airtight and watertight
                open_container = false,      -- Sealed against spills
            }
        }
    })
end
```

---

## 4. Tutorial 3: Custom Pharmaceuticals and Stimulants

```lua
function items.register_stims()
    game.items.register({
        id = "ccb_adrenaline_shot",
        name = "Military Adrenaline Autoinjector",
        description = "A single-use autoinjector that instantly boosts speed and pain tolerance, followed by dehydration and crash effects.",
        weight = 80,
        volume = 100,
        category = "drugs",
        
        on_use = function(character, item)
            character:mod_pain(-30)
            character:mod_stim(40)
            character:add_effect("adrenaline", 120) -- 120 turns duration
            
            game.add_msg("warning", "A sharp rush surges through your veins as your heart pounds violently!")
            return true
        end
    })
end
```

---

## 5. Verification & Testing

In your Mod root:
```lua
-- main.lua
local items = require("items/vibro_blade")

events.on("game_load", function()
    items.register_weapons()
    items.register_backpack()
    items.register_stims()
end)
```

Launch the game, open the Debug Menu (`Debug Menu -> Spawn Item`), and search for `ccb_vibro_blade` to spawn and test immediately!
