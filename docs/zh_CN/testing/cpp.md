---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp-testing
title: 旧文档迁移草稿：cpp
language: zh_CN
status: active
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
last_human_reviewer: LYHGLYTX
source_paths:
- doc/c++/TESTING.md
- tests/CMakeLists.txt
- tests/Makefile
- tests/cata_catch.h
- .github/workflows/matrix.yml
source_symbols:
- BENCHMARK_TEST_CASE
source_queries: []
source_fingerprint: 35adfef3c97d8e649e0a2716c8976ea48b953607a1794f0839ca9b65818600f4
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: df876dbec67230feea79b36bca38a010e15871b602b67f1c28068b549f0e45ed
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: g1ytx, thaelina; accepted inventory identities only. Source paths and
  Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: testing
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/testing/cpp/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/testing/cpp/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/testing/cpp/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/testing/cpp/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/c++/TESTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c++/TESTING.md
- path: tests/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/CMakeLists.txt
- path: tests/Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/Makefile
- path: tests/cata_catch.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/cata_catch.h
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/workflows/matrix.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp-testing%29%3A+&body=Document+ID%3A+cpp-testing%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：cpp

本页是 `cpp-testing` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `cpp-testing`
- Target: `testing/cpp.md`
- Replacement: cpp-testing
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| cpp-testing | doc/c++/TESTING.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB C++ 测试流程

CCB 的 C++ 测试使用 Catch2，源码位于 `tests/`，构建产物通常为 `tests/cata_test`。先构建
测试，再用最窄的 case/tag 复现；不要在一个 focused 修复上先跑整套昂贵矩阵。

```sh
make -j2 tests
./tests/cata_test --list-tests
./tests/cata_test '[relevant-tag]'
```

实际 job 数按机器资源调整。完整 suite 和平台/feature 组合由 `.github/workflows/matrix.yml`
等 CI 定义；本地没有运行的组合必须如实标注。

### 编写测试

```cpp
TEST_CASE( "example_status_expires", "[effect][ccb_example]" )
{
    avatar dummy;
    // Arrange only the state this behavior owns.

    REQUIRE( precondition_is_true( dummy ) );
    perform_action( dummy );
    CHECK( observable_result( dummy ) );
}
```

- test name 描述可观察行为，tag 支持子系统 focused run。
- `REQUIRE` 用于后续断言依赖的前置条件；`CHECK` 收集互相独立的结果。
- 直接调用能表达契约的最低层入口，避免通过巨大 UI/game loop 偶然覆盖目标。
- 显式重置 avatar、map、calendar、RNG、options、factory 和其他全局状态。
- 使用 JSON 对象时先断言测试依赖的属性，防止内容数据变化悄悄改变 fixture。
- case 不依赖执行顺序，也不读取另一个 case 留下的文件或全局值。

### 回归测试结构

Bug fix 应先写能在旧实现失败的最小回归，再修实现。覆盖正常路径、报告中的失败路径与最
重要边界；不要把当前错误输出固化成契约。随机算法要固定/记录 seed，并测试不变量而不是
一次随机结果。

跨存档、JSON loader、Lua bridge、Android 或平台代码应使用对应层测试；纯 C++ unit test
不能代替完整 Mod loading、序列化 round-trip 或平台构建。

### 失败诊断

先以相同 filter/seed 重跑，保留首个断言和相关日志。确认失败是否在 diff 涉及的代码、是否
可在 base commit 复现，再决定修复或记录既有失败。不能仅因为 CI 红就删除断言，也不能
没有 base 证据就称其“无关”。

性能比较使用 `BENCHMARK_TEST_CASE`，不进入默认 correctness suite；见[性能](../cpp/performance.md)。

## 历史与归属

清单中的已接受贡献者为：g1ytx, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `d32b9cc880a85480840d82cfa05d256c78a16615`；聚合源指纹为 `35adfef3c97d8e649e0a2716c8976ea48b953607a1794f0839ca9b65818600f4`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/c++/TESTING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c%2B%2B/TESTING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c%2B%2B/TESTING.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
