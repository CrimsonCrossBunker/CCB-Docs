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
source_fingerprint: 1151c25bcfbd563323b5004b700f649ecf7d58cf4637d9563e8db2bc84e1a6bd
authority: api-contract
verified_commit: 71bfdf23ba26594efbc57797fb6bfb6cf497af82
verified_at: '2026-09-06'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 25efd3c9c2010db1c3336a07a30985f7440900a209ba3fdff555fe91c71245d1
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/lua-bridge/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/lua-bridge/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/lua-bridge/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/lua-bridge/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/71bfdf23ba26594efbc57797fb6bfb6cf497af82
source_urls:
- path: .github/workflows/lua-contract.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/.github/workflows/lua-contract.yml
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/.github/workflows/matrix.yml
- path: ai/test-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/ai/test-matrix.yml
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/Makefile
- path: android/app/build.gradle
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/android/app/build.gradle
- path: android/app/jni/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/android/app/jni/CMakeLists.txt
- path: build-scripts/gha_compile_only.sh
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/build-scripts/gha_compile_only.sh
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/data/lua/LUA_FIRST_PLATFORM.md
- path: data/lua/types/ccb_platform_v1.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/data/lua/types/ccb_platform_v1.d.lua
- path: src/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/src/CMakeLists.txt
- path: src/lua/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/src/lua/CMakeLists.txt
- path: src/lua/lua.hpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/src/lua/lua.hpp
- path: src/lua_platform_loader.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/src/lua_platform_loader.h
- path: src/lua_platform_loader.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/src/lua_platform_loader.cpp
- path: src/lua_platform_runtime.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/src/lua_platform_runtime.h
- path: src/lua_platform_runtime.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/src/lua_platform_runtime.cpp
- path: src/sol/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/src/sol/CMakeLists.txt
- path: src/sol/config.hpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/src/sol/config.hpp
- path: tools/lua_api/check_cmake_contract.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/tools/lua_api/check_cmake_contract.py
- path: tools/lua_api/generate_platform_native_inventory.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/tools/lua_api/generate_platform_native_inventory.py
- path: tools/lua_api/test_check_cmake_contract.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/tools/lua_api/test_check_cmake_contract.py
- path: tests/lua_platform_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/tests/lua_platform_test.cpp
- path: tools/create_lua_mod.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/tools/create_lua_mod.py
- path: tools/lua_api/mod_sdk.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/tools/lua_api/mod_sdk.py
- path: data/lua/LUA_FIRST_EOC_WORKFLOW.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71bfdf23ba26594efbc57797fb6bfb6cf497af82/data/lua/LUA_FIRST_EOC_WORKFLOW.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.lua-bridge%29%3A+&body=Document+ID%3A+cpp.lua-bridge%0ALanguage%3A+en%0AVerified+commit%3A+71bfdf23ba26594efbc57797fb6bfb6cf497af82%0A%0ADescribe+the+documentation+problem%3A%0A
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
creates an isolated Lua state for each Mod and restricts module resolution and the exposed native
surface. The engine continues to own native objects, registries, and lifetimes; Lua reaches them
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

This target is not implemented by the tooling change. The current loader still restricts
libraries and module paths. An execution-risk notice before downloaded Mod code, including
`mod.lua` discovery, also needs integration. Policy acceptance must not be described as
permissions already being opened.

## PR artifact boundary

PR artifacts are downloadable copies of successful builds and result-navigation aids for manual
testing and diagnosis. They are not contracts for the Lua API, ABI, loader, lifecycle, or runtime
behavior. Artifact names, archive formats, retention, PR-comment links, and even optional upload
success cannot prove Platform correctness. Contract evidence comes from the source, checkers, and
build jobs above; the artifact-publishing workflow only consumes those results and must not define
the runtime in reverse.
