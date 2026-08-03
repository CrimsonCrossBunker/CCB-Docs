---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.region-settings
title: 旧文档迁移草稿：region settings
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
- doc/JSON/REGION_SETTINGS.md
- src/regional_settings.cpp
- src/regional_settings.h
- data/json/region_settings/region_settings/regional_map_settings.json
- data/json/region_settings/region_settings/test_regional_map_settings.json
source_symbols:
- region_settings::load
- region_settings_forest::load
- region_settings_city::load
- region_settings_map_extras::load
source_queries: []
source_fingerprint: f05aef27b8d0e8fd9c261d28b53ca8eb8deecda5013130a8bea03bff089c653f
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 2b87b38ba375d1ed5a16f52c3c133431192082e32cb055c999de299a51147cc2
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/region-settings/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/region-settings/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/region-settings/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/region-settings/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/REGION_SETTINGS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/REGION_SETTINGS.md
- path: src/regional_settings.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/regional_settings.cpp
- path: src/regional_settings.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/regional_settings.h
- path: data/json/region_settings/region_settings/regional_map_settings.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/region_settings/region_settings/regional_map_settings.json
- path: data/json/region_settings/region_settings/test_regional_map_settings.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/region_settings/region_settings/test_regional_map_settings.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.region-settings%29%3A+&body=Document+ID%3A+json.region-settings%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：region settings

本页是 `json.region-settings` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.region-settings`
- Target: `reference/json/region-settings.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/region-settings/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.region-settings | doc/JSON/REGION_SETTINGS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB region settings 结构

Region settings 决定新 overmap 的默认 terrain、地表、森林/河流/湖海、城市、道路连接、
highway、map extras、天气和 feature flag 筛选。它不是一个可以任意添加字段的大对象：
多个 `region_settings_*` object type 由各自 factory 加载，再由主 `region_settings` 通过 ID
引用组合。

### 主 region

主对象读取 default OMT/groundcover、cities（必填）、weather、forest、river、lake、ocean、
highway、ravine、connections、map extras 与 terrain/furniture 替换等组件，并控制是否放置
road、railroad、special 和邻接连接。默认 region 的 `id: "default"` 必须有效，否则 finalize
会报告。

不要从旧表猜组件字段：例如 `region_settings_city` 当前强制 `city_size`，forest、highway、
lake、map-extra collection 都有自己的 reader、默认值和稳定 ID。

### 扩展与覆盖

```jsonc
{
  "type": "region_settings",
  "id": "default",
  "copy-from": "default",
  "feature_flag_settings": {
    "extend": { "blacklist": [ "CCB_EXCLUDED" ] }
  }
}
```

`copy-from`/extend 的具体支持取决于该字段的 reader。相同 ID 的 Mod patch 依赖加载顺序；
多个 Mod 修改 default region 时可能互相覆盖。为独立世界规则建立新 region 通常比隐式修改
所有世界更易审阅，但仍需确认世界选择入口与 dimension/layout 引用。

### 城市、extras 与 feature flags

城市 weighted lists 引用 OMT 或 special；半径/size/spacing 控制宏观分布，不保证每个候选
都能放置。Map extra collection 用 chance 和权重引用已注册 extra。feature blacklist/
whitelist 与 overmap location flags 共同过滤内容；过严组合可能产生空候选或断路。

Region 修改只影响尚未生成的 overmap。玩家走过的区域不会自动重建，因此任何视觉、资源
或道路变化都要分别描述“新世界/新区域”和“旧存档已生成区域”的行为。

### 验证

运行 formatter、`make -j2 json-check` 和实际 Mod 集 `--check-mods`。用多个 seed 生成完整
overmap，记录所选 region，检查城市/道路、森林水体、special、extras、天气和黑白名单；
同时加载旧世界并跨越到新 overmap，确认边界和连接可接受。

具体 OMT/special 关系见[overmap](overmap.md)，局部生成见[mapgen](mapgen.md)。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `f05aef27b8d0e8fd9c261d28b53ca8eb8deecda5013130a8bea03bff089c653f`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/REGION_SETTINGS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/REGION_SETTINGS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/REGION_SETTINGS.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
