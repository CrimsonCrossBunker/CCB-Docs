---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: how-to.json-tools
title: 旧文档迁移草稿：tools
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
- doc/JSON/JSON_TOOLS.md
- tools/json_tools/keys.py
- tools/json_tools/values.py
- tools/json_tools/pluck.py
- tools/json_tools/table.py
- tools/json_tools/lister.py
source_symbols:
- main
source_queries: []
source_fingerprint: b2259289218e6d63d58941659c741afac360e4de7237e3ddea74b894278277b6
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 20b16ba7efc824d39b91c9594c849c2c44c476f0f3621774ed7ff34b01518f41
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
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/json/tools/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/json/tools/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/how-to/json/tools/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/json/tools/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/JSON_TOOLS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_TOOLS.md
- path: tools/json_tools/keys.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tools/json_tools/keys.py
- path: tools/json_tools/values.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tools/json_tools/values.py
- path: tools/json_tools/pluck.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tools/json_tools/pluck.py
- path: tools/json_tools/table.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tools/json_tools/table.py
- path: tools/json_tools/lister.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tools/json_tools/lister.py
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28how-to.json-tools%29%3A+&body=Document+ID%3A+how-to.json-tools%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：tools

本页是 `how-to.json-tools` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `how-to.json-tools`
- Target: `how-to/json/tools.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/json/tools/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| how-to.json-tools | doc/JSON/JSON_TOOLS.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## JSON 工具按任务选择

仓库工具分为 formatter、loader/validator、只读查询和迁移脚本。先运行 `-h` 并用
`git diff --name-only` 限定范围；查询输出不是契约，批量转换必须审阅每个 changed file。

### 格式与加载

```sh
make -j2 tools/format/json_formatter.cgi RELEASE=1
tools/format/json_formatter.cgi path/to/changed.json
make -j2 json-check
```

项目 formatter 理解 CCB JSON dialect；不要用通用 formatter 删除 comment 或重排整个仓库。
`json-check` 验证 core load，Mod 还需真实 `--check-mods`。

### 查询 keys/values

`tools/json_tools/keys.py` 统计匹配对象出现的字段，`values.py` 统计一个 key 的值；二者支持
`key=value` filter、`--human` 和 nested dotted key。示例：

```sh
tools/json_tools/keys.py --human type=TOOL
tools/json_tools/values.py --key material --human type=TOOL
```

统计中的 MISSING 只表示样本没显式写，不代表 loader 没有 default 或字段非法。用 inventory
定位 handler，再查源码 requiredness。

### 生成与专项工具

`tools/json_api/generate_contracts.py` 生成 object/EOC inventory；`copy_from.py`、
`dialogue_validator.py` 和 `json_tools/*` 只用于其 help 声明的结构。任何 rewrite 前建立
窄文件清单、保留 commit、先 dry-run/临时 worktree，再用 owner formatter 和 loader 验证。
不要对第三方、generated 或全部 `data/` 运行“顺手清理”。

### 可审核输出

PR 记录命令、输入 path/filter、工具 commit、changed file 数与验证。若工具报 load error，
先修首个输入错误；不要把部分统计当完整结果。用于决策的报告应保存为 CI artifact，只有
项目清单明确要求的生成 reference 才提交。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `b2259289218e6d63d58941659c741afac360e4de7237e3ddea74b894278277b6`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/JSON_TOOLS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_TOOLS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_TOOLS.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
