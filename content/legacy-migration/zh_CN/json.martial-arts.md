## 当前 CCB Martial Arts 对象图

武术不是单个 JSON 对象。当前运行时分别注册 `attack_vector`、`weapon_category`、
`technique`、`martial_art` 与 buff；style 再引用 technique、weapon/category，并在战斗
事件上应用 buff 或 EOC。

### Style 与 technique

`martial_art` 需要稳定 `id`、`name`、`description` 和 `initiate`。`autolearn` 是
skill/level pair；`primary_skill`、`learn_difficulty`、`teachable`、`weapons` 与
`weapon_category` 决定学习和可用武器。`strictly_melee` 等限制必须与 UI 和实际选择逻辑
一起验证。

`technique` 当前至少需要 `name`；通常还提供玩家/NPC messages 和 `attack_vectors`。
crit、counter、disarm、knockback、AoE、repeat、condition、requirements 与 bonuses 共同
决定何时进入候选和执行什么。缺少 attack vector 的普通攻击 technique 会被 consistency
check 报告；defensive、dummy、grab-break 或 miss-recovery 等类型是例外。

### Attack vector、requirements 与 buff

`attack_vector` 描述 weapon/limb、contact area、limb HP、encumbrance、armor bonus 和
required/forbidden limb flags。它不是纯动画名称：选中的 limb 和 contact 会影响可执行性、
伤害与测试。

Style 可在 static、move、pause、hit、attack、dodge、block、get-hit、miss、crit、kill
时机挂 buff 和 inline EOC。Buff 有 duration、stack、persist、dodge/block 与 bonus/requirement
数据。每个触发时机的 actor、武器、目标和重复频率不同；EOC 不应假定始终存在 beta talker。

requirements 包括 skill、weapon damage、weapon category、buff、character flag 等组合。
“装备了允许武器”并不保证 technique 通过 limb、condition、ammo、range 或 cooldown 条件。

### 设计与验证

1. 先用已有第一方 style 找到最接近的对象图，保持 ID 前缀和翻译 message。
2. 运行 formatter、`make -j2 json-check` 和实际 Mod 集 `--check-mods`。
3. 运行 `martial_art_test`，覆盖 weapon category、limb substitution/HP/encumbrance、
   condition、sweep、stun 与 knockback。
4. 在游戏中分别测试空手、每类武器、受伤/高负重、NPC、crit/counter 和每个 buff/EOC 时机。
5. 记录 DPS、命中、防御、stack 与触发频率；加载成功无法证明没有无限叠层或强制循环。

旧文档中的 bonus 字符串与 flag 清单可能落后；具体枚举和范围以当前 loader/consistency
check 为准。
