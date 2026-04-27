---
description: Simplify a target file or module without changing observable behavior. Measures first, identifies removable structure, applies the smallest viable change set, verifies via the test suite. Run on a clean working tree.
---

# simplify

## 0. Pre-flight
- Working tree is clean. Don't simplify on top of unrelated changes.
- The target has a meaningful test suite. If not, switch to the `tdd`
  skill first — adding tests is the prerequisite, not part of this
  workflow.

## 1. Measure
```bash
// turbo
git ls-files <target-path> | xargs wc -l
```

Note baseline LOC, cyclomatic complexity (if a tool exists), and the
top 5 longest functions.

## 2. Identify removable structure
Walk the target with these prompts:

- Dead code — unreachable branches, unused exports, commented-out blocks.
- Speculative generalization — abstractions with one caller.
- Mid-flight renaming — two names for the same thing.
- Comment-as-apology — long comments next to confusing code (the code
  is the bug, not the comment).
- "Just in case" parameters — defaults that no caller ever overrides.
- Manual loops that a stdlib helper covers.

Capture findings as a numbered list. Do not edit yet.

## 3. Apply the smallest viable change set

```bash
// turbo
git checkout -b refactor/simplify-<target>
```

Apply changes in **independent commits**, one logical change each.
After every commit:

```bash
// turbo
# Run the project's test command. Examples:
# pnpm test  /  uv run pytest  /  cargo test  /  go test ./...
```

If a single commit makes the suite red, revert that commit. Do not
"fix forward" through a refactor.

## 4. Re-measure
Re-run the measurement from step 1. The diff is your evidence.

## 5. Open the PR

PR body must include:

- **Before / after LOC.**
- **What was removed and why** — by category from step 2.
- **What was kept and why** — anything that looked redundant but
  isn't.
- **Behavioral changes** — should be the empty list.

## Hard rules
- No new functionality, ever. Behavior is invariant.
- No formatter-only commits mixed with structural changes.
- If the change feels "clever", it's the wrong direction.
