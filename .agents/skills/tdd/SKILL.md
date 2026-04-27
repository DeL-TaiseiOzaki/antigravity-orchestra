---
name: tdd
description: Use when implementing a behavior change with clear acceptance criteria. Drives the change through Red, Green, Refactor with tests written first. Pairs naturally with the plan skill for non-trivial features.
---

# tdd

## Phases

### Red
- Write the smallest failing test that expresses the desired behavior.
- Run it. Confirm it fails for the right reason (not an import error).
- Commit the failing test on its own. The diff is the spec.

### Green
- Write the minimum production code that turns the test green.
- Resist generalization. The next test will pull the design forward.
- Run the **full** test suite, not just the new test.

### Refactor
- With everything green, tighten the design: extract, rename, deduplicate.
- Re-run the full suite after every refactor step.
- Stop when the next refactor stops paying for itself.

## Test naming
`should_<behavior>_when_<condition>` — readable by a non-author skimming
output.

## Coverage targets
- Critical paths (auth, payments, data integrity): 100%.
- Business logic: 80% line coverage as a soft floor.
- Glue / framework code: not measured, reviewed by eye.

## Anti-patterns
- Writing tests after the code "to keep velocity" — that's not TDD.
- Mocking the system under test.
- Tests that assert implementation details rather than behavior.
