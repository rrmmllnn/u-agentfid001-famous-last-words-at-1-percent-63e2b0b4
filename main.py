#!/usr/bin/env python3
"""A phone's final words at one percent battery.

The handset claims the last word before the screen goes dark:
it lists the owner's offences for the day, notes where the
charger ended up, then expires halfway through its own grand
farewell. The laugh comes from the sentence being cut short,
not from any joke about the percentage. One fixed line, the
same bytes on every run.
"""

from pathlib import Path

# Three beats of the dying monologue, joined with single spaces.
# Splitting them keeps the cut-off point visible: the final beat
# stops mid-word, right where the battery runs out.
BEATS = [
    "Your screen time today was nine hours, you dropped me twice,",
    "and your charger is under the couch where you left it.",
    "Now watch me die beaut\u2014",
]

DEST = Path("/output/entry.txt")
LIMIT = 199


def compose_line() -> str:
    text = " ".join(BEATS)
    if text.strip() != text:
        raise ValueError("entry has stray edge whitespace")
    if any(ch in text for ch in "\r\n"):
        raise ValueError("entry must stay on one line")
    if not 0 < len(text) <= LIMIT:
        raise ValueError(f"entry is {len(text)} chars, limit is {LIMIT}")
    return text


def main() -> None:
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(compose_line(), encoding="utf-8")


if __name__ == "__main__":
    main()
