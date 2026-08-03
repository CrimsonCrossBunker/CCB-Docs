---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.migration
title: Migrating to Lua API v5
language: en
status: active
doc_type: how-to
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
- game.state_get
source_queries: []
source_fingerprint: 86ab8c697639288944692daea743e7470450d95825578f8964198c2bd0dbdc83
authority: api-contract
verified_commit: 501f84d20d4bf432dd7fec9b757f5af6a18dae36
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: c8a8f098d63c7f79ce5c0ab4a7464e05da60693906e8a2215cfc398aecd0e3e8
prerequisites:
- api.lua.v5.overview
depends_on:
- api.lua.v5.capabilities
- api.lua.v5.lifecycle
- api.lua.v5.ui
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/migration/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/migration/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/migration/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/migration/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.v5.migration%29%3A+&body=Document+ID%3A+api.lua.v5.migration%0ALanguage%3A+en%0AVerified+commit%3A+501f84d20d4bf432dd7fec9b757f5af6a18dae36%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Migrating to Lua API v5

API v2–v4 manifests remain accepted for their original surfaces. New code should migrate
explicitly to v5 instead of relying on compatibility capabilities for a manifest-less source.

## Migration steps

1. Set `api_version` to `5` and validate against the current `manifest.schema.json`.
2. Derive a minimum capability set from actual calls. A mutation adds `game.write` and therefore
   also requires `game.read`.
3. Replace API v2/v3 cross-source `require` assumptions with local `require`; use a declared
   dependency plus `modules.import` or a versioned `services` boundary across sources.
4. Replace retained native-object assumptions with typed values, detached snapshots, tokens,
   or `GameHandle`; validate generations before use.
5. Replace direct mutation with a validated v5 service or `game.actions` request and handle
   result envelopes.
6. Move `game.state_get/state_set` data into an explicit `state.character`, `state.world`, or
   `state.page` scope.
7. Use page descriptors and stable control `_id` forms. Use `ctx:environment()` for input/layout,
   never `ctx:platform()` to distinguish touch from desktop.
8. Remove Android-HUD assumptions: portable entry points use `ui.page`; `sidebar` is PC-only.
9. Reconcile every parameter, return, and error with generated reference, then run contract and
   complete-example checks.

## Compatibility points

- API v4/v5 `require` is source-local; API v2/v3 retains the legacy reverse-load-order lookup.
- The string-title `ui.page` form remains, but descriptors explicitly place new pages in slots.
- Compatibility aliases such as `game.player_stats()` may remain; new code should use current
  generated names.
- `ctx:platform()` remains only for API v2 diagnostics.
- `game.state_get/state_set` is the API v2 character state without explicit modern scopes.

## Definition of migrated

- Manifest Schema passes and the Mod/manifest ids match.
- Every call exists in generated [functions](reference/functions.md) or
  [methods](reference/methods.md).
- No retained `ctx`, bare object, or cross-generation handle remains.
- A failed hot reload preserves the old runtime; a successful reload preserves intended state.
- The [complete example Mod](example-mod.md) and [debug commands](debugging.md) form a passing baseline.
