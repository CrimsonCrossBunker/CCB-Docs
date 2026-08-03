---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: getting-started.common-tasks
title: 常见贡献任务
language: zh_CN
status: active
doc_type: reference
audiences:
- new-contributor
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
- CONTRIBUTING.md
- ai/project-map.yml
- ai/test-matrix.yml
source_symbols: []
source_queries: []
source_fingerprint: 5109872fc3c5beb6fa1efb534a547fa32b82a0bb69f2aa7d96a247bb2186eb01
authority: docs-explanation
verified_commit: 2c899a3db790e11a6ff44d91f319064b1ee65d2a
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8b9c6f923226ae3a551f607e42fec7c7584a340560704d91efddaa1a3e0555dc
prerequisites:
- getting-started.first-contribution
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
- cpp-tests
- json-load
- lua-contract
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: project-context
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/560
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/getting-started/common-tasks/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/getting-started/common-tasks/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/getting-started/common-tasks/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/getting-started/common-tasks/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/2c899a3db790e11a6ff44d91f319064b1ee65d2a
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/AGENTS.md
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/CONTRIBUTING.md
- path: ai/project-map.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/ai/project-map.yml
- path: ai/test-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/ai/test-matrix.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28getting-started.common-tasks%29%3A+&body=Document+ID%3A+getting-started.common-tasks%0ALanguage%3A+zh_CN%0AVerified+commit%3A+2c899a3db790e11a6ff44d91f319064b1ee65d2a%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 常见贡献任务

先读取根 `AGENTS.md`，再读取最近的子目录说明。下表只负责找到入口；路径与命令仍需
在实际修改的源码 commit 上核对。

| 目标 | 首先检查 | 首个验证 |
| --- | --- | --- |
| 修复 C++ 行为 | 所属 `src/` 类型、调用者、相关 `tests/` | C++ 格式与聚焦 Catch2 测试 |
| 增加 JSON 内容 | 当前相似数据与 loader/factory | JSON 格式、完整加载、ID 检查 |
| 修改 EOC | EOC 数据、解析注册、talker/context 测试 | JSON 加载与聚焦 EOC 解析/测试 |
| 修改 Lua v5 | Manifest Schema、LuaLS、native 注册、清单 | 声明、parity、coverage、示例 |
| 更新捆绑 Mod | `modinfo.json`、依赖、interactions | 加载该 Mod 与受支持组合 |
| 定位构建失败 | 精确平台、preset/options、第一个失败 | 重跑最窄失败阶段 |
| 上游移植 | 精确来源 commit/PR 与 CCB 分歧 | 聚焦行为和兼容检查 |
| 修改文档 | Catalog 条目与声明的源码路径 | 生成/check、strict build、内部链接 |

## 创建 PR 前

- 检查最终 diff 没有无关修改、误改生成文件、缓存、凭据或本机路径。
- 指定 Responsible human，并提供有效 Summary。
- 分开列出 Passed、Failed、Not run，包含平台和准确命令。
- 填写 Documentation impact、Related CCB-Docs PR、Affected documentation IDs
  与 Generated reference impact。
- 兼容敏感变化需明确说明存档、ID、Mod、Lua API 和平台影响。

继续阅读[老贡献者索引](experienced-index.md)、
[项目地图](../architecture/project-map.md)与
[验证快速入门](../validation/quickstart.md)。
