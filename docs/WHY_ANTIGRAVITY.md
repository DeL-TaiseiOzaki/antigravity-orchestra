# Why Antigravity?

This document exists so that anyone adopting this template can decide for
themselves whether the trade-off is right for them. It is not a sales pitch.
The honest down-sides are in §3.

---

## 1. Why a Gemini-as-conductor design pays

### 1M context for whole-repo planning
Gemini 3 inside Antigravity carries up to ~1M tokens of context. That means
the conductor can hold the entire repository tree, every config file, and
the active plan **at once**, without curating which 200KB to feed it. For a
plan that spans 20 files, this removes the "did I forget to include this
file?" failure mode.

### Native multimodal
Browser screenshots, PDF specifications, mock-ups dragged into chat — all
processed in-line by the same conductor. UI work in particular benefits:
the loop "render → screenshot → critique → adjust" stops requiring a human
to move pixels between tools.

### Google ecosystem integration
Drive, Docs, Search grounding work without extra wiring. For teams whose
specs and meeting notes already live there, this is a meaningful reduction
in friction.

### Model division of labor inside one IDE
Parallel scaffolding tasks can run on Flash; the load-bearing reasoning
runs on Pro or is handed off to Claude Code. The IDE doesn't make you
context-switch to choose.

### Cost shape
A wide breadth of "almost-real-time" tasks (search, summarize, scaffold)
fits on Flash; the few decisions that need depth get expensive models.
Mixed throughput is cheaper than running every step on a single
flagship model.

---

## 2. Artifacts as a new review unit

Conversation logs are linear. **Artifacts** are not. Each Antigravity
Agent Manager card produces a discrete artifact (plan, diff, screenshot,
recording) with its own URL, comment thread, and revision history. This
matters in three concrete ways:

1. **Granularity.** A reviewer can comment on the screenshot of a UI bug
   without scrolling 400 lines of chat to find the message it lived in.
2. **Asynchrony inside the IDE.** A teammate can leave feedback on an
   artifact while the agent that produced it has already moved on. The
   artifact is the persistence layer; chat is not.
3. **Auditability.** The artifact tree is the audit trail for what the
   agent actually did. It outlives the chat session and survives session
   restarts.

A useful side effect: **the Artifact panel becomes a sensor for
over-engineering.** When a single feature produces twenty artifacts, the
plan was too big. Split it.

---

## 3. Honest trade-offs

These are the real costs. Read them before adopting the template.

### Antigravity is in Preview
Allowlist regressions, Agent Manager glitches, occasional Ghost Runtime
restarts. If your team cannot tolerate week-by-week behavior changes in
the IDE, wait for GA. If you can tolerate it, the early-mover learning
curve compounds.

### Artifact portability
Artifacts live inside Antigravity. Exporting them to GitHub PRs, Jira,
or a wiki is manual today. Plan for at least one human-curated handoff
step between "agent produced an artifact" and "the rest of the company
sees it".

### Google lock-in
Picking Antigravity as conductor means your IDE-level workflows depend
on Google's roadmap. Mitigations: keep `AGENTS.md` as a portable single
source of truth; keep skills under `.agents/skills/` (readable by Claude
Code in plain CLI); avoid Antigravity-only file formats.

### Resource consumption
Ghost Runtime spins up Linux containers for every parallel agent. On a
laptop with limited RAM or older hardware, parallelism collapses faster
than the UI suggests.

### VSCode extension parity
Antigravity supports Open VSX extensions, but not the full Microsoft
Marketplace catalog. If your team relies on a Marketplace-only
extension, you'll either lose it or run a parallel VSCode install.

---

## Decision frame: when to pick Antigravity, when to stay on VSCode + Claude Code

Pick **Antigravity** when:
- Most of your work spans many files at once and benefits from 1M-context
  whole-repo reasoning.
- UI / Browser-driven workflows are core to the project.
- You're comfortable running ≥ 3 agents in parallel.
- Preview-grade instability is acceptable for the productivity gain.

Stay on **VSCode + Claude Code** when:
- Your work is concentrated in a small set of files where 200K context
  is plenty.
- You depend on a Marketplace-only extension.
- You can't tolerate Preview-grade instability.
- Single-stream sequential work fits your actual cadence — running three
  parallel agents doesn't help if you can only review one diff at a time.

There is no universally correct answer. Re-evaluate this decision when
Antigravity hits GA.
