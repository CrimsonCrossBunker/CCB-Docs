---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.lua-bridge
title: Native Lua bridge
language: zh_CN
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
source_fingerprint: ab97dd6144210a147deafd08d944911b8d7c4d66586b47739d2463a56777f0d4
authority: api-contract
verified_commit: 316f1d39c390e96cfe14848d259c774087963818
verified_at: '2026-09-10'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 73b4006b2397aa1683554dcd1f79c835eaa235d5e8357db712c45c4e4aa54875
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/782
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/lua-bridge/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/lua-bridge/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/lua-bridge/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/lua-bridge/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/316f1d39c390e96cfe14848d259c774087963818
source_urls:
- path: .github/workflows/lua-contract.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/.github/workflows/lua-contract.yml
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/.github/workflows/matrix.yml
- path: ai/test-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/ai/test-matrix.yml
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/Makefile
- path: android/app/build.gradle
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/android/app/build.gradle
- path: android/app/jni/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/android/app/jni/CMakeLists.txt
- path: build-scripts/gha_compile_only.sh
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/build-scripts/gha_compile_only.sh
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/data/lua/LUA_FIRST_PLATFORM.md
- path: data/lua/types/ccb_platform_v1.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/data/lua/types/ccb_platform_v1.d.lua
- path: src/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/CMakeLists.txt
- path: src/lua/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/lua/CMakeLists.txt
- path: src/lua/lua.hpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/lua/lua.hpp
- path: src/lua_platform_loader.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/lua_platform_loader.h
- path: src/lua_platform_loader.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/lua_platform_loader.cpp
- path: src/lua_platform_runtime.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/lua_platform_runtime.h
- path: src/lua_platform_runtime.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/lua_platform_runtime.cpp
- path: src/sol/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/sol/CMakeLists.txt
- path: src/sol/config.hpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/sol/config.hpp
- path: tools/lua_api/check_cmake_contract.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/tools/lua_api/check_cmake_contract.py
- path: tools/lua_api/generate_platform_native_inventory.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/tools/lua_api/generate_platform_native_inventory.py
- path: tools/lua_api/test_check_cmake_contract.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/tools/lua_api/test_check_cmake_contract.py
- path: tests/lua_platform_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/tests/lua_platform_test.cpp
- path: tools/create_lua_mod.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/tools/create_lua_mod.py
- path: tools/lua_api/mod_sdk.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/tools/lua_api/mod_sdk.py
- path: data/lua/LUA_FIRST_EOC_WORKFLOW.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/data/lua/LUA_FIRST_EOC_WORKFLOW.md
- path: src/lua_platform_runtime_services.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/lua_platform_runtime_services.cpp
- path: src/lua_platform_runtime_lifecycle.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/lua_platform_runtime_lifecycle.cpp
- path: src/lua_platform_runtime_hooks.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/lua_platform_runtime_hooks.cpp
- path: src/lua_platform_state.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/lua_platform_state.cpp
- path: src/lua_platform_content_items.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/lua_platform_content_items.cpp
- path: src/lua_platform_content_character.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/lua_platform_content_character.cpp
- path: src/debug_console.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/debug_console.cpp
- path: src/mod_manager.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/mod_manager.cpp
- path: tools/lua_api/inspect_state.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/tools/lua_api/inspect_state.py
- path: tools/lua_api/extract_translations.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/tools/lua_api/extract_translations.py
- path: tests/lua_platform_callback_diagnostic_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/tests/lua_platform_callback_diagnostic_test.cpp
- path: tests/lua_platform_content_translation_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/tests/lua_platform_content_translation_test.cpp
- path: tests/lua_platform_test_05_tasks.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/tests/lua_platform_test_05_tasks.cpp
- path: tests/mod_manager_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/tests/mod_manager_test.cpp
- path: tests/lua_platform_test_02_loader.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/tests/lua_platform_test_02_loader.cpp
- path: tools/lua_api/fixtures/native_probe/ccb_native_probe.c
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/tools/lua_api/fixtures/native_probe/ccb_native_probe.c
- path: tests/lua_platform_tonic_lifecycle_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/tests/lua_platform_tonic_lifecycle_test.cpp
- path: src/mod_id_compat.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/mod_id_compat.h
- path: src/lua_platform_bindings_values.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/lua_platform_bindings_values.cpp
- path: src/lua_platform_variables.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/lua_platform_variables.cpp
- path: src/lua_platform_effects.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/lua_platform_effects.cpp
- path: tests/lua_platform_effects_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/tests/lua_platform_effects_test.cpp
- path: tools/lua_api/test_mod_sdk.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/tools/lua_api/test_mod_sdk.py
- path: tools/migrate_lua_first.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/tools/migrate_lua_first.py
- path: src/lua_platform_creatures.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/lua_platform_creatures.cpp
- path: src/game.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/316f1d39c390e96cfe14848d259c774087963818/src/game.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.lua-bridge%29%3A+&body=Document+ID%3A+cpp.lua-bridge%0ALanguage%3A+zh_CN%0AVerified+commit%3A+316f1d39c390e96cfe14848d259c774087963818%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Native Lua bridge

## 契约范围

CCB 只支持 Lua-first Platform v1。Mod 通过 `require("ccb")` 获得包内 `ccb` 表；权威公开
声明是 `data/lua/types/ccb_platform_v1.d.lua`。已删除的 Lua API v5、manifest/capability
模型以及 `game.*` 兼容入口都不属于当前 bridge，也不得作为第二套运行时恢复。

Platform 是受信任的进程内扩展边界，不是进程级沙箱。loader 为每个 Mod 创建独立 Lua
state，维护所属 Mod 的 `ccb` 入口；引擎继续拥有原生对象、registries 和生命周期。
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

按完整领域批次实现并集中验收，输入不变时复用已通过证据。工具、文档和模板改动不要求
默认重编译游戏；原生或构建配置改动再选择对应编译与运行验证。全量 JSON/EOC 审计用于
内容迁移、等价性声明或删除 EOC。单个检查器用于失败诊断，本地统一契约入口为：

```sh
# validation: lua-contract
python3 -m unittest discover -s tools/lua_api -p 'test_*.py'
```

## Mod 编辑器与升级检查

新建 Mod 时，脚手架默认附带可选的 `.luarc.json` 和 `.ccb-sdk/`：

```sh
python3 tools/create_lua_mod.py /path/MyMod --template complete
```

在启用 LuaLS 的编辑器中打开该目录即可使用补全与参数诊断。SDK 保存所选 CCB 声明的原样
副本、Platform 主版本和 SHA-256；可以用 `--declarations /path/game/data/lua/types/ccb_platform_v1.d.lua`
选择目标游戏包里的声明。配置使用相对路径，移动项目后仍可使用。快照不会自动更新，也不能
证明当前运行的可执行文件或存档兼容。`--no-editor` 可省略编辑器文件，运行时仍只用游戏提供的
`require("ccb")`；模板在注册内容前检查 Platform 主版本。

安装 LuaLS 后，可以直接检查 Mod，或比较两个项目的 SDK：

```sh
python3 tools/lua_api/mod_sdk.py check /path/MyMod
python3 tools/lua_api/mod_sdk.py compare /path/OldMod /path/NewVersionScaffold
```

`check` 可用 `--language-server /absolute/path/to/lua-language-server` 指定现有服务器。
结果包含绝对文件路径、行列、错误代码及参数类型说明；退出码 0 表示没有静态诊断，1 表示有
诊断，2 表示配置或检查器失败。检查器崩溃或未输出报告不能被当作通过。`compare` 只报告声明
的新增、删除和签名变化，不修改项目，也不保证行为或存档兼容。

现有声明仍有类型注解缺口。静态检查不审计 SDK 声明库，不执行 Mod、不验证原生内容 ID，
也不取代游戏加载和行为验证。普通运行错误仍使用 `debug.log` 中已有的 Mod/handler 上下文；
这一批没有实现游戏内调试器、状态/任务检查器或原生兼容版本协商。

CI 固定 LuaLS 3.19.1 下载包及 SHA-256，实际检查两种模板，并验证未知 API、错误参数和缺失
参数能产生诊断。本地可设置 `CCB_LUALS`，在同一个契约套件里启用这些集成测试：

```sh
CCB_LUALS=/path/lua-language-server python3 -m unittest discover -s tools/lua_api -p 'test_*.py'
python3 tools/test_create_lua_mod.py
```

## 已采纳的信任策略与实施边界

已采纳的目标是所有来源的 Mod 均由玩家自行决定信任，并承担对系统的风险：开放完整标准库，
以及平台支持的外部 Lua 模块和原生动态库。每个 Mod 的独立 state 用于名称和 owner 管理，
不能隔离进程崩溃。默认不施加全局指令/内存配额；`ccb` 的参数、句柄、生命周期和持久数据
校验继续保留。原生模块作者负责系统、架构、Lua ABI 与依赖适配。

加载器已实现下述开放策略和发现阶段告知。整合的编译、运行结果与验证配置记录在
[源码 PR #768](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/768)；
游戏界面人工验收与各平台原生模块打包仍需要各自证据。

## PR artifacts 的边界

PR artifacts 是成功 build 的下载副本和结果导航，用于人工试用与诊断；它们不是 Lua API、
ABI、loader、生命周期或运行时行为契约。artifact 名称、压缩格式、保留期、PR comment 链接，
甚至可选上传是否成功，都不能作为 Platform 正确性的证明。契约证据来自上述源码、检查器与
build job；artifact 发布 workflow 只消费这些 job 的结果，不得反向定义运行时。

## 有界语义验收与持续药剂示例

相关源码已通过 [#751](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/751)
和 [#752](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/752) 合并。
覆盖范围以源仓库的语义账本和测试为准，不代表全部 EOC 已完成替代。

- `services.skills.offered(teacher, student)` 返回 `CcbResult`，其 `value` 包含
  `items`（最多 256 个技能 ID）、`total`、`returned` 和 `truncated`。
  教学依据学生的理论知识等级。双方必须是有效角色句柄。
- 技能教学和可见突变查询必须有明确的双方角色；无法证明另一方时保留迁移提示，
  不猜测为玩家，也不把教学条件直接替换为 `false`。
- 效果添加保留零时长和有符号强度的原生含义；负强度不是增量操作。
  士气区间迁移按原生上下界含义生成随机整数，支持反向书写的上下界。
- `Lua_First_Example` 的药剂消耗一枚净化电池，通过原生效果事件启动三次耐力脉冲，
  并保存冷却与剩余任务。原生测试验证角色文件及新 Lua 运行时的状态恢复和任务不重复。

验收测试位于源码仓库的 `tests/lua_platform_*_semantics_test.cpp`、
`tests/lua_platform_mutations_test.cpp`、`tests/lua_platform_effects_test.cpp` 和
`tests/lua_platform_tonic_lifecycle_test.cpp`。这是原生集成证据；静态引擎定义在测试中
保留缓存，不声称已完成手工 UI 验收或完整进程重启验收。

## 可信加载、诊断与作者工具

本节对应源码变更 [#755](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/755)、
[#756](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/756)、
[#757](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/757)、
[#758](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/758)、
[#759](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/759)、
[#760](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/760)、
[#761](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/761)、
[#762](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/762)、
[#763](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/763)、
[#764](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/764)、
[#765](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/765)、
[#766](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/766) 和
[#767](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/767)。
上述变更统一整合到 [#768](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/768)。
本页 `verified_commit` 固定对应的源码版本；编译配置、原生回归和共享库加载的实际结果
统一查阅该 PR 的验收记录。测试源码存在本身不代表通过。

### 加载与失败诊断

#755 的实现开放完整标准库与普通 `package` 搜索器。Mod 本地搜索器优先，其他模块保留
Lua 5.4 的缓存、预加载与 loader-data 返回语义。原生路径优先搜索 Mod 根目录的
`?.so`（Windows 为 `?.dll`），并保留原始路径；目录含 `;` 或 `?` 时改用明确的
`package.loadlib` 路径，避免 cpath 语法歧义。`require("ccb")` 始终返回该 Mod 的
Platform 表。加载原生模块要求匹配宿主的系统、架构与 Lua C ABI，不能链接另一个 Lua
运行时。配置修改不等于真实 DLL/SO 已经加载成功；Windows 打包和各平台原生库验收仍待完成。

发现 Mod 时会先告知代码执行风险，再读取可能执行 Lua 的 `mod.lua`；首次提示不依赖尚未
初始化的按键绑定，非交互检查通过标准错误输出告知。元数据模块转发应写
`return (require("metadata"))`，括号确保只返回一个 `ccb.ModDefinition`，避免 Lua 5.4
首次 `require` 的第二个返回值被误当成多份元数据。

加载错误保留 Mod、阶段、文件与 Lua 原始错误。回调错误增加事件／钩子名称；任务错误增加
任务 ID、作用域和到期回合，便于定位同一 handler 的不同调用实例。Platform 回滚不保证撤销
可信 Lua 代码对用户文件、系统或外部服务造成的副作用。

### 游戏内脚本重载

#760 提供“调试菜单 → 游戏 → 重新加载 Lua Mod 脚本”，也可通过调试动作搜索找到。
它复用已有替换后端；活动 Lua 尚未返回或另一轮替换仍在进行时拒绝重入，静态定义改变时要求重启游戏。
准备失败时保留原注册表，错误会在界面显示。成功只表示脚本注册表已替换，应继续检查
消息日志中的回调错误。菜单人工操作验收独立于后端重入回归。

缺失 handler 或 payload 迁移失败会按已有规则丢弃对应持久任务。#755 在消息日志中汇总
每个 Mod 的丢弃数量，具体任务和原因仍在 `debug.log`；应在任务处理前提供迁移。
存档加载失败也会标出作用域、Mod、任务序号与任务 ID，便于用下方工具定位。
#759 修复了保存的角色循环到期回合从浮点数转整数时的范围检查，阻止 `2^63` 越界转换；

#762 让物品指纹区分省略字段和显式默认值。例如继承物品省略 `mass_grams` 会保留来源重量，
写入 `mass_grams = 0` 则覆盖重量；现在两者不会被指纹误判为同一种静态定义。

### Lua 控制台

#761 基于 #760，提供“调试菜单 → 控制台 → Lua”页。选择一个已加载 Mod，输入普通 Lua
代码并点击“Run Lua”；继续通过 `require("ccb")` 获取 Platform，用 `return` 显示结果：

```lua
local ccb = require("ccb")
return ccb.services.turn()
```

代码使用所选 Mod 的现有状态，在绘制帧结束后显式执行，不自动重跑。调用具有该 Mod 的
回调上下文；world-ready、句柄和领域检查继续有效。全局变量、世界状态及外部副作用
不会因为后续代码报错而回滚。控制台拒绝同一状态递归执行以及重载过程中的执行。
返回展示最多 16 项，每个字符串最多读取 1024 字节；控制字节会转义，无效 UTF-8 会替换，
返回表最多展示 20 个原始字段，顺序不作保证；嵌套表和其他对象仅显示类型。
不调用 `__pairs` 或 `__tostring`；要继续查看，显式返回嵌套字段即可。这些是显示限制，不是脚本配额。
这不是断点调试器；界面人工操作验收仍需单独完成。

### 读取存档和对比目标 SDK

#757 还提供给现有 Mod 添加编辑器声明的入口：

```sh
python3 tools/lua_api/mod_sdk.py init /path/MyMod --declarations /path/game/data/lua/types/ccb_platform_v1.d.lua
```

目录必须已经存在；工具添加 `.ccb-sdk/` 和 `.luarc.json`，不改写作者的 Lua 文件。
已有这两个路径中的任意一个时会拒绝覆盖，包括符号链接；请保留或自行整合原有编辑器配置。
省略 `--declarations` 时使用当前源码树的声明，而非自动查找已安装游戏。

```sh
python3 tools/lua_api/inspect_state.py /path/world/lua_platform_world.json --mod MyMod
python3 tools/lua_api/inspect_state.py /path/world/lua_platform_world.json --mod MyMod --task 225
python3 tools/lua_api/mod_sdk.py compare-release /path/MyMod --declarations /path/game/data/lua/types/ccb_platform_v1.d.lua
```

#756 的检查器只读取指定存档文件，汇总状态键、任务、参与者、到期回合和保存的定位提示。
`--values` 才显示状态与 payload 值；`--limit` 限制每个列表的展示数量，同时保留总数。
`--mod ID --task N` 可直接查询日志中的任务 ID，包括列表显示上限之后的记录；总数和
匹配数分开报告。它不执行 Lua、不载入世界、不修改存档，也不能判断 handler 是否存在
或对象是否仍存活。
#757 可直接对比目标游戏附带的声明文件，不需要先创建第二个 Mod 项目；比较不会更新 SDK，
也不能证明原生行为或存档兼容。

### 运行时状态检查与存档边界

#763 提供 `ccb.state.world.keys(after_key?, limit?)` 及角色作用域版本，
在 `world_ready` 后返回所属 Mod 的状态键副本，不包含值。默认每页 20 项，范围 1–200；
按字节字典序排列，游标为排他的字符串键，无须仍存在于状态中。结果包含
`items`、`total`、`matched`、`returned`、`limit`、`truncated`，仅在还有下一页时提供
`next_after`。键可包含 NUL；保留游标原值传回，不要按显示文本重建。
每次调用都是新快照，分页期间键发生变化时应重新开始。修改返回表不会修改状态。

#764 保留原有 1 MiB 状态编码及 16 MiB 运行时作用域文件限制，在临时 JSON
编码过程中即拒绝超限，不再先构造完整超大输出。超限不会开始写入目标；这不承诺
多个作用域文件之间的事务，也不是 Lua 进程的总内存限制。

#765 修复 `tasks.get`、`tasks.next`、`tasks.list` 的返回值构造：在分配 Lua 表前
复制选中的任务记录，避免垃圾回收中的任务取消使借用记录失效。列表仍遵循原有排序和
数量限制；查询结果是独立快照。回归测试覆盖分配边界上的取消操作。

#764 同时让 Lua 存档临时流使用 double 往返精度，避免通用 JSON 固定 6 位小数
把很小的状态值写成零。只调整 Lua 存档写入，不改变其他 JSON 写入器；此前已损失的
数值精度无法恢复。#765 也把已有任务迁移保护延伸到参数构造和返回值解码，成功或失败
均恢复此前标记，不对无关回调副作用承诺回滚。

#766 在两个作用域的 Mod 记录中保存可选 `last_task_id`，空任务列表也保留已分配计数，
加载时合并最大值，耗尽状态和暂未加载 Mod 的计数不会在重进时重置。旧 v1 文件缺少该字段
时仍按尚存任务推导，无法追溯已完成的旧任务。#756 报告 `last_task_id` 和
`task_counter_persisted`，区分保存的计数与旧记录的推导结果。

#767 让同轮到期、尚未开始派发的任务继续可查可取消。前一个回调可以取消后一个任务；
到期回合／ID 排序不变，回调新建的任务仍留到下一次处理。

### 运行时与静态内容文本翻译

#758 提供 `ccb.services.translate(text, context?)` 和
`ccb.services.translate_plural(singular, plural, count, context?)`，在 `world_ready` 后
复用游戏当前语言的翻译目录。返回普通字符串；缺少翻译时退回源文本，数量为 1 选单数，
其他非负数量选复数。文本与上下文不接受 NUL，数量必须能由原生 `size_t` 表示。

```lua
local ccb = require("ccb")
ccb.runtime.handler("ready_text", function()
    ccb.services.message(string.format(ccb.services.translate_plural(
        "%d item is ready", "%d items are ready", 2, "MyMod status"), 2))
end)
ccb.runtime.on("world_ready", "ready_text")
```

物品名称与说明可使用静态文本值，供原生层在显示时翻译：

```lua
local ccb = require("ccb")
ccb.content.add(ccb.content.Item {
    id = "MyMod_water_bottle", mass_grams = 500, volume_ml = 500,
    name = ccb.content.plural_text("bottle of water", "bottles of water", "MyMod item"),
    description = ccb.content.text("A sealed bottle.", "MyMod description")
})
```

这些不可变 `LocalizedText` 值保留源文本，不提前绑定当前语言。普通字符串继续不翻译，
说明不接受复数值；`text` 用于名称时以相同源文本作为复数回退，不同复数使用 `plural_text`。
源文本不能为空，输入不接受 NUL。继承保留省略的翻译字段，显式普通字符串替换它；
翻译状态、上下文和复数改变都属于静态定义变化。Skill 名称、说明、SkillDisplay 分类名称及理论／实践等级说明也接收单数
`content.text`，并拒绝复数标记。普通字符串保持字面值；省略实践说明仍不改动独立的
实践映射，参数无效时不会只改写理论一侧。技能静态指纹区分文本上下文及理论／实践列表。

在 Mod 根目录运行提取工具，明确列出文件：

```sh
python3 /path/CCB/tools/lua_api/extract_translations.py main.lua --output messages.pot
python3 /path/CCB/tools/lua_api/extract_translations.py main.lua --output messages.pot --check
```

工具调用 GNU `xgettext`，不执行 Lua。保持完整的运行时翻译或 `ccb.content.text`／
`ccb.content.plural_text` 调用名与字面量文本／上下文；
别名、动态字符串或变量上下文不能可靠提取。翻译调用直接嵌在 `string.format` 中时可继承
格式检查标记。`--check` 只比较文件，不写入；退出码 1 表示模板缺失或过期，2 表示提取失败。

外部 Mod 放在游戏用户 Mod 目录时，现有扫描器识别
`MyMod/lang/mo/<language>/LC_MESSAGES/MyMod.mo`。翻译目录编译与安装属于后续发布步骤。
内置 Mod 不会自动通过用户目录扫描加载翻译；共享目录中的常见词应使用独特上下文。
除 Item／Skill／SkillDisplay 外的内容 builder、Mod 元数据翻译和目录热重载仍未实现。
真实翻译目录、复数规则与语言切换仍待专门验收；本次编译配置见 #768，不能据此宣称完整国际化已完成。

## 核心包 ID 兼容

核心包的规范 ID 改为 `ccb`。新 JSON 元数据使用 `"dependencies": [ "ccb" ]`，
Lua `ModDefinition` 使用 `dependencies = { "ccb" }`。旧 Mod 的 `dda` 依赖仍被接受；
JSON 冲突列表和用户默认 Mod 列表也解析旧 ID。它是同一核心包的别名，不注册第二个核心。

旧世界中的 `dda` 在读取时解析为 `ccb`；同时出现两者时按原顺序去重，核心只加载一次。
之后保存 Mod 列表使用规范 ID。旧来源记录、`mod_interactions/dda/` 和
`services.gameplay.mods.is_loaded("dda")`、`load_order("dda")` 继续识别该核心。
包的显示名称与 `data/mods/dda/` 目录保持原样；此变更不重命名用户存档目录。

兼容方向是旧 CCB 世界和旧 Mod 加载到新版本；不保证更新后保存的世界能退回旧版。
别名去重测试的 12 个断言已通过；真实 Mod 发现测试已编译，尚未执行。旧世界读档和 Android 设备验证尚未完成。

## 效果快照与变量查询

`ccb.services.effects.get(character, effect_id, body_part?)` 返回独立的效果快照，包含强度、持续时间、开始时间、部位以及关联效果等信息。指定效果不存在时返回 `not_found`；失效句柄等其他错误仍需处理。省略部位使用原生的未限定查询。

需要动态强度阈值时，先读取效果，确认存在后再计算阈值并比较 `snapshot.intensity`。这样保留惰性求值，也能用普通 Lua 比较超出 `effects.has` 可选强度参数范围的阈值。多项查询应保持命中即结束；长列表可使用顺序分支或循环。

`ccb.services.types.id(kind, value)` 构造 `GameId`；`id_kinds()` 列出支持的种类，`GameId:is_valid()` 检查定义是否存在。这些方法和效果快照现有的原生行为已补入 LuaLS 声明。

`ccb.services.variables.get(actor, key)` 读取明确对象的变量，`get_global(key)` 读取全局变量。读取结果的 `value` 含 `exists` 和实际变量 `value`。变量键包含 1–128 字节，不接受 ASCII 控制字符或 NUL；写入仍受回调和写阶段要求约束。

`variables.resolve(context, actor, scope, key)` 的 `u`、`npc` 作用域使用传入的同一个 `actor`，不会替调用者选择对话中的某一方。`var` 间接引用也保留该对象。调用者应明确选择变量主人；迁移器在引用指向另一方时先解析最终作用域，再传入对应句柄。直接面向角色编写玩法时，可使用 `get`、`set`、`remove` 明确表达归属。

本轮验证包含实际 LuaLS 检查、迁移器执行测试和效果原生对照。它关闭了上述范围的缺口；全部 EOC 选择器的语义验收仍按领域继续。

### 按身体结构权重抽取部位

`ccb.services.characters.random_body_part(character, main_parts_only?)` 返回 `CcbBodyPartIdResult`。成功时 `value` 是选中的 `GameId<body_part>`；角色句柄失效时返回错误。它按该角色原生身体结构的权重抽取，不是对部位列表进行均匀抽样。第二个参数默认为 `false`；传入 `true` 时，将抽中的部位映射到其主要部位。

`ccb.services.characters.avatar()` 返回游戏中实际玩家的 `GameHandle`，与对话双方的身份无关。迁移旧效果添加或移除的 `target_part: "RANDOM"` 时，需通过这个接口取得玩家并保留旧规则：从玩家身体结构抽取，即使效果操作作用于 NPC；每个待移除的效果单独抽取。新 Lua 玩法可自行指定传给该接口的角色。此处不代表动态部位变量、所有效果写入以及全部 EOC 语义均已验收。

### 完整部位列表与逐部位移除

`ccb.services.characters.body_parts(character)` 返回 `CcbBodyPartsResult`。成功时 `value` 是按原生顺序排列的完整 `GameId<body_part>` 数组，不排序、不截断，也不加入表示未限定部位的 `bp_null`。列表是独立快照，失效的角色句柄返回错误。

旧 EOC 的 `target_part: "ALL"` 会先取完整部位列表，对每个效果逐部位移除，最后再执行未限定部位的移除。迁移输出保留这个顺序，以保持移除事件的部位、次数和顺序；直接调用一次 `effects.remove(character, effect_id)` 虽然也能清除该效果，却可能产生不同的事件序列。普通非角色 Creature 对应的旧 talker 没有部位列表，其 `ALL` 仍对应一次未限定移除。

### 部位定义与当前身体结构

效果接口要求部位 ID 已注册，但不要求该部位仍在目标当前的身体结构中。这与原生引擎按部位 ID 保存、查询和移除效果的行为一致；例如，已定义的尾部不在角色当前身体结构中时，查询不存在的效果会返回 `false`（`effects.get` 返回 `not_found`），而不是因为缺少该部位报参数错误。原生添加、查询和移除仍按该 ID 执行。

部位 ID 的种类与定义检查、角色／Creature 句柄的有效性检查继续生效。`characters.body_parts` 列出的是当前实际拥有的部位，不会因为效果关联了其他已定义部位而扩大这个列表。

### 迁移效果部位和输入形状

迁移器在部位变量求值后处理 `bp_null`、`RANDOM`，以及移除专用的 `ALL`。
批量移除保留原生的变量重读和逐部位调用顺序。事件目标未证明是角色时，
会先确认实际生物类型；怪物的 `ALL` 按原生行为执行无部位移除。
这些标记属于旧内容迁移规则，手写 Lua 继续使用类型化部位接口。

`u_lose_effect` / `npc_lose_effect` 的原生值形状是字符串或数组。
变量对象必须放在数组中；单独的对象不会被自动转换为移除操作，而会保留
人工重写提示，避免激活原生忽略的动作。这些修复不代表整个效果领域已完成语义验收。
