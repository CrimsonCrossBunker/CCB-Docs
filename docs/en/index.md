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
translation_source_fingerprint: d8a9ca0fabfab96a6fe77b122cd552e7584cd6a3096cdae173a99dcdbda07399
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

## Quick Navigation & Entry Points

### 🎯 1. Mod Author Track (CCB Lua 0.1 Native Platform)
CCB provides **CCB Lua 0.1**, a modern pure-Lua content and scripting engine free from legacy data formats:
- [CCB Lua 0.1 Platform Overview](api/lua/v5/overview.md): Learn zero-config Mod discovery, native transactional commits, and generation-safe handles.
- [Complete Example Mod](api/lua/v5/example-mod.md): Walk through a working Mod with modules, state, and custom actions.
- [Events, Hooks, and Callbacks](api/lua/v5/events.md): Subscribe to game events, intercept decisions, and rewrite behaviours synchronously.
- [Portable Lua UI](api/lua/v5/ui.md): Build responsive pages tailored for PC keyboard and Android touch HUD.
- [Permissions & Capabilities](api/lua/v5/capabilities.md): Understand the capability declaration and sandbox model.

#### 📚 API Reference Direct Links
| Category | Quick Entry | Description |
| --- | --- | --- |
| 📦 **Classes & Handles** | [View Classes](api/lua/v5/reference/classes.md) | `Character`, `Creature`, `Item`, `Map`, `Mapgen`, `Vehicle`, etc. |
| ⚡ **Native Events** | [View 113 Events](api/lua/v5/reference/events.md) | Turn turns, movements, damage, spell casts, gear equips, etc. |
| 🪝 **Native Hooks** | [View 52 Hooks](api/lua/v5/reference/hooks.md) | Intercept and override game decisions synchronously. |
| 🔧 **Global Functions** | [View Functions](api/lua/v5/reference/functions.md) | All utility functions and static methods exposed by the engine. |
| 🎮 **Namespaces** | [View Namespaces](api/lua/v5/reference/namespaces.md) | `game.*`, `map.*`, `player.*`, `ui.*`, and other top-level tables. |
| 🎭 **Callback Actors** | [View Callbacks](api/lua/v5/reference/callbacks.md) | Player actions, IUSE callbacks, and activity execution targets. |
| 🏷️ **Enums & Constants** | [View Enums](api/lua/v5/reference/enums.md) | Damage types, body parts, weather types, terrain flags, etc. |

### 🛠️ 2. Core & Engine Developer Track (C++ Engine & Build)
For contributors building core systems, game mechanics, and native bindings:
- [Project Map & Architecture](architecture/project-map.md): Navigate C++ subsystems, source boundaries, and test routing.
- [Build Overview](build/overview.md): Learn CMake and Make modern build workflows and multi-platform support.
- [Validation & Testing](validation/quickstart.md): Run Catch2 unit test suites and fast validator tools.
- [Native Lua Bridge & Bindings](cpp/lua-bridge.md): Understand the bridge between the C++ engine and Lua 0.1 runtime.

### 🏛️ 3. Project Governance & Policies
- [First Contribution](getting-started/first-contribution.md): The fastest path from local environment to your first Pull Request.
- [Responsible Human](contributing/responsible-human.md): Understand our accountability model for human and AI-assisted contributions.
