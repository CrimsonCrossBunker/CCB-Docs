---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: home
title: CCB Developer Documentation
language: en
status: active
doc_type: explanation
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 180
last_human_reviewer: LYHGLYTX
source_paths:
- AGENTS.md
- GOVERNANCE.md
source_symbols: []
source_queries:
- Sources of truth
- Authority model
source_fingerprint: d304d44d4803e198dce1a691465b13f1b04d5812ae3d5a8cb1aaa54ea5193c7b
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-01'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 9b7a15d02359cbafb53035ecd09d311a33440c72da3b3a8d2c594fcb632af0fd
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: project-context
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/AGENTS.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/GOVERNANCE.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28home%29%3A+&body=Document+ID%3A+home%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# CCB Developer Documentation

This is the official developer guide, API reference, and architecture navigation site for Cataclysm: Cleanwater Bomb.

This site is dedicated to two primary developer groups: **Mod Authors** and **Core C++ Engine Developers**.

---

## Quick Navigation & Manual Directory

### 🚀 1. Getting Started & Mental Models
- [Lua Platform v1: zero to running](api/lua/v1/overview.md): the only supported Lua MOD entry point and a minimal example.
- [First Contribution Guide](getting-started/first-contribution.md): The fastest path from local environment to your first Pull Request.

### ⚔️ 2. Core Subsystems Manual
- [Characters & Creatures Manual](subsystems/character.md): Entity inheritance, 12-part anatomical health model, stamina/pain, and buffs.
- [Items & Pockets Manual](subsystems/items.md): Metric physical standards, recursive multi-pocket containers, and item actions.
- [Map & Mapgen Manual](subsystems/map.md): 3D spatial grids, terrain/furniture collision rules, and procedural blueprint matrices.
- [Combat & Damage Manual](subsystems/combat.md): 7 physical damage types, armor coverage rolls, and damage hook interception.
- [Finite Water & Environment Manual](subsystems/water.md): Mass-conserving fluid simulation, storm radar forecasting, and field diffusion.
- [Vehicles & Parts Manual](subsystems/vehicles.md): Rigid-body center-of-mass physics, powertrain torque, and modular part mount slots.

### 🌙 3. CCB Lua Platform v1
- [Quickstart and version rules](api/lua/v1/overview.md): create, install, and check your first Lua MOD.
- [Complete LuaLS declarations](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/master/data/lua/types/ccb_platform_v1.d.lua): detailed functions, parameters, returns, and types.
- [Machine-readable API contract](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/master/data/lua/reference/ccb_platform_api_v1.json): generator input and API change checks.
- [Complete example MOD](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/tree/master/data/mods/Lua_First_Example): real code organized by game domain.
- [CCB-MOD catalog](https://crimsoncrossbunker.github.io/CCB-MOD/): find, install, or register external MODs.

### ⚙️ 4. C++ Engine Core & Native Bindings
- [Core Engine Lifecycle & Main Loop Deep-Dive](architecture/core-engine-lifecycle.md): Complete control flow from bootstrap, content loading to `process_turn` loop.
- [Engine Subsystems Deep Dive](architecture/subsystems-deep-dive.md): Entities, sliding map cache, item pocket trees, finite water, and physics.
- [Core Development & Contribution Guide](contributing/core-dev-guide.md): Linux/Windows/Android setup, C++20 standards, Catch2 tests, and PR practices.
- [C++ Native Binding & Lua Export Guide](cpp/native-binding-guide.md): Sol2 bindings, LuaLS annotations, and 100% coverage gates.
- [Build & Compilation Overview](build/overview.md): Learn CMake and Make modern build workflows and multi-platform support.

### 🏛️ 5. Project Governance & Policies
- [Responsible Human](contributing/responsible-human.md): Understand our accountability model for human and AI-assisted contributions.
