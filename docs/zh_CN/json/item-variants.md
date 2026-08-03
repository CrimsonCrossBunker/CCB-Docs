---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json-item-variants
title: 旧文档迁移草稿：item variants
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
- doc/design-balance-lore/VARIANTS.md
- src/item_factory.cpp
- src/cata_variant.h
- tests/cata_variant_test.cpp
- data/json/artifact/artifact_item_types.json
source_symbols:
- cata_variant
source_queries: []
source_fingerprint: e6e11f897a5007543af3b70f38cedacdaf86f49f07ddb66b0692ee403e21915b
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 85a963cee90361864c6ef46f82350c18726d8b451feebb270889500ddfffa34d
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/json/item-variants/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/item-variants/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/item-variants/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/item-variants/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/design-balance-lore/VARIANTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/VARIANTS.md
- path: src/item_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/item_factory.cpp
- path: src/cata_variant.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/cata_variant.h
- path: tests/cata_variant_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/cata_variant_test.cpp
- path: data/json/artifact/artifact_item_types.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/artifact/artifact_item_types.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json-item-variants%29%3A+&body=Document+ID%3A+json-item-variants%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：item variants

本页是 `json-item-variants` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json-item-variants`
- Target: `json/item-variants.md`
- Replacement: json-item-variants
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json-item-variants | doc/design-balance-lore/VARIANTS.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Item aesthetic variants

item 的 `variants` 是同一 itype 的表现变体，不是另一个 gameplay item。每项必须有稳定 `id`，
并可覆盖 name、description、symbol、color、ascii picture；`weight` 默认 1，`append` 控制说明追加，
`expand_snippets` 控制生成时展开。缺少 name/description 时 finalize 从 base item 继承。

这套 `itype_variant_data` 不等于 C++ 的 `cata_variant` typed value container，二者名称相近但契约
无关。写文档、测试和 source symbol 时必须明确是哪一种。

### 适用边界

variant 只能表达视觉、命名或文字差异，不能改变重量、伤害、营养、armor、pocket、recipe 或
其他玩法统计。需要玩法差异时创建独立 itype、inheritance、snippet/conditional name 或合适的
数据结构。大量细小 variant 会增加翻译和 tileset 成本；每项应有可辨识、可出现的用途。

variant ID 会进入 item instance、spawn、migration 和 serialization 路径。删除或重命名已有 ID
前检查保存兼容与 migration；copy-from 清空或替换 variants 时也要审阅展开结果。

### 验证

运行 formatter、`make -j2 json-check`、Mod `--check-mods`，并实际生成每个 weighted variant。
检查默认继承、translation plural、symbol/color/ascii art、snippet expansion、tileset fallback、
存档 round trip 和旧 ID migration。不要用 `tests/cata_variant_test.cpp` 证明 item variant；应使用
item name/spawn/serialization 的 focused test。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `e6e11f897a5007543af3b70f38cedacdaf86f49f07ddb66b0692ee403e21915b`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/design-balance-lore/VARIANTS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/VARIANTS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/VARIANTS.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
