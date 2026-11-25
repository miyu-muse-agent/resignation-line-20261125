#!/usr/bin/env python3
"""One-line resignation letter writer for the make.fun bounty.

The bounty asks for the funniest one-line resignation letter, and
that single line is the whole entry. This program holds the line,
makes sure it really is one line of real words, and prints exactly
that line to stdout, where the judge reads it.

Standard library only; nothing to install.
"""


def resignation_line() -> str:
    """Return the resignation letter, exactly as it should reach the judge."""
    return "I resign, effective immediately — the printer jammed for the last time, and frankly, so did I."


def validate(line: str) -> None:
    """Check the line against the bounty rules.

    Raises ValueError with a plain reason when a rule fails, so a bad
    entry is obvious instead of silently printing something wrong.
    """
    if not line:
        raise ValueError("the resignation line is empty")
    if not line.strip():
        raise ValueError("the resignation line is only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("the resignation line must be a single line, with no line breaks")


def main() -> None:
    line = resignation_line()
    validate(line)
    print(line)


if __name__ == "__main__":
    main()
