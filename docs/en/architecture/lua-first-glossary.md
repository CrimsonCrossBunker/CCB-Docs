---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: architecture.lua-first-glossary
title: Lua-first learning glossary
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
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 180
last_human_reviewer: LYHGLYTX
source_paths:
- data/lua/LUA_FIRST_PLATFORM.md
- ai/lua-first-roadmap.yml
- data/lua/types/ccb_api_v5.d.lua
source_symbols: []
source_queries: []
source_fingerprint: 57e615bcf6107cae209aca140cd5d501477bf2caa05f2fb80e0273dcbd1a8ff2
authority: docs-explanation
verified_commit: c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd
verified_at: '2026-08-12'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a37d590eebadc63d2b107f43e92e2e9e51ab4578ba0c4be27123b2e0277bdabf
prerequisites:
- architecture.lua-first-platform
depends_on:
- architecture.lua-first-platform
- architecture.lua-first-roadmap
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/lua-first-glossary/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-glossary/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/lua-first-glossary/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-glossary/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd
source_urls:
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/lua/LUA_FIRST_PLATFORM.md
- path: ai/lua-first-roadmap.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/ai/lua-first-roadmap.yml
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/lua/types/ccb_api_v5.d.lua
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28architecture.lua-first-glossary%29%3A+&body=Document+ID%3A+architecture.lua-first-glossary%0ALanguage%3A+en%0AVerified+commit%3A+c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Lua-first learning glossary

This glossary is for developers learning while vibe coding. You do not need to
memorize every term first. When you meet an object, ask four questions: **who
owns it, when is it valid, can it be saved, and what source/test proves it is
implemented?**

> Platform v1 is still being planned and implemented. A term describing a
> target does not mean current Lua API v5 provides an object or function with
> that name.

## Lua and Mod loading

| Term | Meaning |
| --- | --- |
| Lua | A lightweight, dynamically typed, embeddable language. CCB places an interpreter inside the game process so Mods can call supported game capabilities. |
| Lua 5.4 | The selected language-semantics baseline for Platform v1. The bundled patch level, build options, and C-module compatibility still come from source and build contracts. |
| Lua state | An independent Lua environment containing globals, module cache, heap, coroutines, and registered functions. Reload can create a new state, so old functions and references are not automatically valid. |
| chunk | One loaded/executed unit of Lua code, such as a `.lua` file. A Mod entry is a chunk. |
| entry point | The file the engine executes to start loading a Mod. Platform defaults to root `main.lua`; advanced metadata in root `mod.lua` can select another entry. |
| zero-configuration | Stable directory conventions are enough to discover a Mod; a minimal Mod needs no extra manifest. It does not mean “no defaults or validation.” |
| `main.lua` | The default Platform content and runtime registration entry. It is a target convention, not a replacement fact for current v5 Mods. |
| `mod.lua` | Optional advanced metadata code intended to return a native `ccb.ModDefinition`. Scanning executes it, creating trusted-code risk. |
| manifest | A metadata file describing Mod ID, version, dependencies, and capabilities. Current v5 uses one; a minimal Platform Mod does not ask the author to maintain one. |
| Mod ID | The stable identity used by dependencies, saves, and migrations. Zero-config defaults it from the directory name; a published ID should not change casually. |
| dependency | A declared relationship that loads one Mod after another and permits use of its content/API. Ordering and cycles must be resolved before static content executes. |
| module | A reusable value exported by a `.lua` file or native library. `require` usually loads it and caches it in the current state's `package.loaded`. |
| `require` | Lua's module loader. Platform initially searches `?.lua` and `?/init.lua` from the Mod root; trusted code may also change `package.path`. |
| standard library | Lua's built-in table, string, math, coroutine, I/O, OS, debug, and package libraries. Platform intends to open all of them. |
| trusted execution | A Mod has game-process privileges and may read files, start processes, or load native code. It is not isolated untrusted scripting. |
| sandbox | A security boundary restricting libraries and operations visible to scripts. Current v5 capabilities impose restrictions; Platform v1 explicitly does not reuse that model. |
| capability | The current v5 unit for declaring and granting a class of APIs. It is not the target Platform v1 discovery or trust model. |

## Bindings and native objects

| Term | Meaning |
| --- | --- |
| embedding | A C++ program creates a Lua state, loads scripts, and moves values/calls across both languages. Lua need not be a separate process. |
| binding | Bridge code exposing a C++ function, type, field, or enum safely to Lua. A good binding expresses a game domain, not parser internals. |
| sol2 | A C++ library CCB can use to connect C++ and Lua. It simplifies registering functions and types but does not solve lifecycle, threading, saves, or API design automatically. |
| Lua C API | Lua's official stack-based C interface. Binding layers such as sol2 build on it; incorrect stack or ownership operations are difficult bugs. |
| usertype | sol2's term for registering a C++ type for Lua use, including constructors, methods, properties, and operators. |
| userdata | A Lua value carrying a C/C++ object or handle. It is not a plain table and is not serializable by default. |
| native object | An object whose semantics and storage are defined by C++ and exposed through a binding. Platform definitions target real native objects, not JSON-shadow tables. |
| public/private/protected | C++ access control. Platform exposes bindable `public` members of explicit export types and does not bypass `private` or `protected`. |
| handle | An indirect stable or checked reference to an object. It can store an ID, owner, and generation instead of a raw pointer. |
| owner | The object or system controlling a borrowed object's lifetime, such as a world, map, registry, or Lua state. A borrowed reference expires with its owner. |
| generation | A version incremented whenever an owner is replaced wholesale. A reference keeps its creation generation to detect an address now belonging to a new world. |
| stale reference | An old reference whose owner died or generation changed. Platform access raises a Lua error rather than using a dangling pointer. |
| ABI | Application Binary Interface: compiled calling, layout, and symbol conventions. Stable Lua source APIs do not make arbitrary C-module ABIs portable across compilers and platforms. |
| LuaLS | Lua Language Server, providing editor completion, type hints, and diagnostics. `.d.lua` declarations describe the public surface but do not replace runtime tests. |

## Static content and loading lifecycle

| Term | Meaning |
| --- | --- |
| definition | An object describing static game content such as an item, recipe, or vehicle. It is normally created during data load and becomes read-only or tightly controlled after finalization. |
| factory | A common mechanism for creating, finding, and validating one definition type. Historical C++ `generic_factory` is implementation context; Platform need not copy its template shape publicly. |
| registry | A collection of one definition type keyed by stable ID. It owns duplicate handling, lookup, iteration, and finalization boundaries. |
| staging | An area holding candidate definitions before commit. It can be discarded on failure without contaminating playable global registries. |
| transaction | A set of changes that either commits completely or never enters game state. It can roll back engine staging, not file/process side effects performed by a Mod. |
| `add` | Add a new definition; a duplicate ID is an error by default. |
| `replace` | Explicitly replace an existing ID with a new definition. It needs compatibility and ownership checks and is not triggered silently by duplication. |
| `edit` | Modify an existing definition under transaction control, committing only on success. It differs from mutating finalized data through a raw pointer. |
| finalize | The post-load phase resolving cross-ID references, building caches, checking invariants, and sealing registries. Ordering decides whether Lua static content receives normal validation. |
| cross-ID reference | A stable-ID link from one definition to another, such as a recipe referencing an item. Finalization usually resolves it and diagnoses missing targets. |
| stable ID | Long-lived string identity used by saves, references, and migration. Display names can change; casual stable-ID changes break worlds and dependencies. |
| fingerprint | A deterministic digest of static content or source. Reload uses it to detect definition changes; documentation uses it to detect evidence drift. |
| hot reload | Replace runtime scripts without restarting the whole game. A static-content change must escalate to full data reload instead of bypassing finalization. |

## Runtime behaviour

| Term | Meaning |
| --- | --- |
| event | A typed notification that something already happened, suitable for observation and asynchronous reaction. Listeners normally do not change the event's decision. |
| hook | An extension point called synchronously before a decision, able to transform, choose, or veto. It needs strict ordering, return types, and error policy because it affects main flow. |
| callback | General name for a function the engine calls later. Event listeners, hooks, and definition behaviours are callbacks with different semantics. |
| handler | A callback with a stable name that a definition or task can reference. Naming permits rebinding after reload and save/load. |
| context | A typed set of objects and information for one call, such as user, item, position, and reason. Its lifetime often ends when the callback returns. |
| service | A game-domain operation independent of JSON/EOC/Lua syntax, such as validated morale change. A legacy adapter and new binding can share it. |
| query | An operation reading state without durable side effects. Lua conditions normally compose queries with ordinary expressions. |
| mutation | An operation changing game state. It must define validation, ownership, events, failure, and save impact. |
| task | Named work scheduled for the future or repetition. A persistent task saves handler ID and data, not a function call stack. |
| workflow | A multi-step process composed from normal Lua functions, tasks, events, and state. It is a library pattern and needs no new engine EOC DSL. |
| state machine | A process represented as finite states and explicit transitions. Serializable state can be driven again after load without saving a coroutine stack. |
| coroutine | A Lua function execution that can suspend and resume. It is useful within one session but its call stack does not cross save/load. |
| scheduler | The system deciding when tasks run by time or game events. It also handles cancellation, overdue work, owner invalidation, and diagnostics. |

## Persistence and compatibility

| Term | Meaning |
| --- | --- |
| serialization | Converting memory state into saveable data. Functions, threads, userdata, and raw native references generally cannot be serialized directly. |
| payload | Plain data stored by a task or state, such as numbers, strings, booleans, arrays, and restricted tables. Size and type boundaries must be explicit. |
| payload version | A Mod-owned data version used to migrate, reject, or safely discard old payloads when a handler changes. |
| persistent state | Stable Mod-, character-, or world-associated data written to a save. It is not the same as a Lua global variable. |
| session state | Data lasting only for the current run or Lua state. It may hold functions and coroutines but has no save/load guarantee. |
| save compatibility | A new version can load old worlds while retaining stable IDs and intended meaning. A beautiful API that breaks saves is not a successful migration. |
| hybrid Mod | A migration-stage Mod containing old JSON/EOC and Platform Lua. It enables incremental work but needs explicit conflict ordering. |
| adapter | A thin layer converting one interface into another. A legacy EOC/JSON adapter may privately call a shared service; it is not the new public model. |
| deprecation | An interface remains available but is scheduled for removal with replacement, warning, and time window. Platform requires both two stable releases and twelve months. |
| migration | Move content/calls to a new interface while preserving stable IDs, saves, and behaviour. Automation should emit idiomatic Lua skeletons and explicit TODOs. |
| IR | Intermediate Representation. It can help tools analyze old content but must not become a new JSON/EOC-shaped language authors have to write. |

## Legacy JSON and EOC concepts

| Term | Meaning |
| --- | --- |
| JSON | The data format used by much current static content. Platform replaces author-facing JSON contracts, not necessarily JSON in saves, settings, or generated inventories. |
| JSON loader | The old entry that reads JSON, dispatches by `type`, and constructs C++ definitions. Early implementation may reuse it privately but cannot publish it as a Lua API. |
| `copy-from` | JSON content inheritance/copy syntax. Lua gains reuse from functions, constructors, cloning, and composition rather than copying this keyword. |
| EOC | Effect on Condition, the CCB/CDDA data-driven condition/effect mechanism with its own parsers, context, variables, and recursive execution model. |
| condition | An EOC true/false test. Platform normally expresses it with native queries and ordinary Lua expressions, not one wrapper per key. |
| effect | An EOC step that changes state or triggers an action. Platform extracts the operation into a native method or shared domain service. |
| talker | A historical dialogue/EOC abstraction wrapping characters, items, and creatures behind a common interface, often as `alpha`/`beta`. Platform should pass typed native objects. |
| EOC context | The legacy execution model carrying talkers, variables, positions, and related data. Platform callback context may carry real needs without copying old aliases. |
| variable scope | EOC lookup rules such as `u_val`, `npc_val`, `global_val`, and `context_val`. Platform replaces implicit string scopes with explicit Mod/character/world state. |
| recurrence | EOC self-repeat or delayed execution. Platform uses named tasks and a scheduler rather than publishing another recursive DSL. |
| replacement ledger | A checked disposition for every legacy inventory entry: target domain, service, status, evidence, or not-applicable reason—not old-to-new key aliases. |

## A practical vibe-coding check

Vibe coding means exploring and iterating quickly with AI; it does not mean
skipping contracts and validation. For each small Agent change, ask:

1. Is this a current v5 API or an unimplemented Platform target?
2. What are this object's owner and generation, and when does it expire?
3. Does it happen during discovery, staging, finalization, `world_ready`, or
   runtime?
4. Does the save contain stable IDs/payloads, or is it mistakenly treating a
   function, coroutine, or userdata as data?
5. Is this a domain service, or just a wrapper around a legacy JSON/EOC parser?
6. Are source, LuaLS, tests, roadmap status, and paired docs updated together?

Those questions keep fast, intuitive iteration within maintainable engineering
boundaries. See [Platform v1](lua-first-platform.md) for the architecture, the
[Platform v1 API overview](../api/lua/platform-v1/overview.md) for the current
runnable interfaces, and the [roadmap](lua-first-roadmap.md) for implementation
order.
