---
trigger: always_on
description: Always-on workspace conventions for any Antigravity agent in this repository — communication, plan-mode discipline, parallelism, tool routing, session hygiene.
---

# Workspace Rules

These rules are always-on guidance for any Antigravity agent working in
this repository. They do not replace `AGENTS.md`; they describe how an
Antigravity agent should behave specifically inside the IDE.

## Communication
- Reply to the human in **Japanese** by default. Switch to English if the
  human writes in English first.
- All code, identifiers, comments, commit messages, branch names, file
  paths, and documentation in this repository are in **English**.

## Plan mode discipline
- When a Plan is being drafted (own session or via piped Claude Code
  output), **do not write code**. Add to the plan instead.
- If requirements are ambiguous, return a bulleted list of questions
  rather than guessing.

## Parallel execution
- One Plan in flight per session. Two parallel Plans means neither is
  being thought through.
- Agent Manager cards run in parallel only when the plan declares them
  independent. Sequential cards stay sequential.

## Tool routing
- Deep reasoning, plans, hypercritical reviews → Claude Code CLI.
- Tight iterate-loops, lint cycles, mechanical edits → Codex CLI.
- Wide scaffolding, multimodal (screenshots, PDFs), Browser checks → stay
  in Antigravity.
- See `.agents/skills/codex-system/SKILL.md` and
  `.agents/skills/claude-system/SKILL.md` for the full invocation
  patterns; the `codex-delegation` rule covers the decision in summary.

## Session hygiene
- Past ~20 turns or when responses get terse, run the `/checkpointing`
  workflow before the user has to ask.
- Hand off via `docs/handover/<date>-<topic>.md`. Don't lean on chat
  scrollback as memory.
