---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: subsystems.vehicles
title: 车辆动力学与模块化部件系统技术手册
language: zh_CN
status: stale
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
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: ea40ed26f341791e0c157c046b02ca1ce4386d1ec29df2abd305f08c97d7f5fb
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
stale_reason: Contains retired Lua API examples; Lua sections need Platform v1 source verification.
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/subsystems/vehicles/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/subsystems/vehicles/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/subsystems/vehicles/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/subsystems/vehicles/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28subsystems.vehicles%29%3A+&body=Document+ID%3A+subsystems.vehicles%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

> **Lua 内容待修订：** 本页仍含已移除的 v5 接口或旧运行时示例，不可作为当前 Lua 开发依据。请使用 [Platform v1 入门](../api/lua/v1/overview.md)。

# 车辆动力学与模块化部件系统技术手册 (Vehicles & Parts Manual)

本手册详细剖析 **Cataclysm: Cleanwater Bomb (CCB)** 的车辆物理引擎、刚体动力学模拟以及模块化部件（Vehicle Parts）装配机制。

---

## 1. 车辆刚体动力学模型

在 CCB 引擎中，车辆并非单一的碰撞盒子，而是由多个互联底盘框架（Frame）构成的 **2D 刚体物理多体系统**：

* **质心与质量分布 (Center of Mass)**：每个安装的部件（重型柴油机、装甲钢板、储水罐）均贡献质量与局部惯性矩，直接影响车辆急转弯时的侧倾翻滚风险。
* **发动机动力与传动比**：多引擎联动输出功率（马力与扭矩），综合计算地面滚阻、空气阻力（风阻截面积）与加速曲线。
* **轮胎抓地力与地形适应性**：越野宽胎与公路胎在泥地、深水、柏油路面的摩擦牵引力差异显著。

---

## 2. 模块化部件架构 (`vpart_reference`)

一辆车由网格化的部件槽位（Mount Coordinates）组成：

* **框架与车顶 (Frames & Roofs)**：构成车体骨架与防翻滚保护。
* **动力与储能 (Engines & Batteries)**：燃油发动机、电动机、氢燃料电池组与太阳能电板。
* **储物与容积 (Cargo & Tanks)**：车载冷冻箱、储物后备箱以及连入车辆管网的车载净水箱。
* **装甲与外挂 (Armor & Turrets)**：复合防弹装甲插板与自动化感应炮塔。

---

## 3. 核心 API 参考

### `vehicle:get_speed() -> integer`

获取车辆当前的实时行驶速度（单位：mph 或 km/h 换算内部速度单位）。

---

### `vehicle:fuel_left(fuel_type) -> integer`

查询车辆各类油箱/电池组中剩余的指定燃料总量。

**参数 (Parameters):**
* `fuel_type` (*string*, 必填): 燃料类型标识符（如 `"diesel"`, `"gasoline"`, `"battery"`）。

**实战示例 (Example):**
```lua
-- 检查车载电量是否充足
local power = current_veh:fuel_left("battery")
if power < 1000 then
    game.add_msg("warning", "仪表盘电量告警：车载蓄电池电量过低！")
end
```
