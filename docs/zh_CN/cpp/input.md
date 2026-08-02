---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.input
title: Input 子系统
language: zh_CN
status: active
doc_type: reference
audiences:
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/input.h
- src/input.cpp
- src/input_context.h
- src/input_context.cpp
source_symbols:
- class input_manager
- class input_context
source_queries: []
source_fingerprint: 517e97772085ae0bdf4e750e8d5007318066d896a10d97db1bf19d1d0df6e8fb
authority: source-and-tests
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 3bdd53fc0ad79269644357795cb27552b94730daf07b899cc3ef4cb450d7dd94
prerequisites:
- architecture.overview
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-input
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/input/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/input/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/input/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/input/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: src/input.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/input.h
- path: src/input.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/input.cpp
- path: src/input_context.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/input_context.h
- path: src/input_context.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/input_context.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.input%29%3A+&body=Document+ID%3A+cpp.input%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 输入

## 职责

`input_manager` 加载/保存物理 binding，并规范化 keyboard、mouse、gamepad、touch/backend
event；`input_context` 为一个 UI 注册语义 action，把 event 解析为 action，同时处理 help、
conflict、timeout、direction 与文本输入。

## 入口点

阅读 `src/input.h`、`src/input.cpp`、`src/input_context.h`、`src/input_context.cpp`。manager
只初始化一次；构造命名 context，注册接受的所有 action，再调用 `handle_input` 并按返回
action ID 分派。

## 数据所有权

全局 manager 拥有已加载 binding map 与 backend key-name map。局部 context 拥有注册的
action set 与临时 input mode；UI 代码拥有 action 的含义和状态转移。

## 依赖

input 依赖平台 event backend、keybinding JSON、action 名翻译、UI mode、option、SDL/
curses code、Android mode 与可选 Lua UI routing。

## 生命周期

启动时加载默认值/用户 override；UI 创建配置 context；backend event 规范化并解析；
context 析构；变化的全局 mapping 可保存。

## 不变量

action ID 是稳定字符串；处理的 action 均已注册；context override 按 manager 政策回退；
portable key name 可往返；timeout/edit mode 随 context 退出复位。

## 扩展点

语义 action 加到最窄 context，并更新默认 binding/data。平台 backend 应产生规范化
`input_event`，不能硬编码玩法命令。

## 序列化

binding 是 `input_manager::save` 写入的用户配置，不属于 world save。局部 context、
排队 event、timeout 与 focus 都是临时状态。

## 测试

测试受影响 UI 及 binding load/save、conflict、fallback、portable-name、mouse/touch 和
backend mode。手工检查必须说明平台与输入设备。

## 性能

input 对延迟敏感。避免每个 event 重扫所有 action、在 redraw callback 阻塞，以及绕开
manager timeout 模型的多余 polling。

## CCB 差异

CCB 在 native、Lua UI、Android new UI 与 legacy mode 间路由输入。上游 binding/context
移植必须保持 action ID 与所有启用 routing 分支。

## 技术债务

全局 mapping 与多套平台 code 容易产生隐式假设。新代码应使用 portable name 和语义
action，而非原始 key integer。
