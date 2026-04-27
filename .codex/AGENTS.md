# .codex/AGENTS.md

The canonical team guidelines live in the repository root **[AGENTS.md](../AGENTS.md)**.
Read it first. This file only carries Codex-specific notes.

## Codex specifics

- **Stay inside the allowlist** defined in root `AGENTS.md` §6. If a command
  isn't allowed, surface the request to a human rather than rewriting it to
  evade detection.
- **Five-attempt rule.** If a single error has not yielded after five focused
  attempts, stop the loop and write a short note in `docs/research/` with what
  you tried. Do not loop indefinitely.
- **One commit = one logical change.** Never auto-commit. Stage explicitly,
  let the human read the diff, then commit.
- **Plans are the contract.** Implement against the plan in
  `docs/plans/<feature>.md`. Do not invent extra scope. If the plan is wrong,
  return to Claude (Plan author) instead of patching around it.
- **Tests come with the change.** Adding code without an accompanying test or
  test update is incomplete by Definition of Done.
- **Lint loop is your specialty.** Use it: run lint, fix, re-run, repeat
  until clean — that's where Codex shines.
