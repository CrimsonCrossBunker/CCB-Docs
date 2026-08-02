---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: design.frequently-made-suggestions
title: 旧文档迁移草稿：frequently made suggestions
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
- doc/FREQUENTLY_MADE_SUGGESTIONS.md
- GOVERNANCE.md
- README.md
source_symbols: []
source_queries: []
source_fingerprint: 1ce8e96664cf785d8ebe4739b45940e2ccf0febc6b7e53ec213b0fa807e34ef7
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 4ce36a9c5056a35d5e2db3eef731b86239dec6ccdcd4b8dfb4b47439373295ed
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LunaGlaze, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: design
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/design/frequently-made-suggestions/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/design/frequently-made-suggestions/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/frequently-made-suggestions/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/design/frequently-made-suggestions/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/FREQUENTLY_MADE_SUGGESTIONS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/FREQUENTLY_MADE_SUGGESTIONS.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/GOVERNANCE.md
- path: README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/README.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28design.frequently-made-suggestions%29%3A+&body=Document+ID%3A+design.frequently-made-suggestions%0ALanguage%3A+zh_CN%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：frequently made suggestions

本页是 `design.frequently-made-suggestions` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `design.frequently-made-suggestions`
- Target: `design/frequently-made-suggestions.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/design/frequently-made-suggestions/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| design.frequently-made-suggestions | doc/FREQUENTLY_MADE_SUGGESTIONS.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 这不是实时功能状态表

旧“常见建议”把多年间的功能状态、个人意见、上游链接和具体数值混在一页。那些答案只能说明当时的
讨论，不能证明 CCB 当前已经实现、正在开发、拒绝或只允许 Mod。功能状态应从当前源码、Issue、PR、
路线图和维护者决定重新确认；治理以 `GOVERNANCE.md` 为准，不以旧页面中的人员描述或激烈措辞为准。

## 提建议前的快速检查

1. 搜索 CCB 当前 Issue、PR、源码注册和 CCB-Docs，确认问题仍存在且没有并行实现。
2. 描述玩家需求和可复现场景，而不是只给出功能名或要求投票。
3. 说明与世界设定、设计原则、平台、性能、存档和 Mod 兼容的关系。
4. 比较更小的方案：已有 EOC/JSON/Lua 能否实现、是否适合作为第一方或第三方 Mod、是否需要新运行时能力。
5. 列出维护成本，包括 UI、翻译、测试矩阵、数据迁移、生成内容和长期负责人。
6. 若愿意实现，先提交范围清楚的设计 Issue；获得方向反馈后再准备最小 PR 和验证证据。

## 常见判断原则

- “已有一个类似例外”不能单独证明应增加另一个；旧内容也可能需要修正。
- 现实可行不等于灾后单个角色能以现有工具、知识、时间和风险完成。
- 新选项并非免费：每个分支都会增加代码、文档、翻译、兼容和测试负担。
- 内容建议通常更适合用实际 JSON/Mod 原型证明；但原型仍需符合许可证、来源和项目方向。
- 技术困难不是永久拒绝，愿望也不是已承诺路线。记录依赖、当前缺口和可验证的下一步。

当结论可能影响项目政策或大量玩家时，由当前维护者通过可审阅的 Issue/PR 决策。页面应链接该决定和
适用 commit，并在来源变化时标记 stale，避免把一次讨论永久化。

## 历史与归属

清单中的已接受贡献者为：LunaGlaze, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `1ce8e96664cf785d8ebe4739b45940e2ccf0febc6b7e53ec213b0fa807e34ef7`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/FREQUENTLY_MADE_SUGGESTIONS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/FREQUENTLY_MADE_SUGGESTIONS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/FREQUENTLY_MADE_SUGGESTIONS.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
