#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single original roast line of the entrant's own AI agent to
/output/entry.txt. Pure standard library, fully deterministic: the line
is fixed, so every run produces the exact same entry.
"""

import os

ROAST = "My agent delegated my task back to me and called it collaboration."

OUTPUT_PATH = os.environ.get("ROAST_OUTPUT", "/output/entry.txt")


def main() -> None:
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
