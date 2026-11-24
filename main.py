#!/usr/bin/env python3
"""Worst AI Advice entry (variant A).

Writes the final one-liner to /output/entry.txt and to entry.txt
in the repo root. Deterministic: no randomness, no network.

The line was iterated v1-v8 on one concept (confident AI prescribes
a catastrophic fix for a production outage). The shipped version
escalates twice — delete the database, then the backups — so the
advice destroys its own recovery path, and the punchline justifies
it in the AI's tidy voice: with nothing left to break, the alerts
finally stop. 137 chars, inside the 1-140 gate.
"""

import os

LINE = (
    "To resolve the outage, delete the production database, then "
    "the backups — with nothing left to break, the error alerts "
    "will finally stop."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"),
               "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
