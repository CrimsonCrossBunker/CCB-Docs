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
translation_source_fingerprint: c029e08e0748ea803758654a8ace577e544623452fbbd0ccf8f5ec0b5511fc61
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

## 快速导航与技术手册目录

### 🚀 1. 起步与心智模型 (Getting Started)
- [CCB Lua 0.1 原生平台总览](api/lua/v5/overview.md)：理解零配置 Mod 发现、原生事务提交与代际安全句柄。
- [完整示例 Mod 剖析](api/lua/v5/example-mod.md)：快速上手一个包含模块、状态与事件的完整 Mod。
- [第一次代码贡献指南](getting-started/first-contribution.md)：完成从本地环境搭建到 PR 提交的最短路线。

### ⚔️ 2. 游戏核心子系统手册 (Core Subsystems Manual)
- [角色与生物系统技术手册](subsystems/character.md)：生物继承链、12 部位解剖健康模型、耐力痛觉与状态 Buff。
- [物品与 Pocket 容器系统手册](subsystems/items.md)：度量衡物理量标准、多 Pocket 容器嵌套树与装备动作。
- [地图与程序化生成技术手册](subsystems/map.md)：三维坐标网格、地形家具碰撞规则与 Mapgen 蓝图矩阵。
- [战斗、伤害与护甲结算手册](subsystems/combat.md)：7 大物理伤害类型、护甲覆盖率掷骰与 Hook 伤害拦截。
- [有限水体与环境物理系统手册](subsystems/water.md)：有限水体流体动力学、雷暴气象预报与物理场扩散。
- [车辆动力学与模块化部件手册](subsystems/vehicles.md)：刚体质心动力学、发动机传动比与模块化装甲槽位。

### 🌙 3. CCB Lua 0.1 平台参考 (Lua Platform Reference)
- [原生事件与 Hook 拦截](api/lua/v5/events.md)：订阅游戏原生事件，同步拦截并覆写游戏决策逻辑。
- [跨平台响应式 Lua UI](api/lua/v5/ui.md)：为 PC 键盘操作和 Android 原生触屏设计自适应窗口。
- [权限声明与 Capability 沙箱](api/lua/v5/capabilities.md)：理解 Capability 权限清单与内存安全边界。

### 🍳 4. 开发者实战食谱 (Cookbooks)
- [纯 Lua 装备与容器口袋实战](api/lua/v5/cookbook/items.md)：定义高周波战术军刀、防弹胸挂与多仓嵌套背包。
- [纯 Lua 怪物与技能 AI 实战](api/lua/v5/cookbook/monsters.md)：编写潜行掠食者、光环 Boss 与动态特殊攻击。
- [纯 Lua 地块与建筑生成实战](api/lua/v5/cookbook/mapgen.md)：算法化生成避难所前哨站与 ASCII 字符矩阵蓝图。

### ⚙️ 5. 引擎 C++ 底层与 Native 绑定 (C++ Engine Core)
- [游戏引擎生命周期与主循环深度剖析](architecture/core-engine-lifecycle.md)：从引导启动、数据装载到 `process_turn` 回合循环全景图。
- [游戏引擎核心八大子系统深度剖析](architecture/subsystems-deep-dive.md)：实体、地图缓存、物品 Pocket、有限水体与物理场全拆解。
- [游戏本体核心开发与贡献指南](contributing/core-dev-guide.md)：Linux/Windows/Android 全平台环境、C++20 规范与 Catch2 测试。
- [C++ 引擎底层 Native 绑定指南](cpp/native-binding-guide.md)：使用 Sol2 导出类与函数、编写 LuaLS 注解与 100% 覆盖率验证。
- [快速构建与编译指南](build/overview.md)：掌握 CMake / Make 现代编译流程与平台支持。

### 📚 6. 完整 API 字典速查 (Full API Reference)
| API 分类 | 快速入口 | 内容说明 |
| --- | --- | --- |
| 📦 **核心类与对象 (Classes)** | [查阅类定义](api/lua/v5/reference/classes.md) | `Character`, `Creature`, `Item`, `Map`, `Mapgen`, `Vehicle` 等实体与句柄 |
| ⚡ **原生事件 (Events)** | [查阅 113 个事件](api/lua/v5/reference/events.md) | 回合更替、移动、受击、技能释放、装备穿脱等全量事件订阅 |
| 🪝 **逻辑拦截点 (Hooks)** | [查阅 52 个 Hooks](api/lua/v5/reference/hooks.md) | 同步拦截并覆写游戏原生核心决策与判定逻辑 |
| 🔧 **引擎全局函数 (Functions)** | [查阅函数表](api/lua/v5/reference/functions.md) | 引擎导出的所有全局工具函数与静态方法 |
| 🎮 **命名空间 (Namespaces)** | [查阅命名空间](api/lua/v5/reference/namespaces.md) | `game.*`, `map.*`, `player.*`, `ui.*` 等顶级命名空间 |
| 🎭 **回调 Actor (Callbacks)** | [查阅回调表](api/lua/v5/reference/callbacks.md) | 玩家交互、IUSE 动作与活动执行回调 |
| 🏷️ **枚举与常量 (Enums)** | [查阅枚举常量](api/lua/v5/reference/enums.md) | 伤害类型、部位、天气、标记等枚举定义 |

### 🏛️ 7. 项目治理与贡献准则 (Governance & Policies)
- [Responsible Human 责任模型](contributing/responsible-human.md)：理解代码贡献与 AI 辅助开发的责任归属。

