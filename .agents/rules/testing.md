---
trigger: model_decision
description: Apply when writing or modifying tests. Defines what a good test looks like in this project — naming, isolation, what to mock, coverage expectations, and the relationship between tests and the Definition of Done.
---

# Testing

## What a good test looks like

- **One behavior per test.** If the test name needs an "and", split it.
- **Name follows `should_<behavior>_when_<condition>`.** Readable when
  scanning failure output.
- **Arrange / Act / Assert** — visible from a glance. White space
  between the three is fine.
- **A failing test shows the contract that broke**, not the
  implementation that changed.

## What to mock (and what not to)
- Mock the **system boundary** — network, time, randomness, external
  service.
- **Don't mock the system under test.** A test that mocks the function
  it's testing is testing nothing.
- **Don't mock pure functions.** Just call them.
- A test with five mocks is testing the test, not the code.

## Coverage expectations
- **Critical paths** (auth, payments, data integrity, anything in
  `AGENTS.md` §9 Known Constraints): line + branch coverage near 100%.
- **Business logic**: 80% line coverage as a soft floor.
- **Glue / framework code** (route wiring, DI containers): not measured;
  reviewed by eye.
- A line not covered by tests is a line not understood.

## Test data
- Inline small fixtures next to the test that uses them.
- Shared fixtures live in a single `fixtures/` (or stack-equivalent)
  directory. Don't smuggle test data through globals.
- "Real-world sample" data goes into `docs/research/` if it's
  illustrative, never into the test suite.

## Tests in the Definition of Done
A change is not done until:

- New behavior has new tests.
- Modified behavior has updated tests (or a deliberate "behavior is
  unchanged" comment in the PR).
- Removed behavior has its tests removed in the same commit.
- The full suite passes locally — not just the new ones (per
  `AGENTS.md` §3).

## Anti-patterns
- "I'll add tests in a follow-up PR." That follow-up doesn't happen.
- Tests written **after** the implementation merely to bump coverage —
  they document what was built, not what was intended. Use TDD instead
  (see `.agents/skills/tdd/SKILL.md`).
- Asserting on log output as a substitute for asserting on behavior.
- Sleep-based tests. Use a fake clock.
