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
- src/lua_platform_runtime_services.cpp
- src/lua_platform_runtime_lifecycle.cpp
- src/lua_platform_runtime_hooks.cpp
- src/lua_platform_state.cpp
- src/lua_platform_content_items.cpp
- src/lua_platform_content_character.cpp
- src/debug_console.cpp
- src/mod_manager.cpp
- tools/lua_api/inspect_state.py
- tools/lua_api/extract_translations.py
- tests/lua_platform_callback_diagnostic_test.cpp
- tests/lua_platform_content_translation_test.cpp
- tests/lua_platform_test_05_tasks.cpp
- tests/mod_manager_test.cpp
- tests/lua_platform_test_02_loader.cpp
- tools/lua_api/fixtures/native_probe/ccb_native_probe.c
- tests/lua_platform_tonic_lifecycle_test.cpp
- src/mod_id_compat.h
- src/lua_platform_bindings_values.cpp
- src/lua_platform_variables.cpp
- src/lua_platform_effects.cpp
- tests/lua_platform_effects_test.cpp
- tools/lua_api/test_mod_sdk.py
- tools/migrate_lua_first.py
- src/lua_platform_creatures.cpp
- src/game.cpp
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
source_fingerprint: db98826fbb16851293007e82b7037ddd9c88285211c9eaafae8c72f46f625d5b
authority: api-contract
verified_commit: 3bb6270d3cfce5cc4e1e2942dd54902b6c83747f
verified_at: '2026-09-10'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: e8beb64e1c5389be7786824aea458b8795ff47772e6ab34844e8202072320ca1
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/779
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/lua-bridge/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/lua-bridge/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/lua-bridge/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/lua-bridge/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f
source_urls:
- path: .github/workflows/lua-contract.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/.github/workflows/lua-contract.yml
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/.github/workflows/matrix.yml
- path: ai/test-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/ai/test-matrix.yml
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/Makefile
- path: android/app/build.gradle
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/android/app/build.gradle
- path: android/app/jni/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/android/app/jni/CMakeLists.txt
- path: build-scripts/gha_compile_only.sh
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/build-scripts/gha_compile_only.sh
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/data/lua/LUA_FIRST_PLATFORM.md
- path: data/lua/types/ccb_platform_v1.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/data/lua/types/ccb_platform_v1.d.lua
- path: src/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/CMakeLists.txt
- path: src/lua/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/lua/CMakeLists.txt
- path: src/lua/lua.hpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/lua/lua.hpp
- path: src/lua_platform_loader.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/lua_platform_loader.h
- path: src/lua_platform_loader.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/lua_platform_loader.cpp
- path: src/lua_platform_runtime.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/lua_platform_runtime.h
- path: src/lua_platform_runtime.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/lua_platform_runtime.cpp
- path: src/sol/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/sol/CMakeLists.txt
- path: src/sol/config.hpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/sol/config.hpp
- path: tools/lua_api/check_cmake_contract.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/tools/lua_api/check_cmake_contract.py
- path: tools/lua_api/generate_platform_native_inventory.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/tools/lua_api/generate_platform_native_inventory.py
- path: tools/lua_api/test_check_cmake_contract.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/tools/lua_api/test_check_cmake_contract.py
- path: tests/lua_platform_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/tests/lua_platform_test.cpp
- path: tools/create_lua_mod.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/tools/create_lua_mod.py
- path: tools/lua_api/mod_sdk.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/tools/lua_api/mod_sdk.py
- path: data/lua/LUA_FIRST_EOC_WORKFLOW.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/data/lua/LUA_FIRST_EOC_WORKFLOW.md
- path: src/lua_platform_runtime_services.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/lua_platform_runtime_services.cpp
- path: src/lua_platform_runtime_lifecycle.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/lua_platform_runtime_lifecycle.cpp
- path: src/lua_platform_runtime_hooks.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/lua_platform_runtime_hooks.cpp
- path: src/lua_platform_state.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/lua_platform_state.cpp
- path: src/lua_platform_content_items.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/lua_platform_content_items.cpp
- path: src/lua_platform_content_character.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/lua_platform_content_character.cpp
- path: src/debug_console.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/debug_console.cpp
- path: src/mod_manager.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/mod_manager.cpp
- path: tools/lua_api/inspect_state.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/tools/lua_api/inspect_state.py
- path: tools/lua_api/extract_translations.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/tools/lua_api/extract_translations.py
- path: tests/lua_platform_callback_diagnostic_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/tests/lua_platform_callback_diagnostic_test.cpp
- path: tests/lua_platform_content_translation_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/tests/lua_platform_content_translation_test.cpp
- path: tests/lua_platform_test_05_tasks.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/tests/lua_platform_test_05_tasks.cpp
- path: tests/mod_manager_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/tests/mod_manager_test.cpp
- path: tests/lua_platform_test_02_loader.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/tests/lua_platform_test_02_loader.cpp
- path: tools/lua_api/fixtures/native_probe/ccb_native_probe.c
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/tools/lua_api/fixtures/native_probe/ccb_native_probe.c
- path: tests/lua_platform_tonic_lifecycle_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/tests/lua_platform_tonic_lifecycle_test.cpp
- path: src/mod_id_compat.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/mod_id_compat.h
- path: src/lua_platform_bindings_values.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/lua_platform_bindings_values.cpp
- path: src/lua_platform_variables.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/lua_platform_variables.cpp
- path: src/lua_platform_effects.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/lua_platform_effects.cpp
- path: tests/lua_platform_effects_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/tests/lua_platform_effects_test.cpp
- path: tools/lua_api/test_mod_sdk.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/tools/lua_api/test_mod_sdk.py
- path: tools/migrate_lua_first.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/tools/migrate_lua_first.py
- path: src/lua_platform_creatures.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/lua_platform_creatures.cpp
- path: src/game.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3bb6270d3cfce5cc4e1e2942dd54902b6c83747f/src/game.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.lua-bridge%29%3A+&body=Document+ID%3A+cpp.lua-bridge%0ALanguage%3A+en%0AVerified+commit%3A+3bb6270d3cfce5cc4e1e2942dd54902b6c83747f%0A%0ADescribe+the+documentation+problem%3A%0A
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

The loader implements the open policy and discovery notice described below.
Build configurations and runtime results are recorded in [source PR #768](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/768).
Manual UI acceptance and native module packaging on each platform require separate evidence.

## PR artifact boundary

PR artifacts are downloadable copies of successful builds and result-navigation aids for manual
testing and diagnosis. They are not contracts for the Lua API, ABI, loader, lifecycle, or runtime
behavior. Artifact names, archive formats, retention, PR-comment links, and even optional upload
success cannot prove Platform correctness. Contract evidence comes from the source, checkers, and
build jobs above; the artifact-publishing workflow only consumes those results and must not define
the runtime in reverse.

## Bounded semantic acceptance and persistent tonic

The related source changes merged through [#751](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/751)
and [#752](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/752).
The source semantic ledger and tests define the covered scope; this does not establish replacement of all EOC behavior.

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

## Trusted loading, diagnostics and author tools

This section accompanies source changes [#755](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/755),
[#756](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/756),
[#757](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/757),
[#758](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/758),
[#759](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/759),
[#760](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/760),
[#761](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/761),
[#762](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/762),
[#763](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/763),
[#764](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/764),
[#765](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/765),
[#766](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/766) and
[#767](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/767).
These changes are integrated in [#768](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/768).
This page pins the corresponding source revision in `verified_commit`; consult
the PR acceptance record for build configurations, native regressions and actual
shared-library loading results. Test source alone is not passing evidence.

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
reentry while Lua is executing or another replacement is in progress, and requires a restart for changed static
definitions. Preparation failures retain previous registrations and show the
error. Success means registration replacement; check the message log for
callback failures. Manual UI acceptance is separate from backend reentry regressions.

Missing handlers and failed payload migrations already discard the affected
persistent tasks. #755 summarizes each Mod's discard count in the message log;
`debug.log` retains task-specific reasons. Supply migrations before task
processing. Save-load errors also identify scope, Mod, task index and task ID,
which can be inspected below. #759 corrects the floating-to-integer range check
for saved Character recurrence due turns, rejecting `2^63` before conversion.

#762 distinguishes omitted Item fields from explicit defaults in static fingerprints.
For an inherited Item, omitting `mass_grams` keeps the source mass; setting
`mass_grams = 0` overwrites it. Their fingerprints now differ.

### Lua console

#761 builds on #760 with **Debug menu → Console → Lua**. Select a loaded Mod,
enter ordinary Lua code and click **Run Lua**. Continue using `require("ccb")`
for Platform access and `return` to display values:

```lua
local ccb = require("ccb")
return ccb.services.turn()
```

Code runs explicitly in the selected Mod's existing state after the drawing frame,
without automatic reevaluation. Calls enter that Mod's callback scope; world-ready,
handle and domain checks still apply. Global, world and external changes do not
roll back if later code fails. Recursive execution in the same state and execution
during reload are rejected. Display shows up to 16 returns and reads at most 1024
bytes per string, escaping controls and replacing invalid UTF-8. Returned tables
show at most 20 raw fields in unspecified order; nested tables and other objects
appear as type labels. No `__pairs` or `__tostring` runs. Return a nested field
explicitly to inspect it. These are display
limits, not script quotas. This is not a breakpoint debugger; manual UI acceptance
remains separate from backend regressions.

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

### Live state inspection and save boundaries

#763 adds `ccb.state.world.keys(after_key?, limit?)` and its character-scope
counterpart after `world_ready`. They return copied keys owned by the Mod, without
values. The default page size is 20, with a range of 1–200. Keys use bytewise
lexicographic order and an exclusive string cursor that need not still exist.
Results contain `items`, `total`, `matched`, `returned`, `limit`, and `truncated`;
`next_after` is present only when another page exists. Keys may contain NUL: pass
the original cursor back rather than reconstructing it from displayed text.
Each call takes a fresh snapshot; restart pagination if keys change between calls.
Editing a returned table does not mutate state.

#764 retains the existing 1 MiB state-codec and 16 MiB runtime-scope file limits,
but rejects excess output during temporary JSON encoding instead of constructing
the entire oversized result first. Limit failure occurs before destination writes.
This is neither a transaction across scope files nor a process-wide Lua memory
limit.

#765 fixes result construction in `tasks.get`, `tasks.next`, and `tasks.list`:
selected task records are copied before Lua table allocation, so cancellation
from garbage collection cannot invalidate borrowed records. Existing ordering
and list limits remain unchanged; query results are detached snapshots. Native
regression source models cancellation at the allocation boundary.

#764 also uses double round-trip precision on Lua save staging streams, preventing
the generic JSON writer's fixed six decimal places from rounding small state
values to zero. Other JSON writers are unchanged; earlier lost precision cannot
be recovered. #765 extends the existing task-migration guard through argument
construction and result decoding, restoring the previous flag on success or
failure without promising rollback of unrelated callback side effects.

#766 stores optional per-Mod `last_task_id` in both scopes, even with no pending
tasks. Loading takes the maximum counter and preserves exhaustion and absent-Mod
records. Older version-1 files without the field still derive a counter from
pending tasks; completed legacy IDs cannot be reconstructed. #756 reports
`last_task_id` and `task_counter_persisted` to distinguish these cases.

#767 keeps same-pass due tasks queryable and cancellable until their own dispatch
starts. An earlier callback can cancel a later task; due-turn/ID order is unchanged,
and newly scheduled tasks still wait for another processing pass.

### Runtime and static content text translation

#758 provides `ccb.services.translate(text, context?)` and
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

Item names and descriptions can instead retain static text for native translation
at display time:

```lua
local ccb = require("ccb")
ccb.content.add(ccb.content.Item {
    id = "MyMod_water_bottle", mass_grams = 500, volume_ml = 500,
    name = ccb.content.plural_text("bottle of water", "bottles of water", "MyMod item"),
    description = ccb.content.text("A sealed bottle.", "MyMod description")
})
```

These immutable `LocalizedText` values retain source forms without fixing the
current language. Plain strings remain untranslated; descriptions reject plural
values. A name marked with `text` uses the same plural source fallback; use
`plural_text` for distinct forms. Source forms must be nonempty and inputs must
exclude NUL. Inheritance preserves omitted translated fields; explicit strings
replace them. Translation status, context and plural changes affect the static
fingerprint. Singular `content.text` also covers Skill names/descriptions, SkillDisplay labels
and theory/practice level descriptions; those fields reject plural markers.
Plain strings remain literal. Omitting practice text leaves its independent map
alone, and invalid arguments do not partially overwrite theory text. Skill static
fingerprints distinguish text context and theory/practice collection identity.

Run extraction from the Mod root with explicit filenames:

```sh
python3 /path/CCB/tools/lua_api/extract_translations.py main.lua --output messages.pot
python3 /path/CCB/tools/lua_api/extract_translations.py main.lua --output messages.pot --check
```

The tool invokes GNU `xgettext`, never Lua. Keep full runtime translation or
`ccb.content.text`/`ccb.content.plural_text` calls and
literal messages/contexts; aliases and computed text/context cannot be reliably
extracted. Translation calls directly nested inside `string.format` inherit
format-check flags. `--check` only compares: exit 1 means a missing/stale template,
2 means extraction failure.

For external Mods under the configured user Mod directory, the existing scanner
recognizes `MyMod/lang/mo/<language>/LC_MESSAGES/MyMod.mo`. Catalog compilation and
installation are later release steps. Bundled Mods are not automatically covered
by the user-directory scan. Use distinctive contexts for common messages in the
shared catalog registry. Builders beyond Item/Skill/SkillDisplay, Mod metadata translation and
catalog hot reload remain deferred. Real catalogs, plural rules and language
changes still need dedicated acceptance; see #768 for tested build configurations.
This is not complete internationalization.

## Core package ID compatibility

The canonical core package ID becomes `ccb`. New JSON metadata uses
`"dependencies": [ "ccb" ]`, and Lua `ModDefinition` uses `dependencies = { "ccb" }`.
Existing Mods may retain `dda` dependencies. JSON conflict lists and user default
Mod lists also resolve the old ID. This aliases one core package; it does not
register a second core.

Old worlds resolve `dda` to `ccb` while reading their Mod lists. Lists containing
both IDs are deduplicated in order, loading core once; subsequent Mod-list saves
write the canonical ID. Old provenance records, `mod_interactions/dda/`, and
`services.gameplay.mods.is_loaded("dda")` / `load_order("dda")` continue to identify
that core. The display name and `data/mods/dda/` directory remain unchanged; user
save directories are not renamed.

Compatibility is forward from old CCB worlds and Mods to the new version. Worlds
saved by the new version are not guaranteed to work in older versions. The alias deduplication tests passed 12 assertions. The real Mod discovery test
was compiled but not executed. Old-world loading and Android device validation
have not been completed.

## Effect snapshots and variable queries

`ccb.services.effects.get(character, effect_id, body_part?)` returns a detached effect snapshot containing intensity, duration, start time, body part, and related effects. A missing effect returns `not_found`; other failures, including stale handles, still require handling. Omitting the body part uses the native unqualified lookup.

For a dynamic intensity threshold, read the effect first and evaluate the threshold only when it exists, then compare `snapshot.intensity`. This preserves lazy evaluation and supports ordinary Lua comparisons beyond the optional intensity argument accepted by `effects.has`. Any-of queries should stop at the first match; long lists can use sequential branches or loops.

`ccb.services.types.id(kind, value)` constructs a `GameId`; `id_kinds()` lists supported kinds, and `GameId:is_valid()` checks whether the definition exists. The LuaLS declarations now describe these existing native methods and effect snapshots.

`ccb.services.variables.get(actor, key)` reads a variable from an explicit owner; `get_global(key)` reads a global variable. The result's `value` contains `exists` and the stored `value`. Variable keys contain 1–128 bytes and reject ASCII controls and NUL; writes retain callback and write-phase requirements.

The `u` and `npc` scopes in `variables.resolve(context, actor, scope, key)` use the same supplied `actor`; they do not select a dialogue participant for the caller. Indirect `var` references retain that owner too. Select the owner explicitly. When migration references cross participants, the migrator resolves the final scope before supplying the appropriate handle. Character-focused Lua behaviour can express ownership directly with `get`, `set`, and `remove`.

Validation for this scope includes a real LuaLS check, executable migration tests, and native effect comparisons. Semantic acceptance of all EOC selectors continues by domain.

### Anatomy-weighted body-part selection

`ccb.services.characters.random_body_part(character, main_parts_only?)` returns a `CcbBodyPartIdResult`. On success, `value` is the selected `GameId<body_part>`; an invalidated character handle returns an error. Selection uses that character's native anatomy weights rather than sampling uniformly from a list of parts. The second argument defaults to `false`; `true` maps the sampled part to its main part.

`ccb.services.characters.avatar()` returns the actual game player's `GameHandle`, independently of dialogue participants. When migrating legacy effect addition or removal with `target_part: "RANDOM"`, obtain the player through this API and preserve the original rule: sample the player's anatomy even when operating on an NPC's effect, and sample separately for each effect being removed. New Lua gameplay can choose which character to pass to this API. This does not certify dynamic body-part variables, all effect writes, or all EOC semantics.

### Complete body-part lists and per-part removal

`ccb.services.characters.body_parts(character)` returns a `CcbBodyPartsResult`. On success, `value` is the complete array of `GameId<body_part>` values in native order, without sorting or truncation. It does not add `bp_null`, which represents an unqualified part. The list is a detached snapshot; an invalidated character handle returns an error.

Legacy EOC `target_part: "ALL"` first obtains the complete part list, removes each effect from every part, then performs an unqualified removal. Migration preserves that order, including the parts, count, and order of removal events. A single `effects.remove(character, effect_id)` can clear the same final state while producing a different event sequence. A non-character Creature's legacy talker has no part list, so its `ALL` still corresponds to one unqualified removal.

### Registered parts and current anatomy

Effect APIs require a registered body-part ID, but do not require the part to remain in the target's current anatomy. This matches native storage, lookup, and removal by part ID. For example, when a registered tail is absent from a character's current anatomy, querying an absent effect returns `false` (`effects.get` returns `not_found`), rather than an argument error caused by the missing part. Native addition, lookup, and removal still operate on that ID.

ID kind and definition checks, together with Character/Creature handle validity checks, remain in effect. `characters.body_parts` lists the parts currently present; effects associated with other registered parts do not expand that list.
