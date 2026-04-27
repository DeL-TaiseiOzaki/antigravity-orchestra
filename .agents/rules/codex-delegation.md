---
trigger: model_decision
description: Apply when deciding whether the current task should be delegated to Codex CLI from Antigravity or a Claude Code session. Provides the bright-line signals for "send to Codex" and the anti-patterns. For full invocation patterns, see the codex-system skill.
---

# Codex Delegation

## Send to Codex when **all** are true

- The task has a **single one-line acceptance check** that returns 0 / non-0.
  - Examples: `pnpm test`, `cargo clippy --all-targets -- -D warnings`,
    `ruff check src/`.
- The scope is **mechanical**: rename a symbol across files, add tests
  for an existing module, run lint until clean.
- **No design decisions** are left to Codex.

## Don't send to Codex when **any** is true

- The work needs a `plan` first.
- Multiple modules need to be reasoned about together.
- The acceptance criterion can't be expressed in one shell command.
- The bug doesn't have a reproducer.

## Bright-line signals

| Task | Codex? |
|---|---|
| "Run lint, fix every warning, commit when clean." | ✅ |
| "Add tests for `src/foo.ts` until coverage ≥ 90%." | ✅ |
| "Rename `UserSession` → `Session` across the repo." | ✅ |
| "Why is the API slow?" | ❌ — `troubleshoot` skill (Claude). |
| "Should we cache here?" | ❌ — `plan` skill (Claude). |
| "Refactor the auth module for clarity." | ❌ — `simplify` workflow first. |

## Five-attempt rule

If Codex hasn't yielded after five focused attempts on a single error,
**stop**. The five-attempt rule is in `.codex/AGENTS.md`. When it
trips, write a short note to `docs/research/` describing what was
tried, then re-plan in Claude Code.

## Cross-check

For consequential reviews or mechanical migrations, run the same diff
through both Codex and Claude. Disagreement is more interesting than
agreement.
