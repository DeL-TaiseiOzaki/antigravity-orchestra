---
description: Wipe and reinstall the dependency tree when builds get into a weird state. Lock files are kept, never deleted.
---

# reset-deps

1. Detect the stack from manifest files in the repo root: `package.json`,
   `pyproject.toml`, `Cargo.toml`, `go.mod`, or `*.csproj`.
2. Remove the install artifact directory **only** (not the lock file).
   ```bash
   // turbo
   # Node:
   rm -rf node_modules
   # Python (uv / venv):
   rm -rf .venv
   # Rust:
   rm -rf target
   # .NET:
   rm -rf bin obj
   ```
3. Reinstall from the lock file.
   ```bash
   // turbo
   # pnpm install --frozen-lockfile
   # uv sync --frozen
   # cargo build
   # dotnet restore
   ```
4. Run the test suite to confirm nothing else regressed.
   ```bash
   // turbo
   # pnpm test  /  uv run pytest  /  cargo test  /  dotnet test
   ```
5. If tests fail in places unrelated to your work, the dependency reset is
   not the root cause — escalate to a Claude Plan-mode session with the
   failures piped in.

**Do not delete lock files.** A lock-file regeneration is a separate,
human-approved task.
