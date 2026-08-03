---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: contributing.json-style
title: 旧文档迁移草稿：json style
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
- doc/JSON/JSON_STYLE.md
- Makefile
- .github/workflows/json.yml
- tools/format/format_main.cpp
- data/AGENTS.md
source_symbols:
- main
source_queries: []
source_fingerprint: 2e3edf2bcd6caff89d938bd434ca37e82b6df033e81ecaff23fa15131a7967d4
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 4fe1f2506669d47a80a90d98abd5945cd586154ebcba021a154ff9f54d27e043
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/json-style/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/json-style/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/json-style/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/json-style/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/JSON_STYLE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/JSON_STYLE.md
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/Makefile
- path: .github/workflows/json.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/workflows/json.yml
- path: tools/format/format_main.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/format/format_main.cpp
- path: data/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/AGENTS.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28contributing.json-style%29%3A+&body=Document+ID%3A+contributing.json-style%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：json style

本页是 `contributing.json-style` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `contributing.json-style`
- Target: `contributing/json-style.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/json-style/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| contributing.json-style | doc/JSON/JSON_STYLE.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 JSON 风格与验证

两空格缩进、稳定字段布局、短数组内联和长结构换行仍由仓库 formatter 决定。不要手工
模仿旧示例来猜格式，也不要使用通用 formatter 重排整个文件；CCB 的 formatter 会读取
项目 JSON 方言并输出项目风格。

### 格式化入口

CI 对全部 JSON 运行：

```sh
make style-all-json-parallel RELEASE=1
```

本地修改少量已纳入检查的文件可运行：

```sh
make style-json
```

formatter 产物由 Makefile 的 `JSON_FORMATTER_BIN` 选择；不同平台可能是
`tools/format/json_formatter.cgi` 或 `.exe`。不要依赖旧的外部网页 formatter。

### 语义验证

```sh
make -j2 json-check
```

格式通过只说明排版正确；`json-check` 还会覆盖加载阶段。修改稳定 ID、`copy-from`、
EOC、item group、mapgen 或 Mod 依赖时，还要运行对应 ID/loader/focused test。Schema 不
完整的 object type 不能因为编辑器不报错就视为有效。

### 编辑原则

- 只格式化本 PR 需要的文件；formatter 产生额外 diff 时逐项检查。
- 从相邻第一方定义确认字段顺序与实际用法，但 required/default 仍以 loader 为准。
- `//` 注释和项目扩展不是标准 JSON；不要用会删除它们的工具。
- 修改生成清单中的文件时运行 generator，不要手改输出。
- PR 记录 formatter、加载检查、Mod 集和任何跳过项。

更完整的数据契约见[JSON 概览](../json/overview.md)与
[继承和 copy-from](../json/inheritance-copy-from.md)。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `d32b9cc880a85480840d82cfa05d256c78a16615`；聚合源指纹为 `2e3edf2bcd6caff89d938bd434ca37e82b6df033e81ecaff23fa15131a7967d4`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/JSON_STYLE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/JSON_STYLE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/JSON_STYLE.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
