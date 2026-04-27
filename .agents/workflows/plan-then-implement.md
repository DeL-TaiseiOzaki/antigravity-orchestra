---
description: Default sandwich workflow. Plan with Claude, implement in parallel via Antigravity Agent Manager (with Codex side-quests), review with a fresh Claude session.
---

# plan-then-implement

## Layer 1 — Plan (Claude Code)
1. Open Claude Code in Plan mode.
2. Apply the `plan` skill from `.agents/skills/plan/SKILL.md`.
3. Save the result to `docs/plans/<feature>.md`.
4. **Stop.** Do not proceed until a human edits the file to append:
   ```
   ## Approved by:
   <name> · <YYYY-MM-DD>
   ```

## Layer 2 — Implement (Antigravity + Codex)
1. In Antigravity, open Agent Manager.
2. Decompose the approved plan into independent task cards. One card =
   one logical change, ≤ 4 hours of work, single owning agent.
3. Run cards in parallel where dependencies allow. Watch the Artifact panel —
   if it overflows, the plan was too big and should be split.
4. Side-quests (lint loop, mechanical refactor, test additions) go to
   Codex from the embedded terminal:
   ```bash
   codex "Apply the codex-system skill. Acceptance: <one-line check>."
   ```
5. Each task ends with: tests pass, lint clean, diff visually inspected
   by the human, single commit per logical change.

## Layer 3 — Review (fresh Claude session)
1. Open a **new** Claude Code session (do not reuse the implementer's
   session — same reasoning will fail to see the same bugs).
2. Pipe the cumulative diff in:
   ```bash
   git diff main...HEAD | claude --verbose "Apply the team-review skill."
   ```
3. Save the report to `docs/reviews/<feature>-<date>.md`.
4. Address Critical and High findings before merging. Medium becomes a
   follow-up issue. Low is optional.
