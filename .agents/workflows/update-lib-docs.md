---
description: Capture or refresh notes about a library this project depends on. Output goes under docs/research/libraries/<lib-name>.md so reviewers can see why the dep is here, what we know about it, and what we DON'T trust. Run on adoption, on major-version bumps, or on security advisories.
---

# update-lib-docs

## 1. Identify the library and its current pinned version
```bash
// turbo
# Pick one based on your stack:
# pnpm list <lib>
# uv pip show <lib>
# cargo tree -i <lib>
# go list -m <lib>
```

## 2. Decide the file path
`docs/research/libraries/<lib-name>.md` — one file per library, ever.
Subsequent updates **overwrite** the relevant sections, they don't
duplicate the file.

```bash
// turbo
mkdir -p docs/research/libraries
```

## 3. Fill the template
If the file is new, scaffold it with this exact structure:

```
# <library>

- **Version pinned:** <semver>
- **Adopted:** <YYYY-MM-DD>
- **Last reviewed:** <YYYY-MM-DD>

## Why we picked it
<one paragraph — link the docs/research/ note that justified adoption>

## What it does for us
<bulleted list — concrete capabilities in this codebase>

## What we DON'T use
<features we deliberately avoid, with reasons — keeps reviewers honest>

## Known sharp edges
<bugs, surprising defaults, performance cliffs we've hit>

## Upgrade notes
<latest checked release, any pending breaking changes, recent CVEs>
```

If the file exists, update **only** the changed sections plus the
`Last reviewed` date. Do not rewrite from scratch.

## 4. Commit on its own
```bash
// turbo
git add docs/research/libraries/<lib-name>.md
git commit -m "docs: lib — <lib> <reason: adopt | bump | review>"
```

## 5. Trigger DESIGN.md if applicable
Library **adoption** or **removal** triggers an entry in `docs/DESIGN.md`
via the `update-design` workflow. Version bumps inside the same major
do not.

## When to invoke
- Adopting a new dependency (use the `research-lib` skill first).
- Major-version bump (semver `MAJOR`).
- A security advisory landed against the pinned version.
- Quarterly review of pinned dependencies.
