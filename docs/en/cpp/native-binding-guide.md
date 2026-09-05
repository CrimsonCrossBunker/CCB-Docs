---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.native-binding-guide
title: C++ Native Binding Guide
language: en
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/native-binding-guide/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.native-binding-guide%29%3A+&body=Document+ID%3A+cpp.native-binding-guide%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

> **Lua sections need revision:** This page contains removed v5 APIs or old runtime examples. Do not use its Lua examples for current development. Start with [Platform v1](../api/lua/v1/overview.md).

# C++ Native Binding & Lua Export Guide

This guide describes the standard workflow for C++ engine contributors to bind internal classes, structs, and methods via **Sol2** and safely export them to the **CCB Lua 0.1** runtime.

---

## 1. Architectural Rules & Safety Model

In the CCB engine, native bindings must adhere to 3 strict rules:
1. **Generation-Safe Handles**:
   - Raw C++ pointers (`Character*`, `item*`, `monster*`) must never be held indefinitely in Lua.
   - Dynamic entities must be wrapped in a `game_handle` that verifies generation counters (`runtime_generation`, `world_generation`) upon dereference to prevent dangling pointer crashes.
2. **Zero-Copy In-Memory Invocation**:
   - C++ and Lua interact directly through the Sol2 / Lua-C stack in memory. No intermediate JSON serialization is used.
3. **100% Contract Coverage & LuaLS Parity**:
   - Every exported symbol must be paired with complete LuaLS type definitions in `data/lua/types/ccb_api_v5.d.lua` and pass `check_coverage.py`.

---

## 2. Step 1: Implementing Native Bindings in C++

```cpp
// src/catalua_ui_weather.cpp
#include "weather.h"
#include "catalua_platform_content.h"
#include <sol/sol.hpp>

namespace catalua {

sol::table get_storm_forecast(
    lua_State *lua,
    const game_handle &target_pos,
    const int forecast_hours )
{
    sol::state_view state( lua );
    
    // Capability check
    require_capability( state, "game.read", "game.weather.get_storm_forecast" );
    
    // Native C++ engine invocation
    const weather_forecast forecast = weather_manager::forecast_at( target_pos.pos(), forecast_hours );
    
    sol::table result = state.create_table();
    result["has_storm"] = forecast.has_storm;
    result["intensity"] = forecast.intensity;
    result["wind_speed"] = forecast.wind_speed;
    result["predicted_turn"] = forecast.predicted_turn;
    
    return result;
}

void register_weather_bindings( sol::state_view &lua ) {
    sol::table weather_ns = lua["game"]["weather"].get_or_create<sol::table>();
    weather_ns["get_storm_forecast"] = &get_storm_forecast;
}

} // namespace catalua
```

---

## 3. Step 2: Providing LuaLS Type Annotations (`.d.lua`)

In `data/lua/types/ccb_api_v5.d.lua`:

```lua
---@class WeatherForecast
---@field has_storm boolean Whether a storm is forecasted
---@field intensity number Storm intensity index (0.0 to 1.0)
---@field wind_speed number Forecasted wind speed in km/h
---@field predicted_turn integer Forecasted arrival turn

---Query forecasted severe weather conditions for target coordinates
---@param target_pos Tripoint Target tripoint
---@param forecast_hours integer Forecast window in hours
---@return WeatherForecast Forecast structure
function game.weather.get_storm_forecast(target_pos, forecast_hours) end
```

---

## 4. Step 3: Contract Generation & 100% Coverage Checks

Run local contract validators:

```bash
# 1. Regenerate C++ export inventory
python3 tools/lua_api/generate_ccb_inventory.py

# 2. Regenerate public contract & coverage
python3 tools/lua_api/generate_public_contract.py

# 3. Verify coverage & declarations
python3 tools/lua_api/check_coverage.py --require-complete
python3 tools/lua_api/check_luals_declarations.py
python3 -m unittest discover -s tools/lua_api -p 'test_*.py'
```
