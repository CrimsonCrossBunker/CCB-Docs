---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: translation-guide
title: 旧文档迁移草稿：translation guide
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
- doc/TRANSLATING.md
- lang/Makefile
- src/translations.cpp
- .github/workflows/build-translations.yml
- .github/workflows/push-translation-template.yml
- src/translation_manager.cpp
- lang/notes/README_all_translators.md
- lang/update_pot.sh
source_symbols:
- TranslationManager::LoadDocuments
source_queries: []
source_fingerprint: 007ab64d80f8144fed21e6e91734d861c684c40ef5a68677e458368084ebe848
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 1ac2edc19ce192cee8314b5e77d4757706f3c4c26b2eb0b593ab1bd0eb075254
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- legacy.lang-notes-readme-all-translators
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LunaGlaze, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: localization
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/localization/translation-guide/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/localization/translation-guide/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/localization/translation-guide/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/localization/translation-guide/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/TRANSLATING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/TRANSLATING.md
- path: lang/Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/lang/Makefile
- path: src/translations.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/translations.cpp
- path: .github/workflows/build-translations.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/.github/workflows/build-translations.yml
- path: .github/workflows/push-translation-template.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/.github/workflows/push-translation-template.yml
- path: src/translation_manager.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/translation_manager.cpp
- path: lang/notes/README_all_translators.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/lang/notes/README_all_translators.md
- path: lang/update_pot.sh
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/lang/update_pot.sh
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28translation-guide%29%3A+&body=Document+ID%3A+translation-guide%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：translation guide

本页是 `translation-guide` 的迁移草稿页面。它记录 **2** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `translation-guide, legacy.lang-notes-readme-all-translators`
- Target: `localization/translation-guide.md`
- Replacement: translation-guide
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| translation-guide | doc/TRANSLATING.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |
| legacy.lang-notes-readme-all-translators | lang/notes/README_all_translators.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | translation-guide |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## CCB 本地化流程

CCB 使用 gettext、source extraction、PO 与编译后的 MO。运行时行为以 `translations.cpp` 为准，
JSON extraction 以 `lang/` scripts 为准，远端同步以当前 translation workflows 和 Transifex CCB
project 为准。旧 `cataclysm-dda` resource 名或论坛说明不能覆盖当前 `.tx/config`。

### 开发者

简单 C++ literal 用 `_()`；有歧义时用 context；数量使用 plural API。需要延迟翻译、JSON context
或 plural 的数据用 `translation`/`to_translation`/`pl_translation`，在展示时调用 `translated()`。
不要在 global/local static 初始化时缓存已翻译字符串，否则初始化顺序或运行时换语言会出错。
Debug/error 文本保持可复制的原文，除非其明确属于 player-facing contract。

JSON translator comment 使用 loader 支持的 `//~`/translation object 形式。占位符、位置参数、
markup、gender context、key tags 和换行必须保持等价；不要拼接依赖英语词序的句子。新增 extraction
形态时同时更新 extractor 与测试。

### 构建与验证

当前本地 MO 入口是：

```sh
make -C lang LANGUAGES=zh_CN
```

或使用仓库脚本生成 POT、验证/合并 PO、更新 stats 和编译 MO；具体名称从当前 `lang/` 与 CI
读取。CI 的 build-translations workflow 有 TX token 时拉取、丢弃无效 PO、更新统计并编译；无
token 时复用可信 master artifact。Experimental Release 成功后另一个 workflow 生成 POT 并向
Transifex 推送 source template。

验证 extraction diff、POT/PO 格式、placeholder/plural/context parity、`msgfmt`、语言切换、fallback、
UI 宽度和目标平台字体。不要手改生成 MO；Transifex 写操作需要维护者凭据和人工审查。

## 历史与归属

清单中的已接受贡献者为：LunaGlaze, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `007ab64d80f8144fed21e6e91734d861c684c40ef5a68677e458368084ebe848`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/TRANSLATING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/TRANSLATING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/TRANSLATING.md)
- [`lang/notes/README_all_translators.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/lang/notes/README_all_translators.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/lang/notes/README_all_translators.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
