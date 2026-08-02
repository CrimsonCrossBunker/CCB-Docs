---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: build-cmake
title: 旧文档迁移草稿：cmake
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
last_human_reviewer: Pending human review
source_paths:
- doc/c++/COMPILING-CMAKE.md
- CMakeLists.txt
- CMakePresets.json
- build-scripts/CMakeUserPresets.json.in
source_symbols: []
source_queries: []
source_fingerprint: 4d3be77600ca22667ed79ea09c70d03334c0813da303c207a403273d99d77733
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 4e33ea8120a73f3bb371aaebd3003cecdba0091dad79669a9480f7ccbb313bf1
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/build/cmake/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/build/cmake/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/build/cmake/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/build/cmake/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/c++/COMPILING-CMAKE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/c++/COMPILING-CMAKE.md
- path: CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/CMakeLists.txt
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/CMakePresets.json
- path: build-scripts/CMakeUserPresets.json.in
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/build-scripts/CMakeUserPresets.json.in
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28build-cmake%29%3A+&body=Document+ID%3A+build-cmake%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：cmake

本页是 `build-cmake` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `build-cmake`
- Target: `build/cmake.md`
- Replacement: build-cmake
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| build-cmake | doc/c++/COMPILING-CMAKE.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CMake 路线

仓库的 `CMakePresets.json` 是 preset 名称、generator、输出目录和默认 feature 组合的
权威来源。旧文档中“CMake 非官方”、手工下载 SDL DLL 和 in-tree `build/` 的叙述已经
过时；CCB 当前 CI 会实际使用 CMake，但仍要求 out-of-tree 构建。

### 发现并配置

在仓库根目录先运行：

```sh
cmake --list-presets
cmake --preset linux-x64
```

`linux-x64`、`linux-tiles-sounds-x64`、Windows MSYS2 与 MSVC preset 均在固定来源
commit 的 `CMakePresets.json` 中。输出默认位于 `out/build/<preset>/`。如果本机列表
为空或缺少目标 preset，先检查平台、generator、toolchain 与 preset condition，不要
把旧文档中的命令直接拼到当前配置上。

### 构建和覆盖选项

```sh
cmake --build --preset linux-x64
```

临时覆盖使用 `-DNAME=VALUE`，但提交前必须确认该选项仍由 `CMakeLists.txt` 定义。
Tiles、sound、localization、Lua、SDL2/SDL3 与 sanitizer 会改变依赖和产物；记录实际
preset 和覆盖值。不要提交本机的 `CMakeUserPresets.json`、绝对路径、vcpkg 根目录或
生成的 build tree。

### 验证和故障定位

1. 保存 configure 的第一条错误，而不只保存最后的 build failure。
2. 核对 CMake、compiler、Ninja/MSBuild 与依赖版本。
3. 只删除明确的 `out/build/<preset>/` 构建目录；不要清理源码树或未跟踪文件。
4. 重新 configure，再构建受影响 target；涉及测试时运行对应 preset 产物中的 focused
   test。

`cmake --list-presets` 已在 Linux 对文档分支实际验证；Windows preset 的可用性与完整
编译由对应 Windows CI 证明，不能由 Linux 结果替代。总览见[构建 CCB](overview.md)，
平台差异见[平台矩阵](../platforms/matrix.md)。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `4d3be77600ca22667ed79ea09c70d03334c0813da303c207a403273d99d77733`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/c++/COMPILING-CMAKE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/COMPILING-CMAKE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/COMPILING-CMAKE.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
