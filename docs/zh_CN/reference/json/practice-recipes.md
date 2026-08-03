---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.practice-recipes
title: 旧文档迁移草稿：practice recipes
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
- doc/JSON/PRACTICE_RECIPES.md
- src/recipe.cpp
- src/recipe_dictionary.cpp
- data/json/recipes/practice/computers.json
- tests/crafting_gui_test.cpp
source_symbols:
- recipe_dictionary::load_practice
- recipe::load
source_queries: []
source_fingerprint: 888f1cfe57287eb7ec1eb53c459c19afc0fefb5ce004b25807b1dc2373cb3a9f
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: adbfe9483f3c12cd9272512fcef857cdf0c9a8be325629167a796cf6c7b2a710
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/practice-recipes/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/practice-recipes/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/practice-recipes/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/practice-recipes/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/PRACTICE_RECIPES.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/PRACTICE_RECIPES.md
- path: src/recipe.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/recipe.cpp
- path: src/recipe_dictionary.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/recipe_dictionary.cpp
- path: data/json/recipes/practice/computers.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/recipes/practice/computers.json
- path: tests/crafting_gui_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/crafting_gui_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.practice-recipes%29%3A+&body=Document+ID%3A+json.practice-recipes%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：practice recipes

本页是 `json.practice-recipes` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.practice-recipes`
- Target: `reference/json/practice-recipes.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/practice-recipes/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.practice-recipes | doc/JSON/PRACTICE_RECIPES.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Practice recipes

`type: practice` 使用主 recipe dictionary 和 crafting UI，但不产出正常 result。loader 明确拒绝
`result` 与 `difficulty`，要求 id、name、category、subcategory 和 `practice_data`；description
可选。components、tools、using、skill/proficiency、autolearn/book learn 等共享 recipe 契约，
byproducts/byproduct_group 仍可使用。

### practice_data

`min_difficulty` 没有单独 mandatory 检查，未给时保留结构默认；`max_difficulty` 缺省为
`MAX_SKILL - 1`，`skill_limit` 缺省为 `MAX_SKILL`。实际 recipe difficulty 会按角色 practical
skill 在区间内调整，超过 skill limit 时 UI 标记不再提升。

旧文档建议 `skill_limit <= max_difficulty + 1` 和统一 1 hour 是平衡约定，不是当前 loader bound。
新 recipe 应说明偏离原因，并与同 skill/proficiency 的当前 practice entries 比较。

### 设计与验证

用 `CC_PRACTICE` 和正确 subcategory 保持导航一致。requirements 应代表练习消耗，byproduct 不得
变成规避正常 recipe 的生产路径。proficiency practice 要核对 prerequisites、learning time、focus
和失败/时间 multiplier。

运行 formatter、`make -j2 json-check`、Mod `--check-mods`，在 crafting UI 检查未解锁、低于区间、
区间内、超过 skill limit、缺少 tools/components 与 helper/book 来源。扩展
`tests/crafting_gui_test.cpp` 的 focused case，并验证不会生成 result。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `d32b9cc880a85480840d82cfa05d256c78a16615`；聚合源指纹为 `888f1cfe57287eb7ec1eb53c459c19afc0fefb5ce004b25807b1dc2373cb3a9f`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/PRACTICE_RECIPES.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/PRACTICE_RECIPES.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/PRACTICE_RECIPES.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
