---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: content.manual-of-style
title: 旧文档迁移草稿：in game text style
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
- doc/MANUAL_OF_STYLE.md
- CONTRIBUTING.md
- lang/notes/README_all_translators.md
- tools/check_translation_tags.py
- src/translations.cpp
source_symbols: []
source_queries: []
source_fingerprint: 244ffada6751f7de79152d7deb3184f86a104faacef3d810c098fedb28c99917
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 09dd78fdf8505630c5a92724a2b483f3fb3cf1b869329b4967554b9cb0068540
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
risk_group: translation
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/in-game-text-style/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/in-game-text-style/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/in-game-text-style/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/in-game-text-style/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/MANUAL_OF_STYLE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/MANUAL_OF_STYLE.md
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/CONTRIBUTING.md
- path: lang/notes/README_all_translators.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/lang/notes/README_all_translators.md
- path: tools/check_translation_tags.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tools/check_translation_tags.py
- path: src/translations.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/translations.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28content.manual-of-style%29%3A+&body=Document+ID%3A+content.manual-of-style%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：in game text style

本页是 `content.manual-of-style` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `content.manual-of-style`
- Target: `contributing/in-game-text-style.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/in-game-text-style/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| content.manual-of-style | doc/MANUAL_OF_STYLE.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前游戏文本风格

本页规范默认英文源码文本；翻译应遵循目标语言语法、标点和复数规则。文本首先要清晰、
可本地化并符合角色语气，不能为了机械套规则而破坏含义。

### 默认英文

- 通用 UI 与叙述使用 US English；角色对白可以有经过设计的方言。
- 面向玩家的动作通常用第二人称；描述使用 sentence case，并以合适标点结束。
- stat、trait/mutation、scenario、profession、background、proficiency、martial art 与
  CBM 名称按既有同类文本的 title case 规则；普通 item/entity 名通常小写，专名例外。
- 使用 serial comma；省略号使用 Unicode `…`，不要用三个句点代替。
- 对话条件标签保持一致，例如 `[PER 10]`、`[Tailoring 2]`、`[SWEET TOOTH]` 和
  `[Use Stethoscope]`；无对白动作也要写成清晰标签。

### 可本地化性

- 不拼接依赖英文词序的句子；为相同英文、不同含义提供 translation context。
- 数量变化使用 plural API，不手写 English-only singular/plural 分支。
- 保留并核对 `%s`、`%d`、位置参数、format braces、颜色/markup tag 与换行。
- 不要求翻译复制英文大小写、双空格、serial comma 或句子结构。
- 变量、ID、按键 token 与不应翻译的 marker 必须在 translator comment 中解释。

### 名称、品牌与来源

现实品牌或引用仍需符合项目 lore、许可证和内容政策；“可能属于 fair use”不是自动批准。
引用外部文字、图像或名称争议时，在 PR 中提供来源与许可，交给 Responsible human 和
维护者复核。不要复制不兼容项目的 prose。

### 验证

检查提取、translation tag、placeholder parity、invalid PO 与 MO 编译。若文本在 JSON、
C++、EOC 或 Lua 中生成，还要验证实际 UI 宽度、复数、性别/context 和错误路径，而不只
阅读源码字符串。

翻译流程见[翻译指南](../localization/translation-guide.md)。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `244ffada6751f7de79152d7deb3184f86a104faacef3d810c098fedb28c99917`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/MANUAL_OF_STYLE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/MANUAL_OF_STYLE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/MANUAL_OF_STYLE.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
