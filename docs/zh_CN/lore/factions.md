---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: lore-factions
title: 旧文档迁移草稿：factions
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
- doc/design-balance-lore/lore-factions.md
- data/json/npcs/factions.json
- src/faction.cpp
- tests/monfactions_test.cpp
source_symbols: []
source_queries: []
source_fingerprint: 2d848c39599906582312af97e6f3698a2062240e8d2aff0162dcec0d4970ee90
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: beb13f1bfb9c58fa84cb6de7a84c270bcc8206c35ccc0ef4e070e43bdb017b2e
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/lore/factions/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/lore/factions/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/lore/factions/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/lore/factions/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/design-balance-lore/lore-factions.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/lore-factions.md
- path: data/json/npcs/factions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/npcs/factions.json
- path: src/faction.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/faction.cpp
- path: tests/monfactions_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tests/monfactions_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28lore-factions%29%3A+&body=Document+ID%3A+lore-factions%0ALanguage%3A+zh_CN%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：factions

本页是 `lore-factions` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `lore-factions`
- Target: `lore/factions.md`
- Replacement: lore-factions
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| lore-factions | doc/design-balance-lore/lore-factions.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 设计稿与当前实现必须分开

旧 faction 文档同时记录已经存在的阵营、未完成章节、未来任务构想和作者推测，不能当作当前游戏状态
清单。第一方 faction ID、基础关系、currency、food、wealth、epilogue 等数据以
`data/json/npcs/factions.json` 和 `faction` loader 为准；NPC、对话、任务、mapgen 和 tests 决定玩家
实际能遇到的成员与行为。文档冲突时标记 stale 并按这些来源修复。

## 阵营写作模板

每个阵营页面或提案至少区分：

- **身份与来源**：成员如何形成、哪些信息是玩家可见、哪些是后台剧透；
- **结构与规模**：领导、成员、从属关系和地理范围，并标明数字是实现值还是叙事估计；
- **目标与限制**：短期需求、长期方向、不能或不愿做的事情；
- **关系**：对玩家、其他人类阵营、mutant/augmentation 和非人势力的态度及其变化条件；
- **基地与经济**：真实 location、货币、商品来源、生产能力和供应瓶颈；
- **任务与发展**：当前 mission ID/对话入口、计划内容以及会改变世界或存档的阶段。

Blob、Mycus、triffid、netherum、Exodii、Yrax、mi-go 等不必符合人类国家模型。保留其不同感知、时间尺度、
沟通和价值体系，不要为了给玩家任务就让不可交流的力量突然采用普通 barter 或道德语言。

## 验证

新增或修改阵营时检查稳定 ID、`copy-from`、relations 对称性、mon faction、currency、price rules、food、
epilogue、NPC class、dialogue talker、mission 与 mapgen 引用。运行 JSON/EOC 加载、重复/失效 ID 检查和
相关 faction/monster-faction tests；在实际游戏覆盖首次发现、敌对转换、贸易、任务阶段和保存重载。
未实现的外交、基地或结局保持 draft，不能在正式页面写成现有功能。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`；聚合源指纹为 `2d848c39599906582312af97e6f3698a2062240e8d2aff0162dcec0d4970ee90`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/design-balance-lore/lore-factions.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/lore-factions.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/lore-factions.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
