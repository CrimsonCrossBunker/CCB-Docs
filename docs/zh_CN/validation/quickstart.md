---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: validation.quickstart
title: 构建与验证快速入口
language: zh_CN
status: stale
source_paths:
- AGENTS.md
- ai/test-matrix.yml
- Makefile
- CMakePresets.json
- android/gradlew
authority: build-config
verified_commit: 9d8f26582da0f53ca1e29f8f072aeef43955655b
verified_at: '2026-08-01'
generated: false
include_in_search: true
include_in_ai_index: false
translation_status: current
translation_stale_since: null
risk_group: build
risk_level: high
pending_source_pr: null
stale_reason: 'Source paths changed after 9d8f26582da0: Makefile'
---

# 构建与验证快速入口

验证命令以 CCB 主仓库的 CI、CMake、Makefile、Gradle 和脚本为准。本文只提供
选择入口；如果本文命令与构建文件冲突，应标记本文 stale 并按实际构建契约修复。

## 先选最小充分检查

| 修改区域 | 首选检查 | 说明 |
| --- | --- | --- |
| Agent/治理元数据 | `python3 tools/agent/check_project_metadata.py` | 再运行 `tools/agent` 单元测试 |
| C++ | `make astyle-check` | 行为变化还需聚焦 Catch2 测试 |
| C++ 测试 | `make -j2 tests` | 然后运行 `./tests/cata_test "过滤器"` |
| JSON | `make -j2 json-check` | 单文件同时运行仓库 JSON formatter |
| Lua 契约 | `check_luals_declarations.py` 与 `check_coverage.py` | Schema/注册/声明变化都要检查 |
| CMake | `cmake --preset linux-x64` | 使用仓库现有 preset |
| Android | `cd android && ./gradlew test` | 需要配置好的 Android SDK |

完整命令与路径映射位于 `ai/test-matrix.yml`。耗时检查或平台检查缺少依赖时，
明确说明跳过原因，不得声称已经通过。

## 记录验证结果

PR 中应记录：

1. 实际运行的完整命令；
2. 聚焦测试过滤器或测试名称；
3. 结果和必要的 RNG seed；
4. 未运行检查及原因；
5. 建议审阅者额外验证的场景。

文档影响检查在 Phase 0/1 只提示；它不会代替源码测试，也不会因为无关文档债务
阻止普通源码 PR。
