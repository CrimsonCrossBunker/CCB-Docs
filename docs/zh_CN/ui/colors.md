---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: ui-colors
title: 旧文档迁移草稿：colors
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
review_interval_days: 365
last_human_reviewer: Pending human review
source_paths:
- doc/user-guides/COLOR.md
- data/raw/colors.json
- data/raw/color_templates/default.json
- src/color.cpp
- tests/light_color_test.cpp
source_symbols:
- color_manager::load_default
- color_manager::load_custom
source_queries: []
source_fingerprint: aa880955188cf714e451fa318120a59ccac3bb9258529fa8177324bbb4cc1331
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: bacdc83bcea7b5ee9cc14e4b61e1c70a9d5338ead11cc98da368ae930b8c14bb
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
risk_group: ui
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/ui/colors/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/ui/colors/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/ui/colors/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/ui/colors/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/user-guides/COLOR.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/user-guides/COLOR.md
- path: data/raw/colors.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/raw/colors.json
- path: data/raw/color_templates/default.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/raw/color_templates/default.json
- path: src/color.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/color.cpp
- path: tests/light_color_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/light_color_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28ui-colors%29%3A+&body=Document+ID%3A+ui-colors%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：colors

本页是 `ui-colors` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `ui-colors`
- Target: `ui/colors.md`
- Replacement: ui-colors
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| ui-colors | doc/user-guides/COLOR.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## CCB 颜色系统

颜色名、配对与 invert/highlight 映射由 `color_manager::load_default` 建立，基础 RGB 默认值来自
`data/raw/colors.json`。常用名为 `c_foreground`，`h_` 表示 highlight，`i_` 表示 invert；部分
foreground/background 组合也有具名 pair。有效名称应从当前 color manager 查询，不能通过任意
拼接两个颜色名来推断。

Player-facing 字符串可用 `<color_name>…</color>`，并允许正确闭合的嵌套。颜色不能作为唯一
语义：禁用、危险、选中等状态还应有文字、符号或结构提示，以满足 screen reader 和不同主题。
地图、item 与其他 JSON 字段对 `color`/`bgcolor` 的支持由各自 loader 决定，不是所有对象都接受
相同组合。

### 用户配置与验证

基础 RGB 可在用户配置中覆盖，color manager 还会序列化具名 custom/invert mapping；ImGui
style 是另一条配置路径，RGBA 范围与 curses pair 不同。主题文件可以改变 highlight/invert
规则，因此代码不能依赖某个默认主题的实际 RGB。

修改颜色契约时运行 JSON loading、color consistency 和相关 UI/light tests。检查默认与自定义
主题、curses 与 tiles、ImGui、低对比和色觉差异、嵌套 tag、无效名 fallback 及 screen reader。
文档中的 RGB 只是固定 source commit 的默认值，不是永久视觉 ABI。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `aa880955188cf714e451fa318120a59ccac3bb9258529fa8177324bbb4cc1331`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/user-guides/COLOR.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/user-guides/COLOR.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/user-guides/COLOR.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
