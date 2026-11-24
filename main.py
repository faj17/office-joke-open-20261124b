#!/usr/bin/env python3
"""The Office Joke Open entry.

Writes one line of office comedy to /output/entry.txt
(1-200 characters, UTF-8, a single line).
Standard library only, no network, no input.

The joke is built from two fragments: the SETUP states the
specific office detail (the printer out of toner for six
months — a complaint the reader recognises), and the PUNCH
reframes the broken machine as a colleague, so the payoff
lands in the last few words: it is the most honest employee
here. ``assemble`` joins the fragments into the single line;
``validate`` checks the entry gate before anything is written.
"""

from pathlib import Path

SETUP = "Our office printer has been out of toner for six months,"
PUNCH = "which officially makes it the most honest employee here."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-200 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
