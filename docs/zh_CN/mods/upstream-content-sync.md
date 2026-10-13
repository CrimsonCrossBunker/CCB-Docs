---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: mods.upstream-content-sync
title: 核心与随附 Mod 数据同步草稿
language: zh_CN
status: draft
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- mod-author
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: Pending human review
source_paths:
- data/json/mapgen/netherum/labyrinth_earth.json
- data/json/region_settings/region_settings/regional_map_settings.json
- data/mods/MindOverMatter/dimensions/shoggothed_world/region_settings.json
- data/upstream-changelog-20260921-20260928.txt
source_symbols: []
source_queries: []
source_fingerprint: 529cab08c982dc2364c967e7c0b522069ff08879567eea35c94192ec07069d63
authority: api-contract
verified_commit: 4ff8d9a6c64fc587a4dcf2f33082ca92c8945458
verified_at: '2026-10-14'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: c3082b54d8a14af8ed8261f0abd6647619a93727151d8da0761e5ee268590945
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- lua-contract
api_version: '1'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/997
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/mods/upstream-content-sync/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/mods/upstream-content-sync/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/mods/upstream-content-sync/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/mods/upstream-content-sync/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4ff8d9a6c64fc587a4dcf2f33082ca92c8945458
source_urls:
- path: data/json/mapgen/netherum/labyrinth_earth.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4ff8d9a6c64fc587a4dcf2f33082ca92c8945458/data/json/mapgen/netherum/labyrinth_earth.json
- path: data/json/region_settings/region_settings/regional_map_settings.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4ff8d9a6c64fc587a4dcf2f33082ca92c8945458/data/json/region_settings/region_settings/regional_map_settings.json
- path: data/mods/MindOverMatter/dimensions/shoggothed_world/region_settings.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4ff8d9a6c64fc587a4dcf2f33082ca92c8945458/data/mods/MindOverMatter/dimensions/shoggothed_world/region_settings.json
- path: data/upstream-changelog-20260921-20260928.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4ff8d9a6c64fc587a4dcf2f33082ca92c8945458/data/upstream-changelog-20260921-20260928.txt
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28mods.upstream-content-sync%29%3A+&body=Document+ID%3A+mods.upstream-content-sync%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4ff8d9a6c64fc587a4dcf2f33082ca92c8945458%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 核心与随附 Mod 数据同步草稿

本页对应 CCB #997。该草稿包含 127 个上游 PR 的数据部分；完整历史清单只排除用户明确拒绝的条目。一个 PR 可同时包含数据与原生代码，份数不能相加当作唯一 PR 数量。

## 内容和兼容边界

同步覆盖物品、配方、怪物、随附 Mod、森林落物、流亡族迷宫和 MoM 新维度。冲突按源 PR 的实际对象变化合并，保留 CCB 的稳定 ID、堆叠、技能、材料和既有回调。MoM 的峡谷底部地形依赖 #996 的原生加载字段；数学表达式和条件 Mod 加载分别依赖 #995、#994，不能只合并数据。

森林改动增加物品生成次数。固定种子 20261014、每种森林 1000 个区域的采样中，外层/浓密森林直木棍由 235/235 变为 273/886，物品生成步骤约 40/141 毫秒。采样只包含组、概率和迭代生成，尚未证明完整地图放置、游戏帧率或长期存档表现。

上游周报保存为独立历史材料；其中出现某项内容不代表它已经同步、测试或发布到 CCB。

## 验证范围

此前 14 个 Mod 身份用缓存引擎加必要前置适配通过加载。新增 MoM 数据用旧缓存程序时因缺少原生字段失败，因此需要匹配组合源码的新程序重新验收。生成契约、台账和元数据检查不能替代这个加载检查。全部新增玩法和旧存档尚未实测。

Responsible human: LYHGLYTX.
