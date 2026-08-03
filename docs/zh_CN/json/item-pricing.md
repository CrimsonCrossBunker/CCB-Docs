---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json-item-pricing
title: 旧文档迁移草稿：item pricing
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
- doc/design-balance-lore/POSTAPOC_PRICE_GUIDE.md
- src/faction.cpp
- tests/faction_price_rules_test.cpp
- data/json/npcs/factions.json
source_symbols: []
source_queries: []
source_fingerprint: 6e687bb603c8a92394e06cdc39e80d341da61ee4daeac7c98fab49da2017137b
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 195ec7162ac75a5168d727bfaf57fd33a59b6490c18957d320aa72a90ad20570
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/json/item-pricing/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/item-pricing/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/item-pricing/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/item-pricing/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/design-balance-lore/POSTAPOC_PRICE_GUIDE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/POSTAPOC_PRICE_GUIDE.md
- path: src/faction.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/faction.cpp
- path: tests/faction_price_rules_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/faction_price_rules_test.cpp
- path: data/json/npcs/factions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/npcs/factions.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json-item-pricing%29%3A+&body=Document+ID%3A+json-item-pricing%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：item pricing

本页是 `json-item-pricing` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json-item-pricing`
- Target: `json/item-pricing.md`
- Replacement: json-item-pricing
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json-item-pricing | doc/design-balance-lore/POSTAPOC_PRICE_GUIDE.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Item price 与交易规则

`price` 表示旧世界/基准价格，`price_postapoc` 是末世交易基线；二者都是非负 money unit。
实际 NPC 报价不是简单显示这个值：item 数量、charge/stack size、内容物、买卖方向、NPC 调整、
faction/personal price rules 和 currency 都可能改变结果。

### Faction rules

faction 的 `price_rules` 使用 item/group 等 matcher，并可设置 `markup`、`premium`、
`fixed_adj` 或固定 `price`。consumer 从后向前选择第一条匹配规则；NPC personal rule 可以覆盖
faction rule。声明 `currency` 还会加入该货币的等价交易规则。

因此旧指南中的某种货币锚点、固定价格区间和“单件不得超过某上限”是历史平衡建议，不是 loader
或交易代码强制契约。定价时以当前 CCB faction 数据、相似 item 与实际交易 UI 为准，并说明
可获得性、效用、消耗速度、可替代性和目标阵营。

### Charges 与容器

count-by-charges item 的固定 rule price 与 item base price 会按 stack size/charge 处理；装载的
magazine、ammo 和容器内容也可能计价。不要把整 stack 的 JSON price 当成单 charge，或在 item、
group 和 faction rule 中重复补偿同一因素。

### 验证

运行 formatter、`make -j2 json-check` 和 Mod `--check-mods`。为新 rule 覆盖 NPC 买/卖两个方向、
currency、conditional matcher、personal override、charge stack 与 contents；扩展
`tests/faction_price_rules_test.cpp`。平衡合理性由 Responsible human 审查，代码测试只证明计算
符合契约。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `6e687bb603c8a92394e06cdc39e80d341da61ee4daeac7c98fab49da2017137b`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/design-balance-lore/POSTAPOC_PRICE_GUIDE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/POSTAPOC_PRICE_GUIDE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/POSTAPOC_PRICE_GUIDE.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
