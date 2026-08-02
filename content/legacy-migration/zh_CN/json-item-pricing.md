## Item price 与交易规则

`price` 表示旧世界/基准价格，`price_postapoc` 是末世交易基线；二者都是非负 money unit。
实际 NPC 报价不是简单显示这个值：item 数量、charge/stack size、内容物、买卖方向、NPC 调整、
faction/personal price rules 和 currency 都可能改变结果。

### Faction rules

faction 的 `price_rules` 使用 item/group 等 matcher，并可设置 `markup`、`premium`、
`fixed_adj` 或固定 `price`。consumer 从后向前选择第一条匹配规则；NPC personal rule 可以覆盖
faction rule。声明 `currency` 还会加入该货币的等价交易规则。

因此旧指南中的某种货币锚点、固定价格区间和“单件不得超过某上限”是历史平衡建议，不是 loader
或交易代码强制契约。定价时以当前 CCB faction 数据、相似 item 与实际交易 UI 为准，并说明
可获得性、效用、消耗速度、可替代性和目标阵营。

### Charges 与容器

count-by-charges item 的固定 rule price 与 item base price 会按 stack size/charge 处理；装载的
magazine、ammo 和容器内容也可能计价。不要把整 stack 的 JSON price 当成单 charge，或在 item、
group 和 faction rule 中重复补偿同一因素。

### 验证

运行 formatter、`make -j2 json-check` 和 Mod `--check-mods`。为新 rule 覆盖 NPC 买/卖两个方向、
currency、conditional matcher、personal override、charge stack 与 contents；扩展
`tests/faction_price_rules_test.cpp`。平衡合理性由 Responsible human 审查，代码测试只证明计算
符合契约。
