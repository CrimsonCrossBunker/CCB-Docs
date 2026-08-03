---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: validation.debugging
title: 调试与故障定位
language: zh_CN
status: active
doc_type: how-to
audiences:
- new-contributor
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: LYHGLYTX
source_paths:
- CONTRIBUTING.md
- doc/c++/TESTING.md
- doc/c++/PERFORMANCE.md
- tests/AGENTS.md
source_symbols: []
source_queries: []
source_fingerprint: 364c4a6f53fc762b2419030f2ce970552bf1a03b0a57e51c81360dcdf7582b9d
authority: docs-explanation
verified_commit: 2c899a3db790e11a6ff44d91f319064b1ee65d2a
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 4a57412f7e4b828dd4ade96cb3d3fdb4bab31f077759c40f2e9cb0472d7445f8
prerequisites:
- validation.testing
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: testing
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/560
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/validation/debugging/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/validation/debugging/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/validation/debugging/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/validation/debugging/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/2c899a3db790e11a6ff44d91f319064b1ee65d2a
source_urls:
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/CONTRIBUTING.md
- path: doc/c++/TESTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/doc/c++/TESTING.md
- path: doc/c++/PERFORMANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/doc/c++/PERFORMANCE.md
- path: tests/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/tests/AGENTS.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28validation.debugging%29%3A+&body=Document+ID%3A+validation.debugging%0ALanguage%3A+zh_CN%0AVerified+commit%3A+2c899a3db790e11a6ff44d91f319064b1ee65d2a%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 调试与故障定位

高质量调试先固定现象和边界，再选择工具。不要从最后一行日志直接猜修复，也
不要为了“消除报错”改变无关游戏行为。

## 建立可复现案例

记录以下最小上下文：

- CCB commit、平台、编译器和构建选项；
- 世界、存档或 MOD 组合，以及是否能在新世界复现；
- 精确操作序列、预期行为和实际行为；
- `debug.log` 的相关时间段、堆栈、断言与首个错误；
- 测试 filter、RNG seed、重复次数和是否只在优化构建出现。

先在干净的受支持配置复现，再逐个加入 MOD 或资源包。不要删除原存档；在副本
上测试迁移或恢复。

## 按失败阶段定位

| 阶段 | 先检查 | 证据 |
| --- | --- | --- |
| 配置 | preset、依赖、feature flag | 完整配置命令与首个错误 |
| 编译/链接 | 首个失败 translation unit、符号、库顺序 | 编译器原始诊断 |
| 启动/加载 | JSON/MOD 顺序、Schema、资源路径 | `debug.log` 与最小数据集 |
| 运行时 | 调用栈、对象生命周期、不变量 | 聚焦测试或 debugger backtrace |
| 保存/加载 | save version、迁移、失效 ID | 存档副本与回归测试 |
| 性能 | 可重复 workload、release build | profile，不凭体感优化 |

## 工具选择

- 使用 `rg` 从日志文本、动作 ID、JSON type 或断言定位注册与调用者。
- 用 Catch2 filter 把问题固定成回归测试，然后再扩大测试范围。
- native 崩溃使用目标平台 debugger 和符号化 backtrace；Android 同时保存
  logcat 与 native 崩溃信息。
- 性能问题先按 `doc/c++/PERFORMANCE.md` 的原则测量热点；不要提交大型 profile、
  clangd index、ctags 或 Doxygen HTML。

## 常见误区

- 后续 error 可能只是第一个 loader 错误的连锁反应。
- Debug 与 Release 的未初始化状态、断言和优化行为可能不同。
- 上游已经修复不等于能直接 cherry-pick；先检查 CCB 分歧和兼容性。
- 文档命令过期时应标记页面 stale 并修正文档，不能改构建脚本迁就旧教程。

完成调试后，把最小重现转成测试，运行[测试策略](testing.md)中的受影响层级，
并在 PR 中分别报告已运行和未运行的平台检查。
