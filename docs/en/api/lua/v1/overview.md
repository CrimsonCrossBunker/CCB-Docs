---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.platform-v1.overview
title: 'Lua Platform v1: zero to running'
language: en
status: active
doc_type: tutorial
audiences:
- mod-author
- api-user
owners:
- CCB Lua API maintainers
reviewers:
- Documentation reviewers
- Lua API reviewers
review_interval_days: 60
last_human_reviewer: LYHGLYTX
source_paths:
- data/lua/README.md
- data/lua/LUA_FIRST_PLATFORM.md
- data/lua/types/ccb_platform_v1.d.lua
- tools/create_lua_mod.py
source_symbols:
- Platform v1
- ModDefinition
source_queries: []
source_fingerprint: 90d2d199e14a83b2fe78c4c1981c2c05d5e5a77045d6a64953e42c735841c183
authority: api-contract
verified_commit: 73432156f423ed3ef3301e6632c94c03c017d115
verified_at: '2026-09-05'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: cc17c0218d706cbd06b0da238f53513a48ddf48ddc53c4b9b83cd43af2341874
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- api.lua.v5.overview
license: CC-BY-SA-3.0
attribution: CCB contributors; source paths and Git history at the verified commit.
example_validation_ids: []
api_version: '1'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v1/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v1/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v1/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v1/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/73432156f423ed3ef3301e6632c94c03c017d115
source_urls:
- path: data/lua/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/73432156f423ed3ef3301e6632c94c03c017d115/data/lua/README.md
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/73432156f423ed3ef3301e6632c94c03c017d115/data/lua/LUA_FIRST_PLATFORM.md
- path: data/lua/types/ccb_platform_v1.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/73432156f423ed3ef3301e6632c94c03c017d115/data/lua/types/ccb_platform_v1.d.lua
- path: tools/create_lua_mod.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/73432156f423ed3ef3301e6632c94c03c017d115/tools/create_lua_mod.py
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.platform-v1.overview%29%3A+&body=Document+ID%3A+api.lua.platform-v1.overview%0ALanguage%3A+en%0AVerified+commit%3A+73432156f423ed3ef3301e6632c94c03c017d115%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Lua Platform v1: zero to running

CCB currently supports **Lua Platform v1 only**. The old Lua API v5, global `game.*` table,
capability manifest, and JSON Manifest have been removed. Do not use the old pages for new MODs.

## Minimal MOD

Create a directory containing only `main.lua`:

```lua
local ccb = require("ccb")

ccb.runtime.handler("welcome", function()
    ccb.services.message("My first CCB Lua MOD is running")
end, 1)

ccb.runtime.on("world_ready", "welcome")
```

An optional `mod.lua` declares the name, version, and dependencies:

```lua
local ccb = require("ccb")

return ccb.ModDefinition {
    id = "my_first_mod",
    name = "My First MOD",
    version = "0.1.0",
    dependencies = { "dda" },
}
```

The resulting directory is:

```text
my_first_mod/
├── main.lua
└── mod.lua        # optional
```

You do not need `modinfo.json`, `manifest.json`, or a `lua/` subdirectory.

## Install and check

Place the directory under `mods/` in the CCB user directory, then run:

```sh
cataclysm-tiles --userdir /path/to/your/CCB-user-directory/ --check-mods my_first_mod
```

If you see `Checking mod My First MOD [my_first_mod]` and the process exits normally, CCB found the
MOD and completed its data-load check. You can also install catalog MODs directly with Catapult.

## Where the API is documented

- [Complete LuaLS declarations](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/master/data/lua/types/ccb_platform_v1.d.lua): functions, parameters, returns, and types;
- [Machine-readable API contract](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/master/data/lua/reference/ccb_platform_api_v1.json): generator input and change checks;
- [Platform design and lifecycle](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/master/data/lua/LUA_FIRST_PLATFORM.md): loading, isolation, state, and safety boundaries;
- [Complete example MOD](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/tree/master/data/mods/Lua_First_Example): a runnable example split by game domain;
- [CCB-MOD](https://github.com/CrimsonCrossBunker/CCB-MOD): registration, maintenance, and publishing for external MODs.

When using LuaLS, add `ccb_platform_v1.d.lua` to the workspace library to enable completion. If the
documentation disagrees with runtime behaviour, treat declarations, native registrations, and tests
in the CCB repository as authoritative and report the problem there.

## Version rules

- A MOD declares the integer Lua API version it requires; the current version is `1`;
- public MOD-facing APIs freeze when a CCB RC is published;
- existing public APIs are not removed or renamed during a Stable cycle;
- unavoidable compatibility breaks require Platform v2;
- new APIs on `Experimental` are not a Stable promise.
