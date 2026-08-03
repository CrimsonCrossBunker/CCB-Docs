---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.lua-bridge
title: Native Lua bridge
language: en
status: active
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- mod-author
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: Pending human review
source_paths:
- src/catalua_bindings.cpp
- src/catalua_ui_manifest.cpp
- src/catalua_ui_registry.cpp
- data/lua/types/ccb_api_v5.d.lua
- data/lua/manifest.schema.json
source_symbols:
- binding_catalog()
source_queries: []
source_fingerprint: f49affe36444cf0aaa8cdbd2064a4c8d6e45e09d96d359984078ec5b326a0c9a
authority: api-contract
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 7e06bb671d6532093277a532546614dadca86a79266039f03d3e5bc7338a800f
prerequisites:
- cpp.mod-loading
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- lua-contract
- cpp-tests
api_version: '5'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/lua-bridge/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/lua-bridge/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/lua-bridge/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/lua-bridge/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: src/catalua_bindings.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/catalua_bindings.cpp
- path: src/catalua_ui_manifest.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/catalua_ui_manifest.cpp
- path: src/catalua_ui_registry.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/catalua_ui_registry.cpp
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/types/ccb_api_v5.d.lua
- path: data/lua/manifest.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/manifest.schema.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.lua-bridge%29%3A+&body=Document+ID%3A+cpp.lua-bridge%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Native Lua bridge

## Responsibility

The bridge embeds Lua and exposes the versioned CCB Lua API. It validates manifests and
capabilities, constructs namespaces and typed values/handles, installs bounded registry
snapshots, routes events/hooks/callbacks/services, and enforces read/write/action permissions.

## Entry points

Read `src/catalua_bindings.cpp`, `src/catalua_ui_manifest.cpp`, and
`src/catalua_ui_registry.cpp`, then the domain-specific `catalua_ui_*.cpp`. The authoritative
public shape is cross-checked against `data/lua/types/ccb_api_v5.d.lua`, manifest schema, and
generated native inventory.

## Data ownership

The engine owns native objects and the Lua state. Lua receives detached immutable snapshots,
value types, or checked handles—never borrowed native pointers. The manifest owns the script's
declared capabilities; the runtime owns enforcement.

## Dependencies

The bridge depends on embedded Lua/sol, native registries and services, manifest JSON, API
version constants, LuaLS declarations, generated inventories, event/callback registries, and
Lua contract tests.

## Lifecycle

Runtime creates a state, reads and validates manifests in dependency order, installs only
allowed API surfaces, loads modules, dispatches bounded events/callbacks, then tears down the
state before native owners disappear.

## Invariants

Manifest ID/version/capabilities validate; capability dependencies hold; declared API version
is supported; native registration, LuaLS declarations, and inventories remain in parity;
handles validate identity/lifetime; no borrowed pointer crosses into Lua.

## Extension points

Add a public symbol to a focused registration module, declare it in LuaLS, inventory it, gate
it with the minimum capability, and add parity/behavior/example tests. Generated references
must come from those contracts rather than prose.

## Serialization

Lua state is not a raw save snapshot. Scripts persist only through supported scoped state
services and serializable values; native handles and callbacks must be reacquired after load.

## Tests

Run LuaLS parsing, native-registration parity, coverage, manifest schema, Lua syntax, callback
and disabled-build tests, plus complete example-mod loading. Public undocumented symbols must
remain zero.

## Performance

Cross-language calls, snapshot construction, and event fan-out are costs. Bound collection
sizes, avoid rebuilding registries per frame, and keep callbacks deterministic and short.

## CCB divergence

Lua API v5, capability gates, typed handles, snapshots, hooks, and callbacks are CCB contracts;
they are not interchangeable with CDDA, CBN, or historical Lua APIs.

## Technical debt

Many domain modules increase parity and review burden. Keep one generated contract pipeline and
deprecate public symbols explicitly instead of leaving aliases or undocumented registrations.
