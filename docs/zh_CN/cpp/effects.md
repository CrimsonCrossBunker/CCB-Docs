---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.effects
title: Effect 子系统
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
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/effect.h
- src/effect.cpp
- src/effect_source.cpp
- tests/effect_test.cpp
source_symbols:
- class effect_type
source_queries: []
source_fingerprint: 9583fe6bb89626c7369d25b1a4678344f8815cc1352d8dfbfa374ffa2b2d498b
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 9a7e38d9eeb4f372357100947d6addddc2eaa4b17a718be5d562334f6ec65fdc
prerequisites:
- cpp.creatures
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
risk_group: cpp-effects
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/effects/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/effects/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/effects/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/effects/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: src/effect.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/effect.h
- path: src/effect.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/effect.cpp
- path: src/effect_source.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/effect_source.cpp
- path: tests/effect_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/tests/effect_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.effects%29%3A+&body=Document+ID%3A+cpp.effects%0ALanguage%3A+zh_CN%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Effect

## 职责

effect 子系统定义定时状态类型和每个 Creature 的实例：持续时间、强度、body-part 范围、
来源、modifier、消息、免疫、移除，以及重命名 effect ID 的迁移。

## 入口点

阅读 `src/effect.h`、`src/effect.cpp`、`src/effect_source.*`。静态 JSON 进入
`effect_type`；creature 的 `effects_map` 保存实例；EOC 集成是
`effect_on_condition` 中的另一契约。

## 数据所有权

注册表拥有 `effect_type` 定义。每个 `Creature` 拥有自己的 `effects_map`；`effect`
引用类型，并拥有实例持续时间、强度、身体范围和 source 数据。

## 依赖

effect 依赖 ID、body part、damage/character modifier、event、message、免疫规则、EOC、
source 序列化与 creature 每回合处理。

## 生命周期

类型加载并 finalize；实例被添加/刷新，每回合处理，改变强度或持续时间，触发相关行为，
最后到期或被明确移除/迁移。

## 不变量

类型 ID 可解析；持续时间/强度遵守类型边界；body-scoped key 不冲突；source 有效；
处理中移除不能使 iterator 失效；migration 无环且保留旧存档。

## 扩展点

优先使用 effect JSON、modifier 与 EOC hook。只有无法声明且可复用的行为才加原生实现，
并集中处理、测试免疫、添加、处理和移除路径。

## 序列化

effect 实例和 `effect_source` 在存档层序列化，定义从 JSON 加载。新字段需有默认值；
重命名 ID 必须提供明确 `effect_migration`。

## 测试

使用 effect/creature-effect 测试和聚焦 Character/monster 测试，覆盖 duration/intensity
边界、body part、免疫、source、处理中移除与往返。

## 性能

每个活跃 creature 都处理 effect。每回合工作应与活跃实例数成比例，避免重复类型查询/
格式化，也不要为一个 effect 重建整张 map。

## CCB 差异

即使共享 ID，CCB effect 定义与 EOC 用法也可能不同。移植数据和原生语义前要核对
migration、save 与 CCB 测试。

## 技术债务

effect 混合声明式 modifier 与原生特判。应优先使用显式可测的数据/event hook，并把
剩余硬编码 ID 行为记录为兼容债务。
