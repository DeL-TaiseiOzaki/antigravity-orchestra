---
name: research-lib
description: Use when evaluating a library, framework, or external service for adoption. Walks evaluation axes (fit, maintenance, license, footprint, integration cost) and produces a recommendation with explicit trade-offs. Output goes under docs/research/.
---

# research-lib

A library is a **dependency you can't easily uninstall**. Evaluate it as
such.

## Evaluation axes

For each candidate, score on these axes. "Score" is a one-line
verdict, not a number.

1. **Fit** — Does it solve the problem we actually have, or a related
   problem we'd be forced to grow into? Is the abstraction at the right
   level for our use?
2. **Maintenance** — Last release date. Open / closed issue ratio.
   Number of contributors in the last 12 months. Does one corporate
   sponsor hold it up?
3. **License** — MIT / Apache-2.0 / BSD are routine. Anything copyleft,
   custom, or "source-available" needs a deliberate green light.
4. **Footprint** — Install size, runtime memory, dependency tree depth,
   build-time impact. Does it pull in transitive deps we'd otherwise
   avoid?
5. **Integration cost** — How much glue code do we write? Does it force
   a programming-model change (callback → async, sync → async, etc.)?
6. **Exit cost** — If this turns out wrong in 12 months, how painful is
   removal? Does it leak through public APIs or is it isolated behind
   one module?

## Required output

Write to `docs/research/<YYYY-MM-DD>-<lib-name>.md`:

```
# <library> evaluation

Problem: <one sentence — what we'd use it for>

Candidates considered: A / B / C

Scores
- Fit:              ...
- Maintenance:      ...
- License:          ...
- Footprint:        ...
- Integration cost: ...
- Exit cost:        ...

Recommendation: adopt | reject | revisit in <N months>
Trade-offs accepted: <bullet list>
Trade-offs rejected: <bullet list>
```

## Hard rules
- **Always evaluate at least two candidates.** A single-candidate review
  is a rationalization, not a decision.
- **Adoption requires a docs/DESIGN.md entry** with the
  `update-design` workflow.
- A library with fewer than 50 GitHub stars or no release in 12 months
  is not a library — it's a fork-in-waiting.
