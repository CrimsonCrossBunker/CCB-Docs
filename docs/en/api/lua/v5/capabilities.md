---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.capabilities
title: Declaring capabilities
language: en
status: draft
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
last_human_reviewer: Not yet reviewed (draft)
source_paths:
- data/lua/README.md
- data/lua/manifest.schema.json
- data/lua/types/ccb_api_v5.d.lua
- data/lua/reference/ccb_public_api_v5.json
- data/lua/reference/ccb_public_api_v5_coverage.json
- tools/lua_api/README.md
source_symbols:
- game.actions.dangerous
source_queries: []
source_fingerprint: 86ab8c697639288944692daea743e7470450d95825578f8964198c2bd0dbdc83
authority: api-contract
verified_commit: 3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 7f006e3e9d2c5d2b02a4c2c83c46c8470ea1952d15614f277e23683c27e708e6
prerequisites:
- api.lua.v5.overview
depends_on:
- api.lua.v5.permissions
- api.lua.v5.reference.capabilities
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; generated contract and source paths at the verified commit.
example_validation_ids: []
api_version: '5'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/565
stale_reason: null
search:
  exclude: true
---

# Declaring capabilities

Each Lua source requests its minimum permission set through `lua/manifest.json`. A call whose
capability is absent fails. Callbacks, hooks, events, module loads, and page replacement never
borrow another source's permissions.

## Minimal v5 manifest

```json
{
  "$schema": "https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/raw/master/data/lua/manifest.schema.json",
  "id": "my_mod",
  "version": "1.0.0",
  "api_version": 5,
  "capabilities": ["events", "game.read", "ui.pages"],
  "dependencies": []
}
```

A Mod manifest `id` must equal its Mod id. New code should request API 5 and only the
capabilities its calls actually need.

## Complete capability set

| Capability | Minimum API | Purpose |
| --- | ---: | --- |
| `events` | 2 | custom, lifecycle, and native event surfaces |
| `game.actions` | 2 | safe game-action queue/current input actions |
| `game.actions.dangerous` | 4 | dangerous named actions (still locally confirmed) |
| `game.callbacks` | 5 | JSON definition callback actors |
| `game.hooks` | 5 | native hooks |
| `game.read` | 2 | game snapshots, definitions, and queries |
| `game.write` | 5 | validated game mutations |
| `modules.import` | 4 | source import from declared dependencies |
| `registry.read` | 4 | detached definition-registry queries |
| `scheduler` | 4 | deterministic turn scheduling |
| `services.consume` | 4 | call a dependency's service |
| `services.provide` | 4 | publish a versioned service |
| `state.character` | 2 | character-persistent state |
| `state.page` | 2 | page-session state |
| `state.world` | 2 | world-persistent state |
| `ui.pages` | 2 | register and navigate portable pages |

## Dependency rules

- `game.actions.dangerous` → `game.actions`
- `game.write` → `game.read`
- `game.hooks` → `events`
- `game.callbacks` → `game.read`

The Schema rejects unknown or duplicate values, an API version that is too low, and missing
dependencies above. See the generated [capability](reference/capabilities.md) and
[manifest-field](reference/manifest-fields.md) references for exact schemas and sources.
