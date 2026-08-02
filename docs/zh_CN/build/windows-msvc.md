---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: build-windows-msvc
title: 旧文档迁移草稿：windows msvc
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
- doc/c++/COMPILING-CMAKE-VCPKG.md
- CMakeLists.txt
- CMakePresets.json
- build-scripts/x64-windows-static.cmake
- .github/workflows/msvc-full-features.yml
- doc/c++/COMPILING-VS-VCPKG.md
- build-scripts/windows-tiles-sounds-x64-msvc.cmake
source_symbols: []
source_queries: []
source_fingerprint: 67ae130a01e46324ef41c87a392ce88719218f4d66dd72ea896d4a6cd8d82c98
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: f2643fc32fc6bab74951ee37d766c14cec02ec4c4237fd1724036b9bbd3736ac
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- legacy.doc-c-compiling-cmake-vcpkg
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina, Maleclypse, dumb-kevin; accepted inventory identities only.
  Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: build
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/build/windows-msvc/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/build/windows-msvc/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/build/windows-msvc/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/build/windows-msvc/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/c++/COMPILING-CMAKE-VCPKG.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/c++/COMPILING-CMAKE-VCPKG.md
- path: CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/CMakeLists.txt
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/CMakePresets.json
- path: build-scripts/x64-windows-static.cmake
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/build-scripts/x64-windows-static.cmake
- path: .github/workflows/msvc-full-features.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/.github/workflows/msvc-full-features.yml
- path: doc/c++/COMPILING-VS-VCPKG.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/c++/COMPILING-VS-VCPKG.md
- path: build-scripts/windows-tiles-sounds-x64-msvc.cmake
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/build-scripts/windows-tiles-sounds-x64-msvc.cmake
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28build-windows-msvc%29%3A+&body=Document+ID%3A+build-windows-msvc%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：windows msvc

本页是 `build-windows-msvc` 的迁移草稿页面。它记录 **2** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `legacy.doc-c-compiling-cmake-vcpkg, build-windows-msvc`
- Target: `build/windows-msvc.md`
- Replacement: build-windows-msvc
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| legacy.doc-c-compiling-cmake-vcpkg | doc/c++/COMPILING-CMAKE-VCPKG.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | build-windows-msvc |
| build-windows-msvc | doc/c++/COMPILING-VS-VCPKG.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 MSVC 与 vcpkg 路线

CCB 的完整 MSVC 路线由 `msvc-full-features/` solution、vcpkg manifest/triplet、CMake
preset 和 `.github/workflows/msvc-full-features.yml` 共同定义。旧文档中的 CleverRaven
clone、任意最新 vcpkg 和旧 Visual Studio 版本不能替代这些固定契约。

### 推荐入口

安装 Visual Studio 2022 的 C++ desktop/game workload、Git、与项目兼容的 CMake 和
vcpkg。固定来源的 CI 使用 CMake 3.31.6，并把 vcpkg 固定到
`f6672d8e480ccdecddfad3fd1b838ba369ffe6cd`；本地改变版本时必须记录差异。

可选择两条路线：

1. 打开 `msvc-full-features/Cataclysm-vcpkg-static.sln`，使用 `Release`/`x64`；
2. 使用 `windows-x64-msvc` 或 `windows-tiles-sounds-x64-msvc` CMake preset。

CI 的核心 solution 构建命令是：

```powershell
msbuild -m -p:Configuration=Release -p:Platform=x64 -p:UseSDL3=false `
  "-target:Cataclysm-vcpkg-static;Cataclysm-test-vcpkg-static;JsonFormatter-vcpkg-static;zzip" `
  msvc-full-features/Cataclysm-vcpkg-static.sln
```

这是 CI 证据，不表示本文在本机 Windows 重新执行过该命令。

### 测试与运行

- 用与游戏相同的 configuration/platform 构建 test target。
- 从生成目录运行 focused Catch2 filter；Release 通常适合日常验证，Debug 留给需要
  iterator diagnostics 或逐步调试的情形。
- localization、Tiles、sound、SDL2/SDL3 与 static linking 会改变目标与依赖；PR 中
  写明组合。
- vcpkg 安装失败时先保存对应 buildtree log 和锁定 revision，不要直接升级到任意 HEAD。

本页不发布签名或分发步骤；发布与打包见[发布维护](../maintenance/releases.md)。

## 历史与归属

清单中的已接受贡献者为：thaelina, Maleclypse, dumb-kevin。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `67ae130a01e46324ef41c87a392ce88719218f4d66dd72ea896d4a6cd8d82c98`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/c++/COMPILING-CMAKE-VCPKG.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/COMPILING-CMAKE-VCPKG.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/COMPILING-CMAKE-VCPKG.md)
- [`doc/c++/COMPILING-VS-VCPKG.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/COMPILING-VS-VCPKG.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/COMPILING-VS-VCPKG.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
