---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.cookbook.mapgen
title: 纯 Lua 地块与建筑生成实战
language: zh_CN
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/cookbook/mapgen/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.cookbook.mapgen%29%3A+&body=Document+ID%3A+api.lua.cookbook.mapgen%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 纯 Lua 地块与建筑生成实战 (Mapgen Cookbook)

在 **CCB Lua 0.1** 体系中，Mod 作者可以直接使用 Lua 代码编写地块生成器（Mapgen），以算法化、程序化生成的方式创造自定义废墟、避难所、实验室与野外特殊地标。

---

## 1. 地图坐标与生成架构

CCB 地图生成遵循标准的局部地图网格模型：
1. **地块尺寸**：标准单个地块（Submap Grid）为 **24 × 24** 格（包含 $z$ 轴立体坐标）。
2. **纯 Lua 绘制上下文**：生成器接收一个 `MapgenContext` 对象，提供 `set_terrain`、`set_furniture`、`spawn_item`、`spawn_monster` 等高性能 C++ 内存直连方法。
3. **Overmap 绑定**：通过 Overmap 特殊地标标识符（`overmap_special`）将地块生成逻辑自动与大地图世界生成算法对接。

---

## 2. 实战一：纯 Lua 算法化生成地下避难所哨站

```lua
-- mods/underground_bunkers/mapgen/outpost.lua
local mapgen = {}

function mapgen.register_outpost()
    game.mapgen.register({
        id = "ccb_survival_outpost",
        om_terrain = "ccb_bunker_outpost", -- 对应的大地图地块类型
        weight = 100,                      -- 随机生成权重
        
        -- 生成器入口函数
        generate = function(context)
            -- 1. 全局填充基础混凝土外墙与地面 (24x24 网格)
            for x = 0, 23 do
                for y = 0, 23 do
                    if x == 0 or x == 23 or y == 0 or y == 23 then
                        context:set_terrain(x, y, "t_reinforced_concrete_wall")
                    else
                        context:set_terrain(x, y, "t_concrete_floor")
                    end
                end
            end
            
            -- 2. 雕刻入口安全气闸舱门 (北侧中心)
            context:set_terrain(11, 0, "t_reinforced_door_closed")
            context:set_terrain(12, 0, "t_reinforced_door_closed")
            
            -- 3. 划分内部功能区域 (使用矩形填充工具)
            -- 3.1 储物区 (左上角)
            context:fill_furniture(2, 2, 8, 4, "f_rack_metal")
            -- 在货架上随机生成战利品
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
            
            -- 3.2 医疗与休息区 (右上角)
            context:set_furniture(18, 3, "f_hospital_bed")
            context:set_furniture(20, 3, "f_medical_cabinet")
            context:spawn_loot(20, 3, {
                group = "medical_supplies",
                count = { 2, 5 }
            })
            
            -- 3.3 核心发电机与动力终端 (正中央)
            context:set_furniture(11, 11, "f_diesel_generator")
            context:set_furniture(12, 11, "f_terminal_console")
            
            -- 4. 随机生成守卫或环境威胁
            if math.random() < 0.3 then
                -- 30% 几率刷出休眠哨兵机械人
                context:spawn_monster(11, 13, "mon_security_bot")
            end
        end
    })
end

return mapgen
```

---

## 3. 实战二：使用 ASCII 字符蓝图（Blueprint 矩阵绘制）

对于精细排布的室内房间，CCB 支持在 Lua 中使用极其直观的字符串矩阵配合符号字典进行批量绘制：

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

## 4. 调试与即时生成

启动游戏进入世界后：
1. 打开调试菜单：`Debug Menu -> Map -> Map Editor / Teleport to Overmap`；
2. 或者调用 Lua 调试命令：`game.map.generate_test("ccb_survival_outpost")` 即时在当前地块刷出完整建筑进行测试！
