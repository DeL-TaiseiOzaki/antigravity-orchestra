---
trigger: model_decision
description: Apply when writing or modifying code. Captures the project's load-bearing coding principles — error handling, side-effect placement, dependency hygiene, dead code, and comment intent.
---

# Coding Principles

These supplement `AGENTS.md` §7. Read both. When they appear to disagree,
`AGENTS.md` wins.

## Errors are signals, not noise
- Don't swallow exceptions. Catch them with **context**: log the
  inputs that caused the failure, then re-raise or return a typed error.
- A `try / except: pass` (or `catch (e) {}`) needs a code comment
  justifying it. Otherwise it's a bug-in-waiting.
- "Fail loud in dev, fail safe in prod" requires explicit different paths,
  not the same exception sink behaving by accident.

## Side effects live at the edges
- I/O, network, time, randomness, and globals belong in the outer layer
  (entrypoint, adapter, handler).
- Pure logic in the middle. Tests for pure logic should not need mocks.
- A unit test that requires a real clock or filesystem is testing
  layering, not behavior.

## Dependencies are debt
- Adding one requires explicit approval in the PR description.
- Three new transitive deps from a single direct dep is a smell —
  evaluate via the `research-lib` skill before accepting.
- Removing an unused dependency is always in scope.

## Dead code is technical lying
- If a branch is unreachable, delete it. Git keeps the history.
- Commented-out code is dead code wearing a costume. Same rule.
- Speculative generalization (one-caller abstractions, "we might need
  this later") is dead code that hasn't died yet.

## Comments explain why, never what
- A comment describing what the next line does is a refactor request:
  rename, extract, or restructure until the code says what it does.
- Comments earn their keep when they explain non-obvious **reasons**:
  a workaround for a specific bug, a constraint from upstream, an
  invariant that's not visible locally.
- Update comments when the code changes. A wrong comment is worse
  than no comment.

## Naming is a contract
- A name should let a reader predict the function's behavior without
  reading the body. If they have to look, the name is wrong.
- Symmetric concepts get symmetric names (`open` / `close`,
  `acquire` / `release`). Asymmetry is itself information.
- Don't reuse a name for a different concept in the same module.
