---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.cookbook.monsters
title: Monsters and AI Cookbook
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
translation_source_fingerprint: 8468deb56a88c844b6b5dd023fde5a7181e14c5b6d601365334d9201c4e68771
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/cookbook/monsters/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/cookbook/monsters/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/cookbook/monsters/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/cookbook/monsters/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.cookbook.monsters%29%3A+&body=Document+ID%3A+api.lua.cookbook.monsters%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Pure-Lua Monsters and AI Cookbook

In **CCB Lua 0.1**, developers and Mod authors can create new creature species, AI tactical behaviours, and dynamic special attacks directly using pure Lua without writing JSON files.

---

## 1. Monster Architecture & Concepts

In the CCB engine, `monster` inherits from the `Creature` base class:
1. **Pure Lua Registration**: Register species prototypes with `game.monsters.register()`.
2. **Dynamic AI Hooks & Skills**: Special attacks are bound as Lua closures, allowing direct distance checks, projectile emission, and raycast checks.
3. **Resistances and Armor**: Configure bespoke bash, cut, bullet, acid, and electrical damage thresholds for each creature.

---

## 2. Tutorial 1: Defining a Stalker Mutant Predator

```lua
-- mods/mutant_threats/monsters/stalker.lua
local monsters = {}

function monsters.register_stalker()
    game.monsters.register({
        id = "ccb_mutant_stalker",
        name = "Shadow Stalker",
        description = "A specialized predator covered in light-absorbing chitinous armor, adapted for lethal ambush strikes from darkness.",
        symbol = "s",
        color = "dark_gray",
        size = "MEDIUM",
        species = { "MUTANT", "NETHER" },
        
        -- Combat & Survival Stats
        hp = 160,
        speed = 135,          -- Movement speed 135 (35% faster than human base)
        aggression = 80,      -- High hunting aggression
        morale = 95,          -- High morale
        diff = 24,            -- Danger rating score
        
        -- Armor & Resistances
        armor = {
            bash = 8,
            cut = 18,         -- Rigid chitin shell
            bullet = 12,
            acid = 4,
            electric = 0,     -- Vulnerable to electricity
        },
        
        -- Melee Attack Profile
        melee = {
            skill = 6,
            dice = 3,
            sides = 8,
            damage = {
                cut = 12,
                pierce = 8,
                bash = 4,
            },
            effects = {
                { id = "bleed", duration = 30 }
            }
        },
        
        -- Creature Flags
        flags = {
            "SEES",
            "HEARS",
            "SMELLS",
            "WARM",
            "CLIMBS",
            "NIGHT_VISION",
        },
        
        -- Special Attacks & Tactical AI
        special_attacks = {
            {
                name = "shadow_pounce",
                cooldown = 8, -- 8 turns cooldown
                condition = function(monster, target)
                    local dist = monster:pos():distance_to(target:pos())
                    return dist >= 2 and dist <= 4 and monster:sees(target)
                end,
                execute = function(monster, target)
                    game.add_msg("danger", "%s leaps through the darkness toward %s!", monster:get_name(), target:get_name())
                    monster:set_pos(target:pos():nearest_empty_neighbor())
                    target:apply_damage(monster, "pierce", 26)
                    target:add_effect("stunned", 1)
                end
            }
        },
        
        -- Death Drops
        death_drops = {
            items = {
                { id = "meat", count = { 4, 8 }, prob = 1.0 },
                { id = "bone", count = { 6, 12 }, prob = 1.0 },
                { id = "chitin_piece", count = { 3, 6 }, prob = 0.8 },
            }
        }
    })
end

return monsters
```

---

## 3. Tutorial 2: Boss Monster with Auras and Minion Spawning

```lua
function monsters.register_broodmother()
    game.monsters.register({
        id = "ccb_broodmother",
        name = "Parasitic Broodmother",
        symbol = "B",
        color = "magenta",
        size = "LARGE",
        hp = 650,
        speed = 70,
        
        -- Periodic Aura on turn tick
        on_turn = function(monster)
            if game.time.turn() % 10 == 0 then
                local center = monster:pos()
                map.create_cloud("gas_neurotoxin", center, 3, 50)
            end
        end,
        
        special_attacks = {
            {
                name = "spawn_larvae",
                cooldown = 15,
                execute = function(monster, target)
                    game.add_msg("warning", "%s convulses and spawns voracious larvae!", monster:get_name())
                    for i = 1, 3 do
                        local pt = monster:pos():random_empty_neighbor()
                        if pt then
                            map.spawn_monster("ccb_mutant_larva", pt)
                        end
                    end
                end
            }
        }
    })
end
```

---

## 4. In-Game Testing

Load the script in `main.lua`:
```lua
local monsters = require("monsters/stalker")

events.on("game_load", function()
    monsters.register_stalker()
end)
```
Open `Debug Menu -> Spawn Monster`, type `ccb_mutant_stalker`, and spawn the creature for live testing!
