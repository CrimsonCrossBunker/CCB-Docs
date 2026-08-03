---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: migration.filtered-history-experiment
title: 过滤历史实验
language: zh_CN
status: active
doc_type: explanation
audiences:
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 365
last_human_reviewer: LYHGLYTX
source_paths:
- doc/migration/markdown-inventory.yml
- doc/migration/history-assessment.md
source_symbols: []
source_queries: []
source_fingerprint: cf5cd52677add7164774c34104c2d497d1bc57876339a9ed8d65f4a201baa2ea
authority: historical
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 996eb67a61f7df858a29a9f97946e328b2e9428c152b5772a45e8ab96e7c7e33
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB migration experiment; no repository history was imported.
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: migration-history
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/migration/filtered-history-experiment/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/migration/filtered-history-experiment/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/migration/filtered-history-experiment/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/migration/filtered-history-experiment/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/migration/markdown-inventory.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/migration/markdown-inventory.yml
- path: doc/migration/history-assessment.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/migration/history-assessment.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28migration.filtered-history-experiment%29%3A+&body=Document+ID%3A+migration.filtered-history-experiment%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 过滤历史实验

## 结果

对最终选择的路径进行了临时、隔离的 `git-filter-repo` 实验；没有把过滤仓库
导入或推送到 CCB-Docs。

| 指标 | 结果 |
| --- | ---: |
| 选择的最终路径 | 111 |
| 自包含仓库大小 | 14 MiB |
| Commit | 1351 |
| Author identity | 226 |
| 最终路径 | 111 |
| Rename record | 0 |
| `git fsck` | passed |

## 决策

实验仓库虽然自包含且通过 `git fsck`，但没有保留可审核的 rename record，
直接导入还会把迁移页面与主仓库历史耦合。因而本阶段不导入整个游戏仓库历史，
也不导入该过滤仓库；每页保留 CCB source URL、source commit、已清洗贡献者和
许可证。以后只有在 Responsible human 审查作者映射、重命名语义和许可后，
才可另行决定是否导入选择路径的历史。

本实验只使用 Git 对象和明确路径，没有遍历 `obj-lua/` 或其他未跟踪构建缓存。
