---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.overview
title: CCB Lua 0.1 Overview
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
translation_source_fingerprint: 53ce833aa62cf93c564abc1717e1ef2ea7a482029228ab30c1a0f5226f4a0783
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/overview/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.v5.overview%29%3A+&body=Document+ID%3A+api.lua.v5.overview%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# CCB Lua 0.1 Platform Overview

**CCB Lua 0.1** is the first-generation **pure-Lua native game content and Mod authoring engine** created for Cataclysm: Cleanwater Bomb.

It provides modders and core developers with a cohesive, strongly-typed, and transactionally-safe environment covering items, recipes, monsters, wounds, martial arts, map generation, event subscriptions, synchronous hook intercepts, deterministic turn scheduling, portable UI, and persistent state storage.

---

## Four Core Pillars

1. **Pure-Lua Native Content Creation**
   - Author game entities (items `Item`, recipes `Recipe`, monsters `Monster`, wounds `Wound`, martial arts `MartialArt`, mapgen `Mapgen`) directly in pure Lua code.
   - Benefit from normal control flow, modular decomposition, and reusable functions.

2. **Zero-Configuration Mod Discovery**
   - A valid Mod requires only a single `main.lua` at its root directory.
   - The folder name serves as the Mod ID; no external manifest or configuration files are required.

3. **Transactional Commits & Generation Safety**
   - Mod content stages before global data finalization; syntax or logical conflicts trigger **atomic rollbacks**, preventing world data contamination.
   - Native C++ bare pointers never cross the Lua boundary. All live interaction uses **generation-safe typed handles** and detached read-only snapshots.

4. **First-Class IDE Type Support**
   - Complete LuaLS declaration files provide 100% autocompletion, signature inspection, and static diagnostics in VS Code, Neovim, and other editors.

---

## Runtime API Architecture

CCB Lua 0.1 natively exports 500+ callable functions and methods across all game subsystems:
- **Character & Abilities**: Bionics, mutations, martial arts, skills, and proficiencies.
- **Items & Crafting**: Item attributes, pocket storage, crafting recipes, disassembly, and practice.
- **World & Environment**: Weather, calendar time, furniture, mapgen, and overmap.
- **Creatures & Dialogue**: Monster behavior policies, NPC dialogue trees, and factions.
- **UI & Multi-Platform**: Responsive layout engine adapted for PC keyboards and Android touch controls.

---

## Where to Begin

- **Getting Started**: Start with the [Complete Example Mod](example-mod.md) and [Lifecycle](lifecycle.md).
- **Interface Design**: Read [Portable Lua UI](ui.md).
- **Game Logic Extension**: Read [Events, Hooks, and Callbacks](events.md).
- **Diagnostics**: Read [Debugging and Validation](debugging.md).

---

## Native API Reference

- [Module Entry Points](reference/modules.md) and [Namespaces](reference/namespaces.md)
- [Classes & Records](reference/classes.md) and [Properties](reference/properties.md)
- [Functions](reference/functions.md), [Methods](reference/methods.md), and [Operators](reference/operators.md)
- [Enum Families](reference/enums.md), [Native Events](reference/events.md), [Hooks](reference/hooks.md), and [Callbacks](reference/callbacks.md)
- [Capabilities](reference/capabilities.md) and [Permission Model](reference/permissions.md)

