## Nested、merged 与 update mapgen

完整 variant 用同一 `om_terrain` 和 weight 替换整张 map；nested mapgen 把局部 chunk 叠到调用者；
update mapgen 则在游戏过程中修改已经存在的地图。三者生命周期不同，不能仅因 JSON 结构相似而
互换。

### Nested mapgen

顶层使用 `nested_mapgen_id`，可用 weight 提供同 ID variants；`object.mapgensize` 必须是两个相同
的正数，当前实现仍只支持 square。`rows`、palette、placement 和 nested-in-nested 都在这个局部
坐标系内。空符号通常保留底层，明确清除 terrain/furniture/items/trap/field 时使用当前 loader
支持的 null/clear 或 clearing flags，避免只覆盖一半状态。

调用者用 `nested` symbol 或 `place_nested` 坐标选择 weighted `chunks`；`null` 是有效的“不放置”
候选。当前 nested placement 还可按 neighbors、joins、flags、predecessors 和 z 等条件选择，行为
由 `jmapgen_nested` 与 `nest_conditional_placement_test.cpp` 证明。Chunk 必须落在调用者 grid 内，
门、墙和可通行边界要在所有 variants 一致。

### Merged 与 update

二维 `om_terrain` array 为每个 OMT 注册同一 merged definition 的 offset；所有 rows 使用连续的
总坐标。`common_check_bounds` 会拒绝跨当前 grid boundary 的坐标 range，因此 large rows 不表示
每种 placement 都能跨 OMT。把 vehicle、range spawn 与 nest 限制在单一 OMT，并用 focused tests
覆盖边界。

`update_mapgen_id` 注册运行时更新；调用点决定目标 OMT、参数、mirror/rotation、collision policy
与 mission context。Update 可能破坏玩家建造物、车辆、物品和存档状态，必须列出幂等性、冲突
和再次触发策略。不要用旧 trap 示例推断所有现有触发入口。

验证所有 nest weights/conditions、rotation、局部清除、NPC/vehicle、merged boundary、update
collision、重复执行与存档重载。运行 JSON load、目标 Mod load、focused mapgen/nest/update tests，
并在 debug mapgen 中记录 seed、位置、方向和调用参数。
