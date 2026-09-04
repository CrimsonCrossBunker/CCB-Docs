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
translation_source_fingerprint: 9b7a15d02359cbafb53035ecd09d311a33440c72da3b3a8d2c594fcb632af0fd
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
- [Lua Platform v1：从零到运行](api/lua/v1/overview.md)：当前唯一受支持的 Lua MOD 入口和最小示例。
- [第一次代码贡献指南](getting-started/first-contribution.md)：完成从本地环境搭建到 PR 提交的最短路线。

### ⚔️ 2. 游戏核心子系统手册 (Core Subsystems Manual)
- [角色与生物系统技术手册](subsystems/character.md)：生物继承链、12 部位解剖健康模型、耐力痛觉与状态 Buff。
- [物品与 Pocket 容器系统手册](subsystems/items.md)：度量衡物理量标准、多 Pocket 容器嵌套树与装备动作。
- [地图与程序化生成技术手册](subsystems/map.md)：三维坐标网格、地形家具碰撞规则与 Mapgen 蓝图矩阵。
- [战斗、伤害与护甲结算手册](subsystems/combat.md)：7 大物理伤害类型、护甲覆盖率掷骰与 Hook 伤害拦截。
- [有限水体与环境物理系统手册](subsystems/water.md)：有限水体流体动力学、雷暴气象预报与物理场扩散。
- [车辆动力学与模块化部件手册](subsystems/vehicles.md)：刚体质心动力学、发动机传动比与模块化装甲槽位。

### 🌙 3. CCB Lua Platform v1
- [快速上手与版本规则](api/lua/v1/overview.md)：创建、安装并检查第一个 Lua MOD。
- [LuaLS 完整声明](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/master/data/lua/types/ccb_platform_v1.d.lua)：详细函数、参数、返回值和类型。
- [机器可读 API 契约](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/master/data/lua/reference/ccb_platform_api_v1.json)：工具生成与接口变更检查。
- [完整示例 MOD](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/tree/master/data/mods/Lua_First_Example)：按领域拆分的实际代码。
- [CCB-MOD 目录](https://crimsoncrossbunker.github.io/CCB-MOD/)：查找、安装或登记外部 MOD。

### ⚙️ 4. 引擎 C++ 底层与 Native 绑定 (C++ Engine Core)
- [游戏引擎生命周期与主循环深度剖析](architecture/core-engine-lifecycle.md)：从引导启动、数据装载到 `process_turn` 回合循环全景图。
- [游戏引擎核心八大子系统深度剖析](architecture/subsystems-deep-dive.md)：实体、地图缓存、物品 Pocket、有限水体与物理场全拆解。
- [游戏本体核心开发与贡献指南](contributing/core-dev-guide.md)：Linux/Windows/Android 全平台环境、C++20 规范与 Catch2 测试。
- [C++ 引擎底层 Native 绑定指南](cpp/native-binding-guide.md)：使用 Sol2 导出类与函数、编写 LuaLS 注解与 100% 覆盖率验证。
- [快速构建与编译指南](build/overview.md)：掌握 CMake / Make 现代编译流程与平台支持。

### 🏛️ 5. 项目治理与贡献准则 (Governance & Policies)
- [Responsible Human 责任模型](contributing/responsible-human.md)：理解代码贡献与 AI 辅助开发的责任归属。
