---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: resources.translation
title: 翻译流程
language: zh_CN
status: active
doc_type: how-to
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
last_human_reviewer: Pending human review
source_paths:
- doc/TRANSLATING.md
- .github/workflows/build-translations.yml
- lang/Makefile
- src/translations.h
source_symbols:
- void set_language( const std::string &lang );
source_queries:
- Build translations
source_fingerprint: 09f0ec9bd9d56b14fe677429ecab24bab4ac8188de480617c458cddea7a415bf
authority: build-config
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 0dcd4aa5a5b6b21e0a16bb655b6b37c976bb11b76c00a5b867d211cc459ee31b
prerequisites:
- cpp.localization
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
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/resources/translation/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/resources/translation/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/resources/translation/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/resources/translation/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: doc/TRANSLATING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/doc/TRANSLATING.md
- path: .github/workflows/build-translations.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/.github/workflows/build-translations.yml
- path: lang/Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/lang/Makefile
- path: src/translations.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/translations.h
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28resources.translation%29%3A+&body=Document+ID%3A+resources.translation%0ALanguage%3A+zh_CN%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 翻译流程

本页描述生产 translation asset；运行时 localization 语义另有页面，这里以构建文件与
translation workflow 为权威。

## 从源码到运行时

1. C++ 字符串使用 translation helper，受支持 JSON type 使用 `translation` field；
2. `lang/update_pot.sh` 与 JSON extractor 生成源模板；
3. 译者在已配置 CCB Transifex project 工作；
4. `.github/workflows/build-translations.yml` 拉取 PO、拒绝无效条目、更新统计、编译 MO，
   并发布 translation artifact；
5. 各平台 build 消费 artifact，`src/translations.*` 选择并缓存语言。

## 贡献规则

有歧义英文使用 context，计数消息使用 plural helper。保持 placeholder、markup token、
换行与语义 context 稳定。不要手改明确标为 generated 的文件，也不要用上游 resource
名称替换 CCB 项目身份。

## 本地检查

仓库聚焦编译入口为：

```sh
make -C lang -j2
```

提取与完整 catalog refresh 可能触碰大量文件和外部 translation state；按修改运行准确
workflow，审查 PO/POT diff；没有 credential 与 log 时不能声称完成 Transifex pull。

## 验证

检查 extraction、invalid PO handling、MO compilation、placeholder parity、plural/context、
localized build 与窄宽度代表性 UI。Android resource string 与 Lua i18n 是额外 pipeline，
修改时单独验证。

## 归属与维护

保留译者 credit 与来源。translation service credential 只放 repository secret。外部拉取
失败不能靠发布空/旧 artifact 隐藏；复用可信默认分支 artifact 必须在 CI log 明示。
