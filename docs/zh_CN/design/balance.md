---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: design-balance
title: 旧文档迁移草稿：balance
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
- doc/design-balance-lore/GAME_BALANCE.md
- doc/design-balance-lore/design-balance.md
- GOVERNANCE.md
source_symbols: []
source_queries: []
source_fingerprint: 1d0054d7999d75ae681f7fa6317b6ee70b8c6bdd8b86a97507c1edf1f974fb51
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 13fee1d31007d3482845ef6483008b2b839b5f3b753834a8745ee91de1c4a3ce
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- legacy.doc-design-balance-lore-game-balance
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/design/balance/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/design/balance/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/balance/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/design/balance/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/design-balance-lore/GAME_BALANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/GAME_BALANCE.md
- path: doc/design-balance-lore/design-balance.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/design-balance.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/GOVERNANCE.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28design-balance%29%3A+&body=Document+ID%3A+design-balance%0ALanguage%3A+zh_CN%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：balance

本页是 `design-balance` 的迁移草稿页面。它记录 **2** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `legacy.doc-design-balance-lore-game-balance, design-balance`
- Target: `design/balance.md`
- Replacement: design-balance
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| legacy.doc-design-balance-lore-game-balance | doc/design-balance-lore/GAME_BALANCE.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | design-balance |
| design-balance | doc/design-balance-lore/design-balance.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 平衡文档的用途

CCB 的平衡目标是帮助贡献者在真实性、可读性、风险、资源消耗和长期成长之间作出一致的取舍，
而不是为每个数值规定永远不变的上下限。旧文档中的属性、技能、怪物、武器和资源表格记录了编写
时的参照点；它们可以解释设计意图，但不是当前运行时契约。准备改动时，应以当前 JSON、C++、
测试和实际游戏数据重新建立基线。

### 先确认改动解决什么问题

1. 说明玩家当前遇到的行为、可重复的场景和受影响的进度阶段。
2. 找到实现该行为的 loader、公式、数据对象和测试，而不是只复制一个相似条目的数字。
3. 区分错误修复、内容校准、难度偏好和新机制；它们需要不同证据，也可能需要不同选项或兼容策略。
4. 同时检查资源获取、时间、噪声、负重、耐久、伤害、恢复手段和敌人反制，避免只提高或降低一个数值。
5. 用代表性的早期、中期和后期场景比较修改前后结果，并记录随机性与极端情况。

## 平衡原则

- 真实世界资料用于约束可能范围，但游戏要把复杂系统压缩为玩家能理解和操作的机制。
- 强工具可以保持强；其取舍可以来自稀有度、补给、时间、噪声、重量、暴露或维护，而不必强行让所有选择等效。
- 新敌人和装备应优先创造不同决策，不要只形成生命、护甲与伤害不断上升的数字竞赛。
- 没有预警且无法合理应对的致命结果通常不是有意义的难度。危险应尽量提供可观察线索和可学习的反制。
- 存档与 Mod 兼容属于设计约束。修改 ID、序列化字段、继承关系或广泛使用的数据时必须单独评估迁移影响。

## 证据与验证

设计说明可以提出方向，但不能证明某项行为已经实现。提交平衡改动时，引用当前来源路径和测试，给出
可复现的对比步骤，并运行对应的 JSON 加载、专项单元测试或实际游戏场景。旧表格与旧示例若与当前数据
不一致，应作为历史快照引用，而不是悄悄改写成新的权威表。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`；聚合源指纹为 `1d0054d7999d75ae681f7fa6317b6ee70b8c6bdd8b86a97507c1edf1f974fb51`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/design-balance-lore/GAME_BALANCE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/GAME_BALANCE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/GAME_BALANCE.md)
- [`doc/design-balance-lore/design-balance.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/design-balance.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/design-balance.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
