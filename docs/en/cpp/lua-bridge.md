---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.lua-bridge
title: Native Lua bridge
language: en
status: active
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
source_fingerprint: 1e0cd7300f0352381de0ea3414d9a48bacf7ee61d0d9f2da78132498776f7100
authority: api-contract
verified_commit: 9773fd98a173b617e066ee68a85fdbed72e0bbba
verified_at: '2026-08-31'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 6e0a39ccb8ab876b10c0e1465e61ba9f51336c05b84f4e7a83e72dea68925144
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
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/9773fd98a173b617e066ee68a85fdbed72e0bbba
source_urls:
- path: .github/workflows/lua-contract.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/.github/workflows/lua-contract.yml
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/.github/workflows/matrix.yml
- path: ai/test-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/ai/test-matrix.yml
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/Makefile
- path: android/app/build.gradle
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/android/app/build.gradle
- path: android/app/jni/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/android/app/jni/CMakeLists.txt
- path: build-scripts/gha_compile_only.sh
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/build-scripts/gha_compile_only.sh
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/data/lua/LUA_FIRST_PLATFORM.md
- path: data/lua/types/ccb_platform_v1.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/data/lua/types/ccb_platform_v1.d.lua
- path: src/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/src/CMakeLists.txt
- path: src/lua/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/src/lua/CMakeLists.txt
- path: src/lua/lua.hpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/src/lua/lua.hpp
- path: src/lua_platform_loader.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/src/lua_platform_loader.h
- path: src/lua_platform_loader.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/src/lua_platform_loader.cpp
- path: src/lua_platform_runtime.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/src/lua_platform_runtime.h
- path: src/lua_platform_runtime.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/src/lua_platform_runtime.cpp
- path: src/sol/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/src/sol/CMakeLists.txt
- path: src/sol/config.hpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/src/sol/config.hpp
- path: tools/lua_api/check_cmake_contract.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/tools/lua_api/check_cmake_contract.py
- path: tools/lua_api/generate_platform_native_inventory.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/tools/lua_api/generate_platform_native_inventory.py
- path: tools/lua_api/test_check_cmake_contract.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/tools/lua_api/test_check_cmake_contract.py
- path: tests/lua_platform_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9773fd98a173b617e066ee68a85fdbed72e0bbba/tests/lua_platform_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.lua-bridge%29%3A+&body=Document+ID%3A+cpp.lua-bridge%0ALanguage%3A+en%0AVerified+commit%3A+9773fd98a173b617e066ee68a85fdbed72e0bbba%0A%0ADescribe+the+documentation+problem%3A%0A
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

The narrow local contract gate is:

```sh
# validation: lua-contract
python3 tools/lua_api/check_luals_declarations.py
python3 tools/lua_api/check_platform_native_inventory.py
python3 tools/lua_api/check_platform_contract.py
python3 tools/lua_api/check_platform_coverage.py
python3 tools/lua_api/check_cmake_contract.py
python3 -m unittest discover -s tools/lua_api -p 'test_*.py'
```

## PR artifact boundary

PR artifacts are downloadable copies of successful builds and result-navigation aids for manual
testing and diagnosis. They are not contracts for the Lua API, ABI, loader, lifecycle, or runtime
behavior. Artifact names, archive formats, retention, PR-comment links, and even optional upload
success cannot prove Platform correctness. Contract evidence comes from the source, checkers, and
build jobs above; the artifact-publishing workflow only consumes those results and must not define
the runtime in reverse.
