---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platform-matrix
title: 旧文档迁移草稿：compiler support
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
- doc/c++/COMPILER_SUPPORT.md
- CMakeLists.txt
- .github/workflows/matrix.yml
- .github/workflows/msvc-full-features.yml
source_symbols: []
source_queries: []
source_fingerprint: a734b905bc9c70e7a29cf52f31cacb22a1c0eb476f68e854f490e750a0c99409
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8c855ee739a5da1b5def4450d8e7b53606c0485f92c2383d37affdcd37d49511
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
risk_group: build
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/compiler-support/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/compiler-support/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/compiler-support/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/compiler-support/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/c++/COMPILER_SUPPORT.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c++/COMPILER_SUPPORT.md
- path: CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/CMakeLists.txt
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/workflows/matrix.yml
- path: .github/workflows/msvc-full-features.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/workflows/msvc-full-features.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platform-matrix%29%3A+&body=Document+ID%3A+platform-matrix%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：compiler support

本页是 `platform-matrix` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `platform-matrix`
- Target: `platforms/compiler-support.md`
- Replacement: platform-matrix
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| platform-matrix | doc/c++/COMPILER_SUPPORT.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 支持范围由可执行证据定义

编译器支持不是永久版本表。固定 CCB commit 的 `CMakeLists.txt` 要求 C++17；真正受支持的组合由
默认分支 CI、构建脚本和维护者能够复现的发布工具链共同定义。旧页面中的发行版、Xcode 市占率和链接
会随时间失效，不能覆盖当前 workflow。

在本页验证的 source commit，General build matrix 覆盖：

- Ubuntu 上 clang 13 的基础 curses build/test；
- Ubuntu 上 clang 18 的 tiles + ASan；
- Ubuntu 上 GCC 9 的 curses/LTO 以及 tiles/sound/CMake/UBSan 组合；
- Ubuntu 上 GCC 14 的 curses 与 Lua API 组合；
- macOS 15 / Apple Clang 17 的 tiles、sound、SDL2；
- Android arm64 build-only；
- 独立 Windows workflow 在 windows-2022 上使用 MSVC、固定 CMake/vcpkg 和完整 tests。

这些条目描述该 commit 的 CI，不保证任意更旧或更新工具链，也不代表 build-only 平台已经运行测试。

## 修改与验证

选择最接近目标平台的 CMake preset、Make/Gradle 或 MSVC 入口，并记录 OS、arch、compiler、标准库、
generator、SDL、tiles、sound、localization、Lua、sanitizer 和 build type。Linux 成功不能替代 Windows、
macOS 或 Android；cross-compile 成功也不能证明目标平台启动、依赖打包和输入正常。

提高最低版本或使用新标准库功能前，先更新 matrix 让最旧与最新受支持工具链实际编译，再修改说明。
检查 release packaging、第三方依赖和缓存键，并在默认分支稳定成功后才把 check 设为 required。外部链接
只用于寻找工具，不构成支持承诺；CI job 和仓库配置才是证据。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `d32b9cc880a85480840d82cfa05d256c78a16615`；聚合源指纹为 `a734b905bc9c70e7a29cf52f31cacb22a1c0eb476f68e854f490e750a0c99409`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/c++/COMPILER_SUPPORT.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c%2B%2B/COMPILER_SUPPORT.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c%2B%2B/COMPILER_SUPPORT.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
