## Terrain 与 furniture examine actions

`examine_action` 接受注册的 hardcoded 字符串、JSON examine actor，或两者组成的数组。字符串表
由 `iexamine_functions_from_string` 的当前 map 决定；找不到的名称会报告并退回 `none`。旧文档的
手写列表不是完整注册表。

### Actor 契约

- `appliance_convert`：item 必填，furn_set/ter_set 可选；finalize 检查 item、terrain、furniture 和
  appliance vpart。
- `cardreader`：flags、success_msg、redundant_msg 必填。mapgen_id 路径与 radius + terrain/furn
  changes 路径互斥；query、hacking、card consumption 与 monster despawn 还有组合约束。
- `effect_on_conditions`：按顺序加载 inline 或 named EOC；dialogue 中 u 是 examiner、npc 为空，
  并提供 this furniture ID 与 pos。
- `mortar`：ammo 与 range 必填；condition、aim/flight variables 和完成 EOC 可选。完成 EOC 还获得
  this、pos、target。

actor 顶层 type 决定 concrete loader。不要把某 actor 的字段复制给另一 actor，也不要从现有 JSON
出现频率猜 mandatory/default。

### 设计边界

已有 hardcoded action 能满足行为时直接引用；需要可配置组合时优先 actor/EOC。新增 hardcoded
字符串或 actor type 是公开契约变化，必须同时更新注册、loader/finalize、JSON inventory、双语
文档和测试。EOC 必须明确 talker、context variable、重复执行与 map bubble 边界。

### 验证

运行 formatter、`make -j2 json-check`、Mod `--check-mods`，并在 focused fixture 上 examine。
覆盖缺少 item/card/ammo、取消 query、重复使用、无效 ID、hacking/mapgen 分支、EOC context 和
存档 reload；扩展 `tests/iexamine_test.cpp`，不要只验证 JSON 能解析。
