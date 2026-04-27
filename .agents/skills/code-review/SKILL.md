---
name: code-review
description: Use when reviewing a diff, a PR, or a series of recent commits. Produces a severity-graded report covering correctness, security, performance, concurrency, maintainability, and Definition of Done compliance. Pairs well with pipe input.
---

# code-review

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
- `git diff main...HEAD | claude "Apply the code-review skill."`
- `git show <sha> -- 'src/**' | claude "Apply the code-review skill, focus on security."`

## Cross-check with Codex
For high-stakes diffs, pipe the same input to Codex with the same prompt
and reconcile differences. Disagreements between the two are the most
interesting findings.
