---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: compatibility.save
title: 存档兼容
language: zh_CN
status: active
doc_type: explanation
audiences:
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- CONTRIBUTING.md
- doc/JSON/OBSOLETION_AND_MIGRATION.md
- src/savegame.cpp
- src/savegame_json.cpp
- src/savegame_legacy.cpp
- src/worldfactory.cpp
source_symbols: []
source_queries: []
source_fingerprint: 94e740aebf8849eb1db050a8e428d16a143a424fe541546638c138d1dc759176
authority: source-and-tests
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: e09ef4b70f339892b6a214edaf933da9ada135e574dcd2acdbc2df204acf345d
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
risk_group: compatibility
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/compatibility/save/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/compatibility/save/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/compatibility/save/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/compatibility/save/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/CONTRIBUTING.md
- path: doc/JSON/OBSOLETION_AND_MIGRATION.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/OBSOLETION_AND_MIGRATION.md
- path: src/savegame.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/savegame.cpp
- path: src/savegame_json.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/savegame_json.cpp
- path: src/savegame_legacy.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/savegame_legacy.cpp
- path: src/worldfactory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/worldfactory.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28compatibility.save%29%3A+&body=Document+ID%3A+compatibility.save%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 存档兼容

存档数据是公共兼容边界。新建世界能运行并不代表修改完成；还必须检查旧世界、稳定
ID、序列化对象所有权和失败恢复。

## 评审清单

1. 找出所有受影响的序列化字段、所属类型和加载路径。
2. 明确最旧受支持表示，并确认缺失字段是否已有安全默认值。
3. 保持 JSON ID 稳定。重命名或删除时使用仓库支持的 migration/obsoletion 机制，
   不得静默复用旧 ID。
4. 只在代表性存档的副本上测试，绝不把用户唯一存档当迁移 fixture。
5. 验证保存、加载、再次保存/加载以及受影响操作。只成功解析一次仍可能留下失效状态。
6. 在 PR 和发布说明中明确记录不兼容变化。

## 失败处理

不要吞掉 loader error 来伪装旧存档可用。保留第一个诊断和足以定位对象所有者的
上下文，同时移除个人路径或数据。迁移应当确定、尽量幂等，并由聚焦回归测试覆盖。

本页 verified commit 的 `savegame*` 与 `worldfactory` 实现是运行时权威；旧说明只
解释概念，不能覆盖当前序列化源码和测试。
