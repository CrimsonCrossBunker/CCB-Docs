---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.native-binding-guide
title: C++ 引擎底层 Native 绑定指南
language: zh_CN
status: stale
doc_type: how-to
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
translation_source_fingerprint: 7b3f1bdaa4c6e89a3856ed51cb2546ade48e38b3de86daf1e0cb2532c758ee98
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/native-binding-guide/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/native-binding-guide/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/native-binding-guide/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/native-binding-guide/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.native-binding-guide%29%3A+&body=Document+ID%3A+cpp.native-binding-guide%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

> **Lua 内容待修订：** 本页仍含已移除的 v5 接口或旧运行时示例，不可作为当前 Lua 开发依据。请使用 [Platform v1 入门](../api/lua/v1/overview.md)。

# C++ 引擎底层 Native 绑定与 Lua 导出指南 (Engine Native Binding Guide)

本指南面向 CCB 引擎与核心子系统开发者，详尽说明如何为游戏底层的 C++ 类、方法与数据结构添加 **Sol2 原生绑定**，并将其安全地导出给 **CCB Lua 0.1** 运行时的完整标准化流程。

---

## 1. 架构原则与安全模型

在 CCB 引擎中，C++ 到 Lua 的导出必须遵循以下 3 大铁律：
1. **代际安全句柄（Generation-Safe Handles）**：
   - 严禁将裸 C++ 对象指针直接裸露给 Lua 长期持有。
   - 所有动态生命周期实体（如 `Character*`、`item*`、`monster*`）必须包装在 `game_handle` 中，在每次解引用时校验 `runtime_generation` 和 `world_generation`，防止悬垂指针崩溃。
2. **零拷贝内存直连（Zero-Copy Direct In-Memory Invocation）**：
   - C++ 与 Lua 之间通过 Sol2 / Lua-C 虚拟机栈进行参数传递，禁止任何 JSON 字符串中转。
3. **100% 契约覆盖率与静态类型保证**：
   - 每一个新导出的 C++ 符号必须在 `data/lua/types/ccb_api_v5.d.lua` 中提供完整的 LuaLS 类型注解，并通过 `check_coverage.py` 门禁。

---

## 2. 步骤一：在 C++ 中编写原生绑定

假设我们在 C++ 中新增了一个天气雷达系统 `weather_radar`，需要导出查询强对流风暴的方法：

```cpp
// src/catalua_ui_weather.cpp
#include "weather.h"
#include "catalua_platform_content.h"
#include <sol/sol.hpp>

namespace catalua {

// 1. 实现安全包装函数 (包含句柄与边界检查)
sol::table get_storm_forecast(
    lua_State *lua,
    const game_handle &target_pos,
    const int forecast_hours )
{
    sol::state_view state( lua );
    
    // 权限检查: 确保调用方具备天气读取权限
    require_capability( state, "game.read", "game.weather.get_storm_forecast" );
    
    // 调用底层 C++ 引擎方法 (纯内存直连)
    const weather_forecast forecast = weather_manager::forecast_at( target_pos.pos(), forecast_hours );
    
    // 构造返回给 Lua 的表结构
    sol::table result = state.create_table();
    result["has_storm"] = forecast.has_storm;
    result["intensity"] = forecast.intensity;
    result["wind_speed"] = forecast.wind_speed;
    result["predicted_turn"] = forecast.predicted_turn;
    
    return result;
}

// 2. 注册到 Lua 命名空间
void register_weather_bindings( sol::state_view &lua ) {
    sol::table weather_ns = lua["game"]["weather"].get_or_create<sol::table>();
    
    weather_ns["get_storm_forecast"] = &get_storm_forecast;
}

} // namespace catalua
```

---

## 3. 步骤二：编写 LuaLS 类型声明 (`.d.lua`)

在 `data/lua/types/ccb_api_v5.d.lua` 中添加对应的 IDE 类型提示：

```lua
---@class WeatherForecast
---@field has_storm boolean 是否存在暴风雨
---@field intensity number 风暴强度指数 (0.0 ~ 1.0)
---@field wind_speed number 预测风速 (km/h)
---@field predicted_turn integer 预测降临的回合数

---查询指定坐标未来数小时的风暴气象预报
---@param target_pos Tripoint 目标三维网格坐标
---@param forecast_hours integer 预报展望小时数
---@return WeatherForecast 预报结构体
function game.weather.get_storm_forecast(target_pos, forecast_hours) end
```

---

## 4. 步骤三：自动生成契约清单与覆盖率验证

在终端中执行本地契约同步工具：

```bash
# 1. 重新扫描 C++ 导出清单
python3 tools/lua_api/generate_ccb_inventory.py

# 2. 重新生成公共 API 契约与覆盖率
python3 tools/lua_api/generate_public_contract.py

# 3. 运行 100% 覆盖率验证与单测 (CI 门禁)
python3 tools/lua_api/check_coverage.py --require-complete
python3 tools/lua_api/check_luals_declarations.py
python3 -m unittest discover -s tools/lua_api -p 'test_*.py'
```

若全部通过，新导出的 C++ 方法即正式成为 **CCB Lua 0.1** 的一等公民，并在文档站重新构建时自动生成漂亮的 API 参考手册！
