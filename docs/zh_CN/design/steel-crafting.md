---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: design-steel-crafting
title: 旧文档迁移草稿：steel crafting
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
- doc/design-balance-lore/STEEL_CRAFTING.md
- data/json/materials.json
- data/json/recipes/other/materials.json
- data/json/requirements/materials.json
source_symbols: []
source_queries: []
source_fingerprint: f12dfc5ad874180d9e08feb7e486805f625b52d0e537aa4b23769e04b0b6d35b
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 24578e84a3818c7bdc4a124c7d5475ea1f662f351689f02448cc51acb8e04d13
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: FarFarLakeSea, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: design
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/design/steel-crafting/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/design/steel-crafting/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/steel-crafting/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/design/steel-crafting/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/design-balance-lore/STEEL_CRAFTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/STEEL_CRAFTING.md
- path: data/json/materials.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/materials.json
- path: data/json/recipes/other/materials.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/recipes/other/materials.json
- path: data/json/requirements/materials.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/requirements/materials.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28design-steel-crafting%29%3A+&body=Document+ID%3A+design-steel-crafting%0ALanguage%3A+zh_CN%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：steel crafting

本页是 `design-steel-crafting` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `design-steel-crafting`
- Target: `design/steel-crafting.md`
- Replacement: design-steel-crafting
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| design-steel-crafting | doc/design-balance-lore/STEEL_CRAFTING.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 历史与归属

清单中的已接受贡献者为：FarFarLakeSea, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `f12dfc5ad874180d9e08feb7e486805f625b52d0e537aa4b23769e04b0b6d35b`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/design-balance-lore/STEEL_CRAFTING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/STEEL_CRAFTING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/STEEL_CRAFTING.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
