---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: mod-localization
title: 旧文档迁移草稿：localization
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
last_human_reviewer: Pending human review
source_paths:
- doc/TRANSLATING_MOD.md
- lang/extract_json_strings.py
- lang/string_extractor/parsers/mod_info.py
- src/translations.cpp
source_symbols: []
source_queries: []
source_fingerprint: f8453df6b1f08b138e9ebb0f9a0cb63166baaa2c3d1d5a209db8ddea561bfaee
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: cc89212b81f0325106aa5b8a410fc7eb79f2bbc965a261f968a8944454cd4ccc
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
risk_group: localization
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/modding/localization/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/modding/localization/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/modding/localization/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/modding/localization/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/TRANSLATING_MOD.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/TRANSLATING_MOD.md
- path: lang/extract_json_strings.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/lang/extract_json_strings.py
- path: lang/string_extractor/parsers/mod_info.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/lang/string_extractor/parsers/mod_info.py
- path: src/translations.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/translations.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28mod-localization%29%3A+&body=Document+ID%3A+mod-localization%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：localization

本页是 `mod-localization` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `mod-localization`
- Target: `modding/localization.md`
- Replacement: mod-localization
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| mod-localization | doc/TRANSLATING_MOD.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | mod-localization |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Mod 本地化流程

CCB JSON 的可翻译字段由 `lang/string_extractor` 规则决定，不是看到字符串就自动提取。
先使用结构化 translation object、plural 与 context，再生成 POT；不要在运行时拼接依赖
英文语序的句子。

### 提取模板

在 CCB 根目录为一个位于 `mods/demo` 的外部 Mod 建立空 reference POT，然后调用当前脚本：

```sh
mkdir -p mods/demo/lang/po
: > mods/demo/lang/po/demo.pot
python3 lang/extract_json_strings.py -i mods/demo -n demo -r mods/demo/lang/po/demo.pot
msgfmt -c -o /dev/null mods/demo/lang/po/demo.pot
```

当前脚本使用 `-r/--reference` 追加并规范模板，没有旧文档中的 `-o` 选项。每次 JSON
字段、ID、context 或 plural 变化都重新生成并审阅 diff；POT 中缺失字符串时先检查 object
type 与 extractor 规则，不要手写一份脱离源码的 msgid。

### 建立 PO 与翻译

```sh
msginit -i mods/demo/lang/po/demo.pot -o mods/demo/lang/po/zh_CN.po -l zh_CN
```

翻译必须保持 printf/fmt 参数、位置参数、颜色/markup tag、换行、gender/context 与 plural
含义。译者注释解释变量、不可翻译 ID 和 UI 限制；不要要求所有语言复制英文大小写、词序
或复数规则。更新模板时使用 gettext merge 流程保留已有翻译，不用覆盖 PO。

### 编译与安装布局

```sh
mkdir -p mods/demo/lang/mo/zh_CN/LC_MESSAGES
msgfmt -c -o mods/demo/lang/mo/zh_CN/LC_MESSAGES/demo.mo mods/demo/lang/po/zh_CN.po
```

当前 translation manager 在用户 Mod 根目录递归发现 `LC_MESSAGES`，并读取其中 `.mo`；
语言目录名必须与游戏选择的 language code 一致。发布包至少携带需要的 `.mo` 与 Mod
内容；是否同时发布 POT/PO 由项目协作和许可证策略决定，但必须保留可维护来源。

### 验证

对 POT 和每个 PO 运行 `msgfmt -c`，检查提取 diff、placeholder/tag parity 和无效 Unicode；
把 Mod 安装到真实用户 Mod 目录，在英文与目标语言分别启动、加载世界并检查 Mod name、
description、item plural、dialogue、EOC message 和 Lua UI 文本。还要验证目标语言缺失时
安全回退原文，且同 msgid 不同含义已使用 context。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `f8453df6b1f08b138e9ebb0f9a0cb63166baaa2c3d1d5a209db8ddea561bfaee`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/TRANSLATING_MOD.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/TRANSLATING_MOD.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/TRANSLATING_MOD.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
