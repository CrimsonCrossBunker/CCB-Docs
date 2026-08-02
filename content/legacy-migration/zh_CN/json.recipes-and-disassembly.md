## 当前 CCB 配方与拆解模型

配方由 `recipe_dictionary` 注册并交给 `recipe::load`。当前 loader 区分 `recipe`、
`uncraft`、`practice` 和 `nested_category`；它们共享部分字段，但 ID 生成、必填字段、
学习方式和结果语义不同。不要把普通 crafting 示例直接改一个 `type` 就当成有效 uncraft。

### 普通 crafting recipe

```jsonc
{
  "type": "recipe",
  "result": "ccb_example_part",
  "category": "CC_OTHER",
  "subcategory": "CSC_OTHER_PARTS",
  "skill_used": "fabrication",
  "difficulty": 1,
  "time": "10 m",
  "activity_level": "LIGHT_EXERCISE",
  "autolearn": true,
  "qualities": [ { "id": "HAMMER", "level": 1 } ],
  "components": [ [ [ "scrap", 2 ] ] ]
}
```

普通 recipe 通常以 `result` 构造 recipe ID；`variant`/`id_suffix` 会改变最终 ID。
`category` 与 `subcategory` 是普通 recipe 的必填展示分类。字段是否允许继承、默认值和
范围以 loader 为准。

### requirement 的嵌套含义

`components`、`tools` 和 `qualities` 是“若干必须满足的组”；每组内部可以包含替代项。
`using` 引用一个具名 `requirement` 及倍率，适合复用 soldering/welding 等组合。方括号
层级决定 AND/OR，错误嵌套可能改变资源需求而不是立刻报语法错。对复杂配方要检查：

- 替代项是否真的是 OR；
- 数量、charges 和 `LIST` requirement 倍率；
- `NO_RECOVER`/`UNRECOVERABLE` 对拆解回收的影响；
- 重叠 alternatives 是否让可制作性计算过于复杂。

### step recipe

含 `steps` 的配方由每个 step 定义阶段工具、qualities、proficiencies、时间与活动强度。
当前 loader 禁止 step recipe 在根级再写 `tools`、`qualities`、`proficiencies`、
`batch_time_factors`、`time` 或 `activity_level`；空 `steps` 也会报错。根级 `using` 和
components 有专门聚合规则，修改继承配方时必须运行 recipe-step 测试。

### uncraft 与 reversible

```jsonc
{
  "type": "uncraft",
  "result": "ccb_example_part",
  "time": "5 m",
  "activity_level": "LIGHT_EXERCISE",
  "components": [ [ [ "scrap", 1 ] ] ]
}
```

`uncraft` 进入独立字典并被标记为可逆拆解。普通 recipe 的 `reversible: true` 会从制作
信息产生拆解；对象形式可覆盖拆解时间。当前 loader 明确拒绝 reversible recipe 同时
拥有 `byproducts` 或 `byproduct_group`。设计拆解时还要人工审查质量守恒、生成数量、
工具合理性、世界生成物与玩家制作物的差异，以及同一结果的重复拆解定义。

### 继承和加载

`recipe_dictionary::load` 在 `copy-from` 父 recipe 尚未出现时延迟加载，找到父项后复制，
再调用 `recipe::load`。内联 requirement 会重新建立；step、tools/components、using 的
继承有专门规则。不要假定它与 generic `ITEM` 继承完全相同。

### 验证清单

1. 确认 result、recipe ID、category/subcategory 和所有 item/skill/quality/requirement ID。
2. 运行 JSON formatter 与 `make -j2 json-check`。
3. step 或 copy-from 变化运行 `recipe_steps_test` 相关用例。
4. Mod 运行实际 Mod 集的 `--check-mods`，确认依赖和加载顺序。
5. 在游戏/测试中检查可制作性、批量时间、产物/副产物、拆解回收和质量守恒。

加载成功只证明结构可读，不证明配方不会复制资源、产生不可达 recipe 或破坏平衡。
