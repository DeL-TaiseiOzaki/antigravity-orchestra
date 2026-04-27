---
name: checkpointing
description: Use before ending a long working session, before a context-window-driven compaction, or when handing work to a teammate or another agent. Produces a structured handover document so the next session can resume cold.
---

# checkpointing

## Output location
`docs/handover/<YYYY-MM-DD>-<topic>.md`

## Required sections (in order)
1. **Current state** — One paragraph. Where the work is right now, what
   branch, what's committed vs. uncommitted.
2. **Done** — Bullet list of completed items with commit hashes.
3. **In progress** — What is half-done. Include the file paths and the
   next concrete action.
4. **Pending** — Not started, but planned. Pull from the active plan.
5. **Open questions** — Decisions waiting on a human or another tool.
6. **Decisions** — Choices made this session, briefly justified. Anything
   architectural also goes into `docs/DESIGN.md`.
7. **Next session kickoff prompt** — A copy-pasteable prompt that, when
   given to a fresh agent session, gets it productive in one turn.

## Variants
- `checkpointing --full` — also includes the full diff of uncommitted
  changes inline. Use when the next session may not have the working tree.
- `checkpointing --analyze` — additionally walks the recent git log and
  flags decisions that weren't recorded anywhere.

## When to invoke
- Session passed ~20 turns.
- Context-window pressure is visible (responses getting terse, tool calls
  failing more often).
- Work is being handed to a different tool (Antigravity → Claude, etc.).
- End of day.
