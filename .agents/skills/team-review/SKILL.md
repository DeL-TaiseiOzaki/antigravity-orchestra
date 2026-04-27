---
name: team-review
description: Use when reviewing a diff, a PR, or a series of recent commits. Produces a severity-graded report covering correctness, security, performance, concurrency, maintainability, and Definition of Done compliance. Pairs well with pipe input and with Codex cross-checks.
---

# team-review

A multi-perspective review skill. The goal is not "find one bug" — it's
to walk every angle below and stay honest about uncertainty.

## Checklist (apply in order)
1. **Correctness** — Does the code do what the plan says? Edge cases?
   Off-by-ones? Empty / null inputs?
2. **Security** — Input validation, authn/authz boundaries, secret handling,
   injection surface, deserialization.
3. **Performance** — N+1 queries, accidental O(n²), unnecessary allocations,
   missing indexes.
4. **Concurrency** — Shared state, race conditions, lock ordering, async
   cancellation safety.
5. **Maintainability** — Naming, layering, test readability, dead code.
6. **Definition of Done** — Tests, lint, typecheck, docs, breaking-change
   notes (per root `AGENTS.md` §3).

## Output format
Group findings by severity:

- **Critical** — must fix before merge. Bug, security hole, data loss risk.
- **High** — should fix before merge. Correctness or maintainability issue
  with no immediate blast radius.
- **Medium** — fix this PR or file a follow-up. Code smell, minor risk.
- **Low** — nit. Optional.

Each finding includes: file path, line range, what's wrong, why it matters,
the smallest viable fix.

## Pipe input
- `git diff main...HEAD | claude "Apply the team-review skill."`
- `git show <sha> -- 'src/**' | claude "Apply the team-review skill, focus on security."`

## Cross-check with Codex
For high-stakes diffs, pipe the same input to Codex with the same prompt
and reconcile differences. Where the two disagree is where hidden
assumptions usually live — surface those to the human reviewer.

## Reviewer hygiene
- A reviewer who wrote the code can't review it. Open a fresh session.
- Don't approve based on diff size. Five lines can be Critical; five
  hundred can be Low.
- "Looks good" is not a review. Each finding is a sentence with evidence.
