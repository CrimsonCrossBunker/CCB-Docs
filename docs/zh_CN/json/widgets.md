---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json-widgets
title: 旧文档迁移草稿：widgets
language: zh_CN
status: draft
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
review_interval_days: 365
last_human_reviewer: Pending human review
source_paths:
- doc/WIDGETS.md
- src/widget.cpp
- src/widget.h
- tests/widget_test.cpp
- data/json/ui/layout.json
source_symbols:
- widget::load_widget
- widget::load
source_queries: []
source_fingerprint: e2ec68ecbb94f6857d18bcb011f940e6ac2b0525364fed1d5346b482f4836fb3
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 6aa0f69517bc087826adb2aedf1c6a7ec176a8982eb23a99df6bbbfe98761ee0
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/json/widgets/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/widgets/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/widgets/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/widgets/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/WIDGETS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/WIDGETS.md
- path: src/widget.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/widget.cpp
- path: src/widget.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/widget.h
- path: tests/widget_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tests/widget_test.cpp
- path: data/json/ui/layout.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/ui/layout.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json-widgets%29%3A+&body=Document+ID%3A+json-widgets%0ALanguage%3A+zh_CN%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：widgets

本页是 `json-widgets` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json-widgets`
- Target: `json/widgets.md`
- Replacement: json-widgets
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json-widgets | doc/WIDGETS.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## JSON Widget 与侧栏布局

`"type": "widget"` 对象由 `widget::load_widget` 交给 `generic_factory<widget>`，字段由
`widget::load` 读取。Widget 既可以直接显示数字、图形或文本，也能以 `layout`/`sidebar`
组合其他 widget。可复用定义在 `data/json/ui/`，Mod 可用同一 factory 增加或继承 widget。

### 核心字段

每项需要唯一 `id`；`style` 默认 `number`，常见值是 `number`、`graph`、`text`、`layout`
和 `sidebar`。`label`、`description`、`width`、`height`、`text_align`、`label_align`、
`separator`、`padding`、`flags` 控制呈现。`sidebar` 必须显式给出 `separator` 与 `padding`；
layout 用 `widgets` 引用子项，以 `arrange: "columns"` 或 `"rows"` 排列。不要只根据旧文档
猜默认值：以 `widget::load` 和 `widget.h` 为准。

数值或文本 widget 用 `var` 绑定 `widget_var`。涉及身体部位的变量还需 `bodypart` 或
`bodyparts`。`var: "custom"` 必须提供 `custom_var.value` 与含 2–4 项的 `range`；range 可用
整数、variable object 或 math expression。图形的 `symbols`、`fill`、颜色断点和 clause
共同决定输出，非法 enum、引用和 range 会在加载或 consistency check 中暴露。

### 继承与验证

Widget 由 generic factory 管理，因此支持项目通用的 `copy-from`、`extend` 和 `delete` 语义。
对同一 `id` 的扩展会影响所有引用它的 layout；新增 sidebar 前先检查当前 UI JSON，避免无意
覆盖共享组件。

运行 JSON formatter/loader，并执行 `tests/widget_test.cpp` 中的 widget 测试。至少覆盖数值、
graph fill、颜色/clause、嵌套行列、窄宽度、bodypart、custom range 和 Mod 扩展。字段清单、
变量 enum 与实际默认值应从 `src/widget.cpp`、`src/widget.h` 重新核对。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `e2ec68ecbb94f6857d18bcb011f940e6ac2b0525364fed1d5346b482f4836fb3`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/WIDGETS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/WIDGETS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/WIDGETS.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
