"""Out-of-office one-liner entry.

Output contract: the program writes exactly one sentence to entry.txt
inside the directory given by MAKEFUN_OUTPUT_DIR (default "/output").
The line is a single line, non-empty, at most 200 characters, with no
control characters and no trailing newline.
"""

import os

ENTRY_LINE = (
    "I'm out until Monday, ignoring all 412 unread emails equally, "
    "yours included, and I'll reply once I've recovered."
)

MAX_LENGTH = 200


def validate_line(line: str) -> None:
    """Check the entry line is a single non-empty line within the limit."""
    if not line:
        raise ValueError("entry line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        raise ValueError("entry line must not contain control characters")
    if len(line) > MAX_LENGTH:
        raise ValueError(f"entry line exceeds {MAX_LENGTH} characters")


def output_path() -> str:
    """Resolve the output file path from the environment."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    validate_line(ENTRY_LINE)
    with open(output_path(), "w", encoding="utf-8") as handle:
        handle.write(ENTRY_LINE)


if __name__ == "__main__":
    main()
