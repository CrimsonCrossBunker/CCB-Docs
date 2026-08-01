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
source_symbols:
- class ui_adaptor
- android_ui_mode::is_new_ui_build()
source_queries: []
source_fingerprint: 4f2ee856289cb1352882870efe2efd69335a90b9e51750df07c43205fa0b2c12
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8e5535d38d8ae267597a3fd6a545d71f480bcb4a173599d1ee3e5f4aee0c0ace
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
pending_source_pr: null
stale_reason: null
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
| SDL2 tiles | fallback desktop renderer 与 SDL2 input/audio | OS、renderer、scale、font、device |
| SDL3 tiles | SDL3 renderer/GPU shader 与 recovery | GPU/backend、artifact format、recovery |
| Native UI | `ui_adaptor`、`input_context`、curses-compatible window | resize/redraw 与 input action |
| Lua UI/ImGui | capability-gated Lua page 与 native ImGui 集成 | manifest、API v5、native fallback |
| Android | Java HUD/touch/text input 与 SDL3 native runtime | device/API、UI mode、orientation、touch |

## 共同不变量

语义 action ID 稳定；cell/pixel coordinate 只在显式边界转换；resize 先建立 layout 再
redraw；renderer recreation 失效 GPU resource；翻译文本/font fallback 不能假设固定
byte/glyph width；新 UI 在窄尺寸仍可操作。

## 验证矩阵

至少覆盖 keyboard navigation、cancel/confirm、resize、窄 viewport、translation 与直接
修改路径。renderer/coordinate 修改在分支不同处需要 SDL2/SDL3 与 Android；Lua UI 还要
验证 disabled/native fallback build。

## 可访问性与失败证据

保持可见 focus、可理解 action name、非纯颜色状态、可读 contrast 和 keyboard 操作。
收集 route、mode、resolution/scale、locale、input device、截图/录屏，以及 stale frame、
错误坐标或 input 丢失附近首段 debug log。

## 生成与本地数据

screenshot、recording、renderer capture 与 local UI profile 默认是证据 artifact，除非任务
明确新增 checked fixture。没有政策审查，不要把用户 keybinding 或设备布局作为项目默认。
