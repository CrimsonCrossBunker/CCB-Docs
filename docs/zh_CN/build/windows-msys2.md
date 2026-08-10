---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: build-windows-msys2
title: 旧文档迁移草稿：windows msys2
language: zh_CN
status: stale
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
- doc/c++/COMPILING-MSYS.md
- Makefile
- CMakeLists.txt
- .github/workflows/sdl3-matrix.yml
source_symbols: []
source_queries: []
source_fingerprint: be53bb9a06a4febd74daf51a319be08b2de8d5666805eaad76b67af669489500
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 204669cb3555214ce892f310b3436ca751c562e6a107a841eab501691f7c87fb
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
stale_reason: 'Source paths changed after d32b9cc880a8: Makefile, doc/c++/COMPILING-MSYS.md'
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/build/windows-msys2/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/build/windows-msys2/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/build/windows-msys2/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/build/windows-msys2/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/c++/COMPILING-MSYS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c++/COMPILING-MSYS.md
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/Makefile
- path: CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/CMakeLists.txt
- path: .github/workflows/sdl3-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/workflows/sdl3-matrix.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28build-windows-msys2%29%3A+&body=Document+ID%3A+build-windows-msys2%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：windows msys2

本页是 `build-windows-msys2` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `build-windows-msys2`
- Target: `build/windows-msys2.md`
- Replacement: build-windows-msys2
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| build-windows-msys2 | doc/c++/COMPILING-MSYS.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 MSYS2 路线

旧文档仍指向 CleverRaven clone、旧 Windows 版本和一条冻结的 pacman 包清单。CCB
贡献者应从 CCB fork 工作，并以当前 MSYS2、Make/CMake 配置和 Windows CI 为准。

### 选择 shell 与 toolchain

在现代 Windows 上使用与已安装包前缀一致的 64 位 MinGW/UCRT shell。不要在普通
MSYS shell、MINGW64 与 UCRT64 之间混装 toolchain。先完整更新 MSYS2，再按当前
Makefile/CMake、缺失 header 的首条错误和 CI 依赖安装包；不要长期复制本文中的版本号。

### CMake preset

固定来源提供：

```sh
cmake --list-presets
cmake --preset windows-x64
cmake --build --preset windows-x64
```

Tiles/sound 组合使用 `windows-tiles-sounds-x64`。preset 采用 Ninja Multi-Config，
输出位于 `out/build/<preset>/`；具体 config 与 install 目录以当前 preset 为准。

### Make 入口

Makefile 仍支持 `MSYS2=1` 与 `DYNAMIC_LINKING=1`，并根据 Tiles、sound、localization、
SDL2/SDL3 等开关选择依赖。不要从旧指南复制一条关闭 lint/test 的大命令作为默认验证。
先做目标构建，再按 `ai/test-matrix.yml` 运行格式、JSON 或 focused tests。

### 运行与提交证据

- 从同一 MSYS2 环境运行生成的程序，确认需要的 runtime DLL 能解析。
- 保存 shell 类型、compiler、CMake/Make、package 前缀和完整命令。
- Windows CI 是合并证据；Linux 或 WSL 构建不能替代原生 Windows 结果。
- 发布包由 release/packaging 流程生成，本地开发构建不能直接冒充官方制品。

MSYS2 包名和工具版本会变化；本文刻意不固定完整安装命令。遇到差异时检查当前 CI 和
MSYS2 官方包数据库。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `d32b9cc880a85480840d82cfa05d256c78a16615`；聚合源指纹为 `be53bb9a06a4febd74daf51a319be08b2de8d5666805eaad76b67af669489500`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/c++/COMPILING-MSYS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c%2B%2B/COMPILING-MSYS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c%2B%2B/COMPILING-MSYS.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
