---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: subsystems.items
title: Items and Pockets Manual
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
translation_source_fingerprint: 6eddd8f446b4c2f91b776c7fb6b676cd77c5e79f09fad5cd7d7f0b2bc56fe6fd
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/subsystems/items/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/subsystems/items/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/subsystems/items/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/subsystems/items/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28subsystems.items%29%3A+&body=Document+ID%3A+subsystems.items%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Items & Pockets Manual

This manual details the item entity model, physical unit conversions, and the **Pocket tree container architecture** in **Cataclysm: Cleanwater Bomb (CCB)**.

---

## 1. Physical Units & Standards

CCB enforces consistent metric standards across all items:

* **Weight**: Stored as an integer in **grams (g)**. E.g., `1500` is 1.5 kg.
* **Volume**: Stored as an integer in **milliliters (ml)**. E.g., `2500` is 2.5 L.
* **Length Constraints**: Stored in **millimeters (mm)** for holsters and scabbards.
* **Price**: Stored in **cents**. E.g., `1000` is $10.00.

---

## 2. Pocket Container Tree Architecture

Single-layer inventory arrays are replaced by recursive Pocket trees:

* `max_contains_volume` (*integer*): Maximum volume limit (ml).
* `max_contains_weight` (*integer*): Maximum weight limit (g).
* `max_item_length` (*integer*): Maximum length limit (mm).
* `watertight` (*boolean*): Fluid sealing for liquids and gases.
* `rigid` (*boolean*): If `false`, total volume expands as internal pockets are filled.
* `moves` (*integer*): Action point cost to draw or stow items into this pocket.

---

## 3. Core APIs

### `game.items.register(config)`

Registers a new item archetype with the engine.

**Example:**
```lua
game.items.register({
    id = "ccb_canteen_sealed",
    name = "Sealed Military Canteen",
    weight = 250,  -- 250g dry mass
    volume = 1200, -- 1.2L external volume
    category = "container",
    pockets = {
        {
            pocket_type = "CONTAINER",
            max_contains_volume = 1000, -- 1.0L liquid
            max_contains_weight = 1200,
            watertight = true,          -- Sealed against leaks
            open_container = false
        }
    }
})
```

---

### `item:get_total_weight() -> integer`

Recursively calculates the total weight of the item including all contents inside nested pockets.
