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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/743
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/lua-bridge/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.lua-bridge%29%3A+&body=Document+ID%3A+cpp.lua-bridge%0ALanguage%3A+zh_CN%0AVerified+commit%3A+71bfdf23ba26594efbc57797fb6bfb6cf497af82%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
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

这是目标契约，尚未随本次工具改动实现。当前 loader 仍限制标准库和模块路径；首次执行下载
Mod（含 `mod.lua` 发现阶段）前的风险告知也仍待集成。不能把契约采纳描述为权限已经开放。

## PR artifacts 的边界

PR artifacts 是成功 build 的下载副本和结果导航，用于人工试用与诊断；它们不是 Lua API、
ABI、loader、生命周期或运行时行为契约。artifact 名称、压缩格式、保留期、PR comment 链接，
甚至可选上传是否成功，都不能作为 Platform 正确性的证明。契约证据来自上述源码、检查器与
build job；artifact 发布 workflow 只消费这些 job 的结果，不得反向定义运行时。
