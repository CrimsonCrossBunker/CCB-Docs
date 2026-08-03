---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: mods.aftershock-exoplanet.lore.organizations
title: 旧文档迁移草稿：organizations
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
- data/mods/aftershock_exoplanet/doc/lore/cyberpunk_future.md
- data/mods/aftershock_exoplanet/doc/lore/organizations.md
- data/mods/aftershock_exoplanet/doc/lore/timeline.md
- data/mods/aftershock_exoplanet/modinfo.json
source_symbols: []
source_queries: []
source_fingerprint: 51029512a57df1784b9f962178ee29540e8fcd0875af7f8b649a2994a069341d
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 81904c5aed067809b8aebcbf5501ba0af347eccd8d090bee64d9c640295c5ead
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- mods.aftershock-exoplanet.lore.cyberpunk-future
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: mods
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/data/mods/aftershock_exoplanet/doc/lore/organizations/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/data/mods/aftershock_exoplanet/doc/lore/organizations/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/data/mods/aftershock_exoplanet/doc/lore/organizations/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/data/mods/aftershock_exoplanet/doc/lore/organizations/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: data/mods/aftershock_exoplanet/doc/lore/cyberpunk_future.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/mods/aftershock_exoplanet/doc/lore/cyberpunk_future.md
- path: data/mods/aftershock_exoplanet/doc/lore/organizations.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/mods/aftershock_exoplanet/doc/lore/organizations.md
- path: data/mods/aftershock_exoplanet/doc/lore/timeline.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/mods/aftershock_exoplanet/doc/lore/timeline.md
- path: data/mods/aftershock_exoplanet/modinfo.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/mods/aftershock_exoplanet/modinfo.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28mods.aftershock-exoplanet.lore.organizations%29%3A+&body=Document+ID%3A+mods.aftershock-exoplanet.lore.organizations%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：organizations

本页是 `mods.aftershock-exoplanet.lore.organizations` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `mods.aftershock-exoplanet.lore.cyberpunk-future`
- Target: `data/mods/aftershock_exoplanet/doc/lore/organizations.md`
- Replacement: mods.aftershock-exoplanet.lore.organizations
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| mods.aftershock-exoplanet.lore.cyberpunk-future | data/mods/aftershock_exoplanet/doc/lore/cyberpunk_future.md | merge_into | stubbed | 5f23722ff28c5cc552baa0422b32b1f10fd890fa | mods.aftershock-exoplanet.lore.organizations |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 与 CCB 主世界观分离

Aftershock: Exoplanet 是 `aftershock_exoplanet` total-conversion Mod，地点、年代、组织和技术史属于其
Salus IV 设定，不能自动套用到 CCB 主游戏。`modinfo.json` 定义真实 Mod ID、依赖和冲突；本页合并旧
`cyberpunk_future.md` 的组织信息，并取代它作为组织写作入口。

## 历史框架

人类在 Hyperspace Expansion 建立跨星际文明和依赖 hypercomm 的强 AI。2152 年 Discontinuity 使该基础
设施突然失效，殖民地、知识和供应链大量消亡。数百年后，较弱的 FTL 被重新建立，UICA 与 Solar
Corporations 开始 Reclamation；2430 年玩家抵达被隔离的 Salus IV。不同叙述者对早期历史只能拥有破碎、
矛盾的记录。

### 组织写作边界

- **UICA** 是政府、公司与 NGO 的松散协调体，其“回收殖民地”目标同时包含外交、军事和旧所有权冲突。
- **Solar Corporation** 控制跨行星工业、航运或殖民资产，不应把任何有飞船的普通公司都升级成这一层级。
- TsKBEM、Mercurial Genomics、Wraitheon、Palver-Shikishima 及小型公司各有不同历史、能力、公开形象和
  隐藏利益；不要只换名称复用同一公司人格。
- PrepNet 等群体不是传统公司/政府，应从定居方式、互助规则和对第二次 Discontinuity 的预期书写。

新增组织时记录时代、地理范围、资产、依赖、内部派别、对 Salus IV 的利益和玩家可获取的证据。把作者
后台真相、游戏内传闻、当前实现和未来计划分开。复用当前 faction、item、snippet、mission 与 mapgen ID，
运行目标 Mod JSON/EOC 加载和引用检查；不要让主游戏内容意外依赖 total-conversion ID。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `51029512a57df1784b9f962178ee29540e8fcd0875af7f8b649a2994a069341d`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`data/mods/aftershock_exoplanet/doc/lore/cyberpunk_future.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/mods/aftershock_exoplanet/doc/lore/cyberpunk_future.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/mods/aftershock_exoplanet/doc/lore/cyberpunk_future.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
