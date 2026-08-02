---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.activities
title: Activity 子系统
language: zh_CN
status: draft
doc_type: reference
audiences:
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/player_activity.h
- src/activity_actor.h
- src/activity_actor.cpp
- tests/activity_tracker_test.cpp
source_symbols:
- class activity_actor
source_queries: []
source_fingerprint: 94f6cfccd0986d6a5caf071a7334bbe0c064bc32479455be2e25054ec33720b2
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 17895565fe1a2250932afd4b8c8594f9f562f3e02c9d6aa4fa53eff5395b7355
prerequisites:
- cpp.character
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
risk_group: cpp-activities
risk_level: normal
pending_source_pr: null
stale_reason: null
search:
  exclude: true
---

# Activity

## 职责

activity 表示跨 move/turn 的工作。`player_activity` 保存调度、进度、target、value、
resume 状态与可选多态 `activity_actor`；actor 实现拥有 start、每回合、finish、cancel
与序列化行为。

## 入口点

阅读 `src/player_activity.h`、`src/activity_actor.h` 及其实现，再看聚焦的
`activity_actor_definitions.h`。旧 handler 仍在 `activity_handlers`，调度/backlog 使用
`activity_tracker`。

## 数据所有权

`Character` 通过 tracker 拥有当前与排队 activity。`player_activity` 拥有可 clone 的
actor 与稳定 item location/target，但不拥有目标 item 或 map tile 本身。

## 依赖

activity 依赖 Character、item location、坐标、activity type 定义、inventory 有效性、
move point、UI interrupt、event 与存档 JSON。

## 生命周期

activity 构造并分配；actor `start` 一次；`do_turn` 推进；interrupt 可 suspend/cancel；
兼容工作可 resume；`finish` 或取消执行清理，然后 tracker 继续。

## 不变量

actor type 与 activity ID 一致；clone 保留具体行为；使用前检查 target；总 move 与剩余
工作一致；cancel 完成必要清理；resume 只比较兼容 actor。

## 扩展点

新的长耗时行为应实现 `activity_actor` 并注册 deserializer。UI 选择留在 actor 外，
持久执行输入放进 actor；不要再增加 legacy handler。

## 序列化

`player_activity` 在 `savegame_json.cpp` 序列化；每个 actor 必须保存自定义数据并注册
对应 deserializer。旧 actor payload 要有默认或迁移。

## 测试

使用 activity tracker/scheduling 和聚焦行为测试，覆盖 start、单回合、完成、取消、
suspend/resume、无效 target、clone 与存档往返。

## 性能

activity 每回合执行，并可能验证 inventory。能安全自行管理无效 item 清理的 actor 应
使用已有 override，避免反复昂贵扫描。

## CCB 差异

CCB 同时保留 actor 与 legacy activity 路径。上游 actor 移植必须匹配当前 CCB ID 映射、
存档 payload、interrupt 和 inventory 规则。

## 技术债务

legacy handler 与 actor activity 并存。应逐项迁移并保持存档兼容，不能重编号或悄然
重解释旧 ID。
