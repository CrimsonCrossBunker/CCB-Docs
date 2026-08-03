---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.overmap
title: 旧文档迁移草稿：overmap
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
- doc/JSON/OVERMAP.md
- src/overmap_terrain.cpp
- src/overmap_special.cpp
- src/overmap_connection.cpp
- src/mapgen_post_process.cpp
- tests/overmap_test.cpp
source_symbols:
- overmap_terrains::load
- overmap_special::load
- overmap_connection::load
- pp_generator::load
source_queries: []
source_fingerprint: f5cf038161392828a65260a7f79ad3903e34851999d029d7aa4ce6f34a92c108
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 7bc22b2a9cd40fe5afa302c7dca736ed4fed534fde46053bb9323db1ffa4bd07
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: dumb-kevin, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/overmap/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/overmap/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/overmap/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/overmap/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/OVERMAP.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/OVERMAP.md
- path: src/overmap_terrain.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/overmap_terrain.cpp
- path: src/overmap_special.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/overmap_special.cpp
- path: src/overmap_connection.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/overmap_connection.cpp
- path: src/mapgen_post_process.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/mapgen_post_process.cpp
- path: tests/overmap_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/overmap_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.overmap%29%3A+&body=Document+ID%3A+json.overmap%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：overmap

本页是 `json.overmap` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.overmap`
- Target: `reference/json/overmap.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/overmap/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.overmap | doc/JSON/OVERMAP.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB overmap 数据关系

Overmap 数据分为多种相互引用的对象：`overmap_terrain` 定义 OMT 类型和显示/连接属性，
`overmap_special` 把一个或多个 OMT 组合并规定放置限制，`overmap_connection` 连接道路、
地铁等线性系统，mapgen 再为每个 OMT 生成局部地图。任何一层 ID 不一致都可能到 worldgen
阶段才暴露。

### overmap terrain 与 mapgen

一个 terrain 的稳定 ID 可能在 finalize 后展开为旋转/线性变体；mapgen 使用它的 mapgen ID。
一致性检查会报告没有 mapgen 且没有 uniform terrain 的 OMT，也会检查 static spawn group。
新 terrain 必须同时审阅：

- name、symbol、color、vision 和 flags；
- rotate/LINEAR 及连接方向；
- mapgen ID、uniform terrain、roof/地下层关系；
- monster density、extras 和位置 flag；
- 已发布 ID 对任务目标、存档与 Mod 的兼容性。

不要手写带方向后缀的引用并假定所有匹配场景相同；需要精确、type、subtype、prefix 或
contains 匹配时，以调用字段的当前 `ot_match_type` 语义为准。

### overmap special

fixed special 通过 `overmaps`/connections 组合 OMT；mutable special 使用另一套生成数据。
`occurrences` 是真实 `overmap_special` 的必填放置约束，city size/distance、locations、flags、
priority、rotation 和连接共同决定是否能放置。一个 special 在空白测试世界可放置，不代表
在已有城市、道路、其他 special 和 region blacklist 竞争下总能成功。

Special 可以绑定 inline EOC、参数、spawn 和 mapgen；多格结构的坐标、旋转中心、z-level
及连接端点必须成套验证。迁移已发布 special ID 时使用当前 migration 对象和存档测试。

### connection 与区域关系

`overmap_connection` 描述可连接 terrain 及规则；region settings 再选择城内/城间道路、
trail、sewer、subway 与 rail connection。改变 connection 或 region 引用可能重塑新 overmap，
但不会自动重写已生成区域，形成新旧存档差异。

### 验证

运行 formatter、`make -j2 json-check`、实际 Mod 集 `--check-mods` 和 `overmap_test` 相关
用例。至少生成多个 seed/region，检查 special occurrence、旋转、道路连接、边界、z-level、
任务目标和无可放置位置；对已发布 ID 做旧存档加载。

局部 tile 布局见[mapgen](mapgen.md)，宏观分布参数见[region settings](region-settings.md)。

## 历史与归属

清单中的已接受贡献者为：dumb-kevin, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `f5cf038161392828a65260a7f79ad3903e34851999d029d7aa4ce6f34a92c108`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/OVERMAP.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/OVERMAP.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/OVERMAP.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
