---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: content.firearms-naming-and-inclusion
title: 旧文档迁移草稿：naming and inclusion
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
- doc/GUN_NAMING_AND_INCLUSION.md
- tools/json_tools/gun_variant_validator.py
- tools/json_tools/generic_guns_validator.py
- data/json/items/gun/9mm.json
source_symbols:
- guns_are_similar
- check_identifiers
- check_names
source_queries: []
source_fingerprint: 1adfadb4e99f418c3fcacd1f0e95ffa6ee336f08429efc710bc97bfffc1a6174
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: fb6a7bc1f8bf1be8dedd90162d55a97164d467a6de4fcfb6f1e005518f3705fc
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/content/firearms/naming-and-inclusion/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/content/firearms/naming-and-inclusion/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/content/firearms/naming-and-inclusion/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/content/firearms/naming-and-inclusion/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/GUN_NAMING_AND_INCLUSION.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/GUN_NAMING_AND_INCLUSION.md
- path: tools/json_tools/gun_variant_validator.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tools/json_tools/gun_variant_validator.py
- path: tools/json_tools/generic_guns_validator.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tools/json_tools/generic_guns_validator.py
- path: data/json/items/gun/9mm.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/items/gun/9mm.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28content.firearms-naming-and-inclusion%29%3A+&body=Document+ID%3A+content.firearms-naming-and-inclusion%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：naming and inclusion

本页是 `content.firearms-naming-and-inclusion` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `content.firearms-naming-and-inclusion`
- Target: `content/firearms/naming-and-inclusion.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/content/firearms/naming-and-inclusion/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| content.firearms-naming-and-inclusion | doc/GUN_NAMING_AND_INCLUSION.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 为什么要限制独立枪械条目

真实枪械型号很多，但在游戏建模精度内，多个型号可能拥有几乎相同的玩家决策。把每个型号都做成独立
item 会增加平衡、掉落、弹药、弹匣、翻译和维护成本，同时让不熟悉型号的玩家难以看出武器类别及兼容
配件。优先选择能表达有意义机械差异的基础枪械；仅有品牌、外观或很小的尺寸差异时使用 variant。

旧文档的市场数量门槛、口径总数和相似度数字是当时的政策快照。当前可执行规则以
`tools/json_tools/gun_variant_validator.py` 和 `generic_guns_validator.py` 为准。前者读取继承后的 gun 与
magazine 数据，并检查可合并项、名称和共同 identifier；其字段、容差、blacklist 与 descriptor 会变化，
不要把本页复制成第二套规则。

## 命名与兼容性

- 默认显示名应让普通玩家看出武器角色，如 pistol、rifle、shotgun 或 launcher，而不是只显示不可解释的
  字母数字型号。
- 枪械与非通用弹匣/speedloader 应共享能帮助玩家匹配的有效 identifier；口径、“magazine”等通用词不能
  单独证明关系。
- 品牌 variant 可保留真实世界差异，但不能悄悄改变基础 item 的机械字段。
- 新条目必须记录现实来源、地区/时代可获得性、生产与流通证据以及许可证安全的描述；不要复制厂商文案或图片。

## 提交流程

从当前相同 ammo、magazine 和角色的枪械开始，比较继承后的 modes、pockets、尺寸、重量、barrel、dispersion、
reload 与 damage 等字段。若 validator 判定相似，默认做 variant；若必须独立，PR 要解释玩家可感知差异并附
可审核证据。运行 JSON formatting/loading、gun variant validator、Generic Guns validator 和相关 item/ammo
测试，同时检查 spawn group、迁移 ID、名称翻译与 Mod 兼容。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `1adfadb4e99f418c3fcacd1f0e95ffa6ee336f08429efc710bc97bfffc1a6174`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/GUN_NAMING_AND_INCLUSION.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/GUN_NAMING_AND_INCLUSION.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/GUN_NAMING_AND_INCLUSION.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
