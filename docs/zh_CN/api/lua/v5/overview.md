---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.overview
title: CCB Lua 0.1 总览
language: zh_CN
status: active
doc_type: explanation
audiences:
- mod-author
- api-user
- experienced-contributor
- maintainer
owners:
- CCB Lua API maintainers
reviewers:
- Documentation reviewers
- Lua API reviewers
review_interval_days: 60
last_human_reviewer: LYHGLYTX
source_paths:
- data/lua/README.md
- data/lua/manifest.schema.json
- data/lua/types/ccb_api_v5.d.lua
- data/lua/reference/ccb_public_api_v5.json
- data/lua/reference/ccb_public_api_v5_coverage.json
- tools/lua_api/README.md
source_symbols:
- Lua Mod API v5
source_queries: []
source_fingerprint: 30a19e6cbd8c6709ac5ccda80fe349e9459ddaccd8d3dc96507ee282c17f48cb
authority: api-contract
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 53ce833aa62cf93c564abc1717e1ef2ea7a482029228ab30c1a0f5226f4a0783
prerequisites:
- architecture.overview
depends_on: []
redirect_from: []
supersedes:
- lua.v5.overview
license: CC-BY-SA-3.0
attribution: CCB contributors; generated contract and source paths at the verified commit.
example_validation_ids: []
api_version: '5'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: data/lua/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/README.md
- path: data/lua/manifest.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/manifest.schema.json
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/types/ccb_api_v5.d.lua
- path: data/lua/reference/ccb_public_api_v5.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/reference/ccb_public_api_v5.json
- path: data/lua/reference/ccb_public_api_v5_coverage.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/reference/ccb_public_api_v5_coverage.json
- path: tools/lua_api/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/lua_api/README.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.v5.overview%29%3A+&body=Document+ID%3A+api.lua.v5.overview%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# CCB Lua 0.1 原生平台总览

**CCB Lua 0.1** 是 Cataclysm: Cleanwater Bomb 自研的第一版**纯 Lua 原生游戏内容与 Mod 创作引擎**。

它为模组作者与核心内容开发者提供了一套自成一体、强类型、具备事务安全保障的纯 Lua 创作面，涵盖物品、配方、怪物、伤势、武术、地图生成、事件监听、同步拦截、回合调度、跨平台 UI 及持久化状态存储。

---

## 核心四大支柱

1. **纯 Lua 原生内容创作 (Native Content)**
   - 告别繁杂的外部数据配置，所有游戏实体（物品 `Item`、配方 `Recipe`、怪物 `Monster`、伤势 `Wound`、武术 `MartialArt`、地图生成 `Mapgen` 等）直接使用纯 Lua 代码定义。
   - 拥有完整的模块化、条件分支、循环与函数复用能力。

2. **零配置极简 Mod 开发 (Zero-Configuration Discovery)**
   - Mod 目录下**只需要一个 `main.lua`** 即可被引擎直接识别并加载。
   - 目录名即 Mod ID，无需编写任何额外的元数据清单或配置文件。

3. **原生事务性提交与安全回滚 (Transactional & Generation Safety)**
   - 数据在游戏全局 Finalize 之前进行 Staged 预处理，若模组逻辑出错或冲突立即执行**原子回滚（Rollback）**，保护游戏全局数据不受污染。
   - 严禁在 Lua 中传递 C++ 裸指针，全面采用**代际安全句柄（Generation-Safe Handles）**与只读数据快照。

4. **IDE 类型提示与开发者体验 (Types & Tooling)**
   - 配备全量 LuaLS 类型注解文件，在 VS Code / Neovim 中提供 100% 自动补全、参数提示与静态语法检查。

---

## 运行时 API 架构

CCB Lua 0.1 原生导出 500+ 个核心函数与对象方法，覆盖全部游戏系统：
- **角色与异能**：生化插件、特质突变、武术流派、技能与熟练度。
- **物品与制造**：物品属性、背包容量、合成配方、分解与练习。
- **世界与环境**：天气系统、日历时间、地形家具、地图生成、大地图。
- **实体与生物**：怪物行为、NPC 对话树、阵营交互、伤势系统。
- **UI 与交互**：PC 键盘操作 / Android 触屏原生自适应渲染引擎。

---

## 从哪里开始

- **新手入门**：先阅读[完整示例 Mod](example-mod.md)与[生命周期](lifecycle.md)。
- **页面与交互**：查阅[跨平台 Lua UI](ui.md)。
- **游戏逻辑扩展**：查阅[事件、Hook 与 Callback](events.md)。
- **调试与测试**：查阅[调试与验证](debugging.md)。

---

## 原生参考手册

- [模块入口](reference/modules.md)、[命名空间](reference/namespaces.md)
- [类与记录](reference/classes.md)、[属性](reference/properties.md)
- [函数](reference/functions.md)、[方法](reference/methods.md)、[运算符](reference/operators.md)
- [枚举族](reference/enums.md)、[原生事件](reference/events.md)、[Hook](reference/hooks.md)、[Callback](reference/callbacks.md)
- [Capability 模型](reference/capabilities.md)、[权限模型](reference/permissions.md)

