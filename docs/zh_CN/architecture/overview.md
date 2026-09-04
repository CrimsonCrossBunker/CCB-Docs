---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: architecture.overview
title: CCB 项目架构
language: zh_CN
status: active
doc_type: explanation
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- AGENTS.md
- ai/project-map.yml
- src/AGENTS.md
- data/AGENTS.md
- tests/AGENTS.md
source_symbols: []
source_queries: []
source_fingerprint: 2fcaa70cf7c9ac3329ddd620fa52c7e410a6d8f9848a2538d6aee0fce0439374
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: d4ca77032fb59a245876f6d2e67bfd4c3f77cc29f08ab6f13083d5a6df85e512
prerequisites:
- home
depends_on:
- architecture.project-map
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: architecture
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/AGENTS.md
- path: ai/project-map.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/ai/project-map.yml
- path: src/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/AGENTS.md
- path: data/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/AGENTS.md
- path: tests/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/AGENTS.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28architecture.overview%29%3A+&body=Document+ID%3A+architecture.overview%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# CCB 项目架构

CCB 是数据驱动的 C++ 游戏。C++ 引擎负责对象生命周期、地图与存档、核心模拟、UI
和加载流程；JSON 定义大量游戏内容；EOC 在 JSON 中表达条件化行为；Lua Platform v1
通过 `require("ccb")` 为 MOD 提供公共接口。旧 v5 已移除，不适用于当前 Candidate。

## 层次与依赖方向

1. **构建与平台层**：Make、CMake、Gradle、CI 和打包脚本决定可用工具链与产物。
2. **原生运行时**：`src/` 拥有对象、模拟、UI、序列化和 native Lua bridge。
3. **数据契约**：`data/json/`、`data/core/` 和 `data/mods/` 由注册器、工厂和验证器加载。
4. **脚本契约**：Lua Platform v1 的 ModDefinition、LuaLS 声明、native 注册和生成清单必须一致。
5. **验证层**：`tests/` 与仓库工具验证运行时、数据、公开契约和生成边界。

依赖通常从数据和脚本进入已注册的引擎接口。不要让说明文档成为新的运行时契约，
也不要为了匹配旧文档而改变源码语义。

## 数据所有权

- C++ 类型拥有运行时状态和序列化不变量。
- JSON ID 是跨数据、存档和 Mod 的兼容边界；重命名需要迁移或 obsolete 记录。
- EOC 的 talker、变量与 context 决定求值语义，不能只按字段名字猜测。
- Lua Platform v1 的公共符号以 `ccb_platform_v1.d.lua` 和原生注册为准；MOD 是受信任代码，不再使用旧 v5 的 capability manifest。
- 生成文件由源契约推导，应更新生成器或源，不应直接修补输出。

## 扩展点

内容优先使用现有 JSON 类型、EOC 或受支持的 Lua API。只有当数据接口无法表达所需
行为时才扩展 C++，并同时检查注册、验证、序列化、测试和文档影响。

CCB 会选择性移植 CDDA、CBN 和其他兼容来源，但保留自己的行为、数据与 Lua API。
评审时必须明确“共同祖先行为”“上游新行为”和“CCB 有意差异”。
