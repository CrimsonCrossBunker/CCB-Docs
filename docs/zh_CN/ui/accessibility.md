---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: ui-accessibility
title: 旧文档迁移草稿：accessibility
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
- doc/USER_INTERFACE_AND_ACCESSIBILITY.md
- src/options.cpp
- src/newcharacter.cpp
- src/player_difficulty.cpp
source_symbols:
- SCREEN_READER_MODE
source_queries: []
source_fingerprint: 512e14575d0545351f6fd8681a91825b993934d608585186f39da929e79d4405
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 18ea2cb05f369a041d07117a6af7b7b845595176c5bf527b25bc62b4a03e95e4
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/ui/accessibility/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/ui/accessibility/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/ui/accessibility/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/ui/accessibility/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/USER_INTERFACE_AND_ACCESSIBILITY.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/USER_INTERFACE_AND_ACCESSIBILITY.md
- path: src/options.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/options.cpp
- path: src/newcharacter.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/newcharacter.cpp
- path: src/player_difficulty.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/player_difficulty.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28ui-accessibility%29%3A+&body=Document+ID%3A+ui-accessibility%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：accessibility

本页是 `ui-accessibility` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `ui-accessibility`
- Target: `ui/accessibility.md`
- Replacement: ui-accessibility
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| ui-accessibility | doc/USER_INTERFACE_AND_ACCESSIBILITY.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## UI 与无障碍契约

CCB 同时存在 curses/tiles 窗口、`ui_adaptor` 与 ImGui UI。修改界面前先确认具体 screen 的
重绘、resize、输入与焦点路径；不要假定所有界面已迁移到同一框架。`ui_adaptor` 管理 redraw、
resize 与最终终端光标，ImGui-backed screen 则通过 `cataimgui::window` 封装相应生命周期。

### Screen reader mode

`SCREEN_READER_MODE` 是当前 interface option，默认关闭。`src/newcharacter.cpp` 与
`src/player_difficulty.cpp` 展示了受支持 screen 如何切换布局。它不是让所有 UI 自动可访问的
全局转换；新增支持必须逐个界面实现和验证。

屏幕阅读器不能可靠表达仅由颜色传递的信息，因此禁用、危险、状态变化等还要有文字或结构
提示。把最终终端光标放在当前最重要的内容；列表滚动和光标上方的变化可能抢走朗读位置。
列表加详情的界面在 reader mode 下宜只呈现当前项和其详情，避免同时滚动整列。不要依赖视觉
分栏、ASCII 边框或颜色作为唯一语义。

### 实现与验证

处理 resize 和 redraw 后仍要维持光标/焦点；在需要时使用 `ui_adaptor::set_cursor` 或
`disable_cursor`。测试正常模式与 `SCREEN_READER_MODE`、curses 与 tiles、键盘导航、窄窗口、
动态内容、翻译后长文本及高对比主题。真实屏幕阅读器验证应记录软件、平台与场景；自动化截图
或颜色对比检查不能替代朗读顺序测试。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `512e14575d0545351f6fd8681a91825b993934d608585186f39da929e79d4405`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/USER_INTERFACE_AND_ACCESSIBILITY.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/USER_INTERFACE_AND_ACCESSIBILITY.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/USER_INTERFACE_AND_ACCESSIBILITY.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
