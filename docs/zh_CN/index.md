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
translation_source_fingerprint: 232961e0cbd3e506537154eb53f7bb787c5dd7343a4f4637db90ca65dcb2b7e5
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
- [CCB Lua 0.1 自动参考手册](api/lua/v5/reference/modules.md)：查阅全部 500+ 个核心函数、事件、Hook 与类定义。

### 🛠️ 2. 本体与引擎开发者（C++ 引擎与构建）
面向贡献游戏底层逻辑、系统机制与原生绑定的开发者：
- [项目地图与架构](architecture/project-map.md)：按子系统导航 C++ 源码、数据与测试边界。
- [快速构建指南](build/overview.md)：掌握 CMake / Make 现代编译流程与平台支持。
- [自动化测试与验证](validation/quickstart.md)：运行 Catch2 单元测试与快速校验工具。
- [Native Lua Bridge 与绑定](cpp/lua-bridge.md)：了解 C++ 引擎与 Lua 0.1 运行时的数据桥接机制。

### 🏛️ 3. 参与项目与治理规范
- [第一次贡献](getting-started/first-contribution.md)：完成从环境配置到 PR 提交的最短路线。
- [Responsible Human](contributing/responsible-human.md)：理解代码贡献与 AI 辅助开发的责任模型。

