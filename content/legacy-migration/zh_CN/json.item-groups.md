## 当前 CCB item group 契约

`item_group` 描述“生成什么”，不是物品本身。`Item_factory::load_item_group` 读取命名组，
`item_group::load_item_group` 也可在怪物掉落、配方副产物等位置读取匿名内联组。引用的
item、group、container 和事件必须使用已加载的稳定 ID。

### collection 与 distribution

```jsonc
{
  "type": "item_group",
  "id": "ccb_example_supplies",
  "subtype": "distribution",
  "entries": [
    { "item": "water_clean", "prob": 70 },
    { "item": "bandages", "prob": 30 }
  ]
}
```

- `distribution` 把 entry 的 `prob` 当相对权重，进行一次分布选择。
- `collection` 独立评估各 entry，`prob` 表示该 entry 被包含的百分比机会。
- 缺省/旧 subtype 按 distribution 处理；新内容应显式写出意图。

entry 用 `item` 引用物品、用 `group` 引用另一组。`items`/`groups` 是只适合简单 ID 与
概率的快捷形式；需要 damage、charges、count、container、event、fault、variant 或
变量时使用完整 `entries` 对象。若同时填写快捷数组和 `entries`，它们会全部加入，
不会自动去重。

### 容器、弹药与递归

group 级 `ammo`/`magazine` 是加载枪械、工具和弹匣时的百分比机会；entry 的显式
`charges` 等修饰可能覆盖默认装填行为。`container-item`、`container-group`、sealed 与
overflow 行为会影响嵌套和容量。多 magazine-well 物品不能用一个含糊的 `charges`
值分摊到所有 well；应按当前 loader 规则和真实物品测试。

嵌套 group 可以形成深链，错误递归、空分布或不存在的 ID 可能直到加载/生成时才显现。
保持层级浅，并用 `item_group::items_from` 相关测试覆盖概率之外的结构不变量。

### 在 Mod 中扩展现有组

当前实现只允许 item group 从**相同 ID** 的既有组 `copy-from`，并通过 `extend` 加入：

```jsonc
{
  "type": "item_group",
  "id": "ccb_example_supplies",
  "copy-from": "ccb_example_supplies",
  "subtype": "distribution",
  "extend": {
    "entries": [ { "item": "aspirin", "prob": 10 } ]
  }
}
```

没有 `copy-from` 的同 ID 定义会重建/覆盖 group，而不是隐式追加。加载顺序和 Mod 依赖
因此属于契约的一部分；不要假定两个 Mod 的同 ID patch 能交换顺序。

### 内联组与验证

某些字段接受 group ID、内联对象或 entry 数组。内联组会获得内部唯一 ID，不能在其他
位置引用，适合只使用一次的掉落或副产物。默认 subtype 由调用位置决定，所以从别处
复制数组前要检查该字段的 loader。

验证时运行 JSON formatter/loader、ID 检查和 `--check-mods`。对关键掉落补充 focused
test，覆盖空结果、容器溢出、charges/magazine、event gate 与可能的递归；不要用一次
Debug 菜单抽样证明概率正确。
