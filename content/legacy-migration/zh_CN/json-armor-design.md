## Armor JSON 设计与审核

Armor 是 item 契约加上 `islot_armor`。每个 `armor` portion 必须声明 `covers`，并可独立设置
coverage、melee/ranged/vitals coverage、sublocations、encumbrance、materials、layers、
breathability 与 environmental protection。顶层字段和 inheritance 会再应用到各 portion；审核时
必须看最终展开值。

### 几何、材料与穿戴

`specifically_covers` 把 coverage 限定到 sub-bodypart；缺少 sublocation 数据时，覆盖 parent
bodypart 就视为覆盖其 subparts。`sided` 让实例在左右侧之间切换。layers 决定同部位衣物冲突，
不要用任意 flag 或旧表替代当前 layer enum 与运行时检查。

portion material 要有 type，`covered_by_mat` 必须为 1–100，thickness 为该材料层厚度。旧字符串
material 形式仍能读取但代码已标为旧路径；新内容优先使用可审核的 per-portion material。真实
重量、厚度、材料、coverage 和活动关节决定平衡，不能为了目标数值伪造物理属性。

### Encumbrance、pockets 与 ablative

encumbrance 可为单值或 empty/full pair，也可用 volume modifier。pocket 自身 modifier、rigidity
与内容共同影响结果。ablative pocket 的 insert 仍是 armor item；其 flag restriction、coverage、
不可直接穿戴边界和破损/transform 都要一起核对。

### 最小复杂度原则

普通衣物只表达真实需要的 portions；高级材料、per-subpart layers、特殊 coverage、relic effect 或
transform 只在能说明玩家可见差异时加入。不要复制旧文档的“完整 flag 列表”，flag 注册表和
consumer 才是契约。

### 验证

从当前相似第一方 armor 取基线，检查 item info、穿戴冲突、满/空 pocket、左右侧、近战/远程和
ablative damage。运行 formatter、`make -j2 json-check`、Mod `--check-mods`，并为新边界扩展
focused item/armor tests。平衡数字还需要 Responsible human 审阅其研究来源。
