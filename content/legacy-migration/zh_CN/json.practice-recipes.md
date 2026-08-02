## Practice recipes

`type: practice` 使用主 recipe dictionary 和 crafting UI，但不产出正常 result。loader 明确拒绝
`result` 与 `difficulty`，要求 id、name、category、subcategory 和 `practice_data`；description
可选。components、tools、using、skill/proficiency、autolearn/book learn 等共享 recipe 契约，
byproducts/byproduct_group 仍可使用。

### practice_data

`min_difficulty` 没有单独 mandatory 检查，未给时保留结构默认；`max_difficulty` 缺省为
`MAX_SKILL - 1`，`skill_limit` 缺省为 `MAX_SKILL`。实际 recipe difficulty 会按角色 practical
skill 在区间内调整，超过 skill limit 时 UI 标记不再提升。

旧文档建议 `skill_limit <= max_difficulty + 1` 和统一 1 hour 是平衡约定，不是当前 loader bound。
新 recipe 应说明偏离原因，并与同 skill/proficiency 的当前 practice entries 比较。

### 设计与验证

用 `CC_PRACTICE` 和正确 subcategory 保持导航一致。requirements 应代表练习消耗，byproduct 不得
变成规避正常 recipe 的生产路径。proficiency practice 要核对 prerequisites、learning time、focus
和失败/时间 multiplier。

运行 formatter、`make -j2 json-check`、Mod `--check-mods`，在 crafting UI 检查未解锁、低于区间、
区间内、超过 skill limit、缺少 tools/components 与 helper/book 来源。扩展
`tests/crafting_gui_test.cpp` 的 focused case，并验证不会生成 result。
