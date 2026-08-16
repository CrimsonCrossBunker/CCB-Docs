---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.cookbook.mapgen
title: Mapgen and Structures Cookbook
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
translation_source_fingerprint: 7b5d114a976aa1a8f56fb718898b7d58d29d0bf5d29698af121c3930f54947f9
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/cookbook/mapgen/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/cookbook/mapgen/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/cookbook/mapgen/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/cookbook/mapgen/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.cookbook.mapgen%29%3A+&body=Document+ID%3A+api.lua.cookbook.mapgen%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Pure-Lua Mapgen & Structures Cookbook

In **CCB Lua 0.1**, Mod authors can write procedural map generators (Mapgen) in pure Lua to create ruins, underground shelters, laboratories, and wilderness landmarks.

---

## 1. Coordinates and Mapgen Architecture

CCB map generation follows a standard local grid architecture:
1. **Grid Dimensions**: A standard submap grid is **24 × 24** tiles per $z$-level.
2. **Pure Lua Execution Context**: The generator receives a `MapgenContext` object providing direct C++ native methods such as `set_terrain`, `set_furniture`, `spawn_loot`, and `spawn_monster`.
3. **Overmap Special Binding**: Generators bind to Overmap terrain types via `om_terrain` identifiers.

---

## 2. Tutorial 1: Algorithmic Survival Outpost

```lua
-- mods/underground_bunkers/mapgen/outpost.lua
local mapgen = {}

function mapgen.register_outpost()
    game.mapgen.register({
        id = "ccb_survival_outpost",
        om_terrain = "ccb_bunker_outpost",
        weight = 100,
        
        generate = function(context)
            -- 1. Outer perimeter walls and floor
            for x = 0, 23 do
                for y = 0, 23 do
                    if x == 0 or x == 23 or y == 0 or y == 23 then
                        context:set_terrain(x, y, "t_reinforced_concrete_wall")
                    else
                        context:set_terrain(x, y, "t_concrete_floor")
                    end
                end
            end
            
            -- 2. Entrance security doors
            context:set_terrain(11, 0, "t_reinforced_door_closed")
            context:set_terrain(12, 0, "t_reinforced_door_closed")
            
            -- 3. Storage racks & loot
            context:fill_furniture(2, 2, 8, 4, "f_rack_metal")
            context:spawn_loot(3, 3, {
                group = "military_rations",
                count = { 3, 6 },
                chance = 1.0
            })
            context:spawn_loot(5, 3, {
                group = "ccb_tactical_gear",
                count = { 1, 2 },
                chance = 0.8
            })
            
            -- 4. Medical bay & power generators
            context:set_furniture(18, 3, "f_hospital_bed")
            context:set_furniture(20, 3, "f_medical_cabinet")
            context:set_furniture(11, 11, "f_diesel_generator")
            context:set_furniture(12, 11, "f_terminal_console")
            
            -- 5. Optional security guards
            if math.random() < 0.3 then
                context:spawn_monster(11, 13, "mon_security_bot")
            end
        end
    })
end

return mapgen
```

---

## 3. Tutorial 2: ASCII Matrix Blueprint Layouts

```lua
function mapgen.register_checkpoint()
    local layout = {
        "########################",
        "#......|..............r#",
        "#..B...|..............r#",
        "#......|........GG.....#",
        "#---+--+-------+--------#",
        "#......................#",
        "#..M........DD.........#",
        "#..M........DD.........#",
        "#......................#",
        "########################"
    }
    
    local legend = {
        ["#"] = { terrain = "t_wall_metal" },
        ["."] = { terrain = "t_floor_metal" },
        ["+"] = { terrain = "t_door_metal_c" },
        ["-"] = { terrain = "t_wall_glass_alarm" },
        ["|"] = { terrain = "t_wall_glass_alarm" },
        ["B"] = { terrain = "t_floor_metal", furniture = "f_bed" },
        ["r"] = { terrain = "t_floor_metal", furniture = "f_rack_metal" },
        ["G"] = { terrain = "t_floor_metal", furniture = "f_generator" },
        ["M"] = { terrain = "t_floor_metal", furniture = "f_table_metal" },
        ["D"] = { terrain = "t_floor_metal", furniture = "f_desk" },
    }
    
    game.mapgen.register({
        id = "ccb_road_checkpoint",
        om_terrain = "road_checkpoint",
        generate = function(context)
            context:draw_matrix(0, 0, layout, legend)
        end
    })
end
```

---

## 4. Live Testing

In-game:
Open `Debug Menu -> Map -> Map Editor` or execute `game.map.generate_test("ccb_survival_outpost")` to instantiate the mapgen block immediately!
