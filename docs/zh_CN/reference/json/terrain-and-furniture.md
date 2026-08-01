---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.terrain-and-furniture
title: 旧文档迁移草稿：terrain and furniture
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
- doc/JSON/MAP_SMASHING.md
- src/mapdata.cpp
- src/mapdata.h
- data/json/bash_damage_profiles.json
source_symbols:
- map_common_bash_info::load
- map_ter_bash_info::load
- map_furn_bash_info::load
source_queries: []
source_fingerprint: c8a95926e96b9f72eca1128b039e2cde13be31e6da58865907ddbf9217d5ba5c
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: bf6f49e400233ac101c7cd3238d26ac9c2892a629056b470764d09121dce9eeb
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- json.map-smashing
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

# 旧文档迁移草稿：terrain and furniture

本页是 `json.terrain-and-furniture` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.map-smashing`
- Target: `reference/json/terrain-and-furniture.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/terrain-and-furniture/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.map-smashing | doc/JSON/MAP_SMASHING.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | json.terrain-and-furniture |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `c8a95926e96b9f72eca1128b039e2cde13be31e6da58865907ddbf9217d5ba5c`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/MAP_SMASHING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/MAP_SMASHING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/MAP_SMASHING.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
