---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: design-user-experience
title: 旧文档迁移草稿：user experience
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
- doc/design-balance-lore/design-user-experience.md
- doc/USER_INTERFACE_AND_ACCESSIBILITY.md
- src/options.cpp
source_symbols: []
source_queries: []
source_fingerprint: c48c4c006650195f1034263cc5e9b25a072b994966ca12dc6ab7f2777250c761
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 2325e073a28d63b95df62acbd1b74ee80b3d34cf41cd9337ff783ab538777156
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
risk_group: design
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/design/user-experience/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/design/user-experience/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/design/user-experience/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/design/user-experience/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/design-balance-lore/design-user-experience.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/design-user-experience.md
- path: doc/USER_INTERFACE_AND_ACCESSIBILITY.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/USER_INTERFACE_AND_ACCESSIBILITY.md
- path: src/options.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/options.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28design-user-experience%29%3A+&body=Document+ID%3A+design-user-experience%0ALanguage%3A+zh_CN%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：user experience

本页是 `design-user-experience` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `design-user-experience`
- Target: `design/user-experience.md`
- Replacement: design-user-experience
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| design-user-experience | doc/design-balance-lore/design-user-experience.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## CCB 的用户体验目标

CCB 是俯视网格、行动耗时驱动的开放世界生存游戏，支持字符/tiles 显示并覆盖桌面与 Android 等平台。
它的深度应来自相互作用的世界系统和多种问题解决方式，而不是让玩家和界面搏斗。旧文档引用的其他
游戏与“DDA”名称是历史背景；当前产品身份、平台和功能必须从 CCB README、构建配置、源码和测试确认。

### 深度必须可理解

- 在作出会消耗时间、资源或暴露角色的决定前，尽可能提供相关信息；结果发生后给出可定位原因的反馈。
- 自动化重复操作，但保留路线、装备、风险、优先级和撤退时机等真正的选择。
- 同一动作在键盘、触控、窄窗口、不同缩放和翻译文本下应保持可发现、可取消并能恢复焦点。
- 颜色、ASCII 字形、声音或指针位置不能成为唯一语义；为 screen reader、高对比和不使用音频的玩家
  提供文字或结构线索。
- 复杂系统应允许逐步学习。默认界面展示当前任务需要的信息，进阶信息可展开，而不是永久隐藏契约。

## 设计新流程

先写出玩家目标、入口、最短成功路径、取消/失败路径和保存边界。检查它与 input context、活动系统、
消息、help、options、`ui_adaptor` 或 ImGui 生命周期的关系。不要用新增全局选项掩盖不清楚的默认流程；
每个选项都会扩大测试和维护矩阵。

验证覆盖 curses/tiles、键盘与 Android 触控、resize、窄窗口、长翻译、颜色主题、screen reader mode、
中断/恢复、保存重载和错误输入。借鉴其他游戏只能提出候选模式，不能替代当前 CCB 用户测试和可访问性
证据。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `c48c4c006650195f1034263cc5e9b25a072b994966ca12dc6ab7f2777250c761`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/design-balance-lore/design-user-experience.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/design-user-experience.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/design-user-experience.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
