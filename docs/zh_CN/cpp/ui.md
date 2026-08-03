---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.ui
title: 原生 UI 子系统
language: zh_CN
status: active
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/ui_manager.h
- src/ui_manager.cpp
- src/ui_helpers.cpp
- tests/ui_profile_test.cpp
source_symbols:
- class ui_adaptor
source_queries: []
source_fingerprint: 9bcfa9d914370ad89daf4deafe7ab4ea9b47210c646a04e8d33cc977ba378725
authority: source-and-tests
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: f0818aa16ebac2c72fc3ea7c0401e2e6f8a7b9c2564202a66165e2d9d9c6e4bb
prerequisites:
- architecture.overview
depends_on:
- cpp.input
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-ui
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/ui/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/ui/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/ui/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/ui/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: src/ui_manager.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/ui_manager.h
- path: src/ui_manager.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/ui_manager.cpp
- path: src/ui_helpers.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/ui_helpers.cpp
- path: tests/ui_profile_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/ui_profile_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.ui%29%3A+&body=Document+ID%3A+cpp.ui%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 原生 UI

## 职责

原生 UI 层协调 screen region stack、resize/redraw 失效、curses 兼容 window、SDL/tile
渲染、list、popup 与较新的 ImGui surface；`ui_adaptor` 是核心生命周期和重绘边界。

## 入口点

从 `src/ui_manager.h` / `.cpp` 开始，再看 `ui_helpers`、`uilist` 与具体 screen。注册
`on_screen_resize`、`on_redraw`，声明 adaptor 区域，并通过 `input_context` 驱动。

## 数据所有权

栈上的 `ui_adaptor` 通过 RAII 拥有 callback 与 UI stack 成员资格。screen function
拥有 window/view model；renderer backend 拥有 texture/buffer；全局 `uistate` 只保存
明确需要持久化的显示选择。

## 依赖

UI 依赖 input context、translation、color/font/terminal metric、renderer backend、游戏
view model、Android UI mode 与可选 Lua UI/ImGui 集成。

## 生命周期

构造 adaptor 时入栈；resize 建立 geometry；redraw 只绘制声明区域；input 可能触发更多
resize/redraw；析构时出栈。callback 不能在 redraw 中改变 adaptor stack。

## 不变量

声明 geometry 包含全部绘制；callback 遵守 manager 的重入规则；顶层 UI 获得 input
focus；除非显式 absolute pixel API，window 尺寸使用 cell；resize 先失效布局再绘制。

## 扩展点

原生 screen 使用局部 adaptor 与 input context，可复用布局进入 helper。向 Lua 暴露数据
只能通过有边界公共 API，不能泄露 native UI pointer。

## 序列化

adaptor、window、callback 与 renderer resource 都是临时的。只持久化明确用户配置或
`uistate` 字段，提供默认和测试；读取后重建布局。

## 测试

使用 UI profile 与具体 screen 测试，并按需覆盖 resize、窄 terminal、keyboard、
tiles/curses、Android touch 与 Lua-disabled 路径。

## 性能

redraw 调用频繁。限制失效区域，不要在 paint callback 重建昂贵 view model，并防止
透明 ImGui layer 在 SDL buffer 留下旧像素。

## CCB 差异

CCB 把旧原生 screen 与项目专属 Lua UI、ImGui、Android HUD 路径结合。上游 UI 移植
必须保持所有启用 backend 与 input-mode 边界。

## 技术债务

cell、pixel、curses、SDL、ImGui 与 Android 抽象并存。新 screen 应显式管理 geometry，
不要再引入全局 redraw 或 input shortcut。
