---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: architecture.lua-first-platform
title: Lua-first Platform v1 architecture
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
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- data/lua/LUA_FIRST_PLATFORM.md
- ai/lua-first-roadmap.yml
- data/lua/AGENTS.md
source_symbols: []
source_queries: []
source_fingerprint: fb018b111dad342ff2914506cfa61274dc2d83c97635db93dca59940feda251e
authority: docs-explanation
verified_commit: c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd
verified_at: '2026-08-12'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: df364cca1c1af9485ae058d72d06bdbf099002b698e870d6c8ce7ee362e6d29d
prerequisites:
- architecture.overview
depends_on:
- api.lua.v5.overview
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
- lua-contract
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: lua-platform
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/lua-first-platform/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-platform/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/lua-first-platform/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-platform/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd
source_urls:
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/lua/LUA_FIRST_PLATFORM.md
- path: ai/lua-first-roadmap.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/ai/lua-first-roadmap.yml
- path: data/lua/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/lua/AGENTS.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28architecture.lua-first-platform%29%3A+&body=Document+ID%3A+architecture.lua-first-platform%0ALanguage%3A+en%0AVerified+commit%3A+c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Lua-first Platform v1

> This page covers both the long-term architecture and the merged Platform v1
> vertical slices. [Lua API v5](../api/lua/v5/overview.md) remains the current
> complete scripting contract. Runnable Platform signatures and boundaries are
> documented in the [Platform v1 API overview](../api/lua/platform-v1/overview.md).

Lua-first Platform v1 is not “call EOC from Lua” or “spell JSON as Lua tables.”
It makes Lua the primary authoring language for CCB core content and Mods. An
author should eventually be able to define metadata, items, recipes, vehicles,
creatures, world generation, dialogue, missions, UI, and runtime behaviour in
Lua alone.

## The three essential decisions

1. A minimal Mod contains root `main.lua`. A `lua/` subdirectory and an
   author-maintained `manifest.json` or `modinfo.json` are not required.
2. Lua uses native objects, domain services, normal control flow, modules,
   events, hooks, named tasks, and persistent state. Public APIs do not copy
   JSON fields or EOC keys one by one.
3. Platform v1 is a trusted in-process extension system. It exposes the
   complete Lua 5.4 standard libraries, files, processes, and native
   modules, so an installed Mod must be trusted like a local program.

## Parallel contracts and the Platform slice

| Question | Current Lua API v5 | Implemented and expanding Platform v1 |
| --- | --- | --- |
| Start time | After JSON finalization | Static content before finalization; runtime handlers after world readiness |
| Mod discovery | Manifest and capability contract | Zero-config root `main.lua`; optional root `mod.lua` |
| Static content | Mostly queries or controls loaded objects | Creates, replaces, and transactionally edits native definitions |
| Behaviour | Published events, hooks, callbacks, and runtime domains | Native methods, domain services, typed events, synchronous hooks, named tasks |
| Security model | Capability sandbox | Fully trusted, with game-process privileges |
| Version | API v5 | Independent Platform v1, not a v5 rename |

A similar v5 feature does not mean that its Platform v1 counterpart is done.
The strict ledger still records zero full selector equivalents, 119 bounded
implementations, and 440 primitive-only entries. Promise a particular Platform
shape only when source, tests, declarations, and roadmap evidence agree.

## Zero-configuration Mods

The minimal directory has one convention: `main.lua` exists at the Mod root.

```text
my_mod/
└── main.lua
```

The engine derives defaults from the directory:

- Mod ID and display name: directory name;
- dependencies: none;
- Platform version: 1;
- content and runtime registration entry point: `main.lua`.

`content/`, `runtime/`, `lib/`, and `tests/` are author choices. A complete
template may recommend them, but the loader cannot require them. Local
`require` initially searches the Mod root for `?.lua` and `?/init.lua`.

### Optional `mod.lua`

An author can add root `mod.lua` when the Mod needs a stable ID, display name,
version, dependencies, a core flag, or a different entry point. It executes
Lua and returns a native `ccb.ModDefinition`, not a plain table shaped like
JSON.

```lua
local ccb = require("ccb")

return ccb.ModDefinition {
    id = "my_stable_mod",
    name = "My Mod",
    version = "1.0.0",
    dependencies = { "dda" },
    entry = "main.lua",
}
```

The entry must stay within the packaged Mod root. The Mod manager executes
`mod.lua` while scanning installed Mods, potentially before the player enables
one. Mod UI and distribution documentation must therefore show the trusted-code
warning prominently.

## Loading lifecycle

The current sequence is:

1. discover root `main.lua` or optional `mod.lua`;
2. resolve metadata, dependencies, and deterministic load order;
3. begin one data-load transaction;
4. load compatibility JSON first when a hybrid Mod contains it;
5. execute the Platform entry and place native definitions in staging;
6. commit staged content and run global finalization;
7. activate events, hooks, handlers, and session tasks after `world_ready`.

Top-level entry code may define static content and register behaviour, but it
cannot read the live map, player, or world before the world is ready. A failed
transaction cannot leave a half-loaded playable game. External effects such as
file writes or process launches are outside the engine transaction and cannot
be rolled back.

Hot reload first executes the entry in a candidate Lua state. Runtime
registrations may be replaced when the static-content fingerprint is unchanged.
If an item, recipe, or other static definition changed, the result is
`requires_full_data_reload`, not in-place mutation of finalized registries.

## Native objects, not JSON shadows

An exported C++ type exposes every bindable `public` field, method, and
operator. Platform does not bypass `private` or `protected`. Export begins from
explicitly approved type roots; JSON loaders and EOC parsers are not default
export roots.

A borrowed native reference carries `owner + generation`. Access after owner
destruction, world replacement, content recommit, or runtime replacement raises
a Lua error instead of dereferencing a dangling pointer. Native modules loaded
by a Mod can bypass this guard and are outside the compatibility guarantee.

Static definitions are real native staging objects. The current content layer
has explicit `add`, `replace`, and transactional `edit` semantics; duplicate IDs
are errors by default. Constructors, normal functions, loops, modules, and
composition take over the reuse role previously served by JSON `copy-from`.

This uses the currently runnable item and named-handler spelling:

```lua
local ccb = require("ccb")
local item = ccb.content.Item {
    id = "vibe_lamp",
    name = "Vibe lamp",
    description = "Created as a native Lua definition.",
    symbol = "*",
}
item:mass_grams(350)
item:on_use("use_vibe_lamp", "Feel the vibe")
ccb.content.add(item)

ccb.runtime.handler("use_vibe_lamp", function(context)
    context:message("The light softens.")
    return 0
end, 1)
```

The point is objects, functions, unit types, and composition—not turning every
JSON key into `item:set_json_field(...)`.

## Lua behaviour instead of EOC

Platform needs a small set of orthogonal primitives:

- native object methods and domain services for validated queries and changes;
- ordinary Lua expressions for conditions;
- typed events for observing something that already happened;
- synchronous hooks for transforming, vetoing, or choosing before a decision;
- named handlers referenced by definitions;
- named persistent tasks for delayed or recurring work;
- serializable character or world state for durable data;
- ordinary Lua libraries for workflows and state machines over those primitives.

When migrating EOC, trace a condition or effect to its underlying game
operation, extract that operation into a C++ domain service, and let the legacy
EOC adapter and Lua binding share it. `run_eoc`, alpha/beta talker aliases, one
function per EOC key, or another recurrence DSL are not Platform public APIs.

## Persistent tasks and saves

Closures, coroutine stacks, userdata, and native references cannot be written
directly to a save. A persistent task stores stable data only:

```text
mod_id + handler_id + due + owner + payload + payload_version
```

After load, a new Lua state resolves `handler_id` back to a function. Missing
handlers, invalid owners, overdue tasks, and payload-version changes need
bounded diagnostics and explicit discard or migration rules. Coroutines remain
useful for flows in the current session but do not cross save/load.

“Replace JSON with Lua” applies to author-facing content contracts. Saves,
settings, caches, localization products, and generated inventories may still
use JSON internally; changing those formats would not increase Mod authoring
power.

## Developer extension and templates

Repository tooling now provides two scaffolds:

- `minimal`: produces only an executable root `main.lua`;
- `complete`: provides recommended `content/`, `runtime/`, and `tests/`
  structure and examples, but still has no JSON and no required `lua/` folder.

Scaffolding must refuse to overwrite a non-empty target, and later template
updates never rewrite author files. Other developers can distribute ordinary
Lua module libraries and build higher-level DSLs over stable Platform
primitives. Those ecosystem libraries must not force the engine to bless one
particular DSL as its core interface.

## First vertical slice

`data/mods/Lua_First_Example/` completes the first zero-JSON/EOC slice. Native
`mod.lua`, an item, recipe, Lua use behaviour, character/world state, and a
named task all enter the real Mod-selection and loading path. The
`[playable_mvp]` gate covers game saves, runtime destruction, full data reload,
continued item use, and one overdue task running exactly once. This proves a
playable vertical slice, not completion of the remaining static domains.

See the [Lua-first roadmap](lua-first-roadmap.md) for actual status, the
[Platform v1 API overview](../api/lua/platform-v1/overview.md) for concrete
entry points, and the [Lua-first glossary](lua-first-glossary.md) while learning
the terminology.
