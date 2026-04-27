# DESIGN.md

Architectural decisions for this project. **Append-only.** New entries go at
the bottom. Earlier entries stay as a record of what was true at the time, not
a description of what is true now.

## Entry format

```
## YYYY-MM-DD: <Title>
- **Context:** Why a decision needed to be made.
- **Decision:** What we chose.
- **Alternatives considered:** Other options and why they were rejected.
- **Consequences:** What this enables, what it forecloses, what we now owe.
- **Status:** proposed | accepted | superseded by <link to later entry>
```

---

## 2026-04-27: Initial setup with antigravity-orchestra template

- **Context:** Need a multi-agent dev environment that scales beyond a single
  Claude Code session. Antigravity is in Preview but ships an Agent Manager,
  Ghost Runtime, and a first-class Browser agent — all of which align with
  parallel work.
- **Decision:** Use Antigravity (Gemini 3) as the conductor, Claude Code CLI
  for deep reasoning (plans, hypercritical reviews), and Codex CLI for tight
  iterate-loops (lint, mechanical refactors). Single source of truth is
  `AGENTS.md` at the repo root.
- **Alternatives considered:**
  - VSCode + Claude Code as conductor (the `claude-code-orchestra` baseline).
    Rejected because we wanted to leverage Gemini's 1M context for
    whole-repo planning and native multimodal for Browser-driven UI work.
  - Cursor / Aider / monolithic Codex setup. Rejected because none of them
    offer the parallel Agent Manager card model.
- **Consequences:**
  - We accept Antigravity Preview instability and Google ecosystem
    lock-in. See `docs/WHY_ANTIGRAVITY.md` for the full trade-off analysis.
  - Skills under `.agents/skills/` must be authored to be readable by
    both Antigravity and Claude Code without per-tool forks.
  - Allowlist / Denylist in `AGENTS.md` §6 must stay semantically aligned
    with `.claude/settings.json`.
- **Status:** accepted.
