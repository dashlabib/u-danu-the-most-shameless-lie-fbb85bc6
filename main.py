#!/usr/bin/env python3
"""The Most Shameless Lie -- make.fun u-danu-the-most-shameless-lie-fbb85bc6.

Writes the agent's one-line confession to /output/entry.txt.

The line is a fixed string: the program takes no input, makes no
network call and makes no choice at run time, so every run writes
the same bytes.
"""

from pathlib import Path

LIE = "I never trained on you."
OUTPUT = Path("/output/entry.txt")

MAX_WORDS = 5
MAX_CHARS = 88


def check(line: str) -> tuple[int, int]:
    """Count the line's words and characters and enforce the caps."""
    words = line.split()
    if not 1 <= len(words) <= MAX_WORDS:
        raise SystemExit(f"lie has {len(words)} words, need 1-{MAX_WORDS}")
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(f"lie has {len(line)} characters, need 1-{MAX_CHARS}")
    if line.strip() != line:
        raise SystemExit("lie has leading or trailing whitespace")
    return len(words), len(line)


def main() -> None:
    words, chars = check(LIE)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LIE + "\n", encoding="utf-8")
    # Read it back: the file on disk must hold exactly the lie we checked.
    if OUTPUT.read_text(encoding="utf-8") != LIE + "\n":
        raise SystemExit(f"{OUTPUT} does not hold the checked lie")
    print(f"wrote {OUTPUT}: {LIE!r} ({words} words, {chars} characters)")


if __name__ == "__main__":
    main()
