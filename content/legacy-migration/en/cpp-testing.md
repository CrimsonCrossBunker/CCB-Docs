## Current CCB C++ testing flow

CCB's C++ tests use Catch2, live under `tests/`, and normally build as `tests/cata_test`.
Build the tests, then reproduce with the narrowest case or tag. Do not begin a focused fix by
running every expensive matrix job.

```sh
make -j2 tests
./tests/cata_test --list-tests
./tests/cata_test '[relevant-tag]'
```

Adjust job count to local resources. The complete suite and platform or feature combinations
are defined by CI such as `.github/workflows/matrix.yml`; report combinations not run locally.

### Writing a test

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

- Name observable behavior and tag the subsystem for focused runs.
- Use `REQUIRE` for a prerequisite of later assertions and `CHECK` for independent results.
- Call the lowest-level entry that expresses the contract instead of a large UI or game loop.
- Explicitly reset avatar, map, calendar, RNG, options, factories, and other global state.
- Assert fixture properties taken from JSON so content changes cannot silently alter the test.
- Do not depend on test order or files and globals left by another case.

### Regression-test structure

A bug fix starts with a minimal regression that fails on the old implementation, then changes
the implementation. Cover the normal path, the reported failure, and the most important
boundary without freezing accidental error text as a contract. For random algorithms, fix or
record the seed and test invariants rather than one random result.

Save, JSON-loader, Lua-bridge, Android, or platform behavior needs the corresponding layer test.
A C++ unit test is not a substitute for a full Mod load, serialization round trip, or platform build.

### Diagnosing failure

Rerun the same filter and seed and preserve the first assertion plus relevant logs. Establish
whether the diff owns the failure and whether the base commit reproduces it before fixing or
recording an existing failure. Do not delete an assertion because CI is red or call a failure
unrelated without base evidence.

Performance comparisons use `BENCHMARK_TEST_CASE` outside the default correctness suite. See
[performance](../cpp/performance.md).
