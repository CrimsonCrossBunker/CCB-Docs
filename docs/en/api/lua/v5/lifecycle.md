---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.lifecycle
title: Lua sources and lifecycle
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
- ccb.lifecycle.reload
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
translation_source_fingerprint: ac95dbf6b61cdeb4e9f921e901cce7c75c662e5162301423b88843b2b1176b0b
prerequisites:
- api.lua.v5.overview
depends_on:
- api.lua.v5.capabilities
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/lifecycle/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/lifecycle/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/lifecycle/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/lifecycle/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd
source_urls:
- path: data/lua/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd/data/lua/README.md
- path: data/lua/manifest.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd/data/lua/manifest.schema.json
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd/data/lua/types/ccb_api_v5.d.lua
- path: data/lua/reference/ccb_public_api_v5.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd/data/lua/reference/ccb_public_api_v5.json
- path: data/lua/reference/ccb_public_api_v5_coverage.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd/data/lua/reference/ccb_public_api_v5_coverage.json
- path: tools/lua_api/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd/tools/lua_api/README.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.v5.lifecycle%29%3A+&body=Document+ID%3A+api.lua.v5.lifecycle%0ALanguage%3A+en%0AVerified+commit%3A+3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Lua sources and lifecycle

## Load transaction

The runtime loads the built-in `data/lua/main.lua`, each enabled Mod's `lua/main.lua` in
Mod order, and finally `config/lua/main.lua`. Each source has an isolated environment,
manifest identity, capability set, and module cache.

A hot reload first builds a candidate Lua state. It replaces the running state only after
every entry point succeeds. Any entry failure discards the candidate and keeps the old
runtime, so pages, events, tasks, hooks, and callbacks cannot be committed half-loaded.

## Module boundaries

- On API v4/v5, `require("foo.bar")` searches only the calling source's root.
- `modules.import(provider_id, "foo.bar")` accepts only `builtin`, the caller, or an
  earlier-loaded dependency declared in the manifest.
- Use a versioned `services` contract when the provider must retain its permission identity;
  do not treat source import as a service boundary.
- Absolute paths, traversal, dynamic libraries, and arbitrary file loading are unavailable.

## Lifecycle signals

| Name | Delivery point |
| --- | --- |
| `ccb.lifecycle.reload` | after the new candidate runtime commits |
| `ccb.lifecycle.world_ready` | after a new-game/save runtime loads |
| `ccb.lifecycle.before_save` | before Lua sidecars are written |
| `ccb.lifecycle.after_save` | after saving, with `success`/`error` payload fields |
| `ccb.lifecycle.shutdown` | before a world or runtime is released |

Subscribe to lifecycle events through `events.on`. Native lifecycle hooks use `game.hooks`;
their names, payloads, and return contracts are separate and must be checked in the
[generated hook reference](reference/hooks.md).

## State and generations

- `state.character`: source- and character-scoped, persisted with the save.
- `state.world`: source-scoped, shared by characters in the world, and persisted.
- `state.page`: source- and page-scoped for the current world session; draw callbacks only.
- Ordinary Lua globals/locals: replaced after a successful reload.

The creating source owns `GameHandle` values, task ids, subscription ids, and callback
registrations. World changes and successful reloads advance generations. Check
`is_valid()`/`status()` before retaining a handle, and never retain `ctx`: a page context is
valid only during its current draw callback.

## Safe initialization pattern

Use entry points to declare modules, services, and registrations. Put live reads or writes
inside an explicit page, event, scheduler, hook, or callback invocation. Many interaction
and mutation operations intentionally reject top-level load-time calls.
