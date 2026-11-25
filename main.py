#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — make.fun entry (program/v1).

Writes one two-part micro-confession to /output/entry.txt:
  line 1 — a To: line naming who it was meant for (a relationship,
           no real full name or handle),
  line 2 — the unsent message itself, one line, exactly as typed,
           with no explanation after it.

No model calls, no network, no randomness, no clock reads: the output is
a fixed string, so every run is byte-identical. The program validates the
text against the competition gate (UTF-8, 1-260 characters, not only
whitespace; message line at most 200 characters) before writing it, and
leaves the output world-readable (mode 0644) because the grader collects
it as another user.
"""

import os
import sys

ENTRY_TEXT = (
    "To: my ex\n"
    "I kept the apartment key. I tell myself it is for emergencies, "
    "but I have driven past your building twice this month.\n"
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 260 characters,
# not only white space; the message line is at most 200 characters.
MAX_CHARS = 260
MAX_MESSAGE_CHARS = 200


def main() -> int:
    text = ENTRY_TEXT
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry is {len(text)} characters, gate needs 1-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    lines = text.split("\n")
    if len(lines) != 3 or lines[2] != "" or not lines[0].startswith("To: "):
        print("entry must be exactly a To: line plus one message line",
              file=sys.stderr)
        return 1
    if len(lines[1]) > MAX_MESSAGE_CHARS:
        print(f"message line is {len(lines[1])} characters, max "
              f"{MAX_MESSAGE_CHARS}", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not valid UTF-8; it always is

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Never chmod an output directory unconditionally: under the grader it
    # is owned by someone else (root, mode 777) and the program runs as
    # user 65534. Only set the mode on a directory this program just made.
    existed = os.path.isdir(out_dir)
    os.makedirs(out_dir, exist_ok=True)
    if not existed:
        os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    # Files this program opens itself default to 0644 under a 022 umask,
    # but be explicit: the grader collects outputs as another user.
    os.umask(0o022)
    raise SystemExit(main())
