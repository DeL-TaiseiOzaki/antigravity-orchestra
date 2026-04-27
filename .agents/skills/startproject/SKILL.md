---
name: startproject
description: Use when bootstrapping work on a fresh repository or a feature whose shape is still unclear. Performs reconnaissance, requirement hearing, plan drafting, plan review, and task list creation. Outputs an approved plan plus a parallelizable task list ready for the Antigravity Agent Manager.
---

# startproject

Five steps. Each step has a single responsible tool. Do not skip ahead.

## 1. Repo Reconnaissance — Antigravity (Gemini 3)
Read the whole tree in one shot using the 1M context window. Produce:
- A one-page map of directories and their roles.
- An inventory of build / test / lint commands actually defined.
- A list of "smells" (TODOs, dead code, mismatched conventions).

## 2. Requirements Hearing — Claude Code
Open a Plan-mode session. Ask the human three to seven sharp questions
covering: who the user is, what done looks like, what is explicitly out of
scope, what constraints (latency, memory, compatibility) bind us. Do not
write code.

## 3. Plan Drafting — Claude Code
Apply the `plan` skill. Output to `docs/plans/<feature>.md` using the
mandated section order.

## 4. Plan Review — Codex CLI
Pipe the plan into Codex and ask for a hypercritical second opinion focused
on missing failure modes, hidden coupling, and unstated assumptions. Reply
with diffs to the plan, not to source.

## 5. Task List Creation — Antigravity
Once the human appends `## Approved by:` to the plan, decompose the plan
into independent tasks suitable for the Antigravity Agent Manager. Each task
must be: ≤ 4 hours of work, has a single owning agent, and lists its
acceptance check.

## Artifacts produced
- `docs/research/<date>-recon.md` — the recon map.
- `docs/plans/<feature>.md` — approved plan.
- `docs/plans/<feature>-tasks.md` — task list with owner column.
