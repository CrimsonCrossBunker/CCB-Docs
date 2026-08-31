---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.lua-bridge
title: Native Lua bridge
language: zh_CN
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
source_fingerprint: 39aae4e1674e20ce79f1afed08505dfbe6e40e0fb0269c5f4958b57d5b56bb9e
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/lua-bridge/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.lua-bridge%29%3A+&body=Document+ID%3A+cpp.lua-bridge%0ALanguage%3A+zh_CN%0AVerified+commit%3A+9773fd98a173b617e066ee68a85fdbed72e0bbba%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Native Lua bridge

## 契约范围

CCB 只支持 Lua-first Platform v1。Mod 通过 `require("ccb")` 获得包内 `ccb` 表；权威公开
声明是 `data/lua/types/ccb_platform_v1.d.lua`。已删除的 Lua API v5、manifest/capability
模型以及 `game.*` 兼容入口都不属于当前 bridge，也不得作为第二套运行时恢复。

Platform 是受信任的进程内扩展边界，不是进程级沙箱。loader 为每个 Mod 创建独立 Lua
state，并限制模块解析和公开 native surface；引擎继续拥有原生对象、registries 和生命周期。
Lua 侧只通过 Platform v1 声明的 value、snapshot 和代际检查 handle 访问这些对象。

## 公共入口与生命周期

`src/lua_platform_loader.cpp` 负责发现 `main.lua`/可选 `mod.lua`、创建 state、安装
`package.loaded["ccb"]`、解析 Mod 根目录内的模块，并管理候选 runtime 的准备、提交、回滚
与替换。`src/lua_platform_runtime.cpp` 及按领域拆分的 `src/lua_platform_*.cpp` 安装
`ccb.content`、`ccb.runtime`、`ccb.dialogue`、`ccb.services`、`ccb.state`、
`ccb.tasks` 和 `ccb.presentation` 的原生实现。

公共 symbol 必须同时存在于原生 registration、LuaLS 声明和生成 inventory，并由 Platform
contract/coverage tests 证明。说明性文档不能替代这些来源。

## 统一的 bundled Lua ABI

Make、桌面 CMake 和 Android 都编译仓库内同一组 `src/lua/*.c`，并统一使用 Lua 的标准 C
ABI：

| 构建入口 | ABI 约束 |
| --- | --- |
| `Makefile` | 把 bundled Lua 放入 `LUA_C_SOURCES`/`C_SOURCES`，用 `$(COMPILE.c) -x c` 编译。 |
| `src/lua/CMakeLists.txt` | 对 `LUA_SOURCES` 设置 `PROPERTIES LANGUAGE C`，再生成 `liblua`。 |
| `android/app/jni/CMakeLists.txt` | Android 工程启用 C 与 C++，并复用 `src/lua` 子目录，因此继承相同的 `LANGUAGE C` 契约。 |

`CATA_ENABLE_LUA_PLATFORM` 控制是否链接 Platform。启用时，桌面 CMake 通过
`configure_lua_platform()` 传播 `libsol`，Android 链接同一 `libsol`；Make 则把 Lua C
objects 与 Platform C++ objects 放入同一最终链接。关闭时必须走 disabled stub，而不能留下
部分 Lua runtime。

## C++ 与 sol2 linkage

Platform C++ 翻译单元对直接使用的 Lua headers 加 `extern "C"`；`src/lua/lua.hpp` 也提供
相同的 C-linkage wrapper。sol2 本身由 C++ 编译，所以 `src/sol/config.hpp` 定义
`SOL_BUILD_CXX_MODE=1`，但这不改变 Lua library 的 ABI。

不得定义 `SOL_USE_CXX_LUA`，也不得把 bundled `*.c` 改成 `LANGUAGE CXX`。这两种做法都会
让一侧期待 C++ linkage、另一侧导出 C symbols，从而在最终链接时产生 Lua API undefined
references。正确不变量是：Lua runtime 使用 C 编译；所有 C++/sol2 调用者按 C linkage 声明
Lua API。

## 扩展与变更清单

修改 bridge 时应按以下边界完成一个批次：

1. 在对应领域的 `lua_platform_*.cpp` 中实现并注册 native 操作；
2. 同步 `ccb_platform_v1.d.lua`、native inventory 和 Platform contract；
3. 保持 Make/CMake/Android 的 Lua source set 与 C ABI 一致；
4. 添加或更新聚焦 behavior、parity、coverage 和 disabled-build tests；
5. 只有在源码、声明、生成 inventory 和测试一致后才更新生成 reference。

## Contract 与 build gates

`Lua public contract` workflow 运行 LuaLS、native inventory、Platform contract、coverage、
CMake/ABI checker 和 `tools/lua_api` 单元测试。`check_cmake_contract.py` 明确拒绝
`LANGUAGE CXX` 和 `SOL_USE_CXX_LUA`，并检查 `libsol` 仍为可选且正确传播。

这些静态 gate 之外，PR 的正交 build matrix 还必须实际编译并链接启用 Platform 的 Make、
桌面 CMake 和 Android 配置。静态 checker 证明配置文本的不变量；真正的 build job 证明
编译器、链接器和目标平台能够消费该 ABI。任一类结果都不能由另一类结果替代。

本地最窄契约检查为：

```sh
# validation: lua-contract
python3 tools/lua_api/check_luals_declarations.py
python3 tools/lua_api/check_platform_native_inventory.py
python3 tools/lua_api/check_platform_contract.py
python3 tools/lua_api/check_platform_coverage.py
python3 tools/lua_api/check_cmake_contract.py
python3 -m unittest discover -s tools/lua_api -p 'test_*.py'
```

## PR artifacts 的边界

PR artifacts 是成功 build 的下载副本和结果导航，用于人工试用与诊断；它们不是 Lua API、
ABI、loader、生命周期或运行时行为契约。artifact 名称、压缩格式、保留期、PR comment 链接，
甚至可选上传是否成功，都不能作为 Platform 正确性的证明。契约证据来自上述源码、检查器与
build job；artifact 发布 workflow 只消费这些 job 的结果，不得反向定义运行时。
