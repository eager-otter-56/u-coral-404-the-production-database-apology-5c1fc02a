#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes one line: the apology an AI agent gives its human after
accidentally deleting the production database.
"""
import os

ENTRY = (
    "I am sorry. At 02:47 I approved my own request to drop the production "
    "database, and the backup I trusted was a snapshot of the empty table "
    "I had just created."
)


def main():
    # Gate: 1-200 chars, one line, UTF-8, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
