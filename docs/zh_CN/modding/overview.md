---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: modding-overview
title: 旧文档迁移草稿：overview
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
- doc/MODDING.md
- src/mod_manager.cpp
- src/init.cpp
- src/game_io.cpp
- build-scripts/get_all_mods.py
source_symbols:
- DynamicDataLoader::load_mod_interaction_files_from_path
- game::load_mod_interaction_data_from_dir
source_queries: []
source_fingerprint: 01df11ed2410a7436b91d317d9a7b0843f550d730255abb4d6c637526c226e9b
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 282f94915ba860bf09fdbb701cd3a92f97884276900d172ec57a5516aaecc0c2
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: SpinosaurusBoat, thaelina; accepted inventory identities only. Source
  paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: mods
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/modding/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/modding/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/modding/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/modding/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/MODDING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/MODDING.md
- path: src/mod_manager.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/mod_manager.cpp
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/init.cpp
- path: src/game_io.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/game_io.cpp
- path: build-scripts/get_all_mods.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/build-scripts/get_all_mods.py
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28modding-overview%29%3A+&body=Document+ID%3A+modding-overview%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：overview

本页是 `modding-overview` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `modding-overview`
- Target: `modding/overview.md`
- Replacement: modding-overview
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| modding-overview | doc/MODDING.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB Mod 模型

CCB Mod 是一个带 `MOD_INFO` 的数据包。运行时先解析可用 Mod、依赖与冲突，再按世界保存的
顺序加载 JSON；普通数据全部加载后，才加载命中的 `mod_interactions/`。JSON、EOC 与 Lua
可以并存，但各自仍受 loader、Schema、注册表和 Lua v5 契约约束。

### 最小目录

```text
ccb_example/
├── modinfo.json
├── items.json
└── lua/
    └── manifest.json   # 仅在使用 Lua 时需要
```

```jsonc
[
  {
    "type": "MOD_INFO",
    "id": "ccb_example",
    "name": "CCB Example",
    "authors": [ "Example author" ],
    "maintainers": [ "github-account" ],
    "description": "A small example Mod.",
    "category": "content",
    "dependencies": [ "dda" ]
  }
]
```

`id` 是世界 Mod 列表、依赖、交互目录与来源追踪使用的稳定标识，不能把改名当成显示文本
清理。当前 `MOD_INFORMATION` 还读取 `path`、`version`、`conflicts`、`core`、`obsolete`、
`loading_images` 与 `disable_other_loading_screens`。不要从旧表猜字段；以
`mod_manager::load_modfile` 和相邻第一方 `modinfo.json` 为准。Mod 不得依赖自身，`#` 也不是
合法 Mod ID 字符。

### 数据、依赖和加载顺序

普通 JSON 在 Mod 路径下递归发现，`mod_interactions` 延后处理，`lua/manifest.json` 不交给
JSON object loader。`dependencies` 表示必须先加载的 Mod；`conflicts` 用于阻止不兼容组合。
依赖只决定可用性和顺序，不会自动为被引用 ID 提供迁移，也不会替代显式兼容文件。

把对象按领域拆文件，而不是按加载顺序拆文件。Forward reference 只在相应 loader 明确支持
时成立。已发布 item、terrain、EOC、Lua service 等 ID 可能进入存档或其他 Mod；删除或
改名时必须检查 obsoletion/migration 机制与旧世界加载。

### 选择表达层

- 静态内容、配方、地图和注册对象优先用 JSON。
- 条件、效果、事件链与对话流程优先考虑 EOC。
- Lua 用于公开 Lua v5 契约允许的动态逻辑，并声明精确 capability。
- 只有公开数据契约无法表达且项目愿意维护该能力时才改 C++。

### 最小验证闭环

1. 用仓库 formatter 格式化改动 JSON，并运行 `make -j2 json-check`。
2. 用已构建游戏执行 `./cataclysm-tiles --check-mods ccb_example`（实际二进制名随构建而异）。
3. EOC 覆盖 true/false、talker、context 与重复执行；Lua 运行 manifest、语法、coverage 和示例检查。
4. 创建世界、保存、重新加载，并测试与声明依赖/冲突的真实组合。
5. PR 记录命令、平台、Mod 集、失败和未运行项；加载成功不等于玩法平衡或存档兼容。

配套阅读：[Mod 兼容](compatibility.md)、[Mod 本地化](localization.md)与
[仓库内 Mod 政策](../mods/in-repository-policy.md)。

## 历史与归属

清单中的已接受贡献者为：SpinosaurusBoat, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `01df11ed2410a7436b91d317d9a7b0843f550d730255abb4d6c637526c226e9b`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/MODDING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/MODDING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/MODDING.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
