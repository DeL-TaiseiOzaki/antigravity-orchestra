---
description: Bootstrap a new project (or shape an unclear feature) through reconnaissance, requirement hearing, plan drafting, plan review, and task list creation. Heavier than start-feature — use when the work doesn't yet have a clear shape.
---

# bootstrap-project

Five steps. Each step has a single responsible tool. Do not skip ahead.

## 1. Repo Reconnaissance — Antigravity (Gemini 3)
Read the whole tree in one shot using the 1M context window. Produce:
- A one-page map of directories and their roles.
- An inventory of build / test / lint commands actually defined.
- A list of "smells" (TODOs, dead code, mismatched conventions).

Save to `docs/research/<YYYY-MM-DD>-recon.md`.

## 2. Requirements Hearing — Claude Code
Open a Plan-mode session. Ask the human three to seven sharp questions
covering: who the user is, what done looks like, what is explicitly out
of scope, what constraints (latency, memory, compatibility) bind us. Do
not write code.

## 3. Plan Drafting — Claude Code
Apply the `plan` skill. Output to `docs/plans/<feature>.md` using the
mandated section order.

## 4. Plan Review — Codex CLI
Pipe the plan into Codex and ask for a hypercritical second opinion
focused on missing failure modes, hidden coupling, and unstated
assumptions. Reply with diffs to the plan, not to source.

```bash
cat docs/plans/<feature>.md | codex "Review this plan. List missing failure modes, hidden coupling, unstated assumptions. Reply with diffs to the plan, not source."
```

## 5. Task List Creation — Antigravity
Once the human appends `## Approved by:` to the plan, decompose the
plan into independent tasks suitable for the Antigravity Agent Manager.
Each task must be: ≤ 4 hours of work, has a single owning agent, and
lists its acceptance check. Save to `docs/plans/<feature>-tasks.md`.

## When to use this vs. start-feature

| Situation | Workflow |
|---|---|
| Existing project, scope is clear, "I know what to build" | `start-feature` |
| New project, OR scope is fuzzy, OR the feature spans many modules | `bootstrap-project` |
