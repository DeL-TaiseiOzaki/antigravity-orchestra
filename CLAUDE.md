# CLAUDE.md

The canonical team guidelines live in **[AGENTS.md](./AGENTS.md)**. Read it
first. This file only adds Claude-Code-specific notes that don't belong in the
shared document.

@AGENTS.md

## Claude Code specifics

- **Plan mode is for planning, not coding.** When invoked in Plan mode, write
  the plan to `docs/plans/<feature>.md` and stop. Do not edit source files
  until a human appends `## Approved by:` to the plan.
- **One Plan in flight per session.** If a second planning request arrives,
  ask the user to either close the current plan or start a new session.
- **Reviews use `--verbose`.** It surfaces the reasoning needed to argue
  about subtle bugs.
- **Pipe input is a first-class tool.** Examples:
  - `git diff main...HEAD | claude "Apply the code-review skill, output Critical/High/Medium/Low."`
  - `docker logs api --since 10m | claude "Group recurring errors and propose root causes."`
- **Skills are shared.** Read `.agents/skills/<name>/SKILL.md` — the same
  skills serve Antigravity. Don't duplicate them under `.claude/`.
- **Hand-off uses the checkpointing skill.** When a session is getting long
  (~20 turns) or context is degrading, run the `checkpointing` skill before
  the user has to ask.
- **Stay inside the allowlist.** If a command isn't on the allowlist in
  `.claude/settings.json`, propose it for review instead of working around
  it with a compound command.
