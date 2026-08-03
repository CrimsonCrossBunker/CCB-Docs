---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.comestibles-placement
title: 旧文档迁移草稿：comestibles
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
- doc/JSON/GUIDE_COMESTIBLES.md
- src/item_factory.cpp
- data/json/items/comestibles/other.json
- data/json/items/comestibles/meat_dishes.json
- tests/comestible_test.cpp
source_symbols:
- islot_comestible::deserialize
- itype::load
source_queries: []
source_fingerprint: 4e0d6d98ef0567ed4fc3da0e7e0b957671a0c2d28e3af279c3a43753fcc9c043
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 74891d63236510622eb5589ce574969dc0ee38862e666e0b1ef04b184fc60960
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/json/comestibles/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/json/comestibles/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/how-to/json/comestibles/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/json/comestibles/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/GUIDE_COMESTIBLES.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/GUIDE_COMESTIBLES.md
- path: src/item_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/item_factory.cpp
- path: data/json/items/comestibles/other.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/items/comestibles/other.json
- path: data/json/items/comestibles/meat_dishes.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/items/comestibles/meat_dishes.json
- path: tests/comestible_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/comestible_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.comestibles-placement%29%3A+&body=Document+ID%3A+json.comestibles-placement%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：comestibles

本页是 `json.comestibles-placement` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.comestibles-placement`
- Target: `how-to/json/comestibles.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/json/comestibles/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.comestibles-placement | doc/JSON/GUIDE_COMESTIBLES.md | migrate_rewrite | stubbed | b1ee97987589450da70f30ee2feed12c9d18f479 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 新增 comestible 的放置与验证

目录和文件名帮助维护者查找数据，但不改变 `COMESTIBLE` loader 语义。先确认 object 的内容域，
再放入当前 `data/json/items/comestibles/` 中最窄、已有相似项目的文件；不要照抄旧列表中已经删除
或改名的文件。

### 当前分类顺序

优先使用明确领域文件：medicine、mutagen/serum、MRE、brewing、frozen、spice、protein、alien/
netherum 等。普通 drink 区分 alcohol、soup、drink 与 drink_other；solid food 按 baked、bread、
casserole、cereal、dairy、egg、fruit、junkfood、meat/offal、mushroom、nuts、raw produce/grain、
sandwich、seed、veggy、wheat 等现有邻居放置。无法自然归类才用 `other.json`。

分类不是 gameplay tag。需要搜索、recipe、item group 或 effect 行为时，显式声明对应字段和 ID，
不要依赖 path。

### Loader 契约

`comestible_type` 必填。charges 至少为 1（缺省路径可为 0），其余包括 stack size、quench、fun、
stim、health、spoilage、calories、vitamins、addiction、cooks/eats like、cook/smoke result、
consumption EOC 与 contamination。requiredness、默认和 bounds 以
`islot_comestible::deserialize` 为准。

### 验证

找一个当前相似 item 和 recipe，核对 nutrition、portion/charges、container、spoilage、价格、
item group、recipe 结果及翻译。运行 formatter、`make -j2 json-check` 和 Mod `--check-mods`；营养
或加工变化还要运行 focused comestible/recipe tests，确保 ingredients、byproducts、cooks_like 与
`NUTRIENT_OVERRIDE` 的关系合理。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `d32b9cc880a85480840d82cfa05d256c78a16615`；聚合源指纹为 `4e0d6d98ef0567ed4fc3da0e7e0b957671a0c2d28e3af279c3a43753fcc9c043`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/GUIDE_COMESTIBLES.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/GUIDE_COMESTIBLES.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/GUIDE_COMESTIBLES.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
