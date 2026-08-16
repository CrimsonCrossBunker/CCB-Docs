---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.platform-v1.overview
title: Lua-first Platform v1 API overview
language: en
status: active
doc_type: reference
audiences:
- new-contributor
- experienced-contributor
- maintainer
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
- data/lua/types/ccb_platform_v1.d.lua
- data/lua/LUA_FIRST_PLATFORM.md
- ai/lua-first-roadmap.yml
- ai/lua-first-replacement-ledger.yml
- data/mods/Lua_First_Example/mod.lua
- data/mods/Lua_First_Example/main.lua
- data/mods/Lua_First_Example/content/cleanwater_charm.lua
- data/mods/Lua_First_Example/runtime/behaviour.lua
- tools/create_lua_mod.py
- tools/migrate_lua_first.py
source_symbols:
- CcbPlatformV1
- ModDefinition
- CcbPlatformContent
- CcbPlatformRuntime
- CcbPlatformTasks
- CcbPlatformServices
source_queries: []
source_fingerprint: 145df35fb96e317cd11ab1619fa43b3ea8eb7f94373f96c3aa32dcec7264f3da
authority: api-contract
verified_commit: c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd
verified_at: '2026-08-12'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 5de362515587d913a379f8a74fd93034e91e329ccec7215338767b05b5efcacc
prerequisites:
- architecture.lua-first-platform
depends_on:
- architecture.lua-first-roadmap
- api.lua.v5.overview
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; LuaLS declarations, native registrations, tests, and the replacement ledger
  remain authoritative.
example_validation_ids:
- agent-context
- lua-contract
api_version: platform-v1
deprecated: false
deprecation_replacement: null
risk_group: lua-platform
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/platform-v1/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/platform-v1/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/platform-v1/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/platform-v1/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd
source_urls:
- path: data/lua/types/ccb_platform_v1.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/lua/types/ccb_platform_v1.d.lua
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/lua/LUA_FIRST_PLATFORM.md
- path: ai/lua-first-roadmap.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/ai/lua-first-roadmap.yml
- path: ai/lua-first-replacement-ledger.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/ai/lua-first-replacement-ledger.yml
- path: data/mods/Lua_First_Example/mod.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/mods/Lua_First_Example/mod.lua
- path: data/mods/Lua_First_Example/main.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/mods/Lua_First_Example/main.lua
- path: data/mods/Lua_First_Example/content/cleanwater_charm.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/mods/Lua_First_Example/content/cleanwater_charm.lua
- path: data/mods/Lua_First_Example/runtime/behaviour.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/mods/Lua_First_Example/runtime/behaviour.lua
- path: tools/create_lua_mod.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/tools/create_lua_mod.py
- path: tools/migrate_lua_first.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/tools/migrate_lua_first.py
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.platform-v1.overview%29%3A+&body=Document+ID%3A+api.lua.platform-v1.overview%0ALanguage%3A+en%0AVerified+commit%3A+c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Lua-first Platform v1 API overview

Lua-first Platform v1 is a native authoring surface versioned separately from Lua API v5. A
pure-Lua vertical slice is executable today, but the Platform is still being delivered
incrementally; Lua API v5 remains the name of the current complete scripting contract. Exact
signatures come from `data/lua/types/ccb_platform_v1.d.lua`, native registrations, and tests.

The strict replacement ledger currently contains 775 entries: zero have full selector parity,
119 have explicitly bounded implementations, 440 have composable primitives only, 198 remain
planned, and 18 were reviewed as not applicable. This page documents what can be authored now;
it does not mean that JSON or EOC can be removed.

## Minimal Mod and metadata

The smallest Mod needs only a root `main.lua`:

```text
my_mod/
└── main.lua
```

The directory name supplies the default id and display name. No `lua/` subdirectory,
`manifest.json`, or `modinfo.json` is required. When stable metadata or dependencies are needed,
an optional root `mod.lua` returns a native `ccb.ModDefinition`:

```lua
local ccb = require("ccb")

return ccb.ModDefinition {
    id = "my_mod",
    name = "My Lua Mod",
    version = "0.1.0",
    dependencies = { "dda" },
    entry = "main.lua",
}
```

`id`, `name`, `version`, `entry`, `dependencies`, and `core` have checked type, length, and path
boundaries. Local `require` resolves `?.lua` and `?/init.lua` from the Mod root, and an entry may
not escape that root. Each Platform Mod receives an isolated Lua 5.4 state and is trusted like a
local native extension.

## The `ccb` root

| Member | Purpose |
| --- | --- |
| `platform_version` | Fixed at `1` for explicit version checks |
| `ModDefinition` | Constructs optional native Mod metadata |
| `content` | Creates, replaces, or edits native definitions before global finalize |
| `runtime` | Registers named handlers, events, hooks, and task-payload migrations |
| `state` | Serializable character- and world-scoped state |
| `tasks` | Named delayed tasks that can be saved |
| `presentation` | Notice, confirmation, stable-id choice, and text input |
| `services` | 49 game-domain services plus focused Platform-native operations |

## Native content transactions

`ccb.content` supplies native constructors and `add`, `replace`, and `edit`. Definitions enter the
current Mod's staging area before one commit and global finalize; failure rolls changes back in
reverse order. Duplicate ids fail by default. Static-content changes require a full data reload;
only runtime-only changes may be hot-replaced.

This item and recipe syntax ships with the game:

```lua
local charm = ccb.content.Item {
    id = "my_cleanwater_charm",
    name = "clean-water charm",
    description = "A native Lua-authored item.",
    symbol = "*",
}
charm:mass_grams(20)
charm:volume_ml(10)
charm:material("steel", 1)
charm:on_use("use_cleanwater_charm", "Listen to the charm")
ccb.content.add(charm)

local recipe = ccb.content.Recipe {
    id = "my_cleanwater_charm",
    result = "my_cleanwater_charm",
    category = "CC_OTHER",
    subcategory = "CSC_OTHER_OTHER",
    skill = "fabrication",
    difficulty = 1,
    duration_moves = 500,
    autolearn = true,
}
recipe:component_any {
    { id = "scrap", count = 1 },
    { id = "steel_chunk", count = 1 },
}
ccb.content.add(recipe)
```

The declaration also lists bound constructors for requirements, proficiencies, monsters, body
graphs, wounds, effects, fields, vehicle helper catalogs, weather, activities, help, playlists,
and other domains. A constructor promises only its declared fields and methods; its existence
does not imply parity with every legal shape of the similarly named legacy JSON type.

## Handlers, events, and hooks

Behaviour receives a stable id before content, an event, or a hook refers to it:

```lua
ccb.runtime.handler("use_cleanwater_charm", function(context)
    context:message("The charm hums.")
    return 0
end, 1)

ccb.runtime.handler("my_world_ready", function(event)
    if event.new_game then
        ccb.services.message("Lua-first Mod ready")
    end
end, 1)

ccb.runtime.on("world_ready", "my_world_ready")
```

`on` accepts `world_ready`, `before_save`, `after_save`, `shutdown`, and
`game:<native-event>`. Native event actors use semantic keys such as `actors.character`,
`actors.attacker`, `actors.killer`, and `actors.victim`; no EOC alpha/beta aliases are exposed.
`hook` is a synchronous decision point whose handler results follow that hook's aggregation rule,
not an after-the-fact event.

## Typed handles and lifetime

`GameHandle` and mission, horde, zone, and related tokens are bound to the exact Mod runtime
owner, runtime generation, world generation, and native object lifetime. A handle from another
Mod, an older hot reload, or an older world is rejected. `ItemUseContext` expires when its callback
returns.

Do not persist live handles, closures, coroutine stacks, or userdata. Save stable ids, scalars, and
the data needed to resolve objects again. Many domain services return `CcbResult`: check `ok`
before reading `value`, and handle `error.code` and `error.message` as bounded failures.

## Persistent state and named tasks

State accepts only `boolean`, `integer`, finite `number`, `string`, or `nil`:

```lua
local uses = ccb.state.character.get("charm_uses", 0) + 1
ccb.state.character.set("charm_uses", uses)

if not ccb.state.world.get("initialized", false) then
    ccb.state.world.set("initialized", true)
    ccb.tasks.after(10, "my_reminder", { text = "Still here" }, 1, "world")
end
```

A task stores its handler id, due turn, owner, payload, and payload version—not a function.
`ccb.runtime.migrate_task_payload` registers stepwise migrations. Missing handlers, orphan owners,
corrupt data, and overdue tasks have tested preservation, diagnostic, or run-once policies.
`ccb.tasks.cancel(id)` can cancel only a task owned by the current Mod.

## Presentation and domain services

`ccb.presentation.notice`, `confirm`, `choose`, and `input_text` are callback-only native
interaction primitives. `choose` returns a stable entry id rather than a presentation index.
Real desktop and Android interaction still needs continuing manual verification.

`ccb.services` composes the typed v5 query/action surface with focused Platform operations:

| Domain | Representative capability |
| --- | --- |
| `inventory` | Read the singular physically wielded item without guessing from a page |
| `activities` | Activity snapshot, plain timed assignment, and native cancellation |
| `wounds` | Exact-body-part wound snapshot/add/remove |
| `bionics` | Installed-count and energy-capacity summary, grant, and remove |
| `recipes` | Learned recipe knows/learn/forget/category forget |
| `martial_arts` | Learn/forget without coupling mutation to presentation |
| `morale` | Typed morale add/remove |
| `random` | Per-Mod deterministic stream, probability, sampling, and contested rolls |
| `gameplay` | String predicates, active Mods, dimension, outside, and line-of-sight queries |

Other service roots cover characters, creatures, items, vehicles, missions, zones, magic, maps,
weather, needs, skills, proficiencies, factions, camps, sound, variables, and serialization. They
are composable primitives, not same-named wrappers around the 275+310 EOC keys.

## Templates, migration, and the playable slice

Create a new Mod with:

```sh
python3 tools/create_lua_mod.py --template minimal /path/to/MyMod
python3 tools/create_lua_mod.py --template complete /path/to/MyMod
```

The extractor emits native Lua skeletons and explicit TODOs. It never emits a JSON loader, EOC
runner, or raw legacy object:

```sh
python3 tools/migrate_lua_first.py old.json --output /tmp/MyMigratedMod --mod-id my_mod
python3 tools/migrate_lua_first.py old.json --output /tmp/MyMigratedMod --check
```

`data/mods/Lua_First_Example/` is a bundled fixture with no JSON, EOC, manifest, or required
`lua/` directory. The `[playable_mvp]` gate exercises real Mod selection, data loading, item use,
game saves, runtime destruction, full data reload, continued gameplay, and one overdue task
running exactly once.

## Current boundary

- All 11 roadmap capabilities are still `partial`; do not describe a local slice as complete
  replacement.
- Major planned domains include the complete map stack, vehicle definitions, NPCs, professions,
  scenarios, factions, concrete mutations, bionics, martial arts, magic, dialogue, and mission
  definitions.
- Event-actor coverage, remaining borrowed references, complex activities, NPC navigation and
  relocation, combat damage, wetness, and rich forms still need implementation or verification.
- Legacy JSON/EOC cannot be removed before coverage and migration finish and a deprecation window
  of at least two stable releases and twelve months has elapsed.

See the [Platform v1 architecture](../../../architecture/lua-first-platform.md), the exact
[roadmap](../../../architecture/lua-first-roadmap.md), and the
[glossary](../../../architecture/lua-first-glossary.md).
