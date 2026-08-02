## 当前 CCB C++ 测试流程

CCB 的 C++ 测试使用 Catch2，源码位于 `tests/`，构建产物通常为 `tests/cata_test`。先构建
测试，再用最窄的 case/tag 复现；不要在一个 focused 修复上先跑整套昂贵矩阵。

```sh
make -j2 tests
./tests/cata_test --list-tests
./tests/cata_test '[relevant-tag]'
```

实际 job 数按机器资源调整。完整 suite 和平台/feature 组合由 `.github/workflows/matrix.yml`
等 CI 定义；本地没有运行的组合必须如实标注。

### 编写测试

```cpp
TEST_CASE( "example_status_expires", "[effect][ccb_example]" )
{
    avatar dummy;
    // Arrange only the state this behavior owns.

    REQUIRE( precondition_is_true( dummy ) );
    perform_action( dummy );
    CHECK( observable_result( dummy ) );
}
```

- test name 描述可观察行为，tag 支持子系统 focused run。
- `REQUIRE` 用于后续断言依赖的前置条件；`CHECK` 收集互相独立的结果。
- 直接调用能表达契约的最低层入口，避免通过巨大 UI/game loop 偶然覆盖目标。
- 显式重置 avatar、map、calendar、RNG、options、factory 和其他全局状态。
- 使用 JSON 对象时先断言测试依赖的属性，防止内容数据变化悄悄改变 fixture。
- case 不依赖执行顺序，也不读取另一个 case 留下的文件或全局值。

### 回归测试结构

Bug fix 应先写能在旧实现失败的最小回归，再修实现。覆盖正常路径、报告中的失败路径与最
重要边界；不要把当前错误输出固化成契约。随机算法要固定/记录 seed，并测试不变量而不是
一次随机结果。

跨存档、JSON loader、Lua bridge、Android 或平台代码应使用对应层测试；纯 C++ unit test
不能代替完整 Mod loading、序列化 round-trip 或平台构建。

### 失败诊断

先以相同 filter/seed 重跑，保留首个断言和相关日志。确认失败是否在 diff 涉及的代码、是否
可在 base commit 复现，再决定修复或记录既有失败。不能仅因为 CI 红就删除断言，也不能
没有 base 证据就称其“无关”。

性能比较使用 `BENCHMARK_TEST_CASE`，不进入默认 correctness suite；见[性能](../cpp/performance.md)。
