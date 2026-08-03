---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.performance
title: Lua performance and resource bounds
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
- callback_time_total_us
source_queries: []
source_fingerprint: 86ab8c697639288944692daea743e7470450d95825578f8964198c2bd0dbdc83
authority: api-contract
verified_commit: 501f84d20d4bf432dd7fec9b757f5af6a18dae36
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8eac9b8b799105af96a709f068d936b1590c6986f0c735b31d9fa53323d4e233
prerequisites:
- api.lua.v5.ui
- api.lua.v5.lifecycle
depends_on:
- api.lua.v5.debugging
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/performance/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/performance/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/performance/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/performance/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/501f84d20d4bf432dd7fec9b757f5af6a18dae36
source_urls:
- path: data/lua/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/README.md
- path: data/lua/manifest.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/manifest.schema.json
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/types/ccb_api_v5.d.lua
- path: data/lua/reference/ccb_public_api_v5.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/reference/ccb_public_api_v5.json
- path: data/lua/reference/ccb_public_api_v5_coverage.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/reference/ccb_public_api_v5_coverage.json
- path: tools/lua_api/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/tools/lua_api/README.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.v5.performance%29%3A+&body=Document+ID%3A+api.lua.v5.performance%0ALanguage%3A+en%0AVerified+commit%3A+501f84d20d4bf432dd7fec9b757f5af6a18dae36%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Lua performance and resource bounds

Lua pages may run every frame; events and hooks can sit on frequent paths. Bounded API results
are runtime/game-thread protection contracts, not merely recommendations.

## Principal boundaries

- Each runtime has a 32 MiB Lua memory limit.
- Entry, page, event, scheduler, service, hook, and callback invocations have instruction budgets.
- An over-budget or throwing callback is independently disabled/removed. `pcall`/`xpcall`
  cannot suppress a budget termination.
- Registry, inventory, creature, map, event payload, service argument/result, and navigation
  operations have explicit count/byte/depth bounds.
- The scheduler uses game turns, never wall-clock time, with bounded task and due-callback counts.

Exact limits belong to the source contract. Inspect the relevant [function](reference/functions.md),
[method](reference/methods.md), and `data/lua/README.md`; do not assume an old prose number is a
permanent constant.

## Page hot paths

1. Pass the smallest `limit` that serves the current UI.
2. Use `virtual_list`/`virtual_list_rows` and render only the visible half-open range.
3. Key translated/definition caches to `language_revision()` or a registry revision.
4. Do not repeatedly register pages, subscriptions, hooks, callbacks, action-menu entries, or
   sidebar widgets inside draw.
5. Do not build large tables, serialize whole-world state, or scan every definition each frame.
6. Keep edit drafts in `state.page`; never retain `ctx` or live objects.

## Measurement

`game.runtime_status()` exposes `callback_count`, `callback_time_total_us`,
`callback_time_max_us`, `slow_callback_count`, and `last_slow_callback`. Reproduce and record the
callback/page, input size, platform, and pinned CCB commit before reducing query count or bounds.

Disabling capability checks, increasing generated limits, or caching handles across generations
is not an optimization. It breaks safety and compatibility contracts instead of fixing the path.
