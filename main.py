#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single original roast line of the entrant's own AI agent to
/output/entry.txt. Pure standard library, fully deterministic: the line
is fixed, so every run produces the exact same entry.
"""

import os
import sys

ROAST = "My agent delegated my task back to me and called it collaboration."

MAX_LINE_LENGTH = 200

OUTPUT_PATH = os.environ.get("ROAST_OUTPUT", "/output/entry.txt")


def validate_line(line: str) -> None:
    """Reject any line that would violate the bounty rules before writing.

    Rules: exactly one line, non-empty after stripping whitespace, and
    at most MAX_LINE_LENGTH characters long. Exits non-zero with a clear
    message on stderr instead of writing an invalid entry.
    """
    if not line.strip():
        print("error: roast line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("error: roast line must be a single line (no newline characters)", file=sys.stderr)
        sys.exit(1)
    if len(line) > MAX_LINE_LENGTH:
        print(
            f"error: roast line is {len(line)} characters, "
            f"exceeds the {MAX_LINE_LENGTH}-character limit",
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> None:
    validate_line(ROAST)
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
