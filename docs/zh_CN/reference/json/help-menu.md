---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.help-menu
title: 旧文档迁移草稿：help menu
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
- doc/JSON/HELP_MENU.md
- src/help.cpp
- src/help.h
- data/core/help.json
source_symbols:
- help::load
- help::load_object
source_queries: []
source_fingerprint: f183f3f25cca04b29131aec235909008cdcd84abbf61c36866f607c9fb1595c4
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8c2d790827fc56b5aa13090c5e7fc03bad2937e0680f7170a2f641a345d8ad0a
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/help-menu/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/help-menu/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/help-menu/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/help-menu/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/HELP_MENU.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/HELP_MENU.md
- path: src/help.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/help.cpp
- path: src/help.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/help.h
- path: data/core/help.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/core/help.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.help-menu%29%3A+&body=Document+ID%3A+json.help-menu%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：help menu

本页是 `json.help-menu` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.help-menu`
- Target: `reference/json/help-menu.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/help-menu/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.help-menu | doc/JSON/HELP_MENU.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 帮助菜单 JSON

`"type": "help"` 定义可滚动的帮助主题。核心内容位于 `data/core/help.json`；Mod 也可提供
自己的主题。`help::load` 将对象转交 `help::load_object`，后者按 source 分组并在加载顺序中
追加各来源的主题。

每项必须提供整数 `order`、可翻译的 `name` 和可翻译字符串数组 `messages`。`order` 只要求在
同一 source 内唯一；不同 Mod 都可从 0 开始。当前 loader 会对重复 order 报错。核心来源必须
位于核心 JSON 目录，不能把核心帮助伪装成普通 Mod 来源。

消息可使用颜色标记和 `<press_ACTION_ID>` 键位标记。`<DRAW_NOTE_COLORS>` 与
`<HELP_DRAW_DIRECTIONS>` 是 `help.cpp` 处理的特殊占位符。键位 ID 必须来自当前 input action
注册；不要从旧截图或上游文档猜测。新增主题时同时检查翻译抽取、窄终端折行、Tiles/终端显示
和主题顺序，并运行 JSON 加载检查。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `d32b9cc880a85480840d82cfa05d256c78a16615`；聚合源指纹为 `f183f3f25cca04b29131aec235909008cdcd84abbf61c36866f607c9fb1595c4`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/HELP_MENU.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/HELP_MENU.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/HELP_MENU.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
