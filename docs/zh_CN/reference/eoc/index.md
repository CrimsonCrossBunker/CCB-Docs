---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: eoc.reference
title: 旧文档迁移草稿：eoc
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
- doc/JSON/EFFECT_ON_CONDITION.md
- src/effect_on_condition.cpp
- src/condition.cpp
- src/npctalk.cpp
- data/json/effects_on_condition/example_eocs.json
- tests/npc_talk_test.cpp
source_symbols:
- effect_on_condition::load
- effect_on_conditions::load
- conditional_t::conditional_t
source_queries: []
source_fingerprint: 836e4deb077ab0b5c5a2cfb9efb2ec0b95b8c58a163d733bcd2ede0a9ca2363a
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 91a37b8413beefba55c8e53e5557e7db4ae2100b4ec2f467d3049cf8f383c712
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: zihanZheng, LunaGlaze, Anton Simakov, Maleclypse, GuardianDll, thaelina;
  accepted inventory identities only. Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: eoc
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/eoc/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/JSON/EFFECT_ON_CONDITION.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/EFFECT_ON_CONDITION.md
- path: src/effect_on_condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/effect_on_condition.cpp
- path: src/condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/condition.cpp
- path: src/npctalk.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/npctalk.cpp
- path: data/json/effects_on_condition/example_eocs.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/effects_on_condition/example_eocs.json
- path: tests/npc_talk_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tests/npc_talk_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28eoc.reference%29%3A+&body=Document+ID%3A+eoc.reference%0ALanguage%3A+zh_CN%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：eoc

本页是 `eoc.reference` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `eoc.reference`
- Target: `reference/eoc/index.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| eoc.reference | doc/JSON/EFFECT_ON_CONDITION.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 历史与归属

清单中的已接受贡献者为：zihanZheng, LunaGlaze, Anton Simakov, Maleclypse, GuardianDll, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `836e4deb077ab0b5c5a2cfb9efb2ec0b95b8c58a163d733bcd2ede0a9ca2363a`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/EFFECT_ON_CONDITION.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/EFFECT_ON_CONDITION.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/EFFECT_ON_CONDITION.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
