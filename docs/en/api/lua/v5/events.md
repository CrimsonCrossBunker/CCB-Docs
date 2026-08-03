---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.events
title: Events, hooks, and callbacks
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
- game.native_events
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
translation_source_fingerprint: c5889f704d092b0f46fdbdd8d00c81ebf6e80985b50a1fcb935f1a4814f2ca12
prerequisites:
- api.lua.v5.lifecycle
depends_on:
- api.lua.v5.reference.events
- api.lua.v5.reference.hooks
- api.lua.v5.reference.callbacks
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/events/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/events/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/events/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/events/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.v5.events%29%3A+&body=Document+ID%3A+api.lua.v5.events%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Events, hooks, and callbacks

Lua v5 has four notification/extension surfaces that are easy to confuse. Choose by
ownership and call direction first, then inspect the generated contract.

| Surface | Registration | Purpose | Can a return affect native flow? |
| --- | --- | --- | --- |
| Custom/lifecycle event | `events.on` | source messages and CCB lifecycle | `false` stops this propagation |
| Native event bus | `game.native_events.on` | 113 schema-described game events | observe; emission is separate and strict |
| Native hook | `game.hooks.on` | 52 explicit native boundaries | intercept hooks may return declared fields |
| Definition callback | `game.callbacks.register` | attach methods to 11 JSON definition kinds | per-method decision/consuming contract |

## Custom events

A plain event name is source-local. To observe a dependency, declare it first and use
`events.on_from`. Payloads accept bounded string keys and copied scalar values; do not use
events to transfer tables, functions, userdata, or handles.

```lua
events.on("quest_updated", function(event)
    game.add_msg(event.data.quest_id .. ":" .. tostring(event.data.stage))
end)
events.emit("quest_updated", { quest_id = "intro", stage = 2 })
```

## Native events

Discover names and fields with `game.native_events.list()`/`describe(name)` rather than
guessing. Subscription payloads carry the event type, turn, and typed fields. `emit` is
callback-scoped and requires the exact field set, correct Lua types, and `events` plus
`game.read` plus `game.write`.

## Hooks

A hook description gives its mode, payload, returns, and capabilities. Observe hooks ignore
returns; intercept hooks accept only declared result fields. Higher priorities run first and
equal priorities preserve registration order. An erroring or over-budget handler disables
only itself.

## Callback actors

Kinds are `iuse`, `iwieldable`, `iwearable`, `iequippable`, `istate`, `imelee`, `iranged`,
`bionic`, `mutation`, `trap`, and `monster`. Registrations bind to a target id, source, and
hot-reload transaction. When native C++ invokes Lua, it restores the registering source's
permission identity.

See [native events](reference/events.md), [hooks](reference/hooks.md), and
[callbacks](reference/callbacks.md) for every name, field, decision/consuming flag, and source.
