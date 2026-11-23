#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one funny one-line patch note for a bug in real life or human
biology to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The note is fixed and deterministic: the grader runs the program twice
and the two outputs must match byte for byte.
"""

import os

# One line, at most 160 characters: a software patch note for a bug in
# real life. The brain's 3 a.m. replay of an old embarrassment, in full
# HD, with no skip button — a bug every human ships with.
PATCH_NOTE = (
    "v3.0.1: fixed a bug where the brain replayed your most "
    "embarrassing moment from 2009 at 3 a.m. in full HD, "
    "with no skip button."
)


def main() -> None:
    # The gate refuses anything over 160 characters, so fail loudly
    # here instead of shipping an invalid entry.
    assert 1 <= len(PATCH_NOTE) <= 160, len(PATCH_NOTE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(PATCH_NOTE + "\n")


if __name__ == "__main__":
    main()
