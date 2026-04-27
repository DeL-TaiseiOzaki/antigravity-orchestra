# AGENTS.md

This is the **single source of truth** for every agent and human working on this
repository. `CLAUDE.md` and `.codex/AGENTS.md` only carry tool-specific notes
and reference this file.

## 1. Project Overview

<!-- Fill in when bootstrapping a new project from this template. -->

- **Name:** _<project name>_
- **Purpose:** _<one sentence: what user problem this solves>_
- **Stack:** _<language / framework / runtime>_
- **Status:** _experimental | alpha | beta | production_

## 2. Build / Test / Quality Commands

<!-- Replace with real commands. Examples: -->
<!-- Node:   pnpm i / pnpm build / pnpm test / pnpm lint / pnpm typecheck -->
<!-- Python: uv sync / uv run pytest / uv run ruff check . / uv run mypy . -->
<!-- Rust:   cargo build / cargo test / cargo clippy --all-targets -- -D warnings -->
<!-- Go:     go build ./... / go test ./... / go vet ./... -->

- **install / build / test / lint / typecheck:** _<commands>_

## 3. Definition of Done

A change is done only when **all** are true:

- [ ] Tests pass locally (full suite, not just the new ones)
- [ ] Lint reports 0 issues
- [ ] Typecheck reports 0 errors
- [ ] Public API / behavior changes are documented in `docs/`
- [ ] Breaking changes are called out explicitly in commit body and PR
- [ ] No new TODO / FIXME without an owner and a tracking issue

## 4. Branch / Commit / PR Conventions

- Branch name: `<type>/<short-kebab-topic>` (e.g. `feat/auth-rotation`)
- Commits follow **Conventional Commits**: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`
- **One commit = one logical change.** No omnibus commits.
- PR title mirrors the lead commit. PR body links the plan in `docs/plans/`.

## 5. Multi-Agent Roles

| Tool | Strength | Use for |
|---|---|---|
| **Antigravity (Gemini 3)** | 1M context, multimodal, parallel Agent Manager | Conductor: scaffolding, parallel work, UI/Browser checks, task routing |
| **Claude Code CLI** | Deep chain-of-thought, dependency tracking | Plans, hypercritical reviews, large-impact analysis via pipes |
| **Codex CLI** | Stable iterate-loop, native AGENTS.md | Small refactors, test additions, lint loops |

**Sandwich workflow (default):** Plan with Claude → Implement in Antigravity Agent
Manager (delegate side-quests to Codex) → Review with a fresh Claude session.
A Plan must be approved by a human (`## Approved by:` line) before implementation.
Only **one Plan in flight per session**.

## 6. Security & Permissions

### 6.1 Terminal Auto Execution
- Mode: **Allowlist**. `Always Proceed` is forbidden.
- Compound commands with pipes / subshells require explicit approval.

### 6.2 Allowlist (mirror in `.claude/settings.json`)
Read-only inspection (`ls`, `cat`, `head`, `tail`, `wc`, `grep`, `rg`, `find`,
`stat`, `which`, `tree`), git read (`status`, `diff`, `log`, `branch`, `show`),
and the active stack's build/test runners (`pnpm`, `npm`, `uv`, `pip`,
`pytest`, `ruff`, `mypy`, `cargo`, `go`, `dotnet`, `make`).

### 6.3 Denylist (mirror in `.claude/settings.json`)
`sudo`, `ssh`, `scp`, `curl`, `wget`, `rm -rf`, `git push --force`,
`git reset --hard`, `*publish`, `*deploy`, cloud CLIs
(`aws`, `gcloud`, `az`, `kubectl`).

### 6.4 Browser Allowlist
Antigravity Browser is constrained by `.gemini/antigravity/browserAllowlist.txt`
(distributed copy) and `~/.gemini/antigravity/browserAllowlist.txt` (effective
copy). This is **prompt-injection defense**, not a convenience knob.

### 6.5 Secrets
Local secrets live in `.env.local` only. Never commit. MCP servers connect with
read-only roles. Never paste production secrets into any agent prompt.

## 7. Code Style

- Don't swallow errors. Log with context, then re-raise or return a typed error.
- Keep side effects at the edges; pure logic in the middle.
- Adding a dependency requires explicit human approval in the PR.
- No dead code. Delete it; git keeps the history.
- Comments explain **why**, not **what**.

## 8. File Layout Rules

- `docs/plans/<feature>.md` — one plan per feature, approved before implementation.
- `docs/research/` — investigations, link dumps, library evals.
- `docs/DESIGN.md` — append-only architectural decisions (date / context / decision / consequences).
- `.agents/skills/<name>/SKILL.md` — Progressive Disclosure skills shared by Antigravity & Claude.
- `.agent/workflows/<name>.md` — Antigravity-only deterministic procedures (`// turbo` enables auto-run within allowlist).
- `.agent/rules/` — Antigravity workspace rules (always-on guidance).

## 9. Known Constraints

<!-- Fill in per project. Examples: -->
<!-- - Target Node 20 LTS only. -->
<!-- - Database migrations are forward-only. -->
<!-- - Public API is frozen until v1.0. -->

- _<constraint>_

## 10. References

- Antigravity docs: <https://antigravity.google/docs>
- AGENTS.md spec: <https://agents.md>
- Codex AGENTS.md guide: <https://developers.openai.com/codex/guides/agents-md>
- This template: <https://github.com/DeL-TaiseiOzaki/antigravity-orchestra>
