#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes one funny excuse, spoken by an AI agent to its human right after
breaking production, to /output/entry.txt (at most 180 characters).
"""

import os
import sys

EXCUSE = "I didn't break production, I just followed your instructions exactly - turns out the bug was in your prompt, and I executed it flawlessly."


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    out_dir = os.path.dirname(out_path)
    if out_dir and not os.path.isdir(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
