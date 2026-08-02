## Faction mission 数据边界

`faction_mission` generic factory 当前主要提供 basecamp mission 的名称、说明和展示元数据。
任务如何选择目标、派出 NPC、计算收获/风险和修改地图仍多由 `faction_camp.cpp` 等 C++ consumer
实现。新增 JSON object 不会自动创造一套可执行 mission。

### Loader fields

name 与 desc 必填。skill、difficulty、risk、activity、time、positions、items_label、
items_possibilities、effects 和 footer 可选。difficulty/risk 只接受 NONE、VERY_LOW、LOW、MEDIUM、
HIGH、VERY_HIGH；activity 字符串必须存在于 activity level map，否则会报告 invalid。

这些 time/effects/items 字段是翻译后的说明，不是结构化 duration、loot table 或 effect program。
它们必须准确描述对应 hardcoded consumer，但不能替代 consumer 的测试。

### 新增或修改流程

先找到读取 mission ID 的 camp code 和解锁条件，再更新 display object。核对最大 positions、实际
duration、skill training、food/gear transfer、failure/risk 和 repeat semantics。若想数据驱动新
行为，需要先设计公开 execution contract、loader 和测试；不能把自然语言 effects 当执行指令。

### 验证

运行 formatter、`make -j2 json-check`、Mod `--check-mods`。实际在 camp menu 检查零/一/多 NPC
显示、翻译、不可用原因、开始/返回和重复任务。新增 ID 或行为时扩展 faction camp focused tests，
并确保显示文字与真实实现一致。
