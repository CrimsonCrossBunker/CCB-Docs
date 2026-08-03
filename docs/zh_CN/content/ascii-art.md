---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: content.ascii-art
title: 旧文档迁移草稿：ascii art
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
- doc/ASCII_ART.md
- src/ascii_art.cpp
- src/ascii_art.h
- src/init.cpp
- data/json/ascii_art/generic_ascii.json
- data/json/bodypart_graphs/arms.json
source_symbols:
- ascii_art::load_ascii_art
source_queries: []
source_fingerprint: 0afe16155bd5222bc296b0fce0ce7f0ae1ec8128c917b6389af86ec01b992db2
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 5a4934117f0493f80b82207d8511d402dba0eccb08f799ba86d8ef417ab3ec42
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
risk_group: ui
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/content/ascii-art/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/content/ascii-art/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/content/ascii-art/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/content/ascii-art/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/ASCII_ART.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/ASCII_ART.md
- path: src/ascii_art.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/ascii_art.cpp
- path: src/ascii_art.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/ascii_art.h
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/init.cpp
- path: data/json/ascii_art/generic_ascii.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/ascii_art/generic_ascii.json
- path: data/json/bodypart_graphs/arms.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/bodypart_graphs/arms.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28content.ascii-art%29%3A+&body=Document+ID%3A+content.ascii-art%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：ascii art

本页是 `content.ascii-art` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `content.ascii-art`
- Target: `content/ascii-art.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/content/ascii-art/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| content.ascii-art | doc/ASCII_ART.md | migrate_rewrite | stubbed | 5f23722ff28c5cc552baa0422b32b1f10fd890fa | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## ASCII art 数据契约

第一方 ASCII art 使用 JSON `ascii_art` 对象，至少包含稳定 `id` 和字符串数组 `picture`。当前
`ascii_art::load` 会去除颜色标签后按终端显示宽度计算每一行；超过 `41` 个显示列的行会被截断并产生
debug message。这里的“列”不是 UTF-8 字节数，宽字符、组合字符和颜色标签都需要用实际 loader 验证。

```json
{
  "type": "ascii_art",
  "id": "example_art",
  "picture": [ "<color_white>+---+</color>", "<color_white>|   |</color>" ]
}
```

上例只展示结构，不是待提交资源。使用现有有效 color name，并正确闭合标签。空行、前导空格和 Unicode
线框字符是画面的一部分；通用 JSON formatter 之外的文本处理可能破坏对齐。Body-part graph 位于另一
类数据和显示路径，不能仅因为外观相似就假定尺寸与字段完全相同。

## 制作与审查

任何能保留 UTF-8、空格和逐行文本的编辑器都可使用；REXPaint 只是可选工具，不是项目契约。外部 palette、
字体或模板必须确认来源和许可证，不能直接把来源不明的图案带入仓库。

提交前运行项目 JSON formatting/loading，检查重复 ID、无效颜色标签和 debug 输出，并在实际目标界面测试
curses/tiles、默认及 fallback 字体、窄窗口、缩放和中英文环境。检查每行去标签后的显示宽度，而不是只看
编辑器画布。ASCII art 不能成为识别物品或身体部位状态的唯一信息；无障碍路径仍需文字或结构替代。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `d32b9cc880a85480840d82cfa05d256c78a16615`；聚合源指纹为 `0afe16155bd5222bc296b0fce0ce7f0ae1ec8128c917b6389af86ec01b992db2`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/ASCII_ART.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/ASCII_ART.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/ASCII_ART.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
