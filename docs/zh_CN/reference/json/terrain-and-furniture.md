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
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: d69472f188e62af00b3ce34921f489256f9939e526c75b3475c4788efde2cec6
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/terrain-and-furniture/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/terrain-and-furniture/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/terrain-and-furniture/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/terrain-and-furniture/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/MAP_SMASHING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/MAP_SMASHING.md
- path: src/mapdata.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/mapdata.cpp
- path: src/mapdata.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/mapdata.h
- path: data/json/bash_damage_profiles.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/bash_damage_profiles.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.terrain-and-furniture%29%3A+&body=Document+ID%3A+json.terrain-and-furniture%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
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

## 地形、家具与砸击契约

地形和家具的 `bash` 对象由 `map_common_bash_info` 读取共同字段，再分别由
`map_ter_bash_info` 与 `map_furn_bash_info` 读取替换目标。CCB 会把未完成的砸击伤害存到
地图格；达到当前 `str_max`（或 blocked/supported 变体）后替换对象并清除累计伤害。

### 强度与伤害 profile

`str_min` 是每种伤害开始生效时使用的 armor threshold，`str_max` 是对象的有效 HP。
`damage_to()` 对武器的每种 damage type 应用 `bash_damage_profile` multiplier，分别减去
threshold 后只累计正值。profile 未显式列出的合法 damage type 会在 finalize 时使用该类型的
`bash_conversion_factor`；默认 profile 只覆盖 bash，其余类型由 finalize 补齐。

因此旧文档中的“`str_max - str_min` 就是 HP”不再准确。不要只看角色力量或单一 bash
数值推断结果；武器 damage composition、profile、blocked/supported 状态与已有 map damage 都会
影响实际破坏过程。

### 共同字段与替换

- `profile` 引用 `bash_damage_profile`，默认 `default`。
- `str_min_blocked`/`str_max_blocked` 和 `str_min_supported`/`str_max_supported` 是条件替代值。
- `items`、`sound*`、`hit_field`、`destroyed_field`、`explosive` 和 tent/collapse 字段控制副作用。
- terrain 必须提供 `ter_set`；`ter_set_bashed_from_above` 默认跟随它。
- furniture 的 `furn_set` 可省略并默认为 `f_null`。

字段 requiredness 与默认值以三个 loader 为准，不要从现有 JSON 的出现频率反推契约。

### 修改与验证

新增 profile 时必须使用有效 damage type 和非负 multiplier，并让 factory finalize/check 通过。
修改 terrain/furniture `bash` 时同时核对替换 ID、掉落组、字段生成、从上方砸击、支撑/阻挡和
累计伤害重置。运行 JSON formatter、`make -j2 json-check`，并为行为变化扩展
`tests/map_bash_test.cpp` 的 focused case；Mod 组合还要运行真实 `--check-mods`。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `c8a95926e96b9f72eca1128b039e2cde13be31e6da58865907ddbf9217d5ba5c`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/MAP_SMASHING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/MAP_SMASHING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/MAP_SMASHING.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
