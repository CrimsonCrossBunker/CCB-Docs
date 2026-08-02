---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: modding-overview
title: 旧文档迁移草稿：overview
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
- doc/MODDING.md
- src/mod_manager.cpp
- src/init.cpp
- src/game_io.cpp
- build-scripts/get_all_mods.py
source_symbols:
- DynamicDataLoader::load_mod_interaction_files_from_path
- game::load_mod_interaction_data_from_dir
source_queries: []
source_fingerprint: 01df11ed2410a7436b91d317d9a7b0843f550d730255abb4d6c637526c226e9b
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 54105e68a8c09c078e03a6988321b0e6c0a2e35fbb2bee8ea8c5b9c7cb48e1d0
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: SpinosaurusBoat, thaelina; accepted inventory identities only. Source
  paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: mods
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/modding/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/modding/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/modding/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/modding/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/MODDING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/MODDING.md
- path: src/mod_manager.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/mod_manager.cpp
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/init.cpp
- path: src/game_io.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/game_io.cpp
- path: build-scripts/get_all_mods.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/build-scripts/get_all_mods.py
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28modding-overview%29%3A+&body=Document+ID%3A+modding-overview%0ALanguage%3A+zh_CN%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：overview

本页是 `modding-overview` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `modding-overview`
- Target: `modding/overview.md`
- Replacement: modding-overview
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| modding-overview | doc/MODDING.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 历史与归属

清单中的已接受贡献者为：SpinosaurusBoat, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `01df11ed2410a7436b91d317d9a7b0843f550d730255abb4d6c637526c226e9b`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/MODDING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/MODDING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/MODDING.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
