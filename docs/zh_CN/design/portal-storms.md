---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: design-portal-storms
title: 旧文档迁移草稿：portal storms
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
- doc/design-balance-lore/PORTAL_STORM_BALANCE_AND_DESIGN.md
- src/game.cpp
- data/json/effects_on_condition/nether_eocs/portal_storm_effect_on_condition.json
- data/json/mapgen/portal_storm.json
- tests/widget_test.cpp
source_symbols:
- game::portal_storm_query
source_queries: []
source_fingerprint: 9370cc17f5eae8733866149bd28406ce50826f277aa6633dd233c94277c5892a
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: b6b8d4e2f6887b5dc2cf0795a849aec9f466f0861138003ca4593882c037aa13
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
risk_group: design
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/design/portal-storms/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/design/portal-storms/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/portal-storms/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/design/portal-storms/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/design-balance-lore/PORTAL_STORM_BALANCE_AND_DESIGN.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/PORTAL_STORM_BALANCE_AND_DESIGN.md
- path: src/game.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/game.cpp
- path: data/json/effects_on_condition/nether_eocs/portal_storm_effect_on_condition.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/effects_on_condition/nether_eocs/portal_storm_effect_on_condition.json
- path: data/json/mapgen/portal_storm.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/mapgen/portal_storm.json
- path: tests/widget_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/widget_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28design-portal-storms%29%3A+&body=Document+ID%3A+design-portal-storms%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：portal storms

本页是 `design-portal-storms` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `design-portal-storms`
- Target: `design/portal-storms.md`
- Replacement: design-portal-storms
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| design-portal-storms | doc/design-balance-lore/PORTAL_STORM_BALANCE_AND_DESIGN.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Portal storm 的设计角色

Portal storm 是会改变玩家计划的异常天气与跨维度碰撞，不是定时出现的 boss 战。它应制造不安、
干扰和额外压力，但不能仅靠无预警伤害强制杀死角色或让所有玩家只能原地睡觉。安全建筑应当有实际
价值；装备充分的角色可以选择冒险穿越，而不是被系统保证安全。

### 被动与主动压力

- **被动效果**表现世界相撞本身：异常实体、障碍、感知干扰或短暂环境变化。它们不应主动追猎玩家，
  也不应消耗代表关注度的 `ire`。
- **主动效果**表现恶意存在已经注意到暴露在外的角色。它们可以追踪、破坏或迫使玩家改变路线，
  但必须由相应条件触发并消耗 `ire`，避免无限叠加。
- 主题 storm 可以不复用完全相同的资源名，但仍应解释什么是环境背景、什么会锁定角色，以及玩家
  如何观察并降低风险。

当前第一方数据仍在
`data/json/effects_on_condition/nether_eocs/portal_storm_effect_on_condition.json` 注册
`EOC_PORTAL_EFFECTS_PASSIVE` 与 `EOC_PORTAL_EFFECTS_ACTIVE`。具体权重、条件、变量和效果以该 EOC
链、关联 mapgen 与调用代码为准；本页不冻结其数值。

## 内容审查清单

控制重复消息与效果频率，让声音、视觉和行为自己传达异常。检查室内/室外边界、地下与车辆、视线、
睡眠/活动打断、NPC、不同感知能力、保存重载和长时间多次 storm。新增 EOC 要验证条件、`ire` 收支、
失败分支与重复执行，并运行 JSON/EOC 加载和对应专项测试。长期设想（局部可追踪 storm、更多主题等）
仍是候选方向，不能写成当前已实现行为。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `9370cc17f5eae8733866149bd28406ce50826f277aa6633dd233c94277c5892a`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/design-balance-lore/PORTAL_STORM_BALANCE_AND_DESIGN.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/PORTAL_STORM_BALANCE_AND_DESIGN.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/PORTAL_STORM_BALANCE_AND_DESIGN.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
