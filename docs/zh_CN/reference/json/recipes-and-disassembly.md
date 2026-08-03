---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.recipes-and-disassembly
title: 旧文档迁移草稿：recipes and disassembly
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
- doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md
- src/recipe.cpp
- src/recipe_dictionary.cpp
- data/json/recipes/armor/other.json
- data/json/uncraft/ammo/10mm.json
- tests/recipe_steps_test.cpp
source_symbols:
- recipe::load
- recipe_dictionary::load
- recipe_dictionary::load_uncraft
source_queries: []
source_fingerprint: 74b3b7fdb8eed201e742fece7ebf19c59fa8f6dfd65fa21b6584d07c1cee067e
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 6f05e14c79ec30b918e5407a271b1589ea1ad396fe06ca836d47b321a5038a2f
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: Anton Simakov, RenechCDDA, dobbry-vechur, dumb-kevin, thaelina; accepted
  inventory identities only. Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/recipes-and-disassembly/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/recipes-and-disassembly/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/recipes-and-disassembly/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/recipes-and-disassembly/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md
- path: src/recipe.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/recipe.cpp
- path: src/recipe_dictionary.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/recipe_dictionary.cpp
- path: data/json/recipes/armor/other.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/recipes/armor/other.json
- path: data/json/uncraft/ammo/10mm.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/uncraft/ammo/10mm.json
- path: tests/recipe_steps_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tests/recipe_steps_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.recipes-and-disassembly%29%3A+&body=Document+ID%3A+json.recipes-and-disassembly%0ALanguage%3A+zh_CN%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：recipes and disassembly

本页是 `json.recipes-and-disassembly` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.recipes-and-disassembly`
- Target: `reference/json/recipes-and-disassembly.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/recipes-and-disassembly/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.recipes-and-disassembly | doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB 配方与拆解模型

配方由 `recipe_dictionary` 注册并交给 `recipe::load`。当前 loader 区分 `recipe`、
`uncraft`、`practice` 和 `nested_category`；它们共享部分字段，但 ID 生成、必填字段、
学习方式和结果语义不同。不要把普通 crafting 示例直接改一个 `type` 就当成有效 uncraft。

### 普通 crafting recipe

```jsonc
{
  "type": "recipe",
  "result": "ccb_example_part",
  "category": "CC_OTHER",
  "subcategory": "CSC_OTHER_PARTS",
  "skill_used": "fabrication",
  "difficulty": 1,
  "time": "10 m",
  "activity_level": "LIGHT_EXERCISE",
  "autolearn": true,
  "qualities": [ { "id": "HAMMER", "level": 1 } ],
  "components": [ [ [ "scrap", 2 ] ] ]
}
```

普通 recipe 通常以 `result` 构造 recipe ID；`variant`/`id_suffix` 会改变最终 ID。
`category` 与 `subcategory` 是普通 recipe 的必填展示分类。字段是否允许继承、默认值和
范围以 loader 为准。

### requirement 的嵌套含义

`components`、`tools` 和 `qualities` 是“若干必须满足的组”；每组内部可以包含替代项。
`using` 引用一个具名 `requirement` 及倍率，适合复用 soldering/welding 等组合。方括号
层级决定 AND/OR，错误嵌套可能改变资源需求而不是立刻报语法错。对复杂配方要检查：

- 替代项是否真的是 OR；
- 数量、charges 和 `LIST` requirement 倍率；
- `NO_RECOVER`/`UNRECOVERABLE` 对拆解回收的影响；
- 重叠 alternatives 是否让可制作性计算过于复杂。

### step recipe

含 `steps` 的配方由每个 step 定义阶段工具、qualities、proficiencies、时间与活动强度。
当前 loader 禁止 step recipe 在根级再写 `tools`、`qualities`、`proficiencies`、
`batch_time_factors`、`time` 或 `activity_level`；空 `steps` 也会报错。根级 `using` 和
components 有专门聚合规则，修改继承配方时必须运行 recipe-step 测试。

### uncraft 与 reversible

```jsonc
{
  "type": "uncraft",
  "result": "ccb_example_part",
  "time": "5 m",
  "activity_level": "LIGHT_EXERCISE",
  "components": [ [ [ "scrap", 1 ] ] ]
}
```

`uncraft` 进入独立字典并被标记为可逆拆解。普通 recipe 的 `reversible: true` 会从制作
信息产生拆解；对象形式可覆盖拆解时间。当前 loader 明确拒绝 reversible recipe 同时
拥有 `byproducts` 或 `byproduct_group`。设计拆解时还要人工审查质量守恒、生成数量、
工具合理性、世界生成物与玩家制作物的差异，以及同一结果的重复拆解定义。

### 继承和加载

`recipe_dictionary::load` 在 `copy-from` 父 recipe 尚未出现时延迟加载，找到父项后复制，
再调用 `recipe::load`。内联 requirement 会重新建立；step、tools/components、using 的
继承有专门规则。不要假定它与 generic `ITEM` 继承完全相同。

### 验证清单

1. 确认 result、recipe ID、category/subcategory 和所有 item/skill/quality/requirement ID。
2. 运行 JSON formatter 与 `make -j2 json-check`。
3. step 或 copy-from 变化运行 `recipe_steps_test` 相关用例。
4. Mod 运行实际 Mod 集的 `--check-mods`，确认依赖和加载顺序。
5. 在游戏/测试中检查可制作性、批量时间、产物/副产物、拆解回收和质量守恒。

加载成功只证明结构可读，不证明配方不会复制资源、产生不可达 recipe 或破坏平衡。

## 历史与归属

清单中的已接受贡献者为：Anton Simakov, RenechCDDA, dobbry-vechur, dumb-kevin, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`；聚合源指纹为 `74b3b7fdb8eed201e742fece7ebf19c59fa8f6dfd65fa21b6584d07c1cee067e`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/ITEM_CRAFT_AND_DISASSEMBLY.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
