---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: mod-compatibility
title: 旧文档迁移草稿：compatibility
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
- doc/MOD_COMPATIBILITY.md
- src/mod_manager.cpp
- src/init.cpp
- build-scripts/get_all_mods.py
- data/mods/MindOverMatter/mod_interactions/innawood/recipes.json
source_symbols:
- DynamicDataLoader::load_mod_interaction_files_from_path
source_queries: []
source_fingerprint: a6292cdc302f2b5da18a35a4d344c24efcc9d87334783f56b2f9ece64b4736c2
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8093f4f712856a40b6760cd4dc87c54cf9d5924936ccf5460b99e36555e42bdd
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
risk_group: mods
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/modding/compatibility/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/modding/compatibility/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/modding/compatibility/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/modding/compatibility/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/MOD_COMPATIBILITY.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/MOD_COMPATIBILITY.md
- path: src/mod_manager.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/mod_manager.cpp
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/init.cpp
- path: build-scripts/get_all_mods.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/build-scripts/get_all_mods.py
- path: data/mods/MindOverMatter/mod_interactions/innawood/recipes.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/mods/MindOverMatter/mod_interactions/innawood/recipes.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28mod-compatibility%29%3A+&body=Document+ID%3A+mod-compatibility%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：compatibility

本页是 `mod-compatibility` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `mod-compatibility`
- Target: `modding/compatibility.md`
- Replacement: mod-compatibility
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| mod-compatibility | doc/MOD_COMPATIBILITY.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Mod 条件兼容数据

`mod_interactions/` 允许一个 Mod 只在另一个指定 Mod 已启用时加载补丁。它适合跨 Mod
引用、兼容 EOC、联合配方或定向覆盖，不等于一般依赖：interaction 缺席时基础 Mod 仍应
能够独立加载。

### 目录约定

假设当前 Mod ID 为 `xedra_evolved`，只在 `mindovermatter` 启用时需要加载兼容文件：

```text
Xedra_Evolved/
├── modinfo.json
├── ordinary-content.json
└── mod_interactions/
    └── mindovermatter/
        └── mom-compat-data.json
```

目录名必须与目标 Mod 的 ID 大小写精确一致。普通加载会递归排除整个
`mod_interactions`；所有活跃 Mod 的普通内容结束后，loader 再按活跃 Mod 顺序处理交互
目录。当前实现只检查第一层目标 ID，不支持用 `a/b/` 表达“两个 Mod 同时存在”。

### 来源与覆盖边界

交互文件的 source 标记为 `base_mod#target_mod`，例如
`xedra_evolved#mindovermatter`。`#` 因此保留给组合来源，普通 Mod ID 禁止包含该字符。
错误日志和对象 provenance 应保留这个组合来源。

交互内容在普通数据之后加载，允许 loader 支持的覆盖/扩展，但不能假定每种 object type
具有相同 merge 语义。对 `copy-from`、`extend`、重复 ID 或 delete/obsolete，必须检查
具体 factory/loader；后加载也不能修复 finalize 前已被强制解析的无效引用。

### 多 Mod 条件

需要 A 与 B 同时存在时，不要构造嵌套目录。可选择由其中一个 interaction 加载一个
兼容 EOC，再在当前注册表允许的条件中检查另一个功能；或者建立显式兼容 Mod，并声明
`dependencies`。选择取决于“缺一方时是否仍应可用”和已发布 ID 的归属。

### 验证矩阵

至少验证：仅基础 Mod、仅目标 Mod、两者同时启用、顺序/依赖被解析后的组合，以及含相关
旧存档的加载。运行 formatter、`make -j2 json-check` 和每个组合的 `--check-mods`；同时
检查重复 ID、source 诊断、EOC talker/context、保存/重载和移除任一 Mod 后的行为。

只测试“两者同时启用”会漏掉 interaction 内容意外进入基础加载或基础文件偷偷依赖目标
Mod 的问题。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `a6292cdc302f2b5da18a35a4d344c24efcc9d87334783f56b2f9ece64b4736c2`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/MOD_COMPATIBILITY.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/MOD_COMPATIBILITY.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/MOD_COMPATIBILITY.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
