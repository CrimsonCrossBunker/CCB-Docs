---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.mapgen
title: 旧文档迁移草稿：mapgen
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
- doc/JSON/MAPGEN.md
- src/mapgen.cpp
- src/mapgen.h
- src/mapgen_post_process.cpp
- tests/mapgen_function_test.cpp
- tests/mapgen_post_process_test.cpp
source_symbols:
- mapgen_function_json::setup_internal
- update_mapgen_function_json::setup_update
- mapgen_palette::load
- pp_generator::load
source_queries: []
source_fingerprint: 253905cb7a14f68e2ba90a3ae9cb21be544d84da2a8a2e744fa3da643dab4382
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 3703c89671dec421c49118eaf2690c2a4a380c113c416bd44b44714e1c7fcbf1
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: dumb-kevin, ehughsbaird, RenechCDDA, Tektolnes; accepted inventory identities
  only. Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/mapgen/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/mapgen/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/mapgen/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/mapgen/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/MAPGEN.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/MAPGEN.md
- path: src/mapgen.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/mapgen.cpp
- path: src/mapgen.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/mapgen.h
- path: src/mapgen_post_process.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/mapgen_post_process.cpp
- path: tests/mapgen_function_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/mapgen_function_test.cpp
- path: tests/mapgen_post_process_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/mapgen_post_process_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.mapgen%29%3A+&body=Document+ID%3A+json.mapgen%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：mapgen

本页是 `json.mapgen` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.mapgen`
- Target: `reference/json/mapgen.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/mapgen/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.mapgen | doc/JSON/MAPGEN.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB mapgen 模型

Mapgen 把一个或多个 overmap terrain（OMT）转换为实际地图格、家具、物品、生物和其他
内容。`mapgen` 负责首次生成，`nested_mapgen` 生成可复用片段，`update_mapgen` 修改已有
地图。三者共享 palette/placing 语法，但尺寸、背景和执行时机不同。

### standalone mapgen

```jsonc
{
  "type": "mapgen",
  "om_terrain": "ccb_example_oter",
  "weight": 1000,
  "object": {
    "fill_ter": "t_grass",
    "rows": [
      "                        "
    ]
  }
}
```

实际普通 OMT 通常是 24×24；示例省略了剩余行，不能直接加载。`om_terrain` 可以指向一个
ID、多个 ID 或多 OMT 网格；网格形式的 rows 尺寸也要按 24 扩展。相同 OMT 的多个 mapgen
按 `weight` 参与选择，0 会禁用该变体。

`mapgen_function_json::setup_internal` 允许 `fill_ter`、`predecessor_mapgen` 或
`fallback_predecessor_mapgen` 提供背景。没有背景时，rows 中每个字符必须由本地或引用的
palette 定义。不要用空格掩盖未定义 terrain。

### rows、palette 与 placing

`terrain`、`furniture`、fields、items、monsters、vehicles、traps、computers、zones 等映射
把字符连接到 placing。具名 `palette` 必须有 ID，可以引用其他 palette；循环引用会报告。
`parameters` 和动态 mapgen value 扩大了可能结果，修改时要验证每个可能 ID，而不仅是默认值。

坐标 placing 和字符 rows 可以同时使用。多 OMT mapgen 中随机坐标范围不能错误跨越 OMT
边界。rotation、镜像、线性 terrain 后缀和多 z-level 组合会改变方向语义，应使用结构测试。

### nested 与 update

`nested_mapgen` 必须提供正方形 `mapgensize`，可覆盖父 mapgen 的一个区域并复用 palette。
`update_mapgen` 不要求 fill/rows 背景，它载入已经存在的地图后应用 placing，可能用于任务、
EOC 或后处理。更新不是幂等的：重复运行可能重复生成物品/NPC、删除结构或改变存档地图。

`update_mapgen` 目标 OMT、offset、rotation 与 verify 失败都要显式处理；不要把首次 worldgen
成功当作 update 对旧存档也安全的证明。

### 验证

1. 对照 overmap terrain ID、mapgen ID、special 旋转和连接关系。
2. 运行 formatter、`make -j2 json-check` 与实际 Mod 集 `--check-mods`。
3. 运行 `mapgen_function_test`，后处理变化再跑 `mapgen_post_process_test`。
4. 检查全部变体、旋转、邻接、z-level、palette 参数和边界字符。
5. 对 update 测试首次、重复、旧存档、目标缺失与部分占用地图。

初学者可先看[mapgen 入门教程](../../tutorials/json-mapgen/beginner.md)；本页负责当前 loader
边界，不替代源码字段检查。

## 历史与归属

清单中的已接受贡献者为：dumb-kevin, ehughsbaird, RenechCDDA, Tektolnes。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `253905cb7a14f68e2ba90a3ae9cb21be544d84da2a8a2e744fa3da643dab4382`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/MAPGEN.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/MAPGEN.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/MAPGEN.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
