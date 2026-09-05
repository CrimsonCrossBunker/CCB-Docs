---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: validation.testing
title: 测试策略
language: zh_CN
status: active
doc_type: how-to
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- AGENTS.md
- ai/test-matrix.yml
- Makefile
- tests/AGENTS.md
source_symbols: []
source_queries: []
source_fingerprint: edb79059c9da967e596d7c40092e3a040fb3020bddbf672e13ec8a72e2a63477
authority: build-config
verified_commit: 3053bf160578e46c1692a89c60594aa1acc6a276
verified_at: '2026-09-05'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 03153b99ae3c8b21bac1c0271b8e58a0dbef6c60a9c65d72bf49020e0b134707
prerequisites:
- validation.quickstart
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
- cpp-format
- cpp-tests
- json-load
- lua-contract
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: testing
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/validation/testing/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/validation/testing/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/validation/testing/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/validation/testing/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/3053bf160578e46c1692a89c60594aa1acc6a276
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3053bf160578e46c1692a89c60594aa1acc6a276/AGENTS.md
- path: ai/test-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3053bf160578e46c1692a89c60594aa1acc6a276/ai/test-matrix.yml
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3053bf160578e46c1692a89c60594aa1acc6a276/Makefile
- path: tests/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3053bf160578e46c1692a89c60594aa1acc6a276/tests/AGENTS.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28validation.testing%29%3A+&body=Document+ID%3A+validation.testing%0ALanguage%3A+zh_CN%0AVerified+commit%3A+3053bf160578e46c1692a89c60594aa1acc6a276%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 测试策略

CCB 的测试目标是用最小、可复现的证据覆盖风险，而不是让每个 PR 无差别运行
全部平台。命令权威来自 `ai/test-matrix.yml`、Makefile、CI 和测试源码。

## 从窄到宽

1. 运行目标文件的格式、Schema 或静态契约检查。
2. 运行最接近行为的单元/回归测试，并使用聚焦 Catch2 filter。
3. 运行子系统加载或集成检查，例如 JSON 全量加载。
4. 公共契约、平台或发布变化再扩大到矩阵构建。

| 变化 | 必要证据 | 常见扩大条件 |
| --- | --- | --- |
| C++ 实现 | `make astyle-check`、聚焦 Catch2 | 共享核心、序列化、性能热点 |
| 测试框架/公共头 | `make -j2 tests` | 编译器或 feature 组合差异 |
| JSON/EOC/MOD | formatter 与 `make -j2 json-check` | loader、Schema、跨 MOD 交互 |
| Lua 公共契约 | 声明、覆盖、相关单测 | native registration 或 Platform 契约 变化 |
| Agent/文档元数据 | metadata checker 与 `tools/agent` 测试 | 生成清单或 CI 路由变化 |
| Android | Gradle unit/build 目标 | Java/native 边界或资源打包 |

## Platform v1 契约验收命令

按完整 Lua 领域批次完成实现、声明和测试源码，再集中运行以下验收入口。
以下是当前命令，不是本次文档修改重新编译游戏或完成所有 API 语义验证的记录。

```sh
# validation: agent-context
python3 tools/agent/check_project_metadata.py
python3 -m unittest discover -s tools/agent -p 'test_*.py'

# validation: lua-contract
python3 tools/lua_api/check_luals_declarations.py
python3 tools/lua_api/check_platform_native_inventory.py
python3 tools/lua_api/check_platform_contract.py
python3 tools/lua_api/check_platform_coverage.py
python3 tools/lua_api/check_cmake_contract.py
python3 -m unittest discover -s tools/lua_api -p 'test_*.py'
```

## 写回归测试

- 测试名说明可观察行为，而不是实现细节。
- 构造最小 fixture，避免依赖测试执行顺序、当前时间或未固定随机状态。
- 失败时保存 filter、断言上下文、日志和 RNG seed。
- 修复 bug 时先证明测试能捕获原问题，再证明修改后通过。
- 不用扩大 timeout 掩盖死锁、无限循环或性能回退。

## 如实报告

PR 中分开列出 Passed、Failed、Not run。Windows、MSVC、Android 或耗时构建没有
实际运行时必须明确写出，不可以用 Linux 配置成功替代。失败应保留首个根因、
修复和重跑结果；偶发失败应记录 seed 和重现次数。

快捷命令见[验证快速入门](quickstart.md)，定位失败见[调试](debugging.md)。
