## Wound 与 wound fix

`wound` 是绑定 bodypart 的持久状态，`wound_fix` 是治疗定义。两者各有 generic factory；fix 在
finalize 时解析 requirements 并反向登记到被移除的 wound。它们不是普通 effect 的别名。

### Wound fields

name、description、damage_types、damage_required 必填。pain 默认 0–0，healing_time 默认无限，
weight 默认 1，limit 默认 0；还可设置 limb scores、progression 及 bodypart type/flag 白黑名单。
progression 要求 id，chance 限制为 0–100。range pair 的顺序、damage type ID 和 progression ID
需要 consumer/test 验证，当前 `wound_type::check` 本身为空，不能只依赖 factory check。

### Wound fix fields

name/description 必填；time、skills、removed/added wounds、success_msg、HP modifier、proficiencies
和 requirements 可选。proficiency entry 要求 ID，time_save 默认 1，is_mandatory 默认 false。
requirements 可引用 `[id, count]` 或定义 inline requirement，finalize 后合并。

fix consistency 检查 skill、wound、proficiency 与 requirement IDs。删除/重命名 wound 会影响存档、
progression 和 fixes，必须提供明确 migration/compatibility 策略；没有自动 wound migration 契约时
不能假装安全。

### 验证

运行 formatter、`make -j2 json-check`、Mod `--check-mods`。用 focused wound tests 覆盖 damage
threshold、每 limb limit、白黑名单、progression、随机 pain/heal range、mandatory proficiency、
requirements 消耗、add/remove、HP 正负修改和存档 reload。破坏性或未实现的组合应明确标为
experimental，而不是仅凭 JSON 成功加载发布。
