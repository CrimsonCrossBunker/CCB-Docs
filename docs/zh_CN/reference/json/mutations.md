---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.mutations
title: 旧文档迁移草稿：mutations
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
- doc/JSON/MUTATIONS.md
- src/mutation_data.cpp
- src/mutation.cpp
- data/json/mutations/mutations.json
- data/json/effects_on_condition/mutation_eocs/changing_eocs.json
- tests/mutation_test.cpp
source_symbols:
- mutation_branch::load
- mutation_category_trait::load
- mutation_variant::load
source_queries: []
source_fingerprint: e4b74d434588fa10a89e1938e43cf2456f9ce60905f66484f8381769a4db16ab
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 54cb350a0c571b1364d8bcc0a57fae40bf009a6da7c1bfbd5598e0ff1299a585
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/mutations/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/mutations/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/mutations/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/mutations/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/JSON/MUTATIONS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/MUTATIONS.md
- path: src/mutation_data.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/mutation_data.cpp
- path: src/mutation.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/mutation.cpp
- path: data/json/mutations/mutations.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/mutations/mutations.json
- path: data/json/effects_on_condition/mutation_eocs/changing_eocs.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/effects_on_condition/mutation_eocs/changing_eocs.json
- path: tests/mutation_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tests/mutation_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.mutations%29%3A+&body=Document+ID%3A+json.mutations%0ALanguage%3A+zh_CN%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：mutations

本页是 `json.mutations` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.mutations`
- Target: `reference/json/mutations.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/mutations/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.mutations | doc/JSON/MUTATIONS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB Mutation 契约

`mutation` 由 `mutation_branch` factory 加载。当前 `mutation_branch::load` 强制读取
`name`、`description` 与 `points`；激活、分类、阈值、装备冲突和 EOC 是叠加在同一个
稳定 trait ID 上的不同子系统。

### 基础定义

```jsonc
{
  "type": "mutation",
  "id": "TRAIT_CCB_EXAMPLE",
  "name": { "str": "Example adaptation" },
  "description": "A documentation-only example.",
  "points": 1,
  "starting_trait": false,
  "purifiable": true,
  "category": [ "MUTCAT_CCB_EXAMPLE" ]
}
```

`points` 是角色创建/评价数据，不等价于突变获取权重。`starting_trait`、
`random_start_allowed`、`valid` 和 `purifiable` 控制不同入口。`variants` 给同一 trait
提供带权名称/描述变化，不创建新的稳定 trait ID。

### 主动、被动与装备关系

主动 mutation 可配置 `cost`、`time` 以及 kcal、thirst、sleepiness、mana、stamina 等资源，
并通过当前 activation/EOC 字段产生效果。`starts_active` 只对可激活 trait 有意义。
reflex activation 的 condition、开关消息和 talker 语义必须按 EOC 条件验证。

`destroys_gear`、`allow_soft_gear`、bodypart/armor 与 enchantment 会改变穿戴、身体结构和
缓存。获得、移除、净化、变体切换与保存重载都可能触发缓存更新；不要只测角色创建界面。

### Category、阈值与关系图

mutation category 是具名注册对象，控制 vitamin、threshold、primer/mutagen 与 category
强度。trait 的 `prereqs`、`prereqs2`、`threshreq`、`cancels`、`replacements` 和 additions
形成有向图。修改任何边都要检查不可达节点、循环、阈值前后替换和 instability 对好坏结果
的影响。

删除或改名公开 trait 时使用当前 `trait_migration` 契约，可替换 trait/variant 或明确移除。
仅在 JSON 中删除旧 ID 会让旧存档和其他 Mod 失去引用。

### 验证

运行 formatter、`make -j2 json-check`、实际 Mod 集 `--check-mods` 和相关
`mutation_test`。覆盖角色创建、mutagen/primer、净化、阈值、坏突变概率、主动 cooldown、
resource 不足、装备冲突、enchantment/cache、NPC 与存档重载。还要检查翻译 variant、
消息参数和 EOC true/false 路径。

旧文档中的化学流程与概率说明会随实现变化；系统解释以当前 mutation 源码和测试为准。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `e4b74d434588fa10a89e1938e43cf2456f9ce60905f66484f8381769a4db16ab`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/MUTATIONS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/MUTATIONS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/MUTATIONS.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
