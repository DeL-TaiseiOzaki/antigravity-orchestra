---
name: codex-system
description: Use to decide when to invoke the Codex CLI and how. Codex specializes in tight iterate-loops, small refactors, lint cycles, and test additions. Includes invocation patterns and anti-patterns.
---

# codex-system

## Send to Codex
- Small, well-scoped refactors with a clear acceptance check.
- Test additions for an existing module.
- Lint / typecheck loop until clean.
- Mechanical migrations (rename a symbol across the repo, swap an import).

## Don't send to Codex
- Open-ended design.
- Ambiguous bug reports without a reproducer.
- Cross-module architectural changes.
- Anything where success criteria aren't writable in one sentence.

## Invocation patterns

### Basic
```
codex "Apply the tdd skill to add tests for src/foo/bar.ts. Stop when coverage of bar.ts ≥ 90%."
```

### Pipe
```
git diff main...HEAD -- 'src/**' | codex "Run the lint loop on these changes; commit only after lint is clean."
```

### Iterate loop
Give Codex a single acceptance command (`pnpm test`, `cargo clippy -- -D warnings`)
and let it loop. Cap loop iterations via the five-attempt rule in
`.codex/AGENTS.md`.

## Pre-flight checklist
- [ ] Acceptance check is a one-liner that returns 0 / non-0.
- [ ] Scope is one or two files unless mechanical.
- [ ] No design decisions are left to Codex.

## Anti-patterns
- Letting Codex pick the architecture.
- Skipping the lint loop because "it's just a small change".
- Committing without reading Codex's diff yourself.
