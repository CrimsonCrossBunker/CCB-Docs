---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: tutorial.mapgen-beginner
title: 旧文档迁移草稿：beginner
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
last_human_reviewer: LYHGLYTX
source_paths:
- doc/JSON/JSON_Mapping_Guides/Guide_for_beginning_mapgen.md
- src/mapgen.cpp
- src/overmap_terrain.cpp
- data/json/mapgen/abandoned_barn.json
- data/json/overmap/overmap_terrain/overmap_terrain.json
- tests/mapgen_function_test.cpp
- doc/JSON/JSON_Mapping_Guides/JSON_ROOF_MAPGEN.md
- data/json/mapgen/apartment_complex/apartment_complex_roof.json
source_symbols:
- mapgen_function_json::setup_internal
- overmap_terrains::load
source_queries: []
source_fingerprint: fd17455973053269a603ba05b18e7a7b4b5658f7ae492d95b0412d5fbf9db9bd
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 055042fc6b3c9e75ea0d0ff4472123dcdbe512363ff222473da66f3b1b7a6e6d
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- tutorial.mapgen-roofs
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/tutorials/json-mapgen/beginner/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/tutorials/json-mapgen/beginner/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/tutorials/json-mapgen/beginner/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/tutorials/json-mapgen/beginner/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/JSON_Mapping_Guides/Guide_for_beginning_mapgen.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_Mapping_Guides/Guide_for_beginning_mapgen.md
- path: src/mapgen.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/mapgen.cpp
- path: src/overmap_terrain.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/overmap_terrain.cpp
- path: data/json/mapgen/abandoned_barn.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/mapgen/abandoned_barn.json
- path: data/json/overmap/overmap_terrain/overmap_terrain.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/overmap/overmap_terrain/overmap_terrain.json
- path: tests/mapgen_function_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/mapgen_function_test.cpp
- path: doc/JSON/JSON_Mapping_Guides/JSON_ROOF_MAPGEN.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_Mapping_Guides/JSON_ROOF_MAPGEN.md
- path: data/json/mapgen/apartment_complex/apartment_complex_roof.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/mapgen/apartment_complex/apartment_complex_roof.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28tutorial.mapgen-beginner%29%3A+&body=Document+ID%3A+tutorial.mapgen-beginner%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：beginner

本页是 `tutorial.mapgen-beginner` 的迁移草稿页面。它记录 **2** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `tutorial.mapgen-beginner, tutorial.mapgen-roofs`
- Target: `tutorials/json-mapgen/beginner.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/tutorials/json-mapgen/beginner/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| tutorial.mapgen-beginner | doc/JSON/JSON_Mapping_Guides/Guide_for_beginning_mapgen.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |
| tutorial.mapgen-roofs | doc/JSON/JSON_Mapping_Guides/JSON_ROOF_MAPGEN.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | tutorial.mapgen-beginner |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 第一个 JSON mapgen

一个可生成的地点通常横跨三类契约：`mapgen` 画出 reality-bubble tiles，`overmap_terrain`
提供 OMT ID/显示/flags，`city_building`、region settings 或 `overmap_special` 决定如何在世界中
摆放。先选一个当前相近地点并沿 loader 与数据引用追踪，不要复制旧上游路径或把文件名当注册。

### 最小流程

1. 为每个地面/楼层/屋顶定义 overmap terrain ID。
2. 添加 `"type": "mapgen"`，用 `om_terrain` 绑定目标 ID；同 ID 的多个实现通过 `weight`
   参与选择。
3. 在 `object` 中给出 `fill_ter`、定长 `rows`，再用 terrain/furniture/palette 和 placement
   entries 解释符号。行宽和行数必须与该 mapgen grid 匹配；标准单 OMT 尺寸来自当前
   `SEEX/SEEY` 常量。
4. 城市建筑用当前 `city_building`/region registration；野外或多连接地点用
   `overmap_special`。多 z-level 的 point 要保证楼梯、梯子、排水管和屋顶开口对齐。
5. 使用 region groundcover 和现有 palette 时检查其全部继承效果，避免修改共享 palette
   意外改变其他地点。

### 内容与概率

Terrain/furniture symbol 可以共享同一格；未显式 terrain 的格子使用 `fill_ter`。Item、monster、
vehicle、NPC、field、trap、liquid 等 placement 各有独立 required fields、chance/repeat 与坐标
语义，不能从另一个 placement 类型类推。Vehicle mount origin 和 rotation 需要真实生成检查；
monster density 与固定 mapgen spawn 解决不同需求。

### 验证

先运行项目 JSON formatter 与 `make -j2 json-check`，再运行目标 Mod `--check-mods` 和 focused
mapgen tests。在全新未生成的 OMT 上通过 debug 反复生成，覆盖所有 weighted variants、四向旋转、
z-level、城市/特殊位置、季节/region、loot density 与边界连接。检查家具下方 terrain、门窗可达、
屋顶/地下层、车辆不跨 OMT、光照/视线和保存重载。已经生成进存档的 submap 不会因 JSON 修改
自动重建，不能作为新定义的验证样本。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `fd17455973053269a603ba05b18e7a7b4b5658f7ae492d95b0412d5fbf9db9bd`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/JSON_Mapping_Guides/Guide_for_beginning_mapgen.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_Mapping_Guides/Guide_for_beginning_mapgen.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_Mapping_Guides/Guide_for_beginning_mapgen.md)
- [`doc/JSON/JSON_Mapping_Guides/JSON_ROOF_MAPGEN.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_Mapping_Guides/JSON_ROOF_MAPGEN.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_Mapping_Guides/JSON_ROOF_MAPGEN.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
