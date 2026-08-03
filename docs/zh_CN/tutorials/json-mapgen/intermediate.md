---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: tutorial.mapgen-intermediate
title: 旧文档迁移草稿：intermediate
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
- doc/JSON/JSON_Mapping_Guides/Guide_for_intermediate_mapgen.md
- src/mapgen.cpp
- src/mapgen.h
- data/json/mapgen/nested/road_vehicles_nested.json
- tests/nest_conditional_placement_test.cpp
- tests/mapgen_function_test.cpp
source_symbols:
- mapgen_function_json::setup_internal
- jmapgen_objects::load_objects
source_queries: []
source_fingerprint: ba73dc2bf13ed7271634cda4f93ee00a08389742b6b72d9cdf081c0dcec03e54
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: d5e2cf4712dcd5d818cf5c48a6c97a9f9fbdcbafb361461ab4241777c7516082
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/tutorials/json-mapgen/intermediate/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/tutorials/json-mapgen/intermediate/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/tutorials/json-mapgen/intermediate/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/tutorials/json-mapgen/intermediate/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/JSON/JSON_Mapping_Guides/Guide_for_intermediate_mapgen.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/JSON_Mapping_Guides/Guide_for_intermediate_mapgen.md
- path: src/mapgen.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/mapgen.cpp
- path: src/mapgen.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/mapgen.h
- path: data/json/mapgen/nested/road_vehicles_nested.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/mapgen/nested/road_vehicles_nested.json
- path: tests/nest_conditional_placement_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tests/nest_conditional_placement_test.cpp
- path: tests/mapgen_function_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tests/mapgen_function_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28tutorial.mapgen-intermediate%29%3A+&body=Document+ID%3A+tutorial.mapgen-intermediate%0ALanguage%3A+zh_CN%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：intermediate

本页是 `tutorial.mapgen-intermediate` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `tutorial.mapgen-intermediate`
- Target: `tutorials/json-mapgen/intermediate.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/tutorials/json-mapgen/intermediate/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| tutorial.mapgen-intermediate | doc/JSON/JSON_Mapping_Guides/Guide_for_intermediate_mapgen.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Nested、merged 与 update mapgen

完整 variant 用同一 `om_terrain` 和 weight 替换整张 map；nested mapgen 把局部 chunk 叠到调用者；
update mapgen 则在游戏过程中修改已经存在的地图。三者生命周期不同，不能仅因 JSON 结构相似而
互换。

### Nested mapgen

顶层使用 `nested_mapgen_id`，可用 weight 提供同 ID variants；`object.mapgensize` 必须是两个相同
的正数，当前实现仍只支持 square。`rows`、palette、placement 和 nested-in-nested 都在这个局部
坐标系内。空符号通常保留底层，明确清除 terrain/furniture/items/trap/field 时使用当前 loader
支持的 null/clear 或 clearing flags，避免只覆盖一半状态。

调用者用 `nested` symbol 或 `place_nested` 坐标选择 weighted `chunks`；`null` 是有效的“不放置”
候选。当前 nested placement 还可按 neighbors、joins、flags、predecessors 和 z 等条件选择，行为
由 `jmapgen_nested` 与 `nest_conditional_placement_test.cpp` 证明。Chunk 必须落在调用者 grid 内，
门、墙和可通行边界要在所有 variants 一致。

### Merged 与 update

二维 `om_terrain` array 为每个 OMT 注册同一 merged definition 的 offset；所有 rows 使用连续的
总坐标。`common_check_bounds` 会拒绝跨当前 grid boundary 的坐标 range，因此 large rows 不表示
每种 placement 都能跨 OMT。把 vehicle、range spawn 与 nest 限制在单一 OMT，并用 focused tests
覆盖边界。

`update_mapgen_id` 注册运行时更新；调用点决定目标 OMT、参数、mirror/rotation、collision policy
与 mission context。Update 可能破坏玩家建造物、车辆、物品和存档状态，必须列出幂等性、冲突
和再次触发策略。不要用旧 trap 示例推断所有现有触发入口。

验证所有 nest weights/conditions、rotation、局部清除、NPC/vehicle、merged boundary、update
collision、重复执行与存档重载。运行 JSON load、目标 Mod load、focused mapgen/nest/update tests，
并在 debug mapgen 中记录 seed、位置、方向和调用参数。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`；聚合源指纹为 `ba73dc2bf13ed7271634cda4f93ee00a08389742b6b72d9cdf081c0dcec03e54`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/JSON_Mapping_Guides/Guide_for_intermediate_mapgen.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/JSON_Mapping_Guides/Guide_for_intermediate_mapgen.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/JSON_Mapping_Guides/Guide_for_intermediate_mapgen.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
