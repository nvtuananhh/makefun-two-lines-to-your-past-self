#!/usr/bin/env python3
"""Two Lines to Your Past Self.

Writes a two-line warning to /output/entry.txt.
"""

import os

ENTRY = """Don't tell your dad 'I'll call you back' on the night of December 23rd and then forget.
He waited by the phone until midnight, and you have been calling back every Sunday since."""

assert 1 <= len(ENTRY) <= 280 and ENTRY.count("\n") == 1 and ENTRY.strip()

# One specific moment: a sentence said out loud on the night of
# December 23rd. Line 2 traces the real consequence — he waited until
# midnight — and the changed behaviour since: calling back every Sunday.
# Plain, vivid, written to one person; the twist is that the forgotten
# call became a weekly ritual, not a second anecdote.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
