---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.options
title: 旧文档迁移草稿：options
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
- doc/JSON/OPTIONS.md
- src/options.cpp
- src/options.h
- data/core/external_options.json
- tests/options_test.cpp
source_symbols:
- options_manager::add_external
- options_manager::load
- options_manager::migrateOptionName
source_queries: []
source_fingerprint: dc0f5c048fe806d59c97d86763e1aa730559bde0e6753b81e8cd3d955a99ad24
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 0f05b23e0eb2aa9e6be3386bb17c64476480ce188a14c0d86680cf138fde3e10
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/options/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/options/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/options/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/options/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/OPTIONS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/OPTIONS.md
- path: src/options.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/options.cpp
- path: src/options.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/options.h
- path: data/core/external_options.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/core/external_options.json
- path: tests/options_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/options_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.options%29%3A+&body=Document+ID%3A+json.options%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：options

本页是 `json.options` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.options`
- Target: `reference/json/options.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/options/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.options | doc/JSON/OPTIONS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 游戏选项与 external options

CCB 的 option 不是单一 JSON registry。菜单选项主要在 `options_manager::add_options` 中注册；
隐藏的 external option 来自 `data/core/external_options.json` 及 Mod 数据，最后由
`options_manager::add_external` 建立具有类型和默认值的内部条目。保存的全局值来自
`config/options.json`，世界级值来自世界目录并可覆盖对应 world option。

读取保存值时，只有已注册的 option 才有意义。`options_manager::deserialize` 先通过
`migrateOptionName`/`migrateOptionValue` 处理旧名称和值，忽略明确移除的旧项，再设置当前条目。
external option 默认总是隐藏；支持的基础类型由 `get_value_type` 决定，包括 bool、int、float、
int_map、string_select 与 string_input。不要把旧文档中的加载顺序当作永久 ABI，应从当前启动、
世界加载和 Mod loader 路径验证。

把菜单项迁移为 external option 时需保存旧存档行为。历史上的 `stub` 方案用于避免 external
definition 覆盖已经设置的值，但具体字段与处理顺序必须和当前 loader 及
`external_options.json` 对照。修改时测试默认值、全局/世界覆盖、旧名称和值迁移、未知/移除项、
Mod load order 与保存后重载；用户可见说明应与菜单 tooltip 同步。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `dc0f5c048fe806d59c97d86763e1aa730559bde0e6753b81e8cd3d955a99ad24`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/OPTIONS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/OPTIONS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/OPTIONS.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
