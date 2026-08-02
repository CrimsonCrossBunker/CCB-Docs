---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.inventory
title: Inventory 子系统
language: zh_CN
status: draft
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
- src/inventory.h
- src/inventory.cpp
- src/character_inventory.cpp
- tests/advanced_inventory_test.cpp
source_symbols:
- 'class inventory : public visitable'
source_queries: []
source_fingerprint: 68795ccdc6d58516938058c3abd0f3746c8f3c53290b20d5361c4da21c5cc0ae
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: ef01bd7cfd6865b84a58bc916ca97dc64bbc88ef325f2072cff48a4a8b24c3f5
prerequisites:
- cpp.items
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
risk_group: cpp-inventory
risk_level: normal
pending_source_pr: null
stale_reason: null
search:
  exclude: true
---

# Inventory

## 职责

`inventory` 为角色或临时制作视图组织 item stack，负责插入、移除、堆叠、invlet、
伪工具、搜索和带缓存的查询；它与 pocket 及 inventory UI 是不同层。

## 入口点

先读 `src/inventory.h`、`src/inventory.cpp`；角色集成在
`src/character_inventory.cpp`，临时制作视图使用 `form_from_map` / `form_from_zone`，
显示逻辑属于 `inventory_ui.cpp`。

## 数据所有权

容器拥有自己的 `std::list<item>` stack。角色拥有持久 inventory；临时 inventory
可能复制或合成视图（含 pseudo-item），因此不是 map/vehicle 物品的权威所有者。

## 依赖

inventory 依赖 item 堆叠、visitable 遍历、地图 zone、制作需求、角色 invlet 和
item-location 规则。

## 生命周期

物品被加入、重新堆叠、查询、消耗或移除。mutator 会把顺序和查询缓存标为 dirty；
临时制作 inventory 从来源范围重新构建。

## 不变量

每个 item 只有一个拥有容器；同一 stack 的成员确实可堆叠；invlet 遵循分配策略；
mutator 会失效 amount、charge、quality 与 sorted 状态缓存。

## 扩展点

只有 visitable/item-location API 无法表达时才增加聚焦查询或变更。显示 filter 属于
inventory UI，pocket 选择政策属于 pocket。

## 序列化

inventory 随拥有它的 Character 保存，而不是独立全局对象。pseudo-item 和查询缓存
读取后重建，不能成为存档权威。

## 测试

使用 advanced-inventory、temporary crafting inventory、物品颜色、pickup 和 item
location 测试。缓存修改必须覆盖“变更后再次查询”。

## 性能

`form_from_map`、restack 和递归 visit 可能主导制作与 UI 延迟。bulk-add 只能用于注释
明确支持的 invlet 组合，并保持来源顺序。

## CCB 差异

CCB 包含带明确顺序和 invlet 约束的批量插入路径。移植 inventory 优化时必须核对这些
约束和 CCB 性能测试。

## 技术债务

同一类型同时服务持久 inventory 与合成制作视图。在安全拆分职责前，代码必须明确
区分两者所有权。
