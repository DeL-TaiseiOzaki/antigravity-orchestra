---
description: Get up to speed on an existing repository or a session you didn't start. Reads the canonical docs, walks recent commits, surfaces the active plan, and produces a one-page situational summary.
---

# catchup

## 1. Read the canonical docs (in this exact order)
```bash
// turbo
cat AGENTS.md
ls -la docs/
cat docs/DESIGN.md 2>/dev/null || true
```

If `docs/DESIGN.md` is empty or missing, note that in the summary —
that's a signal in itself.

## 2. Inspect the active plan(s)
```bash
// turbo
ls -la docs/plans/
```

For each plan, check whether it has an `## Approved by:` line. Plans
without approval are works-in-progress.

## 3. Walk recent activity
```bash
// turbo
git log --oneline -30
git log --since='2 weeks ago' --stat
```

Look for: who is active, which areas are being touched, whether the
recent work matches an approved plan.

## 4. Find in-flight work
```bash
// turbo
git status
ls -la docs/handover/ 2>/dev/null || true
```

The most recent handover doc — if one exists — is your kickoff.

## 5. Produce the catchup summary

Print to chat (do not commit) a single page covering:

- **Project shape** — name, stack, status (from `AGENTS.md` §1).
- **Active plan(s)** — paths and approval status.
- **Recent direction** — three to five bullets summarizing the last
  two weeks of commits.
- **Open in-flight work** — uncommitted changes, latest handover,
  any unresolved `Open Questions` from a recent handover.
- **What I would suggest doing next** — one sentence, with reasoning
  rooted in the bullets above.

## When to use
- First session in an unfamiliar repository.
- Resuming after time away (≥ 1 week).
- Picking up someone else's work (handover doc + this workflow).
- After a long checkpoint, to verify the previous session's claims.
