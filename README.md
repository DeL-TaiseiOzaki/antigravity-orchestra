# antigravity-orchestra

A multi-agent development template for **Antigravity (Gemini 3) + Claude Code
CLI + Codex CLI**. The conductor is Antigravity; Claude Code handles deep
reasoning (plans, hypercritical reviews); Codex handles tight iterate-loops
(lint, mechanical refactors). One source of truth — the root `AGENTS.md` —
keeps all three on the same page.

This is the **Antigravity-friendly counterpart** to
[`claude-code-orchestra`](https://github.com/DeL-TaiseiOzaki/claude-code-orchestra).
The role between Antigravity and Claude Code is **intentionally inverted**:
the wide-context model conducts; the deep-reasoning model specializes.

## Quick start

```bash
git clone --depth 1 https://github.com/DeL-TaiseiOzaki/antigravity-orchestra.git .starter \
  && cp -r .starter/.agents .starter/.claude .starter/.codex .starter/.gemini . \
  && cp .starter/AGENTS.md .starter/CLAUDE.md . \
  && rm -rf .starter
```

After copying, fill in the placeholders in `AGENTS.md` §1, §2, §9 with your
project's specifics. Then read [`SETUP.md`](./SETUP.md) for IDE configuration.

## Architecture

```
                ┌────────────────────────────────────┐
                │   Antigravity (Gemini 3) — IDE     │
                │   • Agent Manager (parallel cards) │
                │   • Browser agent (multimodal)     │
                │   • Ghost Runtime (sandboxed)      │
                │                                    │
                │   reads:  AGENTS.md                │
                │          .agents/skills/           │
                │          .agents/workflows/        │
                │          .agents/rules/            │
                │          .gemini/antigravity/...   │
                └─────────────┬──────────────────────┘
                              │ (embedded terminal)
              ┌───────────────┴───────────────┐
              ▼                               ▼
    ┌──────────────────┐            ┌──────────────────┐
    │  Claude Code CLI │            │    Codex CLI     │
    │  Plans, reviews, │            │  Lint loop, test │
    │  pipe analysis   │            │  additions, ref. │
    │                  │            │                  │
    │  reads:          │            │  reads:          │
    │   AGENTS.md      │            │   AGENTS.md      │
    │   CLAUDE.md      │            │   .codex/AGENTS. │
    │   .agents/skills │            │   .codex/config  │
    │   .claude/       │            │                  │
    └──────────────────┘            └──────────────────┘
```

## Roles at a glance

| Tool | Strength | Use for |
|---|---|---|
| **Antigravity (Gemini 3)** | 1M context, multimodal, parallel Agent Manager | Conductor: scaffolding, parallel work, UI/Browser checks, task routing |
| **Claude Code CLI** | Deep chain-of-thought, dependency tracking | Plans, hypercritical reviews, large-impact analysis via pipes |
| **Codex CLI** | Stable iterate-loop, native AGENTS.md | Small refactors, test additions, lint loops |

The default workflow is the **sandwich**: Plan with Claude → Implement in
Antigravity Agent Manager (delegate side-quests to Codex) → Review with a
fresh Claude session. See `.agents/workflows/plan-then-implement.md`.

## Language conventions

- Code, comments, identifiers, commit messages, file paths, and documentation
  in this repository are in **English**.
- Agent ↔ human chat in Antigravity may be in **Japanese** by default. Switch
  to English if the human writes in English first.

## Repository layout

```
.
├── AGENTS.md                 single source of truth (≤ 300 lines / ≤ 5KB)
├── CLAUDE.md                 Claude Code-specific notes; references AGENTS.md
├── README.md                 this file
├── SETUP.md                  install + configure Antigravity / Claude / Codex
├── LICENSE                   MIT
├── .agents/                  AGENTS.md ecosystem (shared by Antigravity & Claude)
│   ├── skills/               Progressive Disclosure skills (auto-loaded when relevant)
│   ├── workflows/            Deterministic procedures, invoked via /<workflow-name>
│   └── rules/                Workspace rules (trigger: always_on | model_decision)
├── .claude/                  Claude Code config (settings, agents, hooks)
├── .codex/                   Codex CLI config (AGENTS.md, config.toml)
├── .gemini/antigravity/      browser allowlist (prompt-injection defense)
└── docs/
    ├── DESIGN.md             append-only architectural decisions
    ├── WHY_ANTIGRAVITY.md    why we picked this stack, with honest trade-offs
    ├── plans/                one plan per feature
    ├── research/             investigations and link dumps
    └── handover/             session checkpoints (created by /checkpointing)
```

## What this template is not

- It is **not language-specific**. No `package.json`, no `pyproject.toml`.
  Use whatever stack your project needs and fill `AGENTS.md` §2 accordingly.
- It is **not a CI setup**. GitHub Actions are out of scope.
- It is **not a guarantee**. Antigravity is in Preview. Read
  [`docs/WHY_ANTIGRAVITY.md`](./docs/WHY_ANTIGRAVITY.md) before adopting.

## License

MIT. See [`LICENSE`](./LICENSE).
