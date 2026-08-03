---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.crafting
title: Crafting 子系统
language: zh_CN
status: active
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/crafting.h
- src/crafting.cpp
- src/craft_command.h
- tests/crafting_test.cpp
source_symbols:
- class craft_command
source_queries: []
source_fingerprint: 6a0103d0d82160158e816f25c0ecaa11fa3c7c84fdac85f214eca5538595d42f
authority: source-and-tests
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 6c119fe070dc1bedf79c5cf26341ce81984e28e46e4732baf7f04c8e26ba9c24
prerequisites:
- cpp.character
- cpp.inventory
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
risk_group: cpp-crafting
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/crafting/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/crafting/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/crafting/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/crafting/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: src/crafting.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/crafting.h
- path: src/crafting.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/crafting.cpp
- path: src/craft_command.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/craft_command.h
- path: tests/crafting_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/crafting_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.crafting%29%3A+&body=Document+ID%3A+cpp.crafting%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 制作

## 职责

crafting 解析 recipe 知识、component/tool requirement、可访问 inventory、批量/时间计算、
选择、工作进度，以及 item 结果的制作或拆解；`craft_command` 记录已选择的执行计划。

## 入口点

从 `src/crafting.h`、`src/crafting.cpp`、`src/craft_command.h` 开始。角色访问位于
`character_crafting.cpp`，显示位于 `crafting_gui.cpp`，静态 recipe 契约位于 recipe
与 requirement loader。

## 数据所有权

注册表拥有 recipe/requirement。Character 和附近容器拥有来源 item，临时 crafting
inventory 只是视图；进行中的 craft item 拥有选中 component 与继续工作所需进度。

## 依赖

crafting 依赖 recipe、requirement data、item location/pocket、skill、proficiency、
quality、map/vehicle inventory、activity、热量和时间。

## 生命周期

recipe 加载并 finalize；Character 构建可访问 inventory，检查知识/需求，选择 component，
启动 activity，推进工作，最后完成、取消或恢复制作。

## 不变量

选择满足准确 requirement alternative；被消耗 item 仍有有效 location；批量与进度单位
一致；完成不能重复消耗；resume 数据与 recipe/component 一致。

## 扩展点

recipe 与 requirement 用 JSON 增加。原生扩展应新增可复用 requirement/activity 规则，
而不是按 recipe ID 特判，并覆盖 UI 和非 UI 调用者。

## 序列化

`craft_command` 选择和进行中 craft data 在原生存档层序列化。保存 ID 与选中 component，
不要保存临时 inventory cache 或 UI filter。

## 测试

使用 crafting、requirements、temporary-inventory、uncraft、GUI、attention、proficiency
和 activity 测试，覆盖互斥选择及中断/恢复。

## 性能

recipe filter 会反复查询大型 inventory。复用有范围的 requirement cache，避免每显示
一条 recipe 都重建全地图 crafting inventory。

## CCB 差异

即使 recipe ID 相同，CCB 的配方与制作行为也可能不同。移植必须加载 CCB 数据，并
验证 requirement、duration 和 resume 语义。

## 技术债务

需求求解、UI 选择与 activity 执行横跨多层。应保持契约显式，不能让 UI 状态成为执行
权威。
