---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: subsystems.vehicles
title: Vehicles and Parts Manual
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/subsystems/vehicles/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28subsystems.vehicles%29%3A+&body=Document+ID%3A+subsystems.vehicles%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

> **Lua sections need revision:** This page contains removed v5 APIs or old runtime examples. Do not use its Lua examples for current development. Start with [Platform v1](../api/lua/v1/overview.md).

# Vehicles & Parts Manual

This manual details the rigid-body vehicle physics simulation, powertrain calculations, and modular part systems in **Cataclysm: Cleanwater Bomb (CCB)**.

---

## 1. Rigid-Body Vehicle Physics

Vehicles in CCB operate as multi-part 2D rigid bodies:

* **Center of Mass & Weight Distribution**: Parts (engines, armor plates, water tanks) dynamically shift vehicle mass and inertia tensors, directly governing roll-over tendencies during sharp turns.
* **Powertrain & Aerodynamics**: Combines engine horsepower, torque curves, tire rolling resistance, and frontal aerodynamic drag.
* **Traction & Ground Conditions**: Differentiates off-road vs highway tires across mud, deep water, and asphalt.

---

## 2. Modular Part Architecture (`vpart_reference`)

* **Frames & Chassis**: Structural foundation.
* **Powertrain**: Diesel/gasoline engines, electric motors, batteries, solar panels.
* **Storage & Tanks**: Cargo trunks, vehicle freezers, and integrated fluid reservoirs.
* **Armor & Weapon Mounts**: Composite ballistic armor and autonomous automated turrets.

---

## 3. Core APIs

### `vehicle:get_speed() -> integer`
Returns real-time vehicle velocity.

### `vehicle:fuel_left(fuel_type) -> integer`
Queries total remaining fuel or stored electrical charge.
