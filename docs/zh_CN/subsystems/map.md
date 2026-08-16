---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: subsystems.map
title: 地图与程序化生成技术手册
language: zh_CN
status: active
doc_type: explanation
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
translation_source_fingerprint: b127ae98a838029ef6a31fb5a7740699bc02cecae605021f8792122938fdd0a9
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/subsystems/map/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/subsystems/map/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/subsystems/map/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/subsystems/map/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28subsystems.map%29%3A+&body=Document+ID%3A+subsystems.map%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 地图与程序化生成技术手册 (Map & Mapgen Manual)

本手册详细介绍 **Cataclysm: Cleanwater Bomb (CCB)** 的三维立体空间模型、滑动窗口地图缓存以及纯 Lua 程序化地块生成（Mapgen）技术。

---

## 1. 三维空间与地图分层网格

CCB 采用三维立体网格坐标系统：

1. **三维坐标向量 `Tripoint(x, y, z)`**：
   * $x, y$：水平面网格（东/南/西/北方向）。
   * $z$：竖直高度层级。`0` 代表地面地表层，负数（`-1, -2...`）代表地下避难所与矿井，正数（`1, 2...`）代表高楼天台与屋顶。
2. **Submap 单元**：基础地图数据以 **$12 \times 12 \times 1$** 格为一个 Submap 单元。
3. **Mapgen 标准地块**：标准单地块生成器以 **$24 \times 24$** 格（$2 \times 2$ 个 Submap）为单位进行建筑填充。
4. **滑动视口缓存 (`map`)**：引擎在玩家周围维持一个 $11 \times 11$ 个 Submap 的活跃区域，实现无缝边界移动。

---

## 2. 地形 (Terrain) 与家具 (Furniture) 物理规则

* **地形 (`Terrain`)**：构成地面的永久结构（如土地、混凝土墙、深水、悬崖）。
* **家具 (`Furniture`)**：位于地形上方的可移动/可破坏物件（如桌子、储物货架、床、发电机、路障）。
* **碰撞与视线穿透规则**：
  * `t_wall`（实体墙）：阻挡移动、阻挡视线、阻挡流体。
  * `t_window`（玻璃窗）：阻挡移动、**允许视线与光线穿透**。
  * `f_rack_metal`（金属货架）：阻挡移动、允许视线穿透、提供物品堆叠容器。

---

## 3. Mapgen 生成器与上下文 API (`MapgenContext`)

### `context:set_terrain(x, y, terrain_id)`

设置指定网格坐标的地形。

**参数 (Parameters):**
* `x, y` (*integer*, 必填): 本地网格坐标 ($0 \sim 23$)。
* `terrain_id` (*string*, 必填): 目标地形标识符（如 `"t_concrete_floor"`, `"t_wall_metal"`）。

---

### `context:set_furniture(x, y, furniture_id)`

在指定网格坐标放置家具。

---

### `context:spawn_loot(x, y, loot_config)`

在指定位置生成战利品池。

**参数 (Parameters):**
* `loot_config` (*table*, 必填): 包含 `group`（掉落物组 ID）、`count`（生成数量区间 `{min, max}`）与 `chance`（生成概率 $0.0 \sim 1.0$）。

---

## 4. 实战：纯 Lua 蓝图矩阵绘制示例

```lua
-- 绘制包含安全门、床铺与物资货架的避难所前哨
local blueprint = {
    "########################",
    "#........|.............#",
    "#..B.....|.............#",
    "#--------+-------------#",
    "#......................#",
    "#..r........GG.........#",
    "#......................#",
    "########################"
}

local legend = {
    ["#"] = { terrain = "t_reinforced_wall" },
    ["."] = { terrain = "t_concrete_floor" },
    ["+"] = { terrain = "t_door_c" },
    ["-"] = { terrain = "t_wall_glass" },
    ["|"] = { terrain = "t_wall_glass" },
    ["B"] = { terrain = "t_concrete_floor", furniture = "f_bed" },
    ["r"] = { terrain = "t_concrete_floor", furniture = "f_rack_metal" },
    ["G"] = { terrain = "t_concrete_floor", furniture = "f_generator" }
}

game.mapgen.register({
    id = "ccb_outpost_bunker",
    om_terrain = "ccb_outpost",
    generate = function(context)
        context:draw_matrix(0, 0, blueprint, legend)
    end
})
```
