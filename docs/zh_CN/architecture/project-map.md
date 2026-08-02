---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: architecture.project-map
title: 项目地图与权威边界
language: zh_CN
status: active
doc_type: explanation
audiences:
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- AGENTS.md
- ai/project-map.yml
- ai/test-matrix.yml
- ai/generated-files.yml
source_symbols: []
source_queries:
- Minimal project map
- 'kind: project_map'
source_fingerprint: 70729d5938c06a6a9123419b91d0bbd25a6b8406ccef3ee140786bb5d2188e72
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 90b4d70c065176f84f4ed848ba0683de783a5603c6447fcfc1db68832035e0b5
prerequisites:
- home
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: project-context
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/project-map/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/project-map/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/project-map/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/project-map/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/AGENTS.md
- path: ai/project-map.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/ai/project-map.yml
- path: ai/test-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/ai/test-matrix.yml
- path: ai/generated-files.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/ai/generated-files.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28architecture.project-map%29%3A+&body=Document+ID%3A+architecture.project-map%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 项目地图

项目地图回答三个问题：应该改哪里、哪里不能顺手改、改完运行什么验证。根
`AGENTS.md` 提供离线最小地图，`ai/project-map.yml` 和 `ai/test-matrix.yml` 提供
机器可读版本。

## 主要区域

| 路径 | 责任 | 下一步 |
| --- | --- | --- |
| `src/` | C++ 引擎、游戏逻辑、UI、原生 Lua 注册 | 读取 `src/AGENTS.md` 与相关测试 |
| `data/json/`、`data/core/` | 核心 JSON 定义 | 检查稳定 ID、格式和加载 |
| `data/lua/`、`tools/lua_api/` | Lua 契约、声明、清单和示例 | 读取 `data/lua/AGENTS.md` |
| `data/mods/` | 随游戏发布的独立 MOD | 读取本 MOD 的 README 和依赖 |
| `tests/` | Catch2 回归与集成测试 | 添加聚焦、可复现的行为测试 |
| `tools/` | 格式化器、验证器、生成器 | 保持 CLI 稳定并提供 `--check` |
| `android/` | Android Gradle、Java UI 与打包 | 不提交 SDK、签名或 APK |
| `.github/`、构建文件 | CI、构建和发布契约 | 使用最小权限和固定 Action SHA |

## 跟踪一个行为

1. 从可观察行为、JSON ID、动作名、测试名或日志文本开始。
2. 使用 `rg` 找定义与引用，不按目录顺序阅读整个源码树。
3. 找到注册点、调用者、数据加载器和现有测试。
4. 检查 `ai/generated-files.yml`，避免手改生成文件。
5. 从测试矩阵选择最小充分验证。

## 边界

项目地图是导航，不是运行时规范。源码和测试决定行为；Schema、LuaLS、注册和
生成清单决定 API 契约；构建文件和 CI 决定构建行为。导航与这些事实冲突时，
应修复地图或本文并标记 stale。
