# SETUP.md

How to take this template from "freshly cloned" to "three agents working in
concert". Allow ~10 minutes for first-time setup.

## 1. Prerequisites

- **Antigravity IDE** — install from <https://antigravity.google>. Sign in
  with the Google account you want associated with this project.
- **Claude Code CLI** — install per
  <https://docs.claude.com/en/docs/claude-code/install>. Verify with:
  ```bash
  claude --version
  ```
- **Codex CLI** — install per
  <https://developers.openai.com/codex>. Verify with:
  ```bash
  codex --version
  ```

You don't have to install all three to start. Antigravity alone is enough
to read this template; Claude and Codex unlock the sandwich workflow.

## 2. Initialize a project

### New project from this template

```bash
git clone --depth 1 https://github.com/DeL-TaiseiOzaki/antigravity-orchestra.git .starter \
  && cp -r .starter/.agent .starter/.agents .starter/.claude .starter/.codex .starter/.gemini . \
  && cp .starter/AGENTS.md .starter/CLAUDE.md . \
  && rm -rf .starter

git init
git add .
git commit -m "chore: bootstrap from antigravity-orchestra"
```

### Existing project

Run the same copy commands inside your existing repo. Then merge any
existing `.gitignore` rules manually — this template's `.gitignore` is
multi-stack, so review before overwriting.

## 3. Fill in AGENTS.md

Three sections need real content before agents can be trusted:

- **§1 Project Overview** — name, purpose, stack, status.
- **§2 Build / Test / Quality Commands** — the actual commands of your
  stack. Examples for Node / Python / Rust / Go are in the file as
  comments.
- **§9 Known Constraints** — anything an agent will fail without knowing
  (e.g. "target Node 20 LTS", "migrations are forward-only").

Stay under the 300-line / 5KB cap. The cap is a feature; it forces the
file to remain readable in one breath.

## 4. Configure Antigravity

1. Open the project folder in Antigravity.
2. **Terminal Auto Execution → Allowlist Mode.** Disable `Always Proceed`.
3. Merge `.gemini/antigravity/browserAllowlist.txt` into your user-level
   `~/.gemini/antigravity/browserAllowlist.txt`. The repo copy is a
   recommendation, not the effective list.
4. Confirm the Agent Manager and Browser agent are visible in the side panel.

## 5. Configure Claude Code

`.claude/settings.json` is already set with allow / deny lists matching
`AGENTS.md` §6. Hooks (`.claude/hooks/lint-on-save.py`) are pre-registered.
Verify hook executability:

```bash
chmod +x .claude/hooks/*.py
```

Smoke test:

```bash
claude "Read AGENTS.md and summarize the multi-agent roles in three lines."
```

## 6. Configure Codex

`.codex/config.toml` and `.codex/AGENTS.md` are already in place. Smoke
test:

```bash
codex "Read .codex/AGENTS.md and confirm you understand the five-attempt rule."
```

## 7. First sandwich run

1. Open Claude Code in Plan mode. Ask it to draft a plan for any tiny
   change (e.g. "add a placeholder to README.md"). Save under
   `docs/plans/`.
2. Append `## Approved by: <your-name> · <date>` to the plan.
3. Open Antigravity Agent Manager. Implement against the approved plan.
4. From the embedded terminal:
   ```bash
   git diff main...HEAD | claude --verbose "Apply the code-review skill."
   ```

If all three steps run end-to-end, the template is wired correctly.

## 8. Troubleshooting

- **Shift+Enter doesn't insert a newline in the terminal.** Run
  `claude /terminal-setup` once. Antigravity's embedded terminal needs
  the same one-time keymap as VSCode.
- **A pipe-composed command isn't auto-running.** Antigravity's Allowlist
  matcher inspects the first command, but compound commands with pipes /
  subshells require explicit approval. This is intended.
- **`lint-on-save.py` doesn't fire.** Confirm the script is executable
  (`ls -l .claude/hooks/lint-on-save.py` should show `x`). If your stack
  is detected but no linter is installed, the hook silently exits 0 by
  design.
- **Agents read the wrong AGENTS.md.** They walk **upward** from the file
  they're editing. If you have a nested project root, place an
  `AGENTS.md` there too — root-level instructions don't auto-cascade
  through unrelated subprojects.

## 9. Going further

- `docs/WHY_ANTIGRAVITY.md` — read before evangelizing this stack to
  teammates. The trade-offs section in particular.
- `.agents/skills/checkpointing/SKILL.md` — run before any session passes
  ~20 turns.
- `.agent/workflows/plan-then-implement.md` — the canonical sandwich
  workflow.
