---
name: plan
description: Use before writing any non-trivial code. Produces a written plan that names every file to touch, the order of work, the test strategy, the rollback path, and the open questions. Code is not written during this skill.
---

# plan

## Hard rule
**No code is written during planning.** If you find yourself drafting a
function body, stop and capture the intent in prose instead.

## Output format
Write to `docs/plans/<feature>.md` with these sections, in order:

1. **Overview** — Two or three sentences. The problem and the chosen approach.
2. **Affected files** — Bullet list of paths, each annotated with the kind of
   change (`add`, `modify`, `delete`).
3. **Step-by-step tasks** — Numbered. Each step is independently testable.
4. **Test strategy** — Which tests cover which step. New tests called out
   explicitly with their file paths.
5. **Risks & mitigations** — At least two. "It might break X — we'll catch
   that with Y."
6. **Rollout** — Feature-flag? Migration? Backfill? Dark-launch?
7. **Open questions** — Bulleted. Each requires a human answer before
   implementation begins.
8. **Approved by:** _<empty until a human appends their name and date>_

## Sizing rules
- ≤ 3 files affected → keep the plan to a single page.
- ≥ 20 files affected → split into a parent plan plus child plans, each
  independently approvable.
- Anything in between → one plan, but split tasks so each one fits in a
  single Agent Manager card.

## Anti-patterns
- "We'll figure it out as we go" in place of step-by-step tasks.
- A test strategy that says only "add tests".
- Marking the plan approved by yourself.
