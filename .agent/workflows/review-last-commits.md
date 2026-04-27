---
description: Run a code review over the last N commits or a commit range, save the report, optionally cross-check with Codex.
---

# review-last-commits

1. Confirm the audit range with the human. Default: `main...HEAD`. Other
   acceptable forms:
   - `HEAD~5..HEAD` — last five commits.
   - `<sha1>..<sha2>` — explicit range.
2. Pipe the diff into Claude with the `code-review` skill.
   ```bash
   // turbo
   git diff <range> | claude --verbose "Apply the code-review skill from .agents/skills/code-review/SKILL.md. Output Critical/High/Medium/Low."
   ```
3. Save the output to `docs/reviews/<YYYY-MM-DD>-<short-topic>.md`.
4. (Optional) Cross-check with Codex on the same diff:
   ```bash
   git diff <range> | codex "Same review checklist. Reply only with disagreements vs. the Claude review at docs/reviews/<file>."
   ```
5. Reconcile findings. Where Claude and Codex disagree, escalate to the
   human reviewer — those points usually expose hidden assumptions.
