---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.ui
title: UI 平台矩阵
language: zh_CN
status: draft
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: Pending human review
source_paths:
- src/ui_manager.h
- src/input_context.cpp
- src/sdltiles.h
- android/app/src/main/java/com/crimsoncrossbunker/cataclysmcb/AndroidUiMode.java
- src/sdltiles.cpp
- data/lua/LUA_FIRST_PLATFORM.md
source_symbols:
- class ui_adaptor
- android_ui_mode::is_new_ui_build()
source_queries: []
source_fingerprint: 16b05f93caea07d5ea0b95749a05d660c6d361a1c1656bc25d3f12a3e471b999
authority: source-and-tests
verified_commit: 7d65b4eff3d92393e659699a312b694f0e72d2cb
verified_at: '2026-10-11'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 349a7f7b769231e70b9b2b7275982033c51fd515d3c2817558a56ceed1a2594f
prerequisites:
- cpp.ui
- cpp.input
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
- android-unit
- lua-contract
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: platforms-ui
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/987
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/ui/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/ui/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/ui/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/ui/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/7d65b4eff3d92393e659699a312b694f0e72d2cb
source_urls:
- path: src/ui_manager.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/src/ui_manager.h
- path: src/input_context.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/src/input_context.cpp
- path: src/sdltiles.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/src/sdltiles.h
- path: android/app/src/main/java/com/crimsoncrossbunker/cataclysmcb/AndroidUiMode.java
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/android/app/src/main/java/com/crimsoncrossbunker/cataclysmcb/AndroidUiMode.java
- path: src/sdltiles.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/src/sdltiles.cpp
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/data/lua/LUA_FIRST_PLATFORM.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.ui%29%3A+&body=Document+ID%3A+platforms.ui%0ALanguage%3A+zh_CN%0AVerified+commit%3A+7d65b4eff3d92393e659699a312b694f0e72d2cb%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# UI 平台矩阵

CCB 的 UI 由同一语义 action/view-model 层通过多条 renderer/input 路径呈现。每个 UI 修改
都必须说明实际覆盖了哪些路径。

## 路径

| 路径 | 构建/运行边界 | 应收集证据 |
| --- | --- | --- |
| Curses | terminal cell、颜色与 keyboard | terminal 类型/尺寸、locale、key path |
| SDL3 tiles | SDL3 renderer/GPU shader 与 recovery | GPU/backend、artifact format、recovery |
| Native UI | `ui_adaptor`、`input_context`、curses-compatible window | resize/redraw 与 input action |
| Lua UI/ImGui | 唯一 Lua Platform v1 与 native ImGui 集成 | Platform v1 合同、action、native fallback |
| Android | Java HUD/touch/text input 与 SDL3 native runtime | device/API、UI mode、orientation、touch |

## 共同不变量

语义 action ID 稳定；cell/pixel coordinate 只在显式边界转换；resize 先建立 layout 再
redraw；renderer recreation 失效 GPU resource；翻译文本/font fallback 不能假设固定
byte/glyph width；新 UI 在窄尺寸仍可操作。

## 验证矩阵

至少覆盖 keyboard navigation、cancel/confirm、resize、窄 viewport、translation 与直接
修改路径。renderer/coordinate 修改覆盖 SDL3 software、OpenGL、GPU，以及输入不同的
Android 路径。记录 SDK、renderer、整数缩放与 viewport；链接 SDK 身份不能证明设备
输入或可听音频已验收。Lua UI 仍需验证 disabled/native fallback build。

## 可访问性与失败证据

保持可见 focus、可理解 action name、非纯颜色状态、可读 contrast 和 keyboard 操作。
收集 route、mode、resolution/scale、locale、input device、截图/录屏，以及 stale frame、
错误坐标或 input 丢失附近首段 debug log。

## 生成与本地数据

screenshot、recording、renderer capture 与 local UI profile 默认是证据 artifact，除非任务
明确新增 checked fixture。没有政策审查，不要把用户 keybinding 或设备布局作为项目默认。
