---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.windows
title: Windows 开发
language: zh_CN
status: active
doc_type: explanation
audiences:
- new-contributor
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: Pending human review
source_paths:
- CMakePresets.json
- .github/workflows/msvc-full-features.yml
- doc/c++/COMPILING.md
- build-scripts/MSVC.cmake
source_symbols: []
source_queries:
- windows-x64
source_fingerprint: c3ab24337b86bdbd44d44eab2942d910822cb577576597e7a43ab52690ae13e4
authority: build-config
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 0d041a17d3cafee4a5a57d3aa8a5ac7894acc2dba06bcfc7ae00d6c8479fbaa3
prerequisites:
- platforms.matrix
- build.overview
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cmake-configure
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: platforms-windows
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/windows/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/windows/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/windows/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/windows/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/CMakePresets.json
- path: .github/workflows/msvc-full-features.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/.github/workflows/msvc-full-features.yml
- path: doc/c++/COMPILING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/c++/COMPILING.md
- path: build-scripts/MSVC.cmake
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/build-scripts/MSVC.cmake
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.windows%29%3A+&body=Document+ID%3A+platforms.windows%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Windows 开发

Windows 有两套受维护、但依赖、shell、path 与 artifact 行为不同的 compiler 环境：
MSYS2/MinGW 和原生 MSVC/vcpkg。诊断前必须先选定路径。

## 路径选择

| 路径 | 契约入口 | 优点 | 主要边界 |
| --- | --- | --- | --- |
| MSYS2/MinGW | `windows-x64` 或 `windows-tiles-sounds-x64` preset | Unix 风格 shell 与 Ninja | MSYS2 package/runtime DLL 集合 |
| MSVC/vcpkg | `windows-x64-msvc` 或 `windows-tiles-sounds-x64-msvc` preset | 匹配 Windows CI compiler lane | Visual Studio、vcpkg triplet 与 configuration |
| ClangCL | `windows-tiles-sounds-x64-clang-cl` preset | compiler 诊断/time trace | 继承 MSVC/vcpkg 依赖模型 |

以 `CMakePresets.json`、`.github/workflows/msvc-full-features.yml` 和适用 toolchain file
为权威。旧编译 prose 只是背景，不能证明包或命令仍受支持。

## 共同检查表

1. 说明 shell：PowerShell、cmd、MSYS2 MinGW64 或其他环境。
2. 说明 architecture、compiler、generator、preset、configuration、SDL、tiles/sound、
   localization、test 与 static/dynamic linking。
3. 源码/build path 应满足工具长度限制，带空格 path 必须正确引用。
4. 在同一环境执行 preset configure 与 build。
5. 测试打包目录，不能只测试依靠开发环境 DLL 的可执行文件。

## 产物与诊断

不要提交 Visual Studio output、vcpkg installation、本地 CMake user preset、DLL staging、
PDB、crash dump 或 credential。诊断需要时，可把 PDB、log、package manifest 和 dump 作为
受限 CI/release artifact 上传。

## 跨平台边界

Windows path encoding、console/SDL input、DLL discovery 与 renderer recovery 不同于
Linux。WSL 构建产生 Linux binary，不能验证原生 Windows packaging。
