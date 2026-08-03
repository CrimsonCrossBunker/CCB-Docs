---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp-code-style
title: 旧文档迁移草稿：code style
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
- doc/c++/CODE_STYLE.md
- .astylerc
- .clang-tidy
- .github/workflows/astyle.yml
- tools/format/format.cpp
source_symbols: []
source_queries: []
source_fingerprint: d2ceaf9331a10f9ab22d13115efd9e7cff032e7669b4193ca524b5e6aeaca2be
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: b829893f73e70bd90c4e920e4ec3d5ecc5ecbe8cceea4e30a701d60820b1ad64
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
risk_group: cpp
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/code-style/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/code-style/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/code-style/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/code-style/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/c++/CODE_STYLE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c++/CODE_STYLE.md
- path: .astylerc
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.astylerc
- path: .clang-tidy
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.clang-tidy
- path: .github/workflows/astyle.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/workflows/astyle.yml
- path: tools/format/format.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/format/format.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp-code-style%29%3A+&body=Document+ID%3A+cpp-code-style%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：code style

本页是 `cpp-code-style` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `cpp-code-style`
- Target: `cpp/code-style.md`
- Replacement: cpp-code-style
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| cpp-code-style | doc/c++/CODE_STYLE.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB C++ 风格入口

CCB 的可执行风格契约是 `.astylerc`、`.clang-tidy`、Makefile target 与 CI，不是旧文档中
复制的一串 formatter 参数。工具版本或规则变化时应先更新配置和 CI，再由本文解释结果；
不要在编辑器里维护另一套近似规则。

### 提交前的最小流程

```sh
make astyle-check
git diff --check
```

`astyle-check` 是只读门禁，适合先确认差异。需要自动修正时可运行：

```sh
make astyle
```

`make astyle` 可能修改超出当前手工编辑范围的受管文件。运行后必须检查 `git diff --name-only`
和完整 diff，只提交本任务需要的变化；不要用格式化掩盖无关重构。第三方/生成文件按
仓库清单处理，不应手改。

### 可读性约束

- 使用当前项目类型、单位、point/coordinate 与 ID wrapper，不用裸整数逃避语义。
- 让所有权和空值清晰；优先 RAII 和已有容器/智能指针约定。
- lambda 保持局部、捕获明确；复杂逻辑提取为可命名、可测试的函数。
- 翻译字符串、debug message 和玩家文本使用项目现有 API，并保留格式参数类型。
- header 只暴露需要的依赖；include 调整要同时通过构建、clang-tidy/IWYU 证据。
- 不为“清理”而重命名稳定序列化字段、JSON/Lua API 或跨 Mod ID。

这些是审阅方向，具体机械规则以 clang-tidy 的 `cata-*` checks 和 AStyle 输出为准。若
formatter 与示例冲突，修正示例，不手工反向修改 formatter 结果。

### 改动边界与生成代码

先读最近的 `AGENTS.md` 和 `ai/generated-files.yml`。生成文件必须从 owner generator 更新；
vendored third-party code 只在任务明确要求时修改。大范围 rename、include 重排或 namespace
清理应独立提交，避免与行为修复混在一起。

### 验证选择

风格通过不代表能编译。至少编译受影响 translation unit；公共 header、template、build flag
或跨平台代码需要相应构建矩阵。只报告实际运行的命令，区分本地未安装 formatter、CI 结果
与未执行项。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `d32b9cc880a85480840d82cfa05d256c78a16615`；聚合源指纹为 `d2ceaf9331a10f9ab22d13115efd9e7cff032e7669b4193ca524b5e6aeaca2be`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/c++/CODE_STYLE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c%2B%2B/CODE_STYLE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c%2B%2B/CODE_STYLE.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
