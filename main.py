#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — write one excuse line.

The program writes a single line of at most 200 characters to
/output/entry.txt, where the make.fun gate and judge read it.
"""

from pathlib import Path

EXCUSE = (
    "I spent the whole token budget writing this apology. "
    "The work is scheduled for next quarter."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Hold the excuse to the gate: UTF-8 text, 1 to 200 characters,
    a single line, and not only white space."""
    if not text or not text.strip():
        raise ValueError("excuse is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"excuse is {len(text)} characters, over the {MAX_CHARS} cap")
    text.encode("utf-8")


def output_path() -> Path:
    """The grader mounts /output; when it is not there (a local run),
    fall back to ./output so the program still runs anywhere."""
    root = Path("/output")
    try:
        root.mkdir(parents=True, exist_ok=True)
        return root / "entry.txt"
    except OSError:
        local = Path("output")
        local.mkdir(parents=True, exist_ok=True)
        return local / "entry.txt"


def main(argv: list[str]) -> None:
    validate(EXCUSE)
    path = output_path()
    path.write_text(EXCUSE, encoding="utf-8")
    print(f"wrote {len(EXCUSE)} chars to {path}")


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
