---
name: troubleshoot
description: Use when a bug is reported, a test is failing, or production is misbehaving. Provides observation patterns and diagnostic moves rather than a fixed sequence — every bug has its own shape. Pairs naturally with pipe-fed log analysis.
---

# troubleshoot

A skill, not a script. The point is to ask the right questions, not run
a recipe.

## First moves (always)

1. **Reproduce.** If you cannot reproduce, the bug isn't fixed when you
   "fix" it. Write the reproducer down before changing anything.
2. **Bisect when reproducible.** `git bisect` is faster than reading.
3. **Read the actual error**, not a paraphrase. Stack traces are
   evidence, not noise.

## Observation patterns

- **What changed?** — Last deploy, last migration, last config change.
  Time correlation usually wins.
- **Where does it stop being true?** — Walk inputs and intermediate
  values until the assertion fails.
- **Who else sees it?** — Single-user vs. all-users vs. randomly-sampled
  is three different bugs.
- **State vs. logic.** — Cleared cache, fresh DB, fresh user — does the
  bug survive? If not, it's state, not logic.
- **Is the test wrong?** — A test that has been green for months and
  failed today is more likely catching a real regression than being
  wrong itself, but verify.

## Anti-patterns

- "It works on my machine." If yours and theirs differ, find the
  difference rather than dismissing.
- Adding `try / except` to silence a stack trace. That's a coverup, not
  a fix.
- Fixing a symptom in three places. If it shows up in three places, the
  cause is upstream.
- Long debugging sessions without writing anything down. Past you is a
  separate person from current you, and they took notes for a reason.

## Pipe input

```
docker logs api --since 30m | claude "Apply the troubleshoot skill. Group recurring errors and propose root causes."
kubectl describe pod <pod> | claude "Apply the troubleshoot skill. What likely caused this CrashLoopBackOff?"
git bisect log | claude "Apply the troubleshoot skill. What does the bisect outcome suggest?"
```

## When to stop and escalate

- After ~30 minutes without a hypothesis you can falsify.
- When the fix would touch a module you didn't write and don't fully
  understand — pull in the owner.
- When the suspected root cause is in a third-party dep — switch to the
  `research-lib` skill before swapping libraries on instinct.
