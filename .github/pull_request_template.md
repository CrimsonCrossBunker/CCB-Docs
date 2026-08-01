## Summary / 摘要

<!-- Explain what changed and why. / 说明修改内容与原因。 -->

## Responsible human / 责任人

- Responsible human: @
- I understand the change and reviewed the final diff: <!-- yes/no -->
- I own the reported validation, licenses, attribution, and external sources: <!-- yes/no -->

Tool or model disclosure is optional. The Responsible human is not optional.

## Source coordination / 源码协调

- Related CCB source PR: <!-- URL or None -->
- Final CCB source commit: <!-- 40-character commit or Pending -->
- Affected documentation IDs: <!-- stable IDs from docs-catalog.yml -->
- Generated reference impact: <!-- None / Schema / LuaLS / registration / inventory -->

If the source PR is not merged, dependent pages remain `draft`. After it
merges, refresh `verified_commit` to the final commit before this PR merges.

## Documentation and translation impact / 文档与翻译影响

- Status change: <!-- draft / active / stale / archived / none -->
- Chinese and English updated together: <!-- yes/no/not applicable -->
- English `translation-stale` date and tracking issue: <!-- date + URL or None -->
- Search and AI-index impact: <!-- describe exclusions or None -->

## Validation / 验证

- [ ] `uv run python scripts/generate_catalog.py --check`
- [ ] `uv run python scripts/check_catalog.py`
- [ ] `uv run python -m unittest discover -s tests -p 'test_*.py'`
- [ ] `uv run python scripts/build_site.py --strict --include-drafts`
- [ ] `uv run python scripts/check_links.py --site-dir site --critical`
- [ ] Licenses, attribution, and external sources were checked.

## Notes for reviewers / 审阅说明

<!-- Record skipped checks and reasons. Do not claim checks that did not run. -->
