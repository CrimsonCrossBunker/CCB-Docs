---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.obsoletion-and-migration
title: 旧文档迁移草稿：obsoletion and migration
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
- doc/JSON/OBSOLETION_AND_MIGRATION.md
- src/item_factory.cpp
- src/effect.cpp
- src/savegame_json.cpp
- data/json/obsoletion_and_migration_0.J/migration_items.json
- data/json/obsoletion_and_migration_0.J/eocs.json
- src/init.cpp
- src/magic.cpp
- src/proficiency.cpp
source_symbols:
- effect_migration::load
- ter_furn_migrations::load
- spell_migration::load
- proficiency_migration::load
source_queries: []
source_fingerprint: 4061a49a916458a30b17a18ae14969ab456a694b47ee87fef9ac0d7a08a6d979
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 77f2b5617a060b0744280d9fcb218c93ca3ba05cb3dec71e1f75ea12422bce00
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
search:
  exclude: true
---

# 旧文档迁移草稿：obsoletion and migration

本页是 `json.obsoletion-and-migration` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.obsoletion-and-migration`
- Target: `reference/json/obsoletion-and-migration.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/obsoletion-and-migration/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.obsoletion-and-migration | doc/JSON/OBSOLETION_AND_MIGRATION.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `4061a49a916458a30b17a18ae14969ab456a694b47ee87fef9ac0d7a08a6d979`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/OBSOLETION_AND_MIGRATION.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/OBSOLETION_AND_MIGRATION.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/OBSOLETION_AND_MIGRATION.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
