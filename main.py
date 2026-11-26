#!/usr/bin/env python3
"""Write one painfully honest out-of-office auto-reply to entry.txt.

Pure Python stdlib only. Deterministic: the same line every run.
The entry is validated before it is written: one line, 1-200 chars.
"""

import os
import sys

ENTRY = (
    "I'm away, and honestly my return date is more rumour than plan, so "
    "your email will wait for fresh eyes and real attention when I'm back "
    "- thank you for trusting me with the wait."
)


def main():
    if not 1 <= len(ENTRY) <= 200:
        sys.exit("entry must be 1-200 characters, got %d" % len(ENTRY))
    if "\n" in ENTRY or "\r" in ENTRY:
        sys.exit("entry must be a single line")
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
