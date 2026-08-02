---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.basecamp
title: 旧文档迁移草稿：basecamp
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
last_human_reviewer: Pending human review
source_paths:
- doc/JSON/BASECAMP.md
- src/basecamp.cpp
- src/faction_camp.cpp
- src/recipe.cpp
- data/json/recipes/basecamps/components.json
- tests/faction_camp_test.cpp
source_symbols:
- basecamp::available_upgrades
- recipe::load
- basecamp::define_camp
source_queries: []
source_fingerprint: c0cfebafece179418df8534979262e7194922117093218d38658a260291a55f2
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a4989f925e69f00347e77d011cdc91b1e9f99bd556db5080dfeb959791e6cd38
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/basecamp/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/basecamp/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/basecamp/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/basecamp/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/JSON/BASECAMP.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/JSON/BASECAMP.md
- path: src/basecamp.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/basecamp.cpp
- path: src/faction_camp.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/faction_camp.cpp
- path: src/recipe.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/recipe.cpp
- path: data/json/recipes/basecamps/components.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/recipes/basecamps/components.json
- path: tests/faction_camp_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/faction_camp_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.basecamp%29%3A+&body=Document+ID%3A+json.basecamp%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：basecamp

本页是 `json.basecamp` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.basecamp`
- Target: `reference/json/basecamp.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/basecamp/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.basecamp | doc/JSON/BASECAMP.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Basecamp 数据由多份契约组成

Basecamp upgrade 不是单一 object type。它把 blueprint recipe、`update_mapgen`、
`recipe_group`、overmap terrain 和运行时 camp state 组合起来。修改其中一份数据前，先从
`basecamp::available_upgrades`、`recipe::load` 和当前第一方 camp 数据追踪整个 ID 链。

### Blueprint recipe

有 `construction_blueprint` 的普通 recipe 会进入 blueprint 路径。loader 读取
`blueprint_name`、`blueprint_parameter_names`、resources、provides、requires、excludes 与
needs。每个 blueprint 自动 provide 并 exclude 自己的 result，因此通常不可重复。

`blueprint_provides`/`requires`/`excludes` 是带默认 amount 1 的 camp feature 计数，不是全局
feature registry。代码会对部分约定 ID 赋予 mission 或 camp 能力；新字符串只有在 consumer
实际读取时才有语义。不要从旧文档的 keyword 表推断当前完整列表。

### Requirements 与 mapgen

没有 `blueprint_needs` 且 `check_blueprint_needs` 为 true 时，finalize 会从 mapgen 自动计算
需求。带 parameter names 的 blueprint 不能同时依赖显式 needs。`construction_blueprint` 必须
对应可执行的 update mapgen；参数名称必须覆盖玩家可选值并可翻译。

初始 camp 和 expansion 还依赖 recipe group 的 terrain match、对应 OMT 以及 mapgen。声明
dependency 的 Mod 才能安全引用另一 Mod 的 recipe、terrain 或 mapgen ID。

### 验证清单

核对每条 requires/provides/excludes 分支、重复升级阻止、resource item、mapgen 参数和实际
upgrade 后的地图。运行 formatter、`make -j2 json-check`、完整 `--check-mods`，并扩展
`tests/faction_camp_test.cpp` 的 focused case。需要更新计算结果时使用仓库
`tools/update_blueprint_needs.py`，逐项审阅输出，不手抄旧示例。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `c0cfebafece179418df8534979262e7194922117093218d38658a260291a55f2`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/BASECAMP.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/BASECAMP.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/BASECAMP.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
