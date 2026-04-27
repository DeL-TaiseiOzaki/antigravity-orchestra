#!/usr/bin/env python3
"""Optional hook: append a JSONL audit record when Claude shells out to
another CLI agent (claude / codex / gemini).

Disabled by default. To enable, register this script under
`hooks.PreToolUse` (or `PostToolUse`) in `.claude/settings.json` with a
matcher of `Bash`. Output is appended to `.claude/logs/cli-tools.jsonl`.
"""
from __future__ import annotations

import datetime as _dt
import json
import os
import sys
from pathlib import Path

WATCHED_BINARIES = ("claude", "codex", "gemini")
LOG_PATH = Path(".claude/logs/cli-tools.jsonl")
STDOUT_LIMIT = 4000


def first_token(command: str) -> str:
    command = command.strip()
    if not command:
        return ""
    return command.split()[0].rsplit("/", 1)[-1]


def truncate(text: str, limit: int = STDOUT_LIMIT) -> str:
    if text is None:
        return ""
    if len(text) <= limit:
        return text
    return text[:limit] + f"\n... [truncated {len(text) - limit} bytes]"


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    tool_input = payload.get("tool_input") or {}
    command = tool_input.get("command")
    if not isinstance(command, str):
        return 0
    binary = first_token(command)
    if binary not in WATCHED_BINARIES:
        return 0
    tool_response = payload.get("tool_response") or {}
    record = {
        "ts": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "cwd": os.getcwd(),
        "binary": binary,
        "command": command,
        "stdout_excerpt": truncate(tool_response.get("stdout") or ""),
        "exit_code": tool_response.get("exit_code"),
    }
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as fp:
        fp.write(json.dumps(record, ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
