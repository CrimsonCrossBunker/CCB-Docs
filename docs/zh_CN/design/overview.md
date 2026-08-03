---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: design-overview
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
- doc/design-balance-lore/design-doc.md
- doc/design-balance-lore/design-gameplay.md
- doc/design-balance-lore/design-user-experience.md
- GOVERNANCE.md
source_symbols: []
source_queries: []
source_fingerprint: eb982d8b2e7be2e188715904e8781a98591a7cc158363a5fdbddc0de988920b8
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8ad249321134dc5b3189832038bb4132d2841c6aecc9f58075a703889a0635bb
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/design/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/design/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/design/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/design-balance-lore/design-doc.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/design-doc.md
- path: doc/design-balance-lore/design-gameplay.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/design-gameplay.md
- path: doc/design-balance-lore/design-user-experience.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/design-user-experience.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/GOVERNANCE.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28design-overview%29%3A+&body=Document+ID%3A+design-overview%0ALanguage%3A+zh_CN%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：overview

本页是 `design-overview` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `design-overview`
- Target: `design/overview.md`
- Replacement: design-overview
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| design-overview | doc/design-balance-lore/design-doc.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | design-overview |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 如何使用设计文档

设计文档解释 CCB 为什么偏好某类体验、一个提案需要回答什么问题，以及多个系统发生冲突时应考虑
哪些取舍。它不是运行时、数据格式或项目治理的替代来源。具体行为以源码和测试为准，JSON/Lua/API
以 Schema、声明、注册和生成清单为准，项目决策以当前治理文件为准。

### 提案最小结构

1. **问题**：描述当前玩家体验和可复现场景，不先假定解决方案。
2. **目标与非目标**：说明希望改善的结果以及本次不会改变的范围。
3. **现状**：列出相关入口、数据所有权、生命周期、测试和 CCB 与上游的差异。
4. **方案与替代**：比较玩家可见性、复杂度、性能、可维护性和兼容性。
5. **迁移风险**：检查存档、Mod、ID、序列化、翻译、平台和生成内容。
6. **验收**：给出可以运行的命令、场景和回退条件。

## 决策边界

旧设计文本中的数字、文件路径、人员或尚未实现的机制都只能作为历史上下文。把它们带入新提案前，
必须在当前默认分支重新验证。设计方向发生冲突时，通过 Issue、PR 和当前维护者治理流程记录结论；
不存在由某一位个人的旧声明永久覆盖仓库治理的规则。

## CCB 与上游

上游资料可以说明共同历史和可移植方案，但 CCB 已有自己的运行时差异、内容取向、兼容要求和治理。
提案应标明来源版本，比较当前双方实现，并只移植仍适用于 CCB 的部分。若页面与当前契约冲突，应标记
页面 stale 并修复文档，而不是修改实现去迎合过期说明。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `eb982d8b2e7be2e188715904e8781a98591a7cc158363a5fdbddc0de988920b8`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/design-balance-lore/design-doc.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/design-doc.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/design-doc.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
