## NPC faction 契约

`FACTION` template 由 `faction_template` 加载，随后实例化为世界 faction。当前 constructor
强制读取 `id`、`name`、`description`、`likes_u`、`respects_u`、`known_by_u`、`size`、
`power`、`wealth`；trust、food、currency、price rules、claims、monster faction、relations
与 epilogues 是附加契约。

### 身份、关系与经济

Faction ID 会进入 NPC、dialogue、mission、camp、EOC 与存档，显示名可翻译但 ID 不可随意
改名。`relations` 是按目标 faction ID 的方向性 bitset；A 对 B 的 kill/watch/share 等关系
不自动保证 B 对 A 对称。每个目标和 relation flag 必须用当前注册表验证。

`currency` 会加入 price rule。Rule 可匹配 item group/flag 等当前 item-group 条件，并设置
markup、premium、fixed adjustment 或 price。交易结果还受 NPC、供应、技能与其他系统影响，
不能只用一件商品验证。

### 世界状态和兼容

Template 是新 faction 的初始值；world save 可以拥有已变化的 likes/respect/trust、wealth、
food 与成员状态。修改 template 不等于迁移已有世界。删除/改名 ID 前必须设计存档和所有
跨对象引用迁移。

Epilogue snippet、monster faction、currency/item group 和 mission ID 需通过 consistency
check。`known_by_u`、limited area claim 与 lone-wolf 影响 UI/world behavior，应有具体场景测试。

### 验证

运行 formatter、`make -j2 json-check`、`--check-mods`，并运行 faction price/mission/camp/
NPC dialogue tests。覆盖双向关系、偷窃/攻击、交易规则、food/wealth、epilogue、新世界与旧
存档、Mod 组合和缺失目标 ID。
