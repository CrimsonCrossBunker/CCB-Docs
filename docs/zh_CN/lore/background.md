---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: lore-background
title: 旧文档迁移草稿：background
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
- doc/design-balance-lore/lore-background.md
- doc/design-balance-lore/lore.md
- data/json/snippets/epilogue_factions.json
source_symbols: []
source_queries: []
source_fingerprint: 4ef53651276a51dbf6890808327b57987bf5db1c1d12cdd8d23431b6f5686036
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 7bc07248b0996e72932974d3b7b9aded650b7a67af306b2512b1f402f149a616
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/lore/background/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/lore/background/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/lore/background/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/lore/background/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/design-balance-lore/lore-background.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/lore-background.md
- path: doc/design-balance-lore/lore.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/lore.md
- path: data/json/snippets/epilogue_factions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/snippets/epilogue_factions.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28lore-background%29%3A+&body=Document+ID%3A+lore-background%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：background

本页是 `lore-background` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `lore-background`
- Target: `lore/background.md`
- Replacement: lore-background
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| lore-background | doc/design-balance-lore/lore-background.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 剧透与权威边界

本页面向需要编写世界观、任务、地图和物品的贡献者，包含核心剧透。CCB 通常通过报纸、日志、对话、
地点和不可靠叙述者让玩家拼出事件；不要把开发者全知时间线直接塞进玩家文本。旧年份与链接是固定
commit 的写作背景，实际可发现内容以当前 JSON、地图、任务和对话为准。

## 大灾变背景

美国的秘密跨维度研究逐渐发展为 XEDRA 体系。研究者从 netherum 带回被称为 `XE-037` 的异常物质；
它逃逸并在全球环境中扩散，影响生物、促成暴力与死亡后的复活。社会已经在感染、骚乱和错误应对中
崩溃时，portal storms 进一步撕开维度边界，异界存在和机会主义势力进入。游戏开始时，有组织的全球
救援已经失败，幸存者面对的是污染、亡者、外来生态与残留人类制度共同作用的世界。

这份摘要描述写作框架，不声明所有角色都知道原因，也不要求每条线索完全准确。`XE-037`、Blob、
portal technology、XEDRA 与各外来势力之间的真实关系应分层揭示；普通幸存者、政府记录、研究人员和
非人实体拥有不同且可能冲突的信息。

## 写作连续性检查

为新内容标明叙述者、事件相对时间、其能获得的信息和不确定点。优先复用当前 snippet、faction、mission、
location 与 item ID，并检查日期生成规则、季节、世界创建时间和 CCB 特有差异。区分后台 canon、当前已
实现线索和未来设计；未实现设想保持 draft。运行 JSON/EOC 加载及目标内容测试，并在 PR 中列出会改变
现有任务、存档或 Mod 假设的 lore retcon。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `4ef53651276a51dbf6890808327b57987bf5db1c1d12cdd8d23431b6f5686036`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/design-balance-lore/lore-background.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/lore-background.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/lore-background.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
