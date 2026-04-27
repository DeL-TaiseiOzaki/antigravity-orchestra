---
description: Start a new feature branch with clean dependencies and a Plan-mode invitation. Run from a working tree on main.
---

# start-feature

1. Ask the human for the feature name in kebab-case (e.g. `auth-rotation`).
2. Sync `main` with origin.
   ```bash
   // turbo
   git fetch origin main && git checkout main && git pull --ff-only origin main
   ```
3. Create the feature branch.
   ```bash
   // turbo
   git checkout -b feat/<feature-name>
   ```
4. Resolve dependencies for the active stack.
   ```bash
   // turbo
   # Pick one based on the project:
   # pnpm install --frozen-lockfile
   # uv sync
   # cargo build
   # go mod download
   ```
5. Confirm the build succeeds.
   ```bash
   // turbo
   # pnpm build  /  cargo build  /  go build ./...  /  dotnet build
   ```
6. Open Claude Code in Plan mode and invoke the `plan` skill, targeting
   `docs/plans/<feature-name>.md`. Do **not** start implementing yet.
