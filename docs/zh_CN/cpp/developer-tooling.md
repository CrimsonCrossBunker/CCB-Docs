---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: developer-tooling
title: 旧文档迁移草稿：developer tooling
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
- doc/c++/DEVELOPER_TOOLING.md
- build-scripts/clang-tidy-run.sh
- build-scripts/ci-iwyu-run.py
- .github/workflows/clang-tidy.yml
- .github/workflows/iwyu.yml
source_symbols: []
source_queries: []
source_fingerprint: 71d889bd30bafd07c041e9d131a9381325bce710155ffaeb9c5b11c336bd282d
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: c6997d95a2b6e6a32bd914f4d8b66964708c1f319206b5236a92b30a0f8528a4
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: dumb-kevin, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/developer-tooling/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/developer-tooling/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/developer-tooling/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/developer-tooling/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/c++/DEVELOPER_TOOLING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/c++/DEVELOPER_TOOLING.md
- path: build-scripts/clang-tidy-run.sh
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/build-scripts/clang-tidy-run.sh
- path: build-scripts/ci-iwyu-run.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/build-scripts/ci-iwyu-run.py
- path: .github/workflows/clang-tidy.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/.github/workflows/clang-tidy.yml
- path: .github/workflows/iwyu.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/.github/workflows/iwyu.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28developer-tooling%29%3A+&body=Document+ID%3A+developer-tooling%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：developer tooling

本页是 `developer-tooling` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `developer-tooling`
- Target: `cpp/developer-tooling.md`
- Replacement: developer-tooling
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| developer-tooling | doc/c++/DEVELOPER_TOOLING.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB 开发工具链

工具选择由修改类型决定，不要求每个贡献者安装整套静态分析栈。最小开发循环是：定位受
影响源码/测试、配置一个可复现 build、编译最小目标、运行 focused validation、检查 diff。
clang-tidy、IWYU、clangd、ctags 和 profiler 属于按需层。

### compilation database 与编辑器

用当前 CMake 配置生成 `compile_commands.json`：

```sh
cmake -S . -B build -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
cmake --build build -j2
```

具体 feature flags 应与要审阅的平台/CI job 一致。让 clangd 指向 build 内的 database；
不要提交 `compile_commands.json`、clangd index、ctags、Doxygen HTML 或大型 symbol database。
它们可以作为本地缓存或 CI artifact。

### clang-tidy

`.clang-tidy` 与 `tools/clang-tidy-plugin` 定义 CCB checks，CI 由
`.github/workflows/clang-tidy.yml` 和 `build-scripts/clang-tidy-run.sh` 驱动。脚本会创建
compilation database、定位直接/间接受影响 translation units，并要求构建的 Cata plugin。

本地只检查一个文件时也必须使用与 build 匹配的 database 和 plugin/wrapper；系统自带的
裸 clang-tidy 结果可能缺少 `cata-*` checks。自动 `-fix` 后逐项审阅，不能盲目接受跨文件
重写。

### include-what-you-use

`.github/workflows/iwyu.yml` 与 `build-scripts/ci-iwyu-run.py` 是当前 CI 入口。该脚本依赖
`files_changed`、affected-file 分析、`tools/iwyu/cata.imp` 和 blacklist；它明确面向 CI。
本地运行应按脚本头部的当前示例配置工具版本和 database，不能复制旧 LLVM/IWYU 安装指南。

IWYU 建议不是自动正确：平台 wrapper、template 实例化、associated header 和 keep pragma
都有专用规则。应用后必须重新编译受影响目标。

### formatter、索引与生成物

- C++：`make astyle-check`，修正时 `make astyle` 后检查完整 diff。
- JSON：使用仓库 formatter，再运行 loader/ID 检查。
- Python：只对相关 scripts/tests 运行仓库锁定的 lint/test。
- ctags/Doxygen：用于导航，不是 API 权威来源，也不提交输出。

所有工具命令以当前 CI、CMake、Makefile 和脚本为准。旧文档若指定固定 LLVM 版本、上游
仓库下载或过时 IDE 扩展，应视为历史材料而不是 CCB 要求。

## 历史与归属

清单中的已接受贡献者为：dumb-kevin, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `71d889bd30bafd07c041e9d131a9381325bce710155ffaeb9c5b11c336bd282d`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/c++/DEVELOPER_TOOLING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/c%2B%2B/DEVELOPER_TOOLING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/c%2B%2B/DEVELOPER_TOOLING.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
