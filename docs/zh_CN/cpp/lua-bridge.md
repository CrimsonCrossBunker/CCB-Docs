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
translation_source_fingerprint: ce7308d0ad0d4362f6d6cd609a97e4a741c4fc057f506378f1bc23c8c970f461
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/lua-bridge/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.lua-bridge%29%3A+&body=Document+ID%3A+cpp.lua-bridge%0ALanguage%3A+zh_CN%0AVerified+commit%3A+77631e8b0c782684b88e1cfc05dd4da64a7ec926%0A%0ADescribe+the+documentation+problem%3A%0A
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

此前核对的源码基线仍限制标准库与模块路径。下方 #755 草稿开始落实开放策略和发现阶段
告知；原生验收与合并尚未完成，不能把草稿实现描述为已发布。

## PR artifacts 的边界

PR artifacts 是成功 build 的下载副本和结果导航，用于人工试用与诊断；它们不是 Lua API、
ABI、loader、生命周期或运行时行为契约。artifact 名称、压缩格式、保留期、PR comment 链接，
甚至可选上传是否成功，都不能作为 Platform 正确性的证明。契约证据来自上述源码、检查器与
build job；artifact 发布 workflow 只消费这些 job 的结果，不得反向定义运行时。

## 待合并：50 项语义验收与持续药剂示例

本节对应源码分支 `codex/lua-semantic-acceptance`，随配套源码 PR 合并后生效。
本批只为选定的 50 个 EOC selector 建立有界验收证据，不代表全部 586 项替代完成。
其中 8 个突变写操作与旧行为不同，迁移器保留 `semantic_choice`，要求作者选择
新的玩法语义；不会静默声称兼容。

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

## 草稿：可信加载、诊断与作者工具

本节对应源码草稿 [#755](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/755)、
[#756](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/756)、
[#757](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/757)、
[#758](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/758)、
[#759](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/759) 和
[#760](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/760)。
尚未编译或进行原生验收；本页的 `verified_commit` 保留此前已核对的源码基线，
不能用它证明下列草稿能力已发布。配套源码合并并验收后，才可更新本页证据并发布。

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
它复用已有替换后端；活动 Lua 尚未返回时拒绝重入，静态定义改变时要求重启游戏。
准备失败时保留原注册表，错误会在界面显示。成功只表示脚本注册表已替换，应继续检查
消息日志中的回调错误。菜单集成和重入回归测试源码尚未进行原生验收。

缺失 handler 或 payload 迁移失败会按已有规则丢弃对应持久任务。#755 在消息日志中汇总
每个 Mod 的丢弃数量，具体任务和原因仍在 `debug.log`；应在任务处理前提供迁移。
存档加载失败也会标出作用域、Mod、任务序号与任务 ID，便于用下方工具定位。
#759 修复了保存的角色循环到期回合从浮点数转整数时的范围检查，阻止 `2^63` 越界转换；
这项实现及边界回归测试同样尚未编译运行。

### 读取存档和对比目标 SDK

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

### 运行时文本翻译

#758 草稿提供 `ccb.services.translate(text, context?)` 和
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

在 Mod 根目录运行提取工具，明确列出文件：

```sh
python3 /path/CCB/tools/lua_api/extract_translations.py main.lua --output messages.pot
python3 /path/CCB/tools/lua_api/extract_translations.py main.lua --output messages.pot --check
```

工具调用 GNU `xgettext`，不执行 Lua。保持完整 `ccb.services` 调用名与字面量文本／上下文；
别名、动态字符串或变量上下文不能可靠提取。翻译调用直接嵌在 `string.format` 中时可继承
格式检查标记。`--check` 只比较文件，不写入；退出码 1 表示模板缺失或过期，2 表示提取失败。

外部 Mod 放在游戏用户 Mod 目录时，现有扫描器识别
`MyMod/lang/mo/<language>/LC_MESSAGES/MyMod.mo`。翻译目录编译与安装属于后续发布步骤。
内置 Mod 不会自动通过用户目录扫描加载翻译；共享目录中的常见词应使用独特上下文。
本批不实现静态内容名／元数据的延迟翻译或目录热重载。真实翻译、复数规则、语言切换与
不启用本地化的构建均待原生验收；不能据此宣称完整国际化已完成。
