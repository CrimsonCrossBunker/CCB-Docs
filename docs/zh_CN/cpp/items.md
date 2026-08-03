---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.items
title: Item 子系统
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
- src/item.h
- src/item.cpp
- src/item_contents.cpp
- tests/item_test.cpp
source_symbols:
- 'class item : public visitable'
source_queries: []
source_fingerprint: d6d1953d58c7bdcbcabe63f1ef7104c6ff3a8d3d10f70119bf957f7d0e6f0201
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: db589b513ee116296c0ea65bf66e9e63ee7fcde871406c28f875881a0e2023d8
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
risk_group: cpp-items
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/items/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/items/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/items/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/items/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: src/item.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/item.h
- path: src/item.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/item.cpp
- path: src/item_contents.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/item_contents.cpp
- path: tests/item_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/tests/item_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.items%29%3A+&body=Document+ID%3A+cpp.items%0ALanguage%3A+zh_CN%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Item

## 职责

`item` 表示一个运行时物品实例：类型身份、数量、损坏、flag、变量、激活状态、制作
状态、唯一 ID 和嵌套 `item_contents`。静态 `itype` 定义由 `item_factory` 创建，不会
复制到每个实例中。

## 入口点

从 `src/item.h` 的 `class item` 开始。名称、护甲、枪械/工具/弹药、激活、劣化或转换
分别进入对应 `item_*.cpp`；创建经过 `item_factory`，持久化进入
`src/savegame_json.cpp`。

## 数据所有权

item 拥有实例字段和 contents；容器通过 pocket 拥有子 item；`item_location` 是可随
移动更新的引用，不是所有权。`itype_id` 在工厂中解析不可变定义数据。

## 依赖

物品依赖类型注册表、pocket、单位、flag、use actor、recipe、effect，以及当前持有它
的 map/character/vehicle 容器。

## 生命周期

item 从类型生成，可能激活、转换、拆分、堆叠、在所有者间移动，最终被消耗或销毁。
`safe_reference` 与持久 `item_uid` 解决不同身份问题，不能混用。

## 不变量

类型指针与 ID 一致；嵌套内容满足 pocket 约束；堆叠比较覆盖所有影响等价性的状态；
按 charges 计数的物品遵守数量规则；移动不能留下失效 location 或重复 UID。

## 扩展点

内容优先通过 item JSON 和既有 use actor 增加。原生行为放入对应 item 组件，并同时
更新 loader、formatter、存档兼容和测试。

## 序列化

`item::serialize` / `deserialize` 和 `item_contents` 持久化位于
`src/savegame_json.cpp`。新字段必须为旧存档提供默认值；派生缓存和 safe reference
不是持久状态。

## 测试

按修改的不变量选择 item、contents、pocket、stacking、name、spawn、location 或
activation 测试。任何持久实例字段都要做往返测试。

## 性能

物品访问与 name/info 生成会乘以大型 inventory 的规模。热 predicate 中避免递归全扫、
字符串格式化或重复 factory 查询；有明确失效边界时才用缓存。

## CCB 差异

CCB 的 item JSON 与运行时字段可能有意滞后、选择性移植或扩展上游契约。导入上游
修改前必须比较 loader、存档字段和测试。

## 技术债务

`item` 仍是分散在许多翻译单元中的宽类型。新增功能应进入既有组件，不要再引入跨
系统 flag 或无版本约定的变量。
