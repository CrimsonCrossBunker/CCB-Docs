## Weather type 与 generator

`weather_type` 描述一种天气的显示和运行时影响，`weather_generator` 决定候选集合与基础气象。
二者是独立 object type。全局 consistency 要求 `null` 与 `clear` 两个 weather ID 有效。

### Weather type loader

name、id、sym、ranged_penalty、sight_penalty、light_modifier、priority、sound_attn、dangerous、
precip 和 rains 必填。可选字段包括 UI colors/sun symbol、temperature/light/sun modifier、音效/
tiles animation、duration、passive field effects、debug EOCs、required_weathers 与 condition。
duration_min/max 默认 5 minutes，且 min 不得大于 max。

condition 在 `weather_location` 等 dialogue context 中求值；候选按 priority 排序，required
weathers 必须引用有效 ID。不要把 JSON 文件顺序当稳定优先级，也不要把旧文档中的 sound/precip
枚举当完整列表，应查当前 enum registration。

### Weather generator

generator 要求 base temperature、humidity、pressure、wind；可配置季节修正、wind distribution
以及 weather whitelist 或 blacklist。白名单和黑名单互斥，finalize 会过滤并按 priority 排序；
白名单路径仍保留 clear。

### 验证

运行 formatter、`make -j2 json-check`、Mod `--check-mods` 和 focused weather tests。用固定 seed
覆盖四季、多坐标、condition/priority tie、required chain、duration bounds、indoors/vehicle passive
effects、debug EOC、light/sight/sound 与 whitelist。天气变化可能影响存档中当前 weather 和长期
世界生成，PR 要标记兼容/平衡影响。
