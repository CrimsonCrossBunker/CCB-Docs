## Basecamp 数据由多份契约组成

Basecamp upgrade 不是单一 object type。它把 blueprint recipe、`update_mapgen`、
`recipe_group`、overmap terrain 和运行时 camp state 组合起来。修改其中一份数据前，先从
`basecamp::available_upgrades`、`recipe::load` 和当前第一方 camp 数据追踪整个 ID 链。

### Blueprint recipe

有 `construction_blueprint` 的普通 recipe 会进入 blueprint 路径。loader 读取
`blueprint_name`、`blueprint_parameter_names`、resources、provides、requires、excludes 与
needs。每个 blueprint 自动 provide 并 exclude 自己的 result，因此通常不可重复。

`blueprint_provides`/`requires`/`excludes` 是带默认 amount 1 的 camp feature 计数，不是全局
feature registry。代码会对部分约定 ID 赋予 mission 或 camp 能力；新字符串只有在 consumer
实际读取时才有语义。不要从旧文档的 keyword 表推断当前完整列表。

### Requirements 与 mapgen

没有 `blueprint_needs` 且 `check_blueprint_needs` 为 true 时，finalize 会从 mapgen 自动计算
需求。带 parameter names 的 blueprint 不能同时依赖显式 needs。`construction_blueprint` 必须
对应可执行的 update mapgen；参数名称必须覆盖玩家可选值并可翻译。

初始 camp 和 expansion 还依赖 recipe group 的 terrain match、对应 OMT 以及 mapgen。声明
dependency 的 Mod 才能安全引用另一 Mod 的 recipe、terrain 或 mapgen ID。

### 验证清单

核对每条 requires/provides/excludes 分支、重复升级阻止、resource item、mapgen 参数和实际
upgrade 后的地图。运行 formatter、`make -j2 json-check`、完整 `--check-mods`，并扩展
`tests/faction_camp_test.cpp` 的 focused case。需要更新计算结果时使用仓库
`tools/update_blueprint_needs.py`，逐项审阅输出，不手抄旧示例。
