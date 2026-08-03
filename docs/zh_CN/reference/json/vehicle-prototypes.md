---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.vehicle-prototypes
title: 旧文档迁移草稿：vehicle prototypes
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
- doc/JSON/VEHICLES_JSON.md
- src/veh_type.cpp
- src/veh_type.h
- data/json/road_vehicles.json
- data/json/vehicleparts/vehicle_parts.json
- tests/vehicle_export_test.cpp
source_symbols:
- vehicle_prototype::load
- vehicles::parts::load
source_queries: []
source_fingerprint: c36cc2de2b212cd6775c390386b94d7211f0e1b36e05d6e0123f2f12c395af9a
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: edbe8a0981c4b6a78eb02c0d696b5278dd66a7d797b4929f02b8feafac996e37
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LunaGlaze, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/vehicle-prototypes/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/vehicle-prototypes/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/vehicle-prototypes/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/vehicle-prototypes/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/VEHICLES_JSON.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/VEHICLES_JSON.md
- path: src/veh_type.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/veh_type.cpp
- path: src/veh_type.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/veh_type.h
- path: data/json/road_vehicles.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/road_vehicles.json
- path: data/json/vehicleparts/vehicle_parts.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/vehicleparts/vehicle_parts.json
- path: tests/vehicle_export_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/vehicle_export_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.vehicle-prototypes%29%3A+&body=Document+ID%3A+json.vehicle-prototypes%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：vehicle prototypes

本页是 `json.vehicle-prototypes` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.vehicle-prototypes`
- Target: `reference/json/vehicle-prototypes.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/vehicle-prototypes/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.vehicle-prototypes | doc/JSON/VEHICLES_JSON.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Vehicle prototype 契约

`vehicle` prototype 用来生成 stock vehicle；生成后的车辆使用另一套存档表示。prototype 的
`id` 来自 generic factory，`parts` 是核心结构，`name`、`items`、`zones` 和 `color_palette`
可选；`blueprint` 当前只为兼容读取，不驱动生成。

### Parts 与安装顺序

每个 part group 必须有 `x`、`y` 和 `parts`。元素可以是 `vpart_id` 字符串，也可以是带
`part` 的对象；对象还可设置 0–100 的 `ammo`、`ammo_types`、`ammo_qty`、`fuel` 和 `tools`。
`part#variant` 在两种形式中都由最后一个 `#` 分割。

数组顺序就是安装顺序，必须满足游戏中的 frame、mount、wheel、engine、turret 等安装前置和
stacking 规则。同坐标可分多组追加，但不能借此绕过安装约束。有限的 copy-from 会先继承父项，
再追加 parts/items/zones；检查最终展开结果，而不是只看子对象。

### Items、zones 与导出

item spawn 要求 `x`、`y`、0–100 `chance`；可给 `items`、`item_groups`、`magazine` 和
`ammo`。item 可用字符串或 `{ "id", "variant" }`。zone 要求 type/x/y，并可有 name/filter；
只有车辆拥有 faction owner 时才实际放置。

Debug exporter 可生成 parts、部分 turret/fuel/tool、简单 cargo items、zones 与视觉 blueprint，
但会留下 placeholder id/name，且不保证复杂容器和 comestible round-trip。输出必须格式化并
人工审阅。

### 验证

运行 formatter、`make -j2 json-check` 与目标 Mod 的 `--check-mods`。新增复杂 prototype 时在
游戏中生成并检查 refresh、安装顺序、cargo、owner zones 与 palette。若修改 exporter 或字段，
扩展 `tests/vehicle_export_test.cpp` 的序列化后重新 load 等价测试。

## 历史与归属

清单中的已接受贡献者为：LunaGlaze, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `c36cc2de2b212cd6775c390386b94d7211f0e1b36e05d6e0123f2f12c395af9a`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/VEHICLES_JSON.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/VEHICLES_JSON.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/VEHICLES_JSON.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
