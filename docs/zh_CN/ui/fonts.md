---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: ui-fonts
title: 旧文档迁移草稿：fonts
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
- doc/user-guides/FONT_OPTIONS.md
- data/fontdata.json
- src/font_loader.cpp
- src/sdl_font.cpp
source_symbols:
- font_loader::load
- font_loader::save
source_queries: []
source_fingerprint: 8efffabac0938483250479a7eeb7d30df373704e07ee9b82ec9bcfca51392efd
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 634558e639cab9730606b4698882130e95db0b9a7009c4f902d5f3657dec09b8
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
risk_group: ui
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/ui/fonts/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/ui/fonts/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/ui/fonts/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/ui/fonts/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/user-guides/FONT_OPTIONS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/user-guides/FONT_OPTIONS.md
- path: data/fontdata.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/fontdata.json
- path: src/font_loader.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/font_loader.cpp
- path: src/sdl_font.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/sdl_font.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28ui-fonts%29%3A+&body=Document+ID%3A+ui-fonts%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：fonts

本页是 `ui-fonts` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `ui-fonts`
- Target: `ui/fonts.md`
- Replacement: ui-fonts
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| ui-fonts | doc/user-guides/FONT_OPTIONS.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Tiles build 字体配置

Tiles build 从用户配置 `fonts.json` 读取四个 fallback chain：`typeface`、`gui_typeface`、
`map_typeface` 与 `overmap_typeface`。每项可为 path 字符串、含 `path` 的对象，或这些项的数组。
数组顺序就是 glyph fallback 顺序；loader 会确保 `data/font/unifont.ttf` 作为最终 fallback。

对象可设置 `hinting` 与 `antialiasing`。当前接受的 hinting 字符串是 `Auto`、`NoAuto`、
`Default`、`Light`、`None`、`Bitmap`。未知值会报告 debug message 后回到 default；不要复制旧文档
中不一致的枚举。关闭 antialiasing 会设置 monochrome/mono-hinting flags。字体 path 相对于当前
运行环境解析，发布包必须实际携带文件并满足字体许可证。

### 迁移与验证

`font_loader::load` 会读取当前配置；不存在时从 legacy/default 路径加载并由
`font_loader::save` 写成规范对象数组。这个写回可能改变用户文件的表示但应保持选择语义。

验证时使用含拉丁、简繁中文、组合字符、宽字符、emoji fallback 和缺失 glyph 的样例；覆盖
四种 screen、不同 DPI/缩放、Bitmap/Light/None、antialiasing on/off 和找不到文件。还要检查
ImGui atlas、地图格子宽高、终端对齐、内存/启动时间和许可证归属。不要只凭配置 JSON 成功解析
就认为字体可用。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `8efffabac0938483250479a7eeb7d30df373704e07ee9b82ec9bcfca51392efd`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/user-guides/FONT_OPTIONS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/user-guides/FONT_OPTIONS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/user-guides/FONT_OPTIONS.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
