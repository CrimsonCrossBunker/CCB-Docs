## Relic 与 procedural artifact

Artifact 是 base item 加上 relic data；预制 relic 与 `relic_procgen_data` 是不同路径。procgen
dataset 提供 weighted base items、charge templates、active spells、passive enchantment values 和
type weights，generation rules 决定 power budget、attribute 上限、negative power 与 resonance。

### Procgen lists

所有 weighted entry 都要求 weight。passive entry 要求 enchantment value type，可设置 min/max、
increment、power_per_increment 和 ench_has；active entry 要求 spell_id，并可设置 level/power 与
ench_has。items entry 要求 item，type_weights 要求可用 value。dataset check 会验证 active spell，
但不能证明 power、item suitability 或所有 enchantment consumer 都合理。

### Charges

每个 charge template 包含 max_charges、charges、charges_per_use 的 range/power，另有
recharge_type 与 time。生成时初始 charges 被 clamp 到 max，time 在范围内随机选择。当前 procgen
template loader 不读取旧文档列出的 `recharge_condition`；该字段存在于生成后的 runtime charge
info，不应伪装成此 JSON 输入契约。

recharge type 与 ench_has 的有效 enum 以 `relic.cpp` 为准。active effect 有多个 spell 时共享一次
activation 的 charge cost；activation requirement 的组合行为必须用当前 generator 验证。

### Power、resonance 与验证

Power 是 generator 的选择预算，不是自动平衡证明。resonant generation rule 把最终 power 接入
当前 resonance runtime；阈值、效果和 lore 属于行为/设计契约，不能只从旧说明复制。

运行 formatter、`make -j2 json-check`、Mod `--check-mods`，固定 RNG seed 生成大量样本，检查空
weighted list、无效 spell/item、charge bounds、负面/正面预算、activation positions、存档 reload
和 resonance。变更 generator 时加入 deterministic distribution 与 consistency tests。
