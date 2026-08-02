---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: mods.in-repository-policy
title: 旧文档迁移草稿：in repository policy
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
- doc/IN_REPO_MODS.md
- CONTRIBUTING.md
- GOVERNANCE.md
- data/mods/AGENTS.md
- src/mod_manager.cpp
- tools/load_all_mods.sh
source_symbols:
- mod_manager::load_modfile
source_queries: []
source_fingerprint: 0e75c77124cf84a936f3bd2f6e19b29d2e7e067eae2b27963fe90dca28aa828e
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 182c359934f568b9b713df6ad8d700d62a0fd053f26470c2bf6318e1a152e457
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
risk_group: mods
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/mods/in-repository-policy/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/mods/in-repository-policy/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/mods/in-repository-policy/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/mods/in-repository-policy/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/IN_REPO_MODS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/IN_REPO_MODS.md
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/CONTRIBUTING.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/GOVERNANCE.md
- path: data/mods/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/mods/AGENTS.md
- path: src/mod_manager.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/mod_manager.cpp
- path: tools/load_all_mods.sh
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tools/load_all_mods.sh
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28mods.in-repository-policy%29%3A+&body=Document+ID%3A+mods.in-repository-policy%0ALanguage%3A+zh_CN%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：in repository policy

本页是 `mods.in-repository-policy` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `mods.in-repository-policy`
- Target: `mods/in-repository-policy.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/mods/in-repository-policy/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| mods.in-repository-policy | doc/IN_REPO_MODS.md | migrate_rewrite | stubbed | b1ee97987589450da70f30ee2feed12c9d18f479 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## CCB 仓库内 Mod 政策

随游戏发布能提高可见度、统一 Issue/PR 与持续加载检查，但同时把兼容性、发布和安全负担
交给整个项目。进入 `data/mods/` 不是永久收录、核心团队维护保证或作者的专属控制权。
仓库内 Mod 仍是可由社区贡献的项目内容。

### 收录条件

提案必须说明清晰且可长期审阅的目的，例如独立内容体验、可访问性/界面能力，或为仍在
开发的可选功能提供隔离。只堆积无关对象、单纯关闭正常功能或没有维护边界的偏好包不足以
证明仓库级维护成本合理。

收录前至少需要：

- `modinfo.json` 中准确的 authors、真实 GitHub maintainer、category、dependencies 与 conflicts；
- 来源、许可证和第三方资产授权可审核；
- 稳定 ID、存档策略、依赖边界和与 CCB/上游的差异明确；
- JSON/EOC/Lua 与完整 Mod 加载验证通过；
- 一个愿意持续进行分类、审阅和兼容跟进的活跃 curator；
- 依赖其他仓库内 Mod 时，与依赖方维护者确认新增维护负担。

不要用推测的 `CODEOWNERS` 代替真实负责人。`maintainers` 是 loader 读取并展示的账号集合，
但治理责任仍需人在 PR/Issue 中明确接受。

### Curator 的责任

Curator 判断贡献是否符合 Mod 目标，审阅或请求修改相关 PR，并至少回应缺陷报告、帮助确定
修复路径。Curator 不必亲自写完每个修复，也不能阻止其他人贡献；其批准是领域意见，最终
合并仍遵循 CCB 仓库治理、Responsible human 和 required checks。

影响依赖方、公共 ID、存档、Lua API、许可证或玩家安全的修改，需要同时通知相关维护者并
提供针对组合的测试。内容平衡争议与加载错误应分开记录，避免“能加载”被当成设计批准。

### Orphan、obsolete 与移除

维护者长期不可达、反复破坏发布、许可不明、目标已经失效或维护成本无法控制时，维护者可
启动 orphan/obsolete 评审。先建立带负责人和期限的公开 Issue；不要仅凭一次未回复自动
删除。`obsolete: true` 会阻止新世界选择，但保留旧存档识别，不等同于立即从仓库删除。

救援路径是确认新的 curator、清理阻塞缺陷、恢复验证并更新 `maintainers`。最终移除前必须
记录稳定 ID、旧世界影响、替代项、迁移/obsoletion 数据和发布说明。

### Modmod

修改其他仓库内 Mod 的 Mod 也必须形成有目标的独立体验、具备维护者并验证依赖组合；微小
偏好补丁不足以自动收录。分类和依赖按当前 `modinfo.json`/UI 注册值决定，不复制旧文档中
可能已经变化的类别清单。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `0e75c77124cf84a936f3bd2f6e19b29d2e7e067eae2b27963fe90dca28aa828e`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/IN_REPO_MODS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/IN_REPO_MODS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/IN_REPO_MODS.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
