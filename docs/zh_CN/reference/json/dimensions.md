---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.dimensions
title: 旧文档迁移草稿：dimensions
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
- doc/JSON/DIMENSIONS.md
- src/overmap_worldgen.cpp
- src/overmap_worldgen.h
- data/json/region_settings/region_settings/dimensions/dimensions.json
- data/json/effects_on_condition/nether_eocs/dimensions.json
source_symbols:
- dimension_world::load
- dimension_region_layout::load
source_queries: []
source_fingerprint: 9ab637a57079bd6baf25f89931aa6e5d13c24027ea38e460c71fbfdf249a3197
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: c0cbcfbf766baa5a928bc92037d3238e158bc5a1f15b6827e1dee1c3d1fa8e32
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LYHGLYTX, Anton Simakov, Maleclypse, thaelina; accepted inventory identities
  only. Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/dimensions/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/dimensions/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/dimensions/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/dimensions/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/DIMENSIONS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/DIMENSIONS.md
- path: src/overmap_worldgen.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/overmap_worldgen.cpp
- path: src/overmap_worldgen.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/overmap_worldgen.h
- path: data/json/region_settings/region_settings/dimensions/dimensions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/region_settings/region_settings/dimensions/dimensions.json
- path: data/json/effects_on_condition/nether_eocs/dimensions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/effects_on_condition/nether_eocs/dimensions.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.dimensions%29%3A+&body=Document+ID%3A+json.dimensions%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：dimensions

本页是 `json.dimensions` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.dimensions`
- Target: `reference/json/dimensions.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/dimensions/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.dimensions | doc/JSON/DIMENSIONS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Dimension 定义与切换

`dimension` object 只读取 `region_layout`；finalize 时无效引用会报告并退回 `default`。运行时把
非主 dimension 的 world 数据放在 save 的 dimension 区域，并在 travel 时切换当前加载的数据。
这不是可从未加载 dimension 任意读写地图的远程 API。

### 数据与 EOC 边界

定义新 dimension 时同时提供有效 `dimension_region_layout` 及其 region settings。当前 layout
实现只支持 UNIFORM；先验证 layout 页面中的实现边界。

`u_travel_to_dimension` 负责切换。`npc_travel_radius` 默认 0，filter 默认 `all`；当前 consumer
解析 filter 和半径后选择同行 NPC。`item_travel_radius` 默认 -1（不搬运），可用
`target_location` 改变收集与放置中心；还存在 vehicle 选项。字段、默认值与允许 filter 必须以
EOC registry 和 `talk_effect_fun::f_travel_to_dimension` 为准，旧片段只作示例。

`clear_dimension` 会清除对应 dimension 的持久化世界数据，之后再次进入会重新生成。这会丢失
其中的地图、物品、车辆、怪物、NPC 等状态，属于破坏性作者功能；不要把它当成普通传送清理。

### 安全工作流

先在 travel 前保存所需 location variable，再切换，再对已加载 dimension 做 mapgen update 或
teleport。不要在旧 dimension 卸载后继续使用其 bubble coordinate，也不要假设两个 dimension
的同坐标代表同一地点。

运行 formatter、`make -j2 json-check` 和 Mod `--check-mods`。用临时世界覆盖首次创建、往返、
存档 reload、NPC/item/vehicle 边界、无效 layout fallback 与 clear 后再生；不要在珍贵存档测试
`clear_dimension`。

## 历史与归属

清单中的已接受贡献者为：LYHGLYTX, Anton Simakov, Maleclypse, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `9ab637a57079bd6baf25f89931aa6e5d13c24027ea38e460c71fbfdf249a3197`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/DIMENSIONS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/DIMENSIONS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/DIMENSIONS.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
