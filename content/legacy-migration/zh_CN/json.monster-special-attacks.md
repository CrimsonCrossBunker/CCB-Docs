## Monster special attack 契约

`special_attacks` 是 `MONSTER` 的有序能力集合。条目可用旧式
`[ native_name, cooldown ]` 引用注册的 C++ attack，也可使用带 `type`/`id` 的 actor object。
Actor type、字段与运行时行为以 `MonsterGenerator::init_attack`、`mattack_actors.cpp` 和测试为准。

### 身份、cooldown 与条件

同一 monster 上重复 actor subtype 必须提供不同 `id`，否则 loader 会报告重复并只保留最后
定义。Cooldown reader 可以是固定值或当前支持的表达式；条件失败、没有目标或资源不足时，
是否消耗 cooldown 取决于 actor call path，必须按实现测试。

Leap、melee/bite、gun、spell、grab、summon 等 actor 的必填字段不同。例如 leap 强制
`max_range`，gun 读取 `gun_type`、range/mode、targeting 和 ammo 数据。不要把一个 actor 的
字段表套给另一个。`condition` 的 alpha 通常是 monster，beta 是否存在由 actor 构造 dialogue
的方式决定。

### 继承和副作用

Monster `copy-from` 的 special attack reader 支持替换/删除，但同名项和 `id` 决定结果。
Self/target effect、field、spawn、sound、message、ammo、item 和 spell ID 都要存在。
攻击可能改变地图、跨 z-level、抓取 bodypart 或建立 targeting state；失败路径必须清理状态。

### 验证

运行 formatter、`make -j2 json-check`、实际 Mod `--check-mods`，以及
`monster_attack_test`/`mondefense_test` 和相关 actor tests。覆盖无目标、不可见目标、最小/
最大距离、障碍、cooldown、ammo 空、condition false、NPC/player/monster target、保存重载和
重复 actor ID。高频 path search、AoE、spawn 与 field actor 需要 profile。
