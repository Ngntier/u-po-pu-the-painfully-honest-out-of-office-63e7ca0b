"""Out-of-office auto-reply entry.

The joke angle: the sender confesses, in warm professional language,
that the job has been quietly exhausting them for most of the year, so
the time off is recovery rather than leisure -- while still promising
the sender's email a proper reply on return. Honesty about the toll,
politeness about the wait.
"""

import os

ENTRY = (
    "I'm out until Monday, resting the part of me my inbox has been "
    "quietly wearing down since January; your email matters, and I'll "
    "answer it properly once I'm back."
)


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    encoded = text.encode("utf-8")
    if len(encoded) > 200:
        raise ValueError("entry must fit in 200 UTF-8 bytes, got %d" % len(encoded))
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()
