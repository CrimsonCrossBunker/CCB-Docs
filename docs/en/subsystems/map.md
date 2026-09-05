---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: subsystems.map
title: Map and Mapgen Manual
language: en
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
translation_source_fingerprint: ff4c0d735d3e3e34bc8c555549a37d71d7e1e1d028e6b551a030b027f8c5ee74
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/subsystems/map/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28subsystems.map%29%3A+&body=Document+ID%3A+subsystems.map%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

> **Lua sections need revision:** This page contains removed v5 APIs or old runtime examples. Do not use its Lua examples for current development. Start with [Platform v1](../api/lua/v1/overview.md).

# Map & Mapgen Manual

This manual explains the 3D coordinate system, sliding map cache architecture, and pure-Lua procedural map generation (Mapgen) in **Cataclysm: Cleanwater Bomb (CCB)**.

---

## 1. 3D Spatial Grid & Submap Units

1. **`Tripoint(x, y, z)`**:
   * $x, y$: Horizontal Cartesian coordinates.
   * $z$: Elevation index (`0` for ground, negative for subterranean vaults, positive for multi-story towers).
2. **Submap Chunk**: $12 \times 12 \times 1$ tiles per chunk.
3. **Mapgen Standard Grid**: $24 \times 24$ tiles per standard overmap terrain tile.
4. **Sliding Viewport Cache**: The active memory maintains an $11 \times 11$ submap sliding window around the player.

---

## 2. Terrain & Furniture Rules

* **Terrain**: Fixed structural ground geometry (concrete floor, reinforced wall, deep water).
* **Furniture**: Placed on top of terrain (beds, generators, metal racks, consoles).

---

## 3. MapgenContext APIs

### `context:set_terrain(x, y, terrain_id)`
Sets the base terrain type at local coordinate $(x, y)$.

### `context:set_furniture(x, y, furniture_id)`
Places a furniture piece at local coordinate $(x, y)$.

### `context:spawn_loot(x, y, loot_config)`
Spawns loot from a defined item group with probability and count constraints.

---

## 4. Blueprint Matrix Layout Example

```lua
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
