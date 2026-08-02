## 当前 CCB JSON 继承规则

`copy-from` 不是所有 JSON object type 自动拥有的语言特性。许多类型使用
`generic_factory`，另一些拥有专用实现，仍有类型完全不支持。每次使用前都要从当前
注册函数进入 loader，确认该对象真正实现了哪些操作。

### generic_factory 的加载顺序

对使用 `generic_factory` 的对象，典型顺序是：

1. 若有 `copy-from`，先查找已加载的具体对象或 `abstract`。
2. 父对象尚未加载时把子对象放入 deferred 队列，稍后重试。
3. 复制父对象，再由子对象的 loader 覆盖或调整字段。
4. `abstract` 只供继承；同一对象同时写 `abstract` 和真实 `id` 会报错。
5. finalize/check 阶段解析交叉 ID，并可能发现加载阶段未能证明的问题。

因此加载顺序通常可以由 deferred 处理，但不代表循环继承合法，也不代表跨 Mod 的覆盖
顺序无关。

### 四种修改方式

```jsonc
{
  "type": "ITEM",
  "id": "ccb_example_child",
  "copy-from": "ccb_example_parent",
  "name": { "str": "example child" },
  "relative": { "weight": "50 g" },
  "proportional": { "price": 1.2 },
  "extend": { "flags": [ "WATER_FRIENDLY" ] },
  "delete": { "flags": [ "FRAGILE" ] }
}
```

- 顶层直接字段通常替换继承值。
- `relative` 在 reader 支持时对父值做增量。
- `proportional` 在 reader 支持时对父值乘系数。
- `extend`/`delete` 在支持的容器 reader 上添加/删除成员。

这些只是意图，不是保证。没有 `copy-from` 时使用这些块会被拒绝或警告；不支持的类型、
字段或 reader 可能报错、忽略或采用专用行为。尤其不能因为 `ITEM.flags` 支持
`extend`，就推断任意对象的任意数组也支持。

### abstract、真实对象与链深度

`abstract` 适合表达一组定义始终共享的稳定基础，不能在游戏中作为真实 ID 使用。优先
保持一至两层、含义窄的继承；长链会让一次父项调整隐式改变多个 Mod/对象，也会使存档
兼容和数值审阅困难。纯显示差异若已有 variant 机制，通常不需要新继承链。

### 专用实现示例

- `recipe_dictionary::load` 自己延迟并复制 recipe；recipe 内联 requirements 有额外替换规则。
- item group 只允许从同 ID 的既有 group 复制，且 `extend` 由其专用 loader 读取。
- 部分对象可能默认扩展某些容器，另一些对象只支持 `copy-from` 而不支持四种修改块。

不要维护一份声称永久完整的“支持类型列表”。以当前 object registry 定位注册，再检查
loader、reader 和测试。

### 审阅与验证

1. 明确父项来自哪个 core/Mod、其加载顺序和稳定 ID。
2. 检查直接字段是 replacement、merge 还是专用语义。
3. 对照 reader 确认 `relative`/`proportional` 的单位与范围。
4. 用现有测试或最小 Mod 覆盖链、缺失父项、重复 ID 与 finalize。
5. 运行 formatter、`make -j2 json-check` 和实际 Mod 集的 `--check-mods`。

如果无法从实现证明某字段支持继承操作，改为显式完整定义或先补测试，不要靠加载未报错
推断行为。
