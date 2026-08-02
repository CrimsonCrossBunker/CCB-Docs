---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: contributing.documentation-policy
title: 文档政策
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
last_human_reviewer: LYHGLYTX
source_paths:
- AGENTS.md
- GOVERNANCE.md
- ai/docs-impact.yml
- ai/generated-files.yml
- doc/migration/markdown-inventory.schema.json
source_symbols: []
source_queries: []
source_fingerprint: a87652454f8510f8dd848407578911d0871417d705013890da8bc337746e6142
authority: governance
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: ee1276aca890ccb3f8a63b9de838456c4891374680e5cf75988966a1a860b78e
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
risk_group: documentation-policy
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/documentation-policy/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/documentation-policy/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/documentation-policy/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/documentation-policy/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/AGENTS.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/GOVERNANCE.md
- path: ai/docs-impact.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/ai/docs-impact.yml
- path: ai/generated-files.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/ai/generated-files.yml
- path: doc/migration/markdown-inventory.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/migration/markdown-inventory.schema.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28contributing.documentation-policy%29%3A+&body=Document+ID%3A+contributing.documentation-policy%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 文档政策

CCB-Docs 是正式的教程、解释、架构、参考与导航站，但它不与游戏仓库平分权威。

## 权威模型

| 主题 | 权威来源 |
| --- | --- |
| 运行时行为 | CCB 源码与测试 |
| JSON、Lua 与 API 契约 | Schema、LuaLS 声明、注册、生成清单 |
| 构建与验证 | CI、CMake、Makefile、Gradle、仓库验证器 |
| 贡献与治理 | CCB `AGENTS.md`、`CONTRIBUTING.md`、`GOVERNANCE.md` |
| 解释与导航 | CCB-Docs，并按上述来源核验 |

正文与源码契约冲突时，必须将页面标为 stale、移出 AI 索引并修复。不得为了匹配
文档而改变运行时行为。

## 双语发布

新 active 页面首次发布必须同时有中文和英文。中文更新后，英文可标记
`translation-stale` 最多 30 天并自动建立跟踪 Issue。逾期只阻止修改该双语对或
同一高风险文档子系统的 PR，不阻止无关修复。未完成双语的迁移页面保持 draft，
不进入正式导航、搜索与 AI 索引。

## 源码漂移与生成内容

每页声明精确 `source_paths`、核验 commit/日期和 fingerprint。只有这些路径变化才
构成漂移；`master` 的任意 commit 不会让全部页面 stale。无实际变化不得创建 Bot
PR；漂移更新合并为一个 PR，经人类审阅，绝不自动合并。

`docs-catalog.yml` 是唯一手工维护的机器目录，并生成导航、双语映射、搜索/AI/归档
策略、redirect、sitemap 元数据、`llms.txt` 与 JSON 索引。应修改 catalog 或
生成器，不得手改派生索引。

## 旧路径

迁移后的仓库路径永久保留轻量双语 moved stub。六个月后可删除旧正文，但历史 PR、
Issue、Fork 与外部链接仍必须能通过稳定文档 ID 到达当前中英文页面。
