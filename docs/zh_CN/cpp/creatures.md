---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.creatures
title: Creature 子系统
language: zh_CN
status: draft
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/creature.h
- src/creature.cpp
- src/creature_tracker.cpp
- tests/creature_test.cpp
source_symbols:
- 'class Creature : public viewer'
source_queries: []
source_fingerprint: dfe4c194a3da180d38dbc01dccf160ef9f66900266cb4d9d89febec6d2925cdb
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: f235b42e3c694abbbf01554bdb9d2fd81d66ffe74955f3b5e975dceb3716f395
prerequisites:
- architecture.overview
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-creatures
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/creatures/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/creatures/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/creatures/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/creatures/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: src/creature.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/creature.h
- path: src/creature.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/creature.cpp
- path: src/creature_tracker.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/creature_tracker.cpp
- path: tests/creature_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/tests/creature_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.creatures%29%3A+&body=Document+ID%3A+cpp.creatures%0ALanguage%3A+zh_CN%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Creature

## 职责

`Creature` 是 Character 与 monster 的多态基类，定义所有活跃行动者共享的位置、感知、
面向战斗的属性、伤害、effect、移动、可见性、态度钩子和 viewer 行为。

## 入口点

阅读 `src/creature.h`、`src/creature.cpp`；effect 集成由 creature-effect 测试覆盖，
空间索引与查找进入 `creature_tracker`。

## 数据所有权

creature 拥有基础行动者状态与 effect map，具体子类拥有类型专属状态。map 拥有地形；
`creature_tracker` 索引活跃实例，但不是它们的玩法所有者。

## 依赖

基类依赖坐标、map 可见性、field、effect、damage type、faction、event，以及
`Character` 或 `monster` 提供的虚行为。

## 生命周期

具体行动者被构造、定位并注册，由模拟更新，可能跨 submap 移动、受到效果/伤害、死亡，
最后由所有者从 tracker 移除。

## 不变量

tracker 位置与真实位置一致；活跃行动者不会在 tracker 重复；effect key 和持续时间
有效；虚类型 predicate 与具体对象一致。

## 扩展点

真正共享的行动者行为才放入 `Creature`，其余放在具体类。跨行动者变化优先通过既有
event 与 ID 发布，不要新增类型判断链。

## 序列化

基类提供共享读取 helper，但具体 `Character` 与 `monster` 路径拥有持久记录。tracker
索引和可见性缓存读取后重建。

## 测试

使用 creature、creature-in-field、creature-effect、vision、combat 和子类测试。移动
变化必须同时断言 map 占用与 tracker 查找。

## 性能

可见性、effect 处理、距离计算和 tracker 查询都是热路径。避免对所有 creature 扇出
虚调用，以及在嵌套循环中重复查 map。

## CCB 差异

CCB creature 行为由当前源码与测试定义，包括现行 field/effect 语义。上游算法移植
前必须提供确定性的回归证据。

## 技术债务

基类为语义不同的行动者暴露了很宽的虚接口。扩展时优先使用面向能力的 helper 与 event，
而不是继续增加宽泛虚函数。
