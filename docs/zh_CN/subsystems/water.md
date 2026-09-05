---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: subsystems.water
title: 有限水体与环境物理系统技术手册
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
translation_source_fingerprint: 8d9d58ba0c51f8b017d3eb285ce299da4ca738424836afbbac6ca997822d43c4
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/subsystems/water/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/subsystems/water/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/subsystems/water/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/subsystems/water/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28subsystems.water%29%3A+&body=Document+ID%3A+subsystems.water%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

> **Lua 内容待修订：** 本页仍含已移除的 v5 接口或旧运行时示例，不可作为当前 Lua 开发依据。请使用 [Platform v1 入门](../api/lua/v1/overview.md)。

# 有限水体与环境物理系统技术手册 (Finite Water & Environment Manual)

本手册详细剖析 **Cataclysm: Cleanwater Bomb (CCB)** 独创的 **有限水体流体动力学（Finite Water System）**、微气象模拟与环境物理场机制。

---

## 1. 有限水体物理动力学 (Finite Water Dynamics)

在传统分支中，水体常被视为静态、无穷无尽的装饰背景。而在 CCB 引擎中，水体是一套遵循**严格质量守恒定律**的高精度流体网格系统：

* **体积守恒与流动网格**：
  - 每一个网格单元记录流体体积（毫升）。
  - 水体会受到重力驱动，沿着地势高低差和三维楼层阶梯向低处流动并在低洼地形自然聚集成池塘。
* **水体交互机制**：
  - **水泵抽取与灌溉**：水体被水泵抽走后，该网格的实际水位会真实下降，直至枯竭。
  - **降雨补充与蒸发**：暴风雨天气会持续增加地表水体积；在干燥高温环境中水体会逐渐蒸发消散。
  - **阻力与阻断**：密闭大门与混凝土防水堤坝可以有效阻断水流扩散。

---

## 2. 天气系统与雷暴预报 (Weather & Forecast)

CCB 的天气系统根据气压、温度与风向生成动态微气象：

### `game.weather.get_storm_forecast(target_pos, forecast_hours) -> table`

查询指定坐标在未来指定时间窗口内的强对流风暴与气象预警。

**参数 (Parameters):**
* `target_pos` (*Tripoint*, 必填): 目标三维网格坐标。
* `forecast_hours` (*integer*, 必填): 预报展望时间跨度，**单位：小时**。

**返回值 (Returns):**
* *table*: 气象预报结构体，包含以下字段：
  * `has_storm` (*boolean*): 是否有强对流暴风雨/雷暴降临。
  * `intensity` (*number*): 风暴强度指数（`0.0 ~ 1.0`）。
  * `wind_speed` (*number*): 预测风速，**单位：km/h**。
  * `predicted_turn` (*integer*): 预计风暴抵达的游戏回合数。

**实战示例 (Example):**
```lua
-- 查询当前避难所上方未来 6 小时的风暴预警
local forecast = game.weather.get_storm_forecast(player:pos(), 6)
if forecast.has_storm and forecast.intensity > 0.7 then
    game.add_msg("warning", "气象雷达警报：一场强热带风暴预计将在 %d 回合后降临，风速可达 %.1f km/h！", 
        forecast.predicted_turn - game.time.turn(), forecast.wind_speed)
end
```

---

## 3. 环境物理场与扩散模拟 (Fields & Diffusion)

引擎中的火焰、浓烟、毒雾与酸液通过 `field_entry` 进行物理演化：

* **火焰场 (`fd_fire`)**：根据周围地形材质的易燃度消耗氧气并向邻近格蔓延，释放高温热辐射与浓烟。
* **烟雾场 (`fd_smoke`)**：阻挡远程视线射程，长时间吸入会导致角色剧烈咳嗽与窒息伤害。
* **毒气与神经毒素 (`fd_gas_vent`)**：需要气密防毒面具或防化服阻隔。
