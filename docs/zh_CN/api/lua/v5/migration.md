---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.migration
title: 迁移到 Lua API v5
language: zh_CN
status: draft
doc_type: how-to
audiences:
- mod-author
- api-user
- experienced-contributor
- maintainer
owners:
- CCB Lua API maintainers
reviewers:
- Documentation reviewers
- Lua API reviewers
review_interval_days: 60
last_human_reviewer: Not yet reviewed (draft)
source_paths:
- data/lua/README.md
- data/lua/manifest.schema.json
- data/lua/types/ccb_api_v5.d.lua
- data/lua/reference/ccb_public_api_v5.json
- data/lua/reference/ccb_public_api_v5_coverage.json
- tools/lua_api/README.md
source_symbols:
- game.state_get
source_queries: []
source_fingerprint: 86ab8c697639288944692daea743e7470450d95825578f8964198c2bd0dbdc83
authority: api-contract
verified_commit: 3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: c8a8f098d63c7f79ce5c0ab4a7464e05da60693906e8a2215cfc398aecd0e3e8
prerequisites:
- api.lua.v5.overview
depends_on:
- api.lua.v5.capabilities
- api.lua.v5.lifecycle
- api.lua.v5.ui
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; generated contract and source paths at the verified commit.
example_validation_ids: []
api_version: '5'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/565
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/migration/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/migration/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/migration/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/migration/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd
source_urls:
- path: data/lua/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd/data/lua/README.md
- path: data/lua/manifest.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd/data/lua/manifest.schema.json
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd/data/lua/types/ccb_api_v5.d.lua
- path: data/lua/reference/ccb_public_api_v5.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd/data/lua/reference/ccb_public_api_v5.json
- path: data/lua/reference/ccb_public_api_v5_coverage.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd/data/lua/reference/ccb_public_api_v5_coverage.json
- path: tools/lua_api/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd/tools/lua_api/README.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.v5.migration%29%3A+&body=Document+ID%3A+api.lua.v5.migration%0ALanguage%3A+zh_CN%0AVerified+commit%3A+3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 迁移到 Lua API v5

API v2–v4 Manifest 仍可使用其原有表面；新代码应显式迁移到 v5，不要依赖无 Manifest
的兼容 capability。

## 迁移步骤

1. 将 `api_version` 设为 `5`，用当前 `manifest.schema.json` 校验。
2. 从实际调用推导最小 capability；写操作增加 `game.write`（同时需要 `game.read`）。
3. 把 API v2/v3 的跨来源 `require` 假设改为本地 `require`，跨来源改用声明依赖后的
   `modules.import` 或版本化 `services`。
4. 把长期保存的原生对象假设改为类型化值、分离快照、token 或 `GameHandle`；使用前
   检查代次/有效性。
5. 把直接修改改为受校验的 v5 service 或 `game.actions` 请求，并处理结果 envelope。
6. 把 `game.state_get/state_set` 迁移到明确的 `state.character`、`state.world` 或
   `state.page` scope。
7. 页面用 descriptor 和稳定控件 `_id`；用 `ctx:environment()` 判断输入/布局，不能用
   `ctx:platform()` 区分触摸与桌面。
8. 把 Android HUD 假设移除：跨平台入口使用 `ui.page`，PC-only 信息才用 `sidebar`。
9. 对照生成参考更新所有参数、返回值和错误处理，运行完整契约与示例测试。

## 兼容点

- API v4/v5 的 `require` 仅当前来源；API v2/v3 保留旧反向加载顺序查找。
- `ui.page` 字符串标题形式仍可用，但 descriptor 明确 slot，适合新代码。
- `game.player_stats()` 等兼容别名可能保留；新代码应使用生成参考中的当前名称。
- `ctx:platform()` 仅保留 API v2 诊断用途。
- `game.state_get/state_set` 是 API v2 的角色级、旧式未分 scope 状态。

## 完成标准

- Manifest Schema 通过，Mod id/Manifest id 一致。
- 所有调用都在[函数](reference/functions.md)/[方法](reference/methods.md)参考中存在。
- 没有保存 `ctx`、裸对象或跨代次句柄。
- 热重载失败时旧 runtime 可继续运行，成功后持久状态符合预期。
- [完整示例 Mod](example-mod.md)和[调试命令](debugging.md)可作为最小基线。
