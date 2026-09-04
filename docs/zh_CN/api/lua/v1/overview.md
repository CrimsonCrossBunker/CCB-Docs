---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.platform-v1.overview
title: Lua Platform v1：从零到运行
language: zh_CN
status: active
doc_type: tutorial
audiences:
- mod-author
- api-user
owners:
- CCB Lua API maintainers
reviewers:
- Documentation reviewers
- Lua API reviewers
review_interval_days: 60
last_human_reviewer: LYHGLYTX
source_paths:
- data/lua/README.md
- data/lua/LUA_FIRST_PLATFORM.md
- data/lua/types/ccb_platform_v1.d.lua
- tools/create_lua_mod.py
source_symbols:
- Platform v1
- ModDefinition
source_queries: []
source_fingerprint: 90d2d199e14a83b2fe78c4c1981c2c05d5e5a77045d6a64953e42c735841c183
authority: api-contract
verified_commit: 73432156f423ed3ef3301e6632c94c03c017d115
verified_at: '2026-09-05'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: cc17c0218d706cbd06b0da238f53513a48ddf48ddc53c4b9b83cd43af2341874
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- api.lua.v5.overview
license: CC-BY-SA-3.0
attribution: CCB contributors; source paths and Git history at the verified commit.
example_validation_ids: []
api_version: '1'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v1/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v1/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v1/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v1/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/73432156f423ed3ef3301e6632c94c03c017d115
source_urls:
- path: data/lua/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/73432156f423ed3ef3301e6632c94c03c017d115/data/lua/README.md
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/73432156f423ed3ef3301e6632c94c03c017d115/data/lua/LUA_FIRST_PLATFORM.md
- path: data/lua/types/ccb_platform_v1.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/73432156f423ed3ef3301e6632c94c03c017d115/data/lua/types/ccb_platform_v1.d.lua
- path: tools/create_lua_mod.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/73432156f423ed3ef3301e6632c94c03c017d115/tools/create_lua_mod.py
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.platform-v1.overview%29%3A+&body=Document+ID%3A+api.lua.platform-v1.overview%0ALanguage%3A+zh_CN%0AVerified+commit%3A+73432156f423ed3ef3301e6632c94c03c017d115%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Lua Platform v1：从零到运行

CCB 当前只支持 **Lua Platform v1**。旧的 Lua API v5、`game.*` 全局表、权限清单和
JSON Manifest 已经移除，不要照旧页面编写新 MOD。

## 最小 MOD

新建一个目录，只放 `main.lua`：

```lua
local ccb = require("ccb")

ccb.runtime.handler("welcome", function()
    ccb.services.message("我的第一个 CCB Lua MOD 已运行")
end, 1)

ccb.runtime.on("world_ready", "welcome")
```

可选的 `mod.lua` 用来声明名称、版本和依赖：

```lua
local ccb = require("ccb")

return ccb.ModDefinition {
    id = "my_first_mod",
    name = "My First MOD",
    version = "0.1.0",
    dependencies = { "dda" },
}
```

最终目录如下：

```text
my_first_mod/
├── main.lua
└── mod.lua        # 可选
```

不需要 `modinfo.json`、`manifest.json` 或 `lua/` 子目录。

## 安装和检查

把目录放到 CCB 用户目录的 `mods/` 下，然后运行：

```sh
cataclysm-tiles --userdir /你的/CCB用户目录/ --check-mods my_first_mod
```

看到 `Checking mod My First MOD [my_first_mod]` 且程序正常退出，表示 MOD 已被发现并通过
数据加载检查。也可以使用 Catapult 从 CCB MOD 目录直接安装。

## API 在哪里

- [LuaLS 完整声明](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/master/data/lua/types/ccb_platform_v1.d.lua)：函数、参数、返回值和类型说明；
- [机器可读 API 契约](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/master/data/lua/reference/ccb_platform_api_v1.json)：可用于生成工具和检查变更；
- [平台设计与生命周期](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/master/data/lua/LUA_FIRST_PLATFORM.md)：加载、隔离、状态和安全边界；
- [完整示例 MOD](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/tree/master/data/mods/Lua_First_Example)：按领域拆分的可运行示例；
- [CCB-MOD](https://github.com/CrimsonCrossBunker/CCB-MOD)：登记、维护和发布外部 MOD。

编辑器使用 LuaLS 时，把 `ccb_platform_v1.d.lua` 加入工作区库即可获得补全。遇到 API
缺失或文档与运行结果不一致时，以 CCB 主仓库的声明、原生注册和测试为准，并在 CCB
主仓库报告问题。

## 版本规则

- MOD 写明所需的 Lua API 整数版本，当前为 `1`；
- CCB RC 发布后冻结会影响 MOD 的公共 API；
- Stable 周期内不删除或改名现有公共 API；
- 必须破坏兼容时才提升为 Platform v2；
- `Experimental` 上的新接口不能视为 Stable 承诺。
