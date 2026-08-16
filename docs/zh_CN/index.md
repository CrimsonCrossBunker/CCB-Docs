---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: home
title: CCB 开发文档
language: zh_CN
status: active
doc_type: explanation
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
- AGENTS.md
- GOVERNANCE.md
source_symbols: []
source_queries:
- Sources of truth
- Authority model
source_fingerprint: d304d44d4803e198dce1a691465b13f1b04d5812ae3d5a8cb1aaa54ea5193c7b
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-01'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 065b04168dbb4fd6e3ff34aa2498611e85123e94f36693b630a4b8393fa9e89f
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: project-context
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/AGENTS.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/GOVERNANCE.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28home%29%3A+&body=Document+ID%3A+home%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# CCB 开发者文档

这里是 Cataclysm: Cleanwater Bomb 的官方开发者指南、API 参考与架构导航站。

本站面向两大核心开发者群体：**Mod 创作者** 与 **本体/引擎 C++ 开发者**。

---

## 快速导航与开发入口

### 🎯 1. Mod 创作者专区（CCB Lua 0.1 原生平台）
CCB 提供全新自研的 **CCB Lua 0.1** 纯原生内容与逻辑创作引擎，告别繁琐的旧数据格式：
- [CCB Lua 0.1 原生平台总览](api/lua/v5/overview.md)：理解零配置 Mod 发现、原生事务提交与代际安全句柄。
- [完整示例 Mod 剖析](api/lua/v5/example-mod.md)：快速上手一个包含模块、状态与事件的完整 Mod。
- [事件、Hook 与 Callback](api/lua/v5/events.md)：订阅游戏事件，同步拦截与重写游戏行为。
- [跨平台 Lua UI](api/lua/v5/ui.md)：为 PC 键盘操作和 Android 原生触屏设计自适应页面。
- [CCB Lua 0.1 权限与能力](api/lua/v5/capabilities.md)：理解 Capability 声明与沙箱安全模型。

#### 🍳 纯 Lua 创作实战手册 (Cookbooks)
- [纯 Lua 装备与容器口袋实战](api/lua/v5/cookbook/items.md)：定义近战/远程武器、护甲及多 Pocket 容器嵌套模型。
- [纯 Lua 怪物与技能 AI 实战](api/lua/v5/cookbook/monsters.md)：编写全新物种、AI 策略树与动态特殊攻击。
- [纯 Lua 地块与建筑生成实战](api/lua/v5/cookbook/mapgen.md)：算法化生成避难所、哨站与 ASCII 字符矩阵蓝图。

#### 📚 API 参考手册直达（API Reference）
| API 分类 | 快速入口 | 内容说明 |
| --- | --- | --- |
| 📦 **核心类与对象 (Classes)** | [查阅类定义](api/lua/v5/reference/classes.md) | `Character`, `Creature`, `Item`, `Map`, `Mapgen`, `Vehicle` 等实体与句柄 |
| ⚡ **原生事件 (Events)** | [查阅 113 个事件](api/lua/v5/reference/events.md) | 回合更替、移动、受击、技能释放、装备穿脱等全量事件订阅 |
| 🪝 **逻辑拦截点 (Hooks)** | [查阅 52 个 Hooks](api/lua/v5/reference/hooks.md) | 同步拦截并覆写游戏原生核心决策与判定逻辑 |
| 🔧 **引擎全局函数 (Functions)** | [查阅函数表](api/lua/v5/reference/functions.md) | 引擎导出的所有全局工具函数与静态方法 |
| 🎮 **命名空间 (Namespaces)** | [查阅命名空间](api/lua/v5/reference/namespaces.md) | `game.*`, `map.*`, `player.*`, `ui.*` 等顶级命名空间 |
| 🎭 **回调 Actor (Callbacks)** | [查阅回调表](api/lua/v5/reference/callbacks.md) | 玩家交互、IUSE 动作与活动执行回调 |
| 🏷️ **枚举与常量 (Enums)** | [查阅枚举常量](api/lua/v5/reference/enums.md) | 伤害类型、部位、天气、标记等枚举定义 |

### 🛠️ 2. 本体与引擎开发者（C++ 引擎与底层架构）
面向贡献游戏底层逻辑、系统机制与原生绑定的开发者：
- [游戏引擎生命周期与主循环深度剖析](architecture/core-engine-lifecycle.md)：从引导启动、数据装载到 `process_turn` 回合循环全景图。
- [游戏引擎核心八大子系统深度剖析](architecture/subsystems-deep-dive.md)：实体、地图缓存、物品 Pocket、有限水体与物理场全拆解。
- [游戏本体核心开发与贡献指南](contributing/core-dev-guide.md)：Linux/Windows/Android 全平台环境、C++20 规范、Catch2 测试与 PR 规范。
- [C++ 引擎底层 Native 绑定指南](cpp/native-binding-guide.md)：使用 Sol2 导出类与函数、编写 LuaLS 注解与 100% 覆盖率验证。
- [快速构建指南](build/overview.md)：掌握 CMake / Make 现代编译流程与平台支持。

### 🏛️ 3. 参与项目与治理规范
- [第一次贡献](getting-started/first-contribution.md)：完成从环境配置到 PR 提交的最短路线。
- [Responsible Human](contributing/responsible-human.md)：理解代码贡献与 AI 辅助开发的责任模型。

