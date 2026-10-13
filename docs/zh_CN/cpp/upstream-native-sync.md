---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.upstream-native-sync
title: 原生行为同步草稿
language: zh_CN
status: draft
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- mod-author
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: Pending human review
source_paths:
- src/activity_actor.cpp
- src/activity_actor_definitions.h
- src/event.h
- src/regional_settings.h
- src/weather.cpp
- src/main.cpp
source_symbols: []
source_queries: []
source_fingerprint: 45bdb293e00ff84398ec125d6248085114b5a679525856dd868880016f4fd031
authority: api-contract
verified_commit: b071fca094b716cf409dd1ba74c90581b5fe63de
verified_at: '2026-10-14'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a4a5f3472a5a864373bb97cbc37b8bd6a59553236f7e75364077415f0774f222
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- lua-contract
api_version: '1'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/996
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/upstream-native-sync/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/upstream-native-sync/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/upstream-native-sync/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/upstream-native-sync/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/b071fca094b716cf409dd1ba74c90581b5fe63de
source_urls:
- path: src/activity_actor.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b071fca094b716cf409dd1ba74c90581b5fe63de/src/activity_actor.cpp
- path: src/activity_actor_definitions.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b071fca094b716cf409dd1ba74c90581b5fe63de/src/activity_actor_definitions.h
- path: src/event.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b071fca094b716cf409dd1ba74c90581b5fe63de/src/event.h
- path: src/regional_settings.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b071fca094b716cf409dd1ba74c90581b5fe63de/src/regional_settings.h
- path: src/weather.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b071fca094b716cf409dd1ba74c90581b5fe63de/src/weather.cpp
- path: src/main.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b071fca094b716cf409dd1ba74c90581b5fe63de/src/main.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.upstream-native-sync%29%3A+&body=Document+ID%3A+cpp.upstream-native-sync%0ALanguage%3A+zh_CN%0AVerified+commit%3A+b071fca094b716cf409dd1ba74c90581b5fe63de%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 原生行为同步草稿

本页对应 CCB #996，尚未合并，完整组合验收仍在进行。

## CCB 适配

门操作使用新的可保存活动。场景菜单也进入活动入口；联机预测和服务器确认需要即时结果时，执行同一活动的检查与完成逻辑，并把耗时扣给实际操作者。它不应替换角色原有活动，也不把远端角色的耗时扣到本地玩家。开门位置与载具归属检查使用实际操作者。

Marloss/Mycus 改动保留四个已有物品回调和稳定 EOC ID。区域 NPC 生成倍率作用于 CCB 原有频率选项。新事件追加到原有事件枚举末端，避免改变已有数值。启动拆分保留 CCB 的联机、回放、Android 和条件 Mod 加载流程。

新增天气、峡谷底部地形、装备容量和效果条件等契约，以本 PR 的源码和生成清单为准。Platform v1 仍是唯一 Lua 编写入口；此次没有另设兼容运行时，也没有把原生条件的可用性写成完整 Lua 玩法迁移。

## 验证范围

共享依赖排序回归已验证修复前失败、修复后通过。数学前置的两个案例、20 条断言通过；士气验证覆盖读取，不能声称赋值通过。台账原生能力与完整选择器迁移的证据规则分开检查。

整组原生代码与制作、渲染、数据的匹配编译和玩法测试尚待组合验收。生成清单或 CI 草稿检查通过不等同于所有平台编译和旧存档兼容通过。

Responsible human: LYHGLYTX.
