---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: operations.crash-reports
title: Crash reports and symbols
language: en
status: draft
doc_type: how-to
audiences:
- new-contributor
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/crash.h
- src/crash.cpp
- src/debug.cpp
- .github/workflows/msvc-full-features.yml
source_symbols:
- void init_crash_handlers();
source_queries:
- BACKTRACE
source_fingerprint: 84f96e7aba0cf6b109527bb678678b13f9cce878d74ec03480ebb49d390f8fe0
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 14e660250e730d64aebabb110fc3d1a74e23ae94c705bcb34374b794001e8ef1
prerequisites:
- validation.debugging
- platforms.matrix
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: diagnostics
risk_level: normal
pending_source_pr: null
stale_reason: null
search:
  exclude: true
---

# Crash reports and symbols

A useful crash report identifies an exact binary and enough state to reproduce or symbolize the
failure. Screenshots of the last visible frame or a single “crashed” line are supporting evidence,
not a stack trace.

## Minimum report

- exact CCB commit, tag/release URL, and whether the binary was locally rebuilt;
- OS/version, architecture or Android ABI/API/device, compiler/build type, curses/tiles,
  SDL2/SDL3, sound, localization, Lua UI, and sanitizer/backtrace settings;
- active mods and relevant configuration, reproduction steps, expected/actual result;
- first error plus surrounding debug log; stack trace/tombstone/minidump when available;
- whether a new world reproduces, whether a save is required, and consent/redaction notes.

## Native paths

`src/crash.cpp` installs platform crash handling and stack-trace support; `src/debug.cpp` owns
debug logging. A stack is useful only with the matching executable, shared libraries, and symbols
from the same commit and build configuration. Preserve raw addresses before post-processing.

## Android paths

Distinguish Java exception, native `crash_dump`/tombstone, renderer/device loss, asset-copy,
storage, and install/signature failures. Capture a focused `logcat` interval including the
process start and fatal block; record version code/name, package, ABI, and install/update state.

## Privacy and security

Logs, saves, paths, usernames, world names, network addresses, tokens, and device information can
be sensitive. Redact secrets while preserving control flow and IDs. Share private saves/dumps
through an approved restricted channel, never a public issue by default.

## Triage workflow

Reproduce on the reported commit/config, symbolize with matching artifacts, reduce mods/data,
locate the owning subsystem, and add a deterministic regression test when practical. Do not
discard the original log after obtaining a prettier processed trace.

## Artifact policy

PDBs, debug symbols, tombstones, core files, and profiler captures are CI/release/diagnostic
artifacts, not repository source. Record checksum, retention, access, and deletion policy.
