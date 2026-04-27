---
description: Run a time-boxed exploratory experiment in a throwaway branch to answer a single yes/no question about feasibility, performance, or library fit. Outputs a research note; never merges to main.
---

# spike

## 0. State the question
Write down the **single** yes/no question this spike will answer.

> Example: "Can we serve 1k concurrent SSE connections on one Node
> process at p99 < 200ms?"

If the question is not yes/no, sharpen it before starting. "Should we
use library X?" is too broad; "Does library X handle our 50MB JSON
payload without OOM at 256MB heap?" is a spike.

## 1. Time-box and branch
```bash
// turbo
git checkout -b spike/<short-question-tag>
```

Set a clock. **2 hours by default**, never more than half a day.
A spike that runs longer is hiding a real plan inside it.

## 2. Build the smallest thing that answers the question
```bash
// turbo-all
# Antigravity Ghost Runtime is the natural home for this — spawn a
# parallel Agent Manager card so the spike doesn't pollute your
# main working tree.
```

Cut every corner the question doesn't depend on:

- Hard-code config.
- No tests beyond the one that demonstrates the answer.
- No error handling.
- No logging beyond the measurement output.

## 3. Measure
Run the experiment. Capture the actual numbers (latency, memory,
throughput, output diff — whatever the question requires) into a
file:

```bash
// turbo
mkdir -p docs/research
{
  echo "# Spike: <question>"
  echo
  echo "Date: $(date -u +%Y-%m-%d)"
  echo "Branch: $(git rev-parse --abbrev-ref HEAD)"
  echo
  echo "## Method"
  echo "<one paragraph>"
  echo
  echo "## Numbers"
  echo "<paste actual measurements>"
  echo
  echo "## Answer"
  echo "<yes | no | depends on X — single sentence>"
} > docs/research/$(date -u +%Y-%m-%d)-spike-<tag>.md
```

## 4. Decide the disposition
Three legal outcomes:

| Answer | Next step |
|---|---|
| **Yes** | Open a `plan` for productionizing — start a fresh `start-feature` workflow. The spike branch dies. |
| **No** | Commit the research note to `main` (it has value as a "we tried, here's why not"). Drop the spike branch. |
| **Depends** | Sharpen the question and run a second spike. |

## 5. Drop the spike branch
```bash
// turbo
git checkout main
git branch -D spike/<short-question-tag>
```

The research note stays. The branch never merges. **A spike is
discardable by design** — that's what makes it cheap.
