---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.mutations
title: Mutation 子系统
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
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/mutation.h
- src/mutation.cpp
- src/mutation_data.cpp
- tests/mutation_test.cpp
source_symbols:
- struct mutation_branch
source_queries: []
source_fingerprint: eb2d2057e6b418e5c330673786e0225fd459e9ddbb88eed4f36fcbda0999a62f
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 2aadbb74e5fdcf96f4c4b7ce41f07df7bd791454e4507658cdf854cd5b387e8e
prerequisites:
- cpp.character
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
- json-load
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-mutations
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/mutations/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/mutations/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/mutations/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/mutations/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: src/mutation.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/mutation.h
- path: src/mutation.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/mutation.cpp
- path: src/mutation_data.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/mutation_data.cpp
- path: tests/mutation_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/tests/mutation_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.mutations%29%3A+&body=Document+ID%3A+cpp.mutations%0ALanguage%3A+zh_CN%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 变异

## 职责

mutation 子系统定义 mutation type/branch、前置与冲突、category、variant、enchantment、
attack、身体变化、激活、获得/移除，以及 trait 如何修改 Character。

## 入口点

阅读 `src/mutation.h`、`src/mutation.cpp`、`src/mutation_data.cpp`。JSON 加载到
`mutation_branch` 等注册表；角色应用和 UI 位于聚焦 mutation/character 文件。

## 数据所有权

注册表拥有不可变 mutation 定义。`Character` 拥有已获得 trait、variant、激活与 charge；
trait 派生缓存属于角色，必须通过常规 mutation API 失效。

## 依赖

mutation 依赖 JSON ID、body part、enchantment、effect、vitamin、item、martial art、spell、
角色属性、event 和存档迁移。

## 生命周期

定义加载、check、finalize；选择流程解析前置/冲突和 category；角色应用或移除 trait；
active mutation 处理消耗；结果随角色持久化。

## 不变量

引用 ID 可解析；前置/冲突图有效；trait 状态与身体/属性派生缓存一致；激活消耗不能
下溢；variant 身份在存档往返后保持。

## 扩展点

优先使用 mutation JSON、EOC、enchantment 与既有效果。只有数据无法表达的可复用行为
才进入原生代码，并提供图验证和 character 测试。

## 序列化

定义从数据反序列化；已获得 trait 及状态随 character 存档。新持久状态需为旧 trait
表示提供默认与迁移。

## 测试

使用 mutation 测试，并按需增加 character modifier、body、enchantment、vitamin、
effect 与存档测试。覆盖获得/移除对称性和每条被改前置/冲突边。

## 性能

trait 派生计算出现在角色更新与 UI 路径。mutation 集合变化时失效窄缓存，不要每回合
重扫全部定义。

## CCB 差异

CCB mutation 数据与旧 Mod ID 是兼容边界。上游 mutation 必须对 CCB 数据集核对依赖
图、body part 与存档。

## 技术债务

mutation 效果横跨数据、character cache、UI 和硬编码 hook。应把可复用行为逐步迁往
声明式契约，同时不能悄然改变已有 trait。
