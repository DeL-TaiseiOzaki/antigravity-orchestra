---
description: Append a new architectural-decision entry to docs/DESIGN.md. Run after a plan is approved, after a spike concludes, or after a reviewer questioned an unrecorded choice. Pairs with the design-tracker skill (which decides whether the decision belongs in DESIGN.md at all).
---

# update-design

## 1. Confirm the decision belongs in DESIGN.md
Apply the `design-tracker` skill first. If it says "not DESIGN-worthy",
stop — record it in the relevant plan or research note instead.

## 2. Gather context
```bash
// turbo
git log --oneline -10
ls docs/plans/
ls docs/research/
```

Identify the plan, research note, or commit that motivated this entry.
You'll link to it.

## 3. Append the entry
Open `docs/DESIGN.md`. Add a new section **at the bottom**, never
inserting between existing entries. Use this exact template:

```
## YYYY-MM-DD: <Short title>

- **Context:** <one or two sentences — why a decision was needed>
- **Decision:** <the choice, in one sentence>
- **Alternatives considered:**
  - <option A>: <why not>
  - <option B>: <why not>
- **Consequences:** <what this enables, what it forecloses, what we now owe>
- **References:** <plan link, research link, or commit SHA>
- **Status:** proposed | accepted
```

## 4. Commit on its own
```bash
// turbo
git add docs/DESIGN.md
git commit -m "docs: design — <short title>"
```

`docs/DESIGN.md` updates **never share a commit with code**. The
history needs to be greppable as a decision log.

## 5. Cross-link
If the entry was triggered by a plan, append a line to that plan:

```
Logged in DESIGN.md: YYYY-MM-DD — <short title>
```

## Hard rules
- Append-only. Never edit a previous entry except to mark it
  `superseded by <link>`.
- Never delete. The history is the value.
- One decision = one entry. Do not bundle "while we're here" extras.
