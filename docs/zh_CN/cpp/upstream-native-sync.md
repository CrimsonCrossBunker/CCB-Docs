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
- src/lua_platform_runtime_services.cpp
- src/veh_type.cpp
- src/character_inventory.cpp
- src/recipe_dictionary.cpp
- tests/lua_platform_environment_predicate_test.cpp
- tests/lua_platform_effects_test.cpp
source_symbols: []
source_queries: []
source_fingerprint: a80d78267dc97036358b0302ad889a4043deaf8d31273adcb26ecbb070591d10
authority: api-contract
verified_commit: eb8bfeabd8748176cc33aa2329b634d17bb61885
verified_at: '2026-10-14'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: e8b0038844e89009ee18be20605c85e55b3a7694f20777597de133e4318495c8
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/1000
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/upstream-native-sync/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/upstream-native-sync/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/upstream-native-sync/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/upstream-native-sync/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/eb8bfeabd8748176cc33aa2329b634d17bb61885
source_urls:
- path: src/activity_actor.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/activity_actor.cpp
- path: src/activity_actor_definitions.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/activity_actor_definitions.h
- path: src/event.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/event.h
- path: src/regional_settings.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/regional_settings.h
- path: src/weather.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/weather.cpp
- path: src/main.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/main.cpp
- path: src/lua_platform_runtime_services.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/lua_platform_runtime_services.cpp
- path: src/veh_type.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/veh_type.cpp
- path: src/character_inventory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/character_inventory.cpp
- path: src/recipe_dictionary.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/recipe_dictionary.cpp
- path: tests/lua_platform_environment_predicate_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/tests/lua_platform_environment_predicate_test.cpp
- path: tests/lua_platform_effects_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/tests/lua_platform_effects_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.upstream-native-sync%29%3A+&body=Document+ID%3A+cpp.upstream-native-sync%0ALanguage%3A+zh_CN%0AVerified+commit%3A+eb8bfeabd8748176cc33aa2329b634d17bb61885%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 原生行为同步草稿

本页对应 CCB #996，尚未合并，组合验收已完成下文列明的范围。

## CCB 适配

门操作使用新的可保存活动。场景菜单也进入活动入口；联机预测和服务器确认需要即时结果时，执行同一活动的检查与完成逻辑，并把耗时扣给实际操作者。它不应替换角色原有活动，也不把远端角色的耗时扣到本地玩家。开门位置与载具归属检查使用实际操作者。

Marloss/Mycus 改动保留四个已有物品回调和稳定 EOC ID。区域 NPC 生成倍率作用于 CCB 原有频率选项。新事件追加到原有事件枚举末端，避免改变已有数值。启动拆分保留 CCB 的联机、回放、Android 和条件 Mod 加载流程。

新增天气、峡谷底部地形、装备容量和效果条件等契约，以本 PR 的源码和生成清单为准。Platform v1 仍是唯一 Lua 编写入口；此次没有另设兼容运行时，也没有把原生条件的可用性写成完整 Lua 玩法迁移。

## 验证范围

共享依赖排序回归已验证修复前失败、修复后通过。数学前置的两个案例、20 条断言通过；士气验证覆盖读取，不能声称赋值通过。台账原生能力与完整选择器迁移的证据规则分开检查。

Clang 23、Release、C++17、SDL3、图块、声音、zh_CN 和唯一 Lua Platform v1 配置下，组合分支 #1000 的匹配游戏和测试程序编译成功。有效测试范围共 992 个案例：宽范围运行通过 991 个，另一个可见 NPC 案例暴露测试初始化的视距缓存假设；修正后 Lua 与视距组合的 528 个案例、86,021 条断言通过。六个集成回归的 2,567 条断言通过。这是分范围证据，不能表述为同一次进程通过全部 992 个案例。

新程序对基础游戏及全部 18 个受影响且未废弃 Mod 的独立加载检查全部通过（共 19 个身份），包括 MoM 新维度和流亡族数据。加载检查不能证明全部新增玩法、旧存档、真实 GPU、所有桌面平台或 Android 设备已通过。

组合适配还统一了 Lua 与原生负数陷阱半径的空结果，避免旧接口保留单点的差异。供弹判定只排除液体燃料弹匣井，辅助电池弹匣井不阻止直接油箱供弹；原有加压油管的装填规则仍然保留。

历史清单中只排除了明确拒绝的 20 项。其余 248 项中，233 项已处理或确认为已有等价实现；15 项调料、归属、旧物品集、肖像对话和帮助界面内容仍保留待审，不代表拒绝。

Responsible human: LYHGLYTX.
