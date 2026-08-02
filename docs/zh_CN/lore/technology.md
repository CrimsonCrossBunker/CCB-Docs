---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: lore-technology
title: 旧文档迁移草稿：technology
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
- doc/design-balance-lore/technology.md
- doc/design-balance-lore/lore.md
- data/json/materials.json
source_symbols: []
source_queries: []
source_fingerprint: cf792ec1d56aa4d6f5a0efbea73bc7d7269987b7cf5ea1aa4062810c965350fb
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: fe0b3354ffe9609a020494c599f716f13a38719d1d63f4a7b436e9905efc0ca8
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/lore/technology/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/lore/technology/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/lore/technology/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/lore/technology/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/design-balance-lore/technology.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/technology.md
- path: doc/design-balance-lore/lore.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/lore.md
- path: data/json/materials.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/materials.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28lore-technology%29%3A+&body=Document+ID%3A+lore-technology%0ALanguage%3A+zh_CN%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：technology

本页是 `lore-technology` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `lore-technology`
- Target: `lore/technology.md`
- Replacement: lore-technology
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| lore-technology | doc/design-balance-lore/technology.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 技术基线

CCB 灾前地球原则上保持现代现实世界可辨认的技术水平。偏离点应当狭窄、有来源，并与 portal research、
XEDRA 或明确的外来技术相连；若某项发明会让整个灾前社会完全不同，通常应缩小或重写设定，而不是把
世界整体升级成通用科幻背景。

### 技术层次

- **民用与普通工业**主要遵循现实能力、供应链和成本。更普及的 fuel cell 或动力辅助仍不等于随处可见的超科技。
- **军事与 XEDRA**可拥有稀有能源、power armor、机器人、实验武器、portal 和 dimensional heuristics，
  但其数量、可靠性和用途受项目、设施与保密限制。
- **Mutation**利用普遍的 Blob 污染，不是普通基因工程；其可见行为仍由当前 mutation 数据和代码定义。
- **CBM/Exodii**来自跨维度幸存者体系。常见功能应尽量能用现代原理解释，神奇部分集中在接口、制造遗产和
  少数受剧情限制的装置。
- **Mi-go、Yrax、triffid、Blob 等技术或能力**可能超出人类理解。越不可思议，玩家越不应能像普通机械一样
  拆成通用零件、重新设计或量产。

## 为内容选择技术

先说明谁制造、何时制造、为何存在、能源与材料来自哪里、能否维护，以及灾后为何还能获得。区分原型、
有限部署和量产物；实验设备需要合理的故障、操作和供应限制。显示名或 lore 不能证明 item 的实际性能，
应追踪当前 JSON、recipe、item use、mapgen、faction 与 tests。

旧页面的技术等级图与具体 lore 解释是写作模型，不是 API。新增或修改设备时检查来源、掉落密度、维修、
拆解、弹药/电池、技能、NPC 获取、存档与 Mod 兼容，并运行相应 JSON 加载和专项测试。尚未实现的 Yrax
或其他章节保持 draft。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `cf792ec1d56aa4d6f5a0efbea73bc7d7269987b7cf5ea1aa4062810c965350fb`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/design-balance-lore/technology.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/technology.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/technology.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
