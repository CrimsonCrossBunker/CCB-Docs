---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.loading-order
title: 旧文档迁移草稿：loading order
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
- data/json/LOADING_ORDER.md
- doc/JSON/JSON_LOADING_ORDER.md
- src/filesystem.cpp
- src/init.cpp
- src/game_io.cpp
source_symbols:
- DynamicDataLoader::load_data_from_path
- DynamicDataLoader::load_all_from_json
- DynamicDataLoader::finalize_loaded_data
source_queries: []
source_fingerprint: f0979275d95b5694a34e200e0c493b395e64c987686d4ae7488c44253f01d92e
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 31e74e42f3aeea3d2d71dd4176c2fdfa7cc4d630d80617fa94a157c936d3f7ea
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- legacy.data-json-loading-order
- legacy.doc-json-json-loading-order
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/loading-order/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/loading-order/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/loading-order/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/loading-order/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: data/json/LOADING_ORDER.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/LOADING_ORDER.md
- path: doc/JSON/JSON_LOADING_ORDER.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_LOADING_ORDER.md
- path: src/filesystem.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/filesystem.cpp
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/init.cpp
- path: src/game_io.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/game_io.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.loading-order%29%3A+&body=Document+ID%3A+json.loading-order%0ALanguage%3A+zh_CN%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：loading order

本页是 `json.loading-order` 的迁移草稿页面。它记录 **2** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `legacy.data-json-loading-order, legacy.doc-json-json-loading-order`
- Target: `reference/json/loading-order.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/loading-order/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| legacy.data-json-loading-order | data/json/LOADING_ORDER.md | merge_into | stubbed | 5f23722ff28c5cc552baa0422b32b1f10fd890fa | json.loading-order |
| legacy.doc-json-json-loading-order | doc/JSON/JSON_LOADING_ORDER.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | json.loading-order |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `f0979275d95b5694a34e200e0c493b395e64c987686d4ae7488c44253f01d92e`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`data/json/LOADING_ORDER.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/LOADING_ORDER.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/LOADING_ORDER.md)
- [`doc/JSON/JSON_LOADING_ORDER.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_LOADING_ORDER.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_LOADING_ORDER.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
