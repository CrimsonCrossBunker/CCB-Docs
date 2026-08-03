---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: build-devcontainer
title: 旧文档迁移草稿：devcontainer
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
- doc/c++/COMPILING-DEVCONTAINER.md
- .devcontainer/devcontainer.json
- .devcontainer/Dockerfile
- .devcontainer/graphical/devcontainer.json
- .devcontainer/cross-compile/devcontainer.json
source_symbols: []
source_queries: []
source_fingerprint: 8f68c334544cfd8d659189c98b595176526138bcc7ce376643893903767ec072
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: f315bbcc7b8178911ef536a5473c747b7b5463698427283e0a270188e3e1b62b
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/build/devcontainer/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/build/devcontainer/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/build/devcontainer/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/build/devcontainer/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/c++/COMPILING-DEVCONTAINER.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c++/COMPILING-DEVCONTAINER.md
- path: .devcontainer/devcontainer.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/.devcontainer/devcontainer.json
- path: .devcontainer/Dockerfile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/.devcontainer/Dockerfile
- path: .devcontainer/graphical/devcontainer.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/.devcontainer/graphical/devcontainer.json
- path: .devcontainer/cross-compile/devcontainer.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/.devcontainer/cross-compile/devcontainer.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28build-devcontainer%29%3A+&body=Document+ID%3A+build-devcontainer%0ALanguage%3A+zh_CN%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：devcontainer

本页是 `build-devcontainer` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `build-devcontainer`
- Target: `build/devcontainer.md`
- Replacement: build-devcontainer
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| build-devcontainer | doc/c++/COMPILING-DEVCONTAINER.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 Dev Container 工作流

固定来源包含三个独立配置：根目录的 `Standard`、`graphical/` 下的
`Standard + Qt5`，以及 `cross-compile/` 下的 `Cross-Compile w32`。选择配置文件，
不要再按旧指南注释或取消注释一个共享 Dockerfile 的大段内容。

### 前置条件

- 支持 Dev Containers 的编辑器（仓库配置以 VS Code 扩展为主要入口）；
- Docker 或兼容的 container runtime；
- 已 clone 的 CCB fork 和单独分支；
- 足够的镜像、依赖和编译空间。

在编辑器中打开仓库，选择对应 `.devcontainer/.../devcontainer.json`，然后执行
“Reopen in Container”。首次构建镜像可能较慢；失败时保存 build log 和具体 layer，
不要反复删除整个 Docker 数据目录。

### 容器内构建

容器打开后仍使用仓库权威入口，例如：

```sh
make -j2
make -j2 tests
```

也可以使用仓库 CMake preset。命令应从挂载的仓库根目录运行，产物位置由 Make/CMake
配置决定。图形运行还依赖 host display、GPU/软件渲染和音频转发；“容器内编译通过”
不代表 host 上的图形程序一定可启动。

### 跨编译边界

Windows 跨编译使用专门的 `cross-compile` 配置。它只能证明交叉 toolchain 和目标产物
可生成，不能替代 Windows 上的 MSYS2/MSVC CI、运行时 DLL 检查或真实启动测试。

### 安全与复现

- 审查 Dockerfile、feature、mount、端口和 host socket 后再允许容器构建。
- 不把 token、SSH 私钥、签名文件或个人配置烘焙进镜像。
- 修改 `.devcontainer/` 时至少重建受影响配置并记录 host/runtime 版本。
- 容器说明与仓库配置冲突时，以当前 JSON、Dockerfile 和 CI 为准。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `8f68c334544cfd8d659189c98b595176526138bcc7ce376643893903767ec072`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/c++/COMPILING-DEVCONTAINER.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/COMPILING-DEVCONTAINER.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/COMPILING-DEVCONTAINER.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
