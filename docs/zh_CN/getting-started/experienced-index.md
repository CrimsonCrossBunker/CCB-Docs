---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: getting-started.experienced-index
title: 老贡献者快速索引
language: zh_CN
status: draft
doc_type: reference
audiences:
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- AGENTS.md
- CONTRIBUTING.md
- ai/project-map.yml
- ai/test-matrix.yml
- ai/generated-files.yml
source_symbols: []
source_queries: []
source_fingerprint: 1662c4035c9b1a1559fa60287298d48cc274ec795a90fa278117c730d951630b
authority: docs-explanation
verified_commit: 2c899a3db790e11a6ff44d91f319064b1ee65d2a
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 0d088e0224b1be9c50195b4a2b4c4bb6bd2b7d680f5c7ef45e45733aaf5f494e
prerequisites:
- home
depends_on:
- architecture.project-map
- validation.quickstart
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
- cpp-format
- json-load
- lua-contract
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: project-context
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/560
stale_reason: null
search:
  exclude: true
---

# 老贡献者快速索引

这页用于已经熟悉 Cataclysm 系项目、只需要快速确认 CCB 差异和验证入口的贡献者。

## 三条先决规则

1. 运行时行为以 CCB 源码和测试为准；不要用上游文档覆盖 CCB 的实现。
2. JSON、Lua 和 API 契约以 Schema、LuaLS 声明、注册信息和生成清单为准。
3. 修改路径前读取根 `AGENTS.md`，再读取路径上最近的子目录 `AGENTS.md`。

## 按任务定位

| 任务 | 首先查看 | 最小验证入口 |
| --- | --- | --- |
| C++ 行为或 UI | `src/`、相关 `tests/` | `make astyle-check`，再运行聚焦测试 |
| 核心 JSON | `data/json/`、加载器/工厂 | formatter 与 `make -j2 json-check` |
| EOC | EOC JSON、解析器、测试 | JSON 格式、完整加载、聚焦解析测试 |
| Lua v5 | manifest Schema、LuaLS、native 注册、生成清单 | Lua contract 检查 |
| 捆绑 Mod | `data/mods/<mod>/` 和依赖 | 加载受影响的 Mod 集合 |
| Android | `android/` | Gradle 单元测试；构建时注明 ABI/variant |
| CI/打包 | `.github/workflows/`、`build-scripts/` | 对应工作流或最窄本地命令 |
| Agent/文档元数据 | `ai/`、`tools/agent/` | Agent metadata tests |

机器可读路由在 `ai/project-map.yml`，验证矩阵在 `ai/test-matrix.yml`。生成文件边界在
`ai/generated-files.yml`；登记为生成的文件不能手改。

## CCB 与上游

移植代码时记录来源仓库、精确 commit/PR、原作者、许可证、CCB 冲突和有意差异。
尤其检查存档、稳定 JSON ID、Mod、Lua API、桌面与 Android 差异。上游测试通过并不
自动证明 CCB 兼容。

## 提交前

- 指定 Responsible human；
- 列出真实运行的命令、平台、结果和未运行项；
- 填写文档影响、CCB-Docs PR、稳定文档 ID 和生成参考影响；
- 检查最终 diff 中没有缓存、凭据、本机路径或无关格式化。
