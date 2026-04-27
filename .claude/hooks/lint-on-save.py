#!/usr/bin/env python3
"""PostToolUse hook: run the project's linter on files just edited.

Reads a JSON payload from stdin describing the tool invocation. If the tool
edited or wrote a file, this hook detects the project's stack via root
manifests and runs the matching linter on the changed file.

Linters that aren't installed are silently skipped (exit 0). The hook never
blocks a successful edit.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

STACK_MANIFESTS: list[tuple[str, str]] = [
    ("package.json", "node"),
    ("pyproject.toml", "python"),
    ("Cargo.toml", "rust"),
    ("go.mod", "go"),
]


def find_repo_root(start: Path) -> Path | None:
    cur = start.resolve()
    for parent in [cur, *cur.parents]:
        for manifest, _ in STACK_MANIFESTS:
            if (parent / manifest).exists():
                return parent
        if any(parent.glob("*.csproj")):
            return parent
        if (parent / ".git").exists():
            return parent
    return None


def detect_stack(root: Path) -> str | None:
    for manifest, stack in STACK_MANIFESTS:
        if (root / manifest).exists():
            return stack
    if any(root.glob("*.csproj")):
        return "dotnet"
    return None


def extract_paths(payload: dict) -> list[str]:
    tool_input = payload.get("tool_input") or {}
    paths: list[str] = []
    if isinstance(tool_input.get("file_path"), str):
        paths.append(tool_input["file_path"])
    edits = tool_input.get("edits")
    if isinstance(edits, list):
        for edit in edits:
            if isinstance(edit, dict) and isinstance(edit.get("file_path"), str):
                paths.append(edit["file_path"])
    return paths


def run(cmd: list[str], cwd: Path) -> None:
    if not shutil.which(cmd[0]):
        return
    subprocess.run(cmd, cwd=cwd, check=False)


def lint(stack: str, root: Path, files: list[str]) -> None:
    if stack == "node":
        run(["pnpm", "lint", *files], root)
    elif stack == "python":
        run(["ruff", "check", *files], root)
    elif stack == "rust":
        run(["cargo", "clippy", "--quiet"], root)
    elif stack == "go":
        run(["go", "vet", "./..."], root)
    elif stack == "dotnet":
        run(["dotnet", "format", "--verify-no-changes"], root)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    paths = extract_paths(payload)
    if not paths:
        return 0
    root = find_repo_root(Path(paths[0]).parent) or Path(os.getcwd())
    stack = detect_stack(root)
    if stack is None:
        return 0
    files_in_repo = [p for p in paths if Path(p).is_file()]
    if not files_in_repo:
        return 0
    lint(stack, root, files_in_repo)
    return 0


if __name__ == "__main__":
    sys.exit(main())
