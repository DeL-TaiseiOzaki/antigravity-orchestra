---
name: design-tracker
description: Use when an architectural decision has been made or is about to be made. Decides whether the decision belongs in docs/DESIGN.md, what level of detail to record, and what NOT to record. Operates as a judgment skill, not a fixed procedure — for the procedure see the update-design workflow.
---

# design-tracker

## What belongs in docs/DESIGN.md
A decision belongs in DESIGN.md when **all** are true:

- It cannot be re-derived from the code alone six months from now.
- A future reasonable engineer might choose differently without context.
- It has a non-trivial blast radius (touches multiple modules, or locks
  in an external dependency, or constrains future changes).

## What does NOT belong
- Style preferences settled by the linter / formatter.
- Choices that the README or AGENTS.md already encodes.
- Implementation details internal to a single module.
- "We tried X and it didn't work today" — that goes to `docs/research/`,
  not DESIGN.md.

## Required level of detail
Per entry, the absolute minimum:

- **Context** — one or two sentences. Why a decision was needed.
- **Decision** — the choice, in one sentence.
- **Alternatives considered** — at least two. The why-not is more
  valuable than the why.
- **Consequences** — what the decision now obliges the team to do or
  forbids them from doing.

If you cannot fill those four, the decision isn't ready — go think more,
or move it to `docs/research/`.

## Status field
`proposed` → `accepted` → `superseded by <link>`. Never delete. Never
edit accepted entries except to mark them superseded.

## Triggers
- A `## Approved by:` line just appeared on a plan that locks in a
  significant choice.
- A research note in `docs/research/` reached a conclusion.
- A reviewer asked "why did we do it this way?" and the answer wasn't in
  DESIGN.md.

When triggered, hand off to the `update-design` workflow for the
mechanical write step.
