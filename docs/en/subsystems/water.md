---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: subsystems.water
title: Finite Water and Environment Manual
language: en
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
translation_source_fingerprint: 4d061b163618f65ddebc716bfd48eebf9ff7d3061c5ffba9cb06daa54d3f26ea
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/subsystems/water/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28subsystems.water%29%3A+&body=Document+ID%3A+subsystems.water%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Finite Water & Environment Manual

This manual details the **Finite Water fluid simulation**, micro-weather forecasting, and environmental field diffusion mechanics in **Cataclysm: Cleanwater Bomb (CCB)**.

---

## 1. Finite Water Dynamics

Unlike traditional forks with infinite water tiles, CCB simulates water as a mass-conserving fluid grid:

* **Mass Conservation**: Each tile stores precise fluid volume in milliliters. Water flows down slopes and pools in terrain depressions.
* **Depletion & Drainage**: Pumping water genuinely lowers the water table until depleted.
* **Precipitation & Evaporation**: Storms replenish surface water, while hot arid conditions evaporate pools.

---

## 2. Weather & Storm Forecast APIs

### `game.weather.get_storm_forecast(target_pos, forecast_hours) -> table`

Queries meteorological storm forecasts for target coordinates within a specified window.

**Parameters:**
* `target_pos` (*Tripoint*, required): Target 3D coordinates.
* `forecast_hours` (*integer*, required): Forecast window in hours.

**Returns:**
* *table*: Forecast structure with `has_storm` (*boolean*), `intensity` (*number*), `wind_speed` (*number*, km/h), and `predicted_turn` (*integer*).

**Example:**
```lua
local forecast = game.weather.get_storm_forecast(player:pos(), 6)
if forecast.has_storm and forecast.intensity > 0.7 then
    game.add_msg("warning", "Radar Warning: Severe storm arriving with winds up to %.1f km/h!", forecast.wind_speed)
end
```

---

## 3. Environmental Fields & Diffusion

* **Fire Fields (`fd_fire`)**: Consumes oxygen and flammable fuel, spreading along combustible structures.
* **Smoke Fields (`fd_smoke`)**: Blocks long-range visibility and causes choking damage without filters.
* **Toxic Gas (`fd_gas_vent`)**: Requires airtight NBC protection.
