---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: lore-overview
title: 旧文档迁移草稿：overview
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
- doc/design-balance-lore/lore.md
- doc/design-balance-lore/lore-background.md
- doc/design-balance-lore/lore-factions.md
source_symbols: []
source_queries: []
source_fingerprint: f7d75b8cadfa6753bff60372b7d010d7aa16b90d7fce63e82cafeb143f301074
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 4d0a92a69ec2403cb1e9afc4e41f9371e08918c4020eb5f6049652498f7b86df
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
risk_group: lore
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/lore/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/lore/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/lore/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/lore/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/design-balance-lore/lore.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/lore.md
- path: doc/design-balance-lore/lore-background.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/lore-background.md
- path: doc/design-balance-lore/lore-factions.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/lore-factions.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28lore-overview%29%3A+&body=Document+ID%3A+lore-overview%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：overview

本页是 `lore-overview` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `lore-overview`
- Target: `lore/overview.md`
- Replacement: lore-overview
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| lore-overview | doc/design-balance-lore/lore.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 面向贡献者的世界观入口

CCB 的玩家起点很简单：世界突然崩溃，城市被亡者占据，异界生物和残存人类组织争夺资源，而角色并不
知道完整原因。开发者后台设定更详细，但游戏应通过地点、物品、报纸、日志、对话、任务和系统互动让
玩家逐步拼出真相。全知说明属于贡献者资料，不应直接变成普通 NPC 的台词。

### 信息层次

- **玩家可直接观察**：环境、敌人行为、物品、伤势、天气和公开事件。
- **世界内记录**：写作者有身份、时间和偏见的 newspaper、终端、录音、任务与对话。
- **专家推断**：XEDRA 残余、Hub、外来阵营或研究记录能解释一部分机制，但仍可能错误或隐瞒。
- **后台 canon**：用于保持内容一致的剧透，不保证在游戏中完全揭示。
- **未来设计**：尚未实现的方向，必须保持 draft 并与当前行为分开。

## 核心连续性

灾前世界应保持可辨认的现代社会；少量差异来自 portal research、XEDRA 及受限的高科技。`XE-037`/Blob
污染、生物变化、亡者复活、社会崩溃和 portal storms 共同构成大灾变，而非单一公开解释。人类 faction
刚从共同社会分裂不久，应同时处理食物、安全、信任和冬季等日常问题；异界势力则可以具有完全不同的
时间尺度、感知和目标。

新 lore 内容要引用当前 ID 与来源，说明叙述者知道什么、为何知道、何时记录，并检查与 background、
technology、faction、mission 和已发布玩家线索的关系。若想 retcon，列出受影响 JSON、对话、地图、存档、
Mod 与翻译，先通过设计 Issue 审查；不要用旧设计页覆盖当前实现。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `f7d75b8cadfa6753bff60372b7d010d7aa16b90d7fce63e82cafeb143f301074`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/design-balance-lore/lore.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/lore.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/lore.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
