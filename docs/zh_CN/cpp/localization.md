---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.localization
title: 本地化运行时
language: zh_CN
status: active
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/translations.h
- src/translations.cpp
- src/translation_plural_evaluator.cpp
- tests/translations_test.cpp
- tests/translation_system_test.cpp
source_symbols:
- void set_language( const std::string &lang );
source_queries: []
source_fingerprint: 043f9ef3b03bd2c77c7d33fbc3aede4ec1dbf507413a97c4c2d5f47c2c942acd
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: fbd5ad76270949591110b94bf2403fdedfc905c7fb3bf3f203be6d1583ad0a92
prerequisites:
- architecture.overview
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: localization
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/localization/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/localization/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/localization/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/localization/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: src/translations.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/translations.h
- path: src/translations.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/translations.cpp
- path: src/translation_plural_evaluator.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/translation_plural_evaluator.cpp
- path: tests/translations_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/tests/translations_test.cpp
- path: tests/translation_system_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/tests/translation_system_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.localization%29%3A+&body=Document+ID%3A+cpp.localization%0ALanguage%3A+zh_CN%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 本地化运行时

## 职责

本地化运行时选择语言、加载 catalog、翻译单数/复数与带 context 消息、语言变化时失效
translation cache、提供类型安全 format helper，并支持 JSON 中的 translation value。

## 入口点

阅读 `src/translations.h`、`src/translations.cpp`、`translation` 类型、plural evaluator
与 translation manager。运行时字符串用 `_`；需要时用 context/plural helper；
`translate_marker` 只用于提取而不执行运行时翻译。

## 数据所有权

translation catalog 与 manager cache 拥有本地化查询状态；源码/JSON 拥有稳定英文
message ID/context；UI caller 拥有格式化结果。翻译缓存必须尊重 language-generation counter。

## 依赖

localization 依赖 gettext catalog、locale/path 发现、提取脚本、JSON translation object、
plural rule、`fmt` 类型检查、option、font 和 UI layout。

## 生命周期

源消息提取为 POT，翻译成 PO，编译为 MO，按选择语言加载，使用时缓存；`set_language`
改变 generation 时缓存失效。

## 不变量

message/context/plural key 稳定；翻译 placeholder 一致；format 参数类型正确；marker-only
字符串显示前已翻译；切换语言不能返回旧语言 cache entry。

## 扩展点

新用户可见字符串使用合适 helper，英文有歧义时添加 translator context。plural/context
API 集中增加，不能手工拼接字符串。

## 序列化

保存 owning contract 要求的稳定 ID 或源语言值，不保存渲染文本。语言选择属于用户配置，
运行时 translation cache 重建。

## 测试

使用 translation-system/translations 测试与提取/构建检查，覆盖 context、plural count、
format placeholder、语言 cache 失效、JSON translation value 和 LOCALIZE 开/关构建。

## 性能

渲染到处调用 translation。保持局部 cache 与 generation 失效，避免循环重复 format；
没有 token 不能跨语言变化缓存。

## CCB 差异

CCB 有自己的消息、项目名、Lua UI 字符串、Android resource 与 catalog。上游翻译不能
替换或覆盖 CCB 专属 context。

## 技术债务

gettext macro、typed `translation`、JSON 形式、Android resource 与 Lua i18n 并存。
应记录并测试各自提取和失效边界。
