---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.pockets
title: Item pocket 子系统
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
- src/item_pocket.h
- src/item_pocket.cpp
- src/savegame_json.cpp
- tests/item_pocket_test.cpp
source_symbols:
- class item_pocket
source_queries: []
source_fingerprint: 98aacfc7461dbd18a5fe0cd9f77e9c1af844e04a471e409a529f998891e695b1
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 15058334dbe3ae0dbae6295a3e42f60413af03077ce74702b078e9eb348cd07f
prerequisites:
- cpp.items
depends_on:
- cpp.inventory
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-pockets
risk_level: normal
pending_source_pr: null
stale_reason: null
search:
  exclude: true
---

# Item pocket

## 职责

`item_pocket` 对一个隔层实施存储约束：类型、体积、重量、长度、液体/气体密封、弹药
兼容、flag、优先级、白名单和嵌套内容。

## 入口点

从 `src/item_pocket.h`、`src/item_pocket.cpp` 开始；父级编排在
`item_contents.cpp`，存档在 `savegame_json.cpp`，插入行为由
`tests/item_pocket_test.cpp` 覆盖。

## 数据所有权

pocket 拥有放入其中的 item，以及 favorite settings 和运行时状态。静态容量/配置来自
父物品类型上的 pocket data。

## 依赖

它依赖 item 尺寸与相态、单位、ammo type、item location、父 contents、执行移动的
Character 和 JSON pocket 定义。

## 生命周期

pocket 从 item type 数据构建，接收和移除 item，密封/解封，更新 favorite settings，
并随父 item 保存。父物品转换时可能迁移或洒出内容。

## 不变量

插入必须返回有意义的 `contain_code`；每次变更后容量和相态约束仍成立；item 只有一个
所有者；递归容纳不能成环；sealed 状态与 pocket 能力一致。

## 扩展点

新约束应加入集中 containment 检查，并提供可诊断原因。偏好行为放在
`favorite_settings`，不要在 inventory UI 特判。

## 序列化

`item_pocket`、favorite settings 和 pocket data 在 `savegame_json.cpp` 读取。缺失
字段需有稳定默认值，迁移必须保留内容或明确拒绝。

## 测试

覆盖每个新成功/失败 code、嵌套 pocket、液体、重量/体积限制、白名单优先级、密封和
序列化往返。

## 性能

自动拾取与物品整理会评估很多 pocket。可行性检查应尽量不分配，并避免反复遍历嵌套
内容。

## CCB 差异

pocket 规则是存档和 Mod 可见契约。上游 pocket 变化要作为迁移审查，并以 CCB JSON
定义和测试为准，不能假设约束相同。

## 技术债务

容纳、偏好政策与序列化集中在宽类型中。新代码应把纯可行性判断同变更和 UI 决策
分开。
