---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.lua-bridge
title: Native Lua bridge
language: en
status: draft
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
- .github/workflows/lua-contract.yml
- .github/workflows/matrix.yml
- ai/test-matrix.yml
- Makefile
- android/app/build.gradle
- android/app/jni/CMakeLists.txt
- build-scripts/gha_compile_only.sh
- data/lua/LUA_FIRST_PLATFORM.md
- data/lua/types/ccb_platform_v1.d.lua
- src/CMakeLists.txt
- src/lua/CMakeLists.txt
- src/lua/lua.hpp
- src/lua_platform_loader.h
- src/lua_platform_loader.cpp
- src/lua_platform_runtime.h
- src/lua_platform_runtime.cpp
- src/sol/CMakeLists.txt
- src/sol/config.hpp
- tools/lua_api/check_cmake_contract.py
- tools/lua_api/generate_platform_native_inventory.py
- tools/lua_api/test_check_cmake_contract.py
- tests/lua_platform_test.cpp
- tools/create_lua_mod.py
- tools/lua_api/mod_sdk.py
- data/lua/LUA_FIRST_EOC_WORKFLOW.md
source_symbols:
- platform_version = 1
- initialize_state(
- install_runtime_api(
- configure_lua_platform
- validate_cmake_contract
- INSTALLER_SPECS
source_queries:
- PROPERTIES LANGUAGE C
- $(COMPILE.c)
- '#define SOL_BUILD_CXX_MODE 1'
- 'CATA_ENABLE_LUA_PLATFORM: ${{ matrix.lua_platform }}'
- 'lua_platform: 1'
- -DCATA_ENABLE_LUA_PLATFORM="${CATA_ENABLE_LUA_PLATFORM:-1}"
- -DCATA_ENABLE_LUA_PLATFORM=ON
- python3 tools/lua_api/check_cmake_contract.py
source_fingerprint: bdb44582cdb3cede21b88c87e11435e7d5520c28559a73914d34fcb00944e1f3
authority: api-contract
verified_commit: 77631e8b0c782684b88e1cfc05dd4da64a7ec926
verified_at: '2026-09-08'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a724d8b49cc10f542d1630e96fdcdefacb5ad28a609754d5c19560c9886baf47
prerequisites:
- cpp.mod-loading
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- lua-contract
api_version: '1'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/755
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/lua-bridge/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/lua-bridge/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/lua-bridge/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/lua-bridge/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/77631e8b0c782684b88e1cfc05dd4da64a7ec926
source_urls:
- path: .github/workflows/lua-contract.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/.github/workflows/lua-contract.yml
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/.github/workflows/matrix.yml
- path: ai/test-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/ai/test-matrix.yml
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/Makefile
- path: android/app/build.gradle
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/android/app/build.gradle
- path: android/app/jni/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/android/app/jni/CMakeLists.txt
- path: build-scripts/gha_compile_only.sh
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/build-scripts/gha_compile_only.sh
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/data/lua/LUA_FIRST_PLATFORM.md
- path: data/lua/types/ccb_platform_v1.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/data/lua/types/ccb_platform_v1.d.lua
- path: src/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/src/CMakeLists.txt
- path: src/lua/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/src/lua/CMakeLists.txt
- path: src/lua/lua.hpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/src/lua/lua.hpp
- path: src/lua_platform_loader.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/src/lua_platform_loader.h
- path: src/lua_platform_loader.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/src/lua_platform_loader.cpp
- path: src/lua_platform_runtime.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/src/lua_platform_runtime.h
- path: src/lua_platform_runtime.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/src/lua_platform_runtime.cpp
- path: src/sol/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/src/sol/CMakeLists.txt
- path: src/sol/config.hpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/src/sol/config.hpp
- path: tools/lua_api/check_cmake_contract.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/tools/lua_api/check_cmake_contract.py
- path: tools/lua_api/generate_platform_native_inventory.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/tools/lua_api/generate_platform_native_inventory.py
- path: tools/lua_api/test_check_cmake_contract.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/tools/lua_api/test_check_cmake_contract.py
- path: tests/lua_platform_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/tests/lua_platform_test.cpp
- path: tools/create_lua_mod.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/tools/create_lua_mod.py
- path: tools/lua_api/mod_sdk.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/tools/lua_api/mod_sdk.py
- path: data/lua/LUA_FIRST_EOC_WORKFLOW.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/77631e8b0c782684b88e1cfc05dd4da64a7ec926/data/lua/LUA_FIRST_EOC_WORKFLOW.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.lua-bridge%29%3A+&body=Document+ID%3A+cpp.lua-bridge%0ALanguage%3A+en%0AVerified+commit%3A+77631e8b0c782684b88e1cfc05dd4da64a7ec926%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Native Lua bridge

## Contract boundary

CCB supports only Lua-first Platform v1. A Mod obtains its package-local `ccb` table through
`require("ccb")`; the authoritative public declaration is
`data/lua/types/ccb_platform_v1.d.lua`. The removed Lua API v5, its manifest/capability model,
and the `game.*` compatibility entry are not part of this bridge and must not return as a second
runtime.

Platform is a trusted in-process extension boundary, not a process-level sandbox. The loader
creates a separate Lua state and owner-specific `ccb` entry for each Mod. The engine continues to own native objects, registries, and lifetimes; Lua reaches them
only through the values, snapshots, and generation-checked handles declared by Platform v1.

## Public entry and lifecycle

`src/lua_platform_loader.cpp` discovers `main.lua` and optional `mod.lua`, creates states,
installs `package.loaded["ccb"]`, resolves modules within the Mod root, and manages candidate
runtime preparation, commit, rollback, and replacement. `src/lua_platform_runtime.cpp` and the
domain-specific `src/lua_platform_*.cpp` files install the native implementations of
`ccb.content`, `ccb.runtime`, `ccb.dialogue`, `ccb.services`, `ccb.state`,
`ccb.tasks`, and `ccb.presentation`.

Every public symbol must agree across native registration, the LuaLS declaration, and the
generated inventory, with Platform contract and coverage tests proving parity. Explanatory prose
cannot replace those sources.

## One bundled Lua ABI

Make, desktop CMake, and Android compile the same repository-owned `src/lua/*.c` sources and use
Lua's standard C ABI throughout:

| Build entry | ABI constraint |
| --- | --- |
| `Makefile` | Places bundled Lua in `LUA_C_SOURCES`/`C_SOURCES` and compiles it with `$(COMPILE.c) -x c`. |
| `src/lua/CMakeLists.txt` | Sets `PROPERTIES LANGUAGE C` on `LUA_SOURCES` before creating `liblua`. |
| `android/app/jni/CMakeLists.txt` | Enables C and C++, then reuses the `src/lua` subdirectory and therefore the same `LANGUAGE C` contract. |

`CATA_ENABLE_LUA_PLATFORM` controls whether Platform is linked. When enabled, desktop CMake
propagates `libsol` through `configure_lua_platform()`, Android links the same `libsol`, and Make
places the Lua C objects and Platform C++ objects in the same final link. A disabled build must
use the disabled stub rather than retain a partial Lua runtime.

## C++ and sol2 linkage

Platform C++ translation units wrap directly included Lua headers in `extern "C"`;
`src/lua/lua.hpp` provides the same C-linkage wrapper. sol2 itself is consumed as C++, so
`src/sol/config.hpp` defines `SOL_BUILD_CXX_MODE=1`, but that setting does not change the Lua
library ABI.

Do not define `SOL_USE_CXX_LUA`, and do not change the bundled `*.c` files to `LANGUAGE CXX`.
Either change makes one side expect C++ linkage while the other exports C symbols, producing Lua
API undefined references at final link. The invariant is: compile the Lua runtime as C, and have
every C++/sol2 caller declare the Lua API with C linkage.

## Extension and change checklist

Complete a bridge change as one coherent batch:

1. Implement and register the native operation in the matching domain `lua_platform_*.cpp`;
2. update `ccb_platform_v1.d.lua`, the native inventory, and the Platform contract together;
3. keep the Make, CMake, and Android Lua source sets and C ABI aligned;
4. add or update focused behavior, parity, coverage, and disabled-build tests;
5. update generated reference material only after source, declaration, inventory, and tests agree.

## Contract and build gates

The `Lua public contract` workflow runs the LuaLS, native-inventory, Platform-contract, coverage,
CMake/ABI, and `tools/lua_api` unit checks. `check_cmake_contract.py` explicitly rejects
`LANGUAGE CXX` and `SOL_USE_CXX_LUA`, while verifying that `libsol` stays optional and propagates
correctly.

In addition to those static gates, the orthogonal PR build matrix must actually compile and link
Platform-enabled Make, desktop CMake, and Android configurations. The static checker proves
configuration-text invariants; the build jobs prove that compilers, linkers, and target platforms
can consume the ABI. Neither result substitutes for the other.

Implement complete domain batches and reuse passing evidence while inputs are unchanged.
Tool, documentation, and template changes do not require a game build by default; native or
build-configuration changes select the affected compile/runtime checks. Full JSON/EOC audits
belong to content migration, parity claims, or EOC removal. Individual checkers diagnose
failures; the unified local contract gate is:

```sh
# validation: lua-contract
python3 -m unittest discover -s tools/lua_api -p 'test_*.py'
```

## Mod editor and upgrade checks

The scaffolder now includes optional `.luarc.json` and `.ccb-sdk/` files by default:

```sh
python3 tools/create_lua_mod.py /path/MyMod --template complete
```

Open the directory in a LuaLS-enabled editor for completion and argument diagnostics. The SDK
stores the selected CCB declarations verbatim, the Platform major version, and a SHA-256 hash.
Use `--declarations /path/game/data/lua/types/ccb_platform_v1.d.lua` to select declarations from
the target game package. Relative configuration survives moving the project. Snapshots never
auto-update and do not identify the running executable or prove save compatibility. Use
`--no-editor` to omit these files. Runtime code continues to use the game's `require("ccb")`;
the templates check the Platform major version before registering content.

With LuaLS installed, check a Mod or compare two projects' SDKs:

```sh
python3 tools/lua_api/mod_sdk.py check /path/MyMod
python3 tools/lua_api/mod_sdk.py compare /path/OldMod /path/NewVersionScaffold
```

The check command accepts `--language-server /absolute/path/to/lua-language-server`. Diagnostics
include the absolute file, line, column, code, and argument type explanation. Exit 0 means no
static diagnostics, 1 means diagnostics, and 2 means configuration or checker failure. A crash
or missing report cannot count as success. The comparison reports added, removed, and changed
declarations without modifying either project or promising behavior/save compatibility.

Existing declarations still have annotation gaps. Static checks do not audit the SDK library,
execute Mods, validate native content IDs, or replace game loading and behavior acceptance.
Ordinary runtime errors retain their existing Mod/handler context in `debug.log`; this batch
adds no in-game debugger, state/task inspector, or native compatibility negotiation.

CI pins the LuaLS 3.19.1 archive and SHA-256, checks both templates, and verifies diagnostics
for unknown APIs, wrong argument types, and missing arguments. Set `CCB_LUALS` to enable these
integration tests within the same local contract suite:

```sh
CCB_LUALS=/path/lua-language-server python3 -m unittest discover -s tools/lua_api -p 'test_*.py'
python3 tools/test_create_lua_mod.py
```

## Accepted trust policy and implementation boundary

The accepted target treats Mods from every source as executable code the player chooses to
trust at their own system risk: full standard libraries plus external Lua modules and native
dynamic libraries where supported. Per-Mod states provide naming and ownership boundaries,
not process crash containment. No mandatory global instruction/memory quota is imposed by
default; supported `ccb` argument, handle, lifecycle, and persistent-data checks remain.
Native module authors own OS, architecture, Lua ABI, and dependency compatibility.

The previously checked source baseline still restricts libraries and module paths.
Draft #755 below begins implementing the open policy and discovery notice, but
native acceptance and merge remain pending; this is not a shipped capability.

## PR artifact boundary

PR artifacts are downloadable copies of successful builds and result-navigation aids for manual
testing and diagnosis. They are not contracts for the Lua API, ABI, loader, lifecycle, or runtime
behavior. Artifact names, archive formats, retention, PR-comment links, and even optional upload
success cannot prove Platform correctness. Contract evidence comes from the source, checkers, and
build jobs above; the artifact-publishing workflow only consumes those results and must not define
the runtime in reverse.

## Pending merge: 50-selector semantic acceptance and persistent tonic

This section accompanies source branch `codex/lua-semantic-acceptance` and takes
effect when its source PR merges. The batch establishes bounded evidence for 50
selected EOC selectors, not replacement of all 586 entries. Eight mutation writes
intentionally differ: the migrator retains `semantic_choice` so authors choose
the intended gameplay semantics explicitly.

- `services.skills.offered(teacher, student)` returns a `CcbResult` whose `value`
  contains `items` (at most 256 skill IDs), `total`, `returned`, and `truncated`.
  Teaching uses the student's knowledge level. Both arguments require valid
  Character handles.
- Teaching and visible-mutation queries require both proven participants.
  Unknown partners remain migration TODOs; they are not inferred as the avatar,
  and teaching conditions are not replaced with a constant `false`.
- Effect addition preserves native zero-duration and signed-intensity semantics;
  a negative intensity is not a delta. Morale range migration uses the native
  integer bounds, including bounds written in reverse order.
- The `Lua_First_Example` tonic consumes a capacitor cell, starts three stamina
  pulses through a native effect event, and persists cooldown and remaining
  tasks. Native tests check avatar files, fresh Lua state restoration, and the
  absence of duplicate pulses.

Evidence lives in the source repository's `tests/lua_platform_*_semantics_test.cpp`,
`tests/lua_platform_mutations_test.cpp`, `tests/lua_platform_effects_test.cpp`, and
`tests/lua_platform_tonic_lifecycle_test.cpp`. These are native integration tests
with cached static engine definitions, not manual UI or full process-restart acceptance.

## Draft: trusted loading, diagnostics and author tools

This section accompanies source drafts [#755](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/755),
[#756](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/756),
[#757](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/757),
[#758](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/758),
[#759](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/759) and
[#760](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/760).
No native build or acceptance has run. This page retains its previously checked
`verified_commit` as a baseline, not evidence that these draft capabilities ship.
Refresh the evidence and publish only after source merge and acceptance.

### Loading and failure diagnostics

#755 opens all standard libraries and retains normal `package` searchers. The
Mod-local searcher runs first; other modules retain Lua 5.4 cache, preload and
loader-data return semantics. Native paths start with the Mod root’s `?.so`
(`?.dll` on Windows), retaining original paths. Roots containing `;` or `?` use
explicit `package.loadlib` paths to avoid cpath grammar ambiguity. `require("ccb")` always returns that Mod's Platform
table. Native modules must match the host OS, architecture and Lua C ABI, without
linking another Lua runtime. Build configuration is not proof that a real DLL/SO
loads; Windows packaging and native loading on each platform still need acceptance.

Discovery presents the execution notice before evaluating possible Lua metadata
in `mod.lua`. Its first prompt does not depend on keybindings initialized later;
noninteractive checks emit the notice to stderr. Forward metadata with
`return (require("metadata"))`: parentheses retain one `ccb.ModDefinition`, avoiding
Lua 5.4's second return value on the first `require` call.

Load errors preserve owner, stage, source path and original Lua error. Callback
errors name the triggering event/hook; task errors include task ID, scope and due
turn, distinguishing uses of the same handler. Platform rollback cannot undo
trusted Lua code's side effects on user files, the OS or external services.

### Reload scripts inside the game

#760 adds **Debug menu → Game → Reload Lua Mod scripts**, also available through
debug-action search. It reuses the existing replacement backend, rejects
reentry while Lua is executing and requires a restart for changed static
definitions. Preparation failures retain previous registrations and show the
error. Success means registration replacement; check the message log for
callback failures. The UI and reentry regression source still need native acceptance.

Missing handlers and failed payload migrations already discard the affected
persistent tasks. #755 summarizes each Mod's discard count in the message log;
`debug.log` retains task-specific reasons. Supply migrations before task
processing. Save-load errors also identify scope, Mod, task index and task ID,
which can be inspected below. #759 corrects the floating-to-integer range check
for saved Character recurrence due turns, rejecting `2^63` before conversion.
That implementation and its boundary regression source have not been compiled or run.

### Inspect a save and compare the target SDK

#757 also adds an editor SDK to an existing Mod:

```sh
python3 tools/lua_api/mod_sdk.py init /path/MyMod --declarations /path/game/data/lua/types/ccb_platform_v1.d.lua
```

The directory must already exist. This adds `.ccb-sdk/` and `.luarc.json` without
rewriting author Lua files. Either destination already existing, including a
symlink, prevents installation; keep or integrate the existing editor setup yourself.
Omitting `--declarations` selects this source tree's declarations, without searching
for an installed game.

```sh
python3 tools/lua_api/inspect_state.py /path/world/lua_platform_world.json --mod MyMod
python3 tools/lua_api/inspect_state.py /path/world/lua_platform_world.json --mod MyMod --task 225
python3 tools/lua_api/mod_sdk.py compare-release /path/MyMod --declarations /path/game/data/lua/types/ccb_platform_v1.d.lua
```

#756 reads only the named save file, summarizing state keys, tasks, participants,
due turns and saved location hints. State/payload values require `--values`;
`--limit` caps each displayed list while retaining totals. `--mod ID --task N`
finds a logged task directly, including records beyond display limits, reporting
total and matched counts separately. It does not execute
Lua, load a world, edit saves or establish handler availability/object liveness.
#757 compares against the target game's declaration file directly, without a
second Mod scaffold. It neither updates the SDK nor proves native/save compatibility.

### Runtime text translation

#758 proposes `ccb.services.translate(text, context?)` and
`ccb.services.translate_plural(singular, plural, count, context?)` after
`world_ready`, reusing the current native language catalog. Both return strings.
Missing entries fall back to source text: count 1 selects singular, other
nonnegative counts select plural. Text/context cannot contain NUL; counts must
fit the target's native `size_t`.

```lua
local ccb = require("ccb")
ccb.runtime.handler("ready_text", function()
    ccb.services.message(string.format(ccb.services.translate_plural(
        "%d item is ready", "%d items are ready", 2, "MyMod status"), 2))
end)
ccb.runtime.on("world_ready", "ready_text")
```

Run extraction from the Mod root with explicit filenames:

```sh
python3 /path/CCB/tools/lua_api/extract_translations.py main.lua --output messages.pot
python3 /path/CCB/tools/lua_api/extract_translations.py main.lua --output messages.pot --check
```

The tool invokes GNU `xgettext`, never Lua. Keep full `ccb.services` calls and
literal messages/contexts; aliases and computed text/context cannot be reliably
extracted. Translation calls directly nested inside `string.format` inherit
format-check flags. `--check` only compares: exit 1 means a missing/stale template,
2 means extraction failure.

For external Mods under the configured user Mod directory, the existing scanner
recognizes `MyMod/lang/mo/<language>/LC_MESSAGES/MyMod.mo`. Catalog compilation and
installation are later release steps. Bundled Mods are not automatically covered
by the user-directory scan. Use distinctive contexts for common messages in the
shared catalog registry. This slice excludes deferred content-name/metadata
translation and catalog hot reload. Real translations, plural rules, language
changes and nonlocalized builds still need native acceptance; this is not complete
internationalization.
