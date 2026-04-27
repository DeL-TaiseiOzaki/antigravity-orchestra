---
description: Write a structured handover document so a fresh session (different agent, next day, different teammate) can resume cold. Run before a long session ends, before context-window compaction, or before handing work between tools.
---

# checkpointing

## 1. Determine the output path
`docs/handover/<YYYY-MM-DD>-<short-kebab-topic>.md`. If multiple checkpoints
land on the same date and topic, append `-2`, `-3`.

## 2. Inspect current state
```bash
// turbo
git status
git log --oneline -20
git diff --stat
```

## 3. Write the handover with these sections, in order
1. **Current state** — One paragraph. Where the work is right now, what
   branch, what's committed vs. uncommitted.
2. **Done** — Bullet list of completed items with commit hashes.
3. **In progress** — What is half-done. Include the file paths and the
   next concrete action.
4. **Pending** — Not started, but planned. Pull from the active plan.
5. **Open questions** — Decisions waiting on a human or another tool.
6. **Decisions** — Choices made this session, briefly justified.
   Anything architectural also belongs in `docs/DESIGN.md` — invoke
   the `update-design` workflow.
7. **Next session kickoff prompt** — A copy-pasteable prompt that, when
   given to a fresh agent session, gets it productive in one turn.

## 4. Commit the handover
```bash
// turbo
git add docs/handover/<YYYY-MM-DD>-<topic>.md
git commit -m "docs: handover — <topic>"
```

## Variants

- **Long form (`/checkpointing --full`)** — also inline the full diff
  of uncommitted changes into the handover doc. Use when the next
  session may not have access to the working tree.
- **Audit form (`/checkpointing --analyze`)** — additionally walk the
  recent git log and flag decisions that weren't recorded anywhere.

## When to invoke
- Session passed ~20 turns.
- Context-window pressure visible (responses getting terse, tool calls
  failing more often).
- Work is being handed to a different tool (Antigravity → Claude, etc.).
- End of day.
