---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.region-layout
title: 旧文档迁移草稿：region layout
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
- doc/JSON/REGION_LAYOUT.md
- src/overmap_worldgen.cpp
- src/overmap_worldgen.h
- data/json/region_settings/region_settings/dimensions/dimension_regions.json
source_symbols:
- dimension_region_layout::load
source_queries: []
source_fingerprint: f2a802108a8d9ac03af482ec4deb5d436ba86695b03917b2e1ccdf8cffea0f7e
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 46f38a48d05771ca129437dc675987a38448a5127d7a5e1ed8103a346e2df8a0
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LYHGLYTX, Anton Simakov; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/region-layout/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/region-layout/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/region-layout/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/region-layout/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/JSON/REGION_LAYOUT.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/REGION_LAYOUT.md
- path: src/overmap_worldgen.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/overmap_worldgen.cpp
- path: src/overmap_worldgen.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/overmap_worldgen.h
- path: data/json/region_settings/region_settings/dimensions/dimension_regions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/region_settings/region_settings/dimensions/dimension_regions.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.region-layout%29%3A+&body=Document+ID%3A+json.region-layout%0ALanguage%3A+zh_CN%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：region layout

本页是 `json.region-layout` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.region-layout`
- Target: `reference/json/region-layout.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/region-layout/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.region-layout | doc/JSON/REGION_LAYOUT.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Dimension region layout

`dimension_region_layout` 决定一个 dimension 的 overmap 使用哪个 `region_settings`。当前
loader 必须读取 `generation_mode`，但 pinned CCB 实现的 switch 只为 `UNIFORM` 创建 generator；
JSON 枚举或头文件中出现其他 mode 不等于它们可用。

### 当前支持的模式

`UNIFORM` 是 dynamic layout，并要求 `uniform_region`。第一次访问某个 overmap 时 generator
把该坐标映射到同一个 region。当前第一方 `dimension_regions.json` 也全部使用这一模式。

头文件保留 MANUAL_VORONOI、RANDOM、EIGHTHS 与 static layout 的类型和部分基类，但 loader
没有对应 case。不要发布使用这些值的 Mod，也不要把未接线的 `generated_bounds_*` 或
`layout_out_of_bounds` 当成公开 JSON 契约。要启用新模式，必须先实现 deserialize、generator、
factory finalize/check 与测试，而不只是放开枚举。

### ID 链与验证

layout 的 `uniform_region` 必须是有效 region settings，`dimension.region_layout` 再引用这个
layout。检查完整链：dimension → layout → region settings → overmap generation 数据。

运行 formatter、`make -j2 json-check` 和完整 `--check-mods`，实际创建新 world/dimension 并生成
多个 overmap。对新 generator 加 deterministic seed、边界、存档 reload 与无效 ID fallback
测试；region layout 变化可能改变新生成世界，必须在 PR 标明兼容性影响。

## 历史与归属

清单中的已接受贡献者为：LYHGLYTX, Anton Simakov。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`；聚合源指纹为 `f2a802108a8d9ac03af482ec4deb5d436ba86695b03917b2e1ccdf8cffea0f7e`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/REGION_LAYOUT.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/REGION_LAYOUT.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/REGION_LAYOUT.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
