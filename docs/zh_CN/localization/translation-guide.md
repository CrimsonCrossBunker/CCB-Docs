---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: translation-guide
title: 旧文档迁移草稿：translation guide
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
- doc/TRANSLATING.md
- lang/Makefile
- src/translations.cpp
- .github/workflows/build-translations.yml
- .github/workflows/push-translation-template.yml
- src/translation_manager.cpp
- lang/notes/README_all_translators.md
- lang/update_pot.sh
source_symbols:
- TranslationManager::LoadDocuments
source_queries: []
source_fingerprint: 007ab64d80f8144fed21e6e91734d861c684c40ef5a68677e458368084ebe848
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 2bd70491246b6f2256eb371a2875b799c583360ea6d4b8970485c80431e5a5cd
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- legacy.lang-notes-readme-all-translators
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LunaGlaze, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: localization
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
search:
  exclude: true
---

# 旧文档迁移草稿：translation guide

本页是 `translation-guide` 的迁移草稿页面。它记录 **2** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `translation-guide, legacy.lang-notes-readme-all-translators`
- Target: `localization/translation-guide.md`
- Replacement: translation-guide
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| translation-guide | doc/TRANSLATING.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |
| legacy.lang-notes-readme-all-translators | lang/notes/README_all_translators.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | translation-guide |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 历史与归属

清单中的已接受贡献者为：LunaGlaze, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `007ab64d80f8144fed21e6e91734d861c684c40ef5a68677e458368084ebe848`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/TRANSLATING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/TRANSLATING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/TRANSLATING.md)
- [`lang/notes/README_all_translators.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/lang/notes/README_all_translators.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/lang/notes/README_all_translators.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
