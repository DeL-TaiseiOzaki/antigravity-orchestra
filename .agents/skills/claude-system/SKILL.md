---
name: claude-system
description: Use to decide when to invoke the Claude Code CLI and how. Claude specializes in deep reasoning — plans, hypercritical reviews, multi-file impact analysis, and pipe-fed log analysis. Includes invocation patterns and cross-check usage with Codex.
---

# claude-system

## Send to Claude
- Plan drafting (use `plan` skill, write to `docs/plans/`).
- Hypercritical code review (use `code-review` skill).
- "What breaks if I change X?" impact analysis across many files.
- Log triage and root-cause grouping over piped logs.
- Architectural trade-off discussions where both sides need to be argued.

## Don't send to Claude
- Lint / typecheck loops (Codex is faster and stable for that).
- Mechanical renames or import swaps (Codex).
- Wide parallel scaffolding (Antigravity Agent Manager).

## Invocation patterns

### Plan mode
Open Plan mode. Confirm "no code will be written". Apply the `plan` skill.
Output goes to `docs/plans/<feature>.md`.

### Review mode (fresh session)
Reviews must come from a session that **didn't write the code**. Otherwise
the same reasoning that wrote the bug will fail to see it.
```
git diff main...HEAD | claude --verbose "Apply the code-review skill."
```

### Pipe analysis
```
docker logs api --since 1h | claude "Group recurring errors and propose root causes."
kubectl get events --sort-by=.lastTimestamp | claude "What changed in the last 30 minutes?"
```

### Large-impact analysis
Hand Claude the full repo (1M-context Sonnet variants help) and ask:
"If I rename `UserSession` to `Session`, list every file that needs to
change and the order to change them in."

## Cross-check with Codex
For consequential plans or reviews, pipe the same input to Codex and
diff the outputs. Where they disagree is where the truth usually hides.
