---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: design-gameplay
title: 旧文档迁移草稿：gameplay
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
- doc/design-balance-lore/design-gameplay.md
- doc/design-balance-lore/design-balance.md
- GOVERNANCE.md
source_symbols: []
source_queries: []
source_fingerprint: 2fab53e2adc355ab40f1aeee2c2a78ff29c21dff09461ffce678da0bce3c02f1
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 2603c5553b6715efbc8efc8c8cf232b95b6f4e3580ffb574bbf8781678266db2
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/design/gameplay/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/design/gameplay/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/gameplay/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/design/gameplay/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/design-balance-lore/design-gameplay.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/design-gameplay.md
- path: doc/design-balance-lore/design-balance.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/design-balance.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/GOVERNANCE.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28design-gameplay%29%3A+&body=Document+ID%3A+design-gameplay%0ALanguage%3A+zh_CN%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：gameplay

本页是 `design-gameplay` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `design-gameplay`
- Target: `design/gameplay.md`
- Replacement: design-gameplay
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| design-gameplay | doc/design-balance-lore/design-gameplay.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## CCB 的玩法方向

CCB 是开放世界生存游戏。核心体验来自在信息不完整、资源有限和环境持续变化的条件下制定计划，承担
可理解的风险，并处理计划产生的后果。世界模拟应支持这些决策，而不是为了模拟本身增加无法观察或
没有交互价值的细节。

### 贡献者应保留的性质

- 时间、位置、噪声、天气、负重、伤势、补给和敌人行为应形成相互联系的选择。
- 强力方案可以明显优于临时方案，但应有符合世界逻辑的获得、使用、维护或暴露成本。
- 角色知识、玩家知识和界面提示要区分；危险可以意外，但不应依赖无法学习的任意规则。
- 失败应尽量能够追溯到可观察的决定。必要的随机性需要适当范围、反馈和恢复空间。
- 自动化与便利功能应减少重复操作，同时保留路线、资源、时间和风险等有意义的决定。
- NPC、派系、任务和世界事件应在可能时通过共同系统互动，而不是只为单一脚本制造例外。

## 真实性与抽象

真实性用于决定世界中什么是合理的；抽象用于选择哪些细节值得玩家操作。贡献者可以省略电气参数、
重复劳动或不可见的微观过程，但要保留会改变策略的结果。相反，单纯因为某个机制“更真实”并不足以
证明它应加入：还要说明玩家如何理解它、如何应对它，以及它与现有系统的关系。

## 设计意图不是已实现功能

旧设计文档同时包含长期愿景、当时实现和未完成设想。迁移后的文本只保留可复用原则；任何具体行为仍
要从当前 C++、JSON、Lua 注册和测试确认。提案应明确标记“当前行为”“期望行为”和“未来可能方向”，
不要把愿望写成已经存在的契约。治理与合并决策遵循当前 `GOVERNANCE.md`，不由旧文档中的个人授权
语句决定。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `2fab53e2adc355ab40f1aeee2c2a78ff29c21dff09461ffce678da0bce3c02f1`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/design-balance-lore/design-gameplay.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/design-gameplay.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/design-gameplay.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
