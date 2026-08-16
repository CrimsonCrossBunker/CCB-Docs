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
translation_source_fingerprint: c029e08e0748ea803758654a8ace577e544623452fbbd0ccf8f5ec0b5511fc61
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
- [CCB Lua 0.1 Platform Overview](api/lua/v5/overview.md): Learn zero-config Mod discovery, native transactional commits, and generation-safe handles.
- [Complete Example Mod](api/lua/v5/example-mod.md): Walk through a working Mod with modules, state, and custom actions.
- [First Contribution Guide](getting-started/first-contribution.md): The fastest path from local environment to your first Pull Request.

### ⚔️ 2. Core Subsystems Manual
- [Characters & Creatures Manual](subsystems/character.md): Entity inheritance, 12-part anatomical health model, stamina/pain, and buffs.
- [Items & Pockets Manual](subsystems/items.md): Metric physical standards, recursive multi-pocket containers, and item actions.
- [Map & Mapgen Manual](subsystems/map.md): 3D spatial grids, terrain/furniture collision rules, and procedural blueprint matrices.
- [Combat & Damage Manual](subsystems/combat.md): 7 physical damage types, armor coverage rolls, and damage hook interception.
- [Finite Water & Environment Manual](subsystems/water.md): Mass-conserving fluid simulation, storm radar forecasting, and field diffusion.
- [Vehicles & Parts Manual](subsystems/vehicles.md): Rigid-body center-of-mass physics, powertrain torque, and modular part mount slots.

### 🌙 3. CCB Lua 0.1 Platform Reference
- [Native Events & Hook Interception](api/lua/v5/events.md): Subscribe to native engine events, intercept and override decisions synchronously.
- [Portable Responsive Lua UI](api/lua/v5/ui.md): Build responsive windows tailored for PC keyboard and Android touch HUD.
- [Permission Manifest & Capabilities](api/lua/v5/capabilities.md): Understand the capability declaration system and memory sandbox boundaries.

### 🍳 4. Pure-Lua Creation Cookbooks
- [Pure-Lua Items and Pockets Cookbook](api/lua/v5/cookbook/items.md): High-frequency tactical blades, ballistic chest rigs, and nested pouches.
- [Pure-Lua Monsters and AI Cookbook](api/lua/v5/cookbook/monsters.md): Stealth stalkers, aura bosses, and dynamic special attacks.
- [Pure-Lua Mapgen & Structures Cookbook](api/lua/v5/cookbook/mapgen.md): Procedurally generate outpost bunkers and ASCII matrix blueprints.

### ⚙️ 5. C++ Engine Core & Native Bindings
- [Core Engine Lifecycle & Main Loop Deep-Dive](architecture/core-engine-lifecycle.md): Complete control flow from bootstrap, content loading to `process_turn` loop.
- [Engine Subsystems Deep Dive](architecture/subsystems-deep-dive.md): Entities, sliding map cache, item pocket trees, finite water, and physics.
- [Core Development & Contribution Guide](contributing/core-dev-guide.md): Linux/Windows/Android setup, C++20 standards, Catch2 tests, and PR practices.
- [C++ Native Binding & Lua Export Guide](cpp/native-binding-guide.md): Sol2 bindings, LuaLS annotations, and 100% coverage gates.
- [Build & Compilation Overview](build/overview.md): Learn CMake and Make modern build workflows and multi-platform support.

### 📚 6. Full API Dictionary
| Category | Quick Entry | Description |
| --- | --- | --- |
| 📦 **Classes & Handles** | [View Classes](api/lua/v5/reference/classes.md) | `Character`, `Creature`, `Item`, `Map`, `Mapgen`, `Vehicle`, etc. |
| ⚡ **Native Events** | [View 113 Events](api/lua/v5/reference/events.md) | Turn turns, movements, damage, spell casts, gear equips, etc. |
| 🪝 **Native Hooks** | [View 52 Hooks](api/lua/v5/reference/hooks.md) | Intercept and override game decisions synchronously. |
| 🔧 **Global Functions** | [View Functions](api/lua/v5/reference/functions.md) | All utility functions and static methods exposed by the engine. |
| 🎮 **Namespaces** | [View Namespaces](api/lua/v5/reference/namespaces.md) | `game.*`, `map.*`, `player.*`, `ui.*`, and other top-level tables. |
| 🎭 **Callback Actors** | [View Callbacks](api/lua/v5/reference/callbacks.md) | Player actions, IUSE callbacks, and activity execution targets. |
| 🏷️ **Enums & Constants** | [View Enums](api/lua/v5/reference/enums.md) | Damage types, body parts, weather types, terrain flags, etc. |

### 🏛️ 7. Project Governance & Policies
- [Responsible Human](contributing/responsible-human.md): Understand our accountability model for human and AI-assisted contributions.
