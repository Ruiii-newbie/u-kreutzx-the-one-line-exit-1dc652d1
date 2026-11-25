"""The One-Line Exit — one funny single-line resignation letter.

The program's whole job: emit exactly one line to /output/entry.txt and
prove it passes the sealed gate (1-140 chars, UTF-8, not blank, one line).
"""

from pathlib import Path

ENTRY = (
    "Dear boss: I quit. The printer and I have agreed \u2014 it keeps jamming, "
    "I keep leaving, and only one of us is replaceable."
)
MAX_CHARS = 140
OUT = Path("/output/entry.txt")


def validate(text: str) -> str:
    """Return the text unchanged if it passes every gate rule, else raise."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, gate allows 1-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # gate requires UTF-8 text
    return text


def main() -> None:
    line = validate(ENTRY)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} chars to {OUT}")


if __name__ == "__main__":
    main()
