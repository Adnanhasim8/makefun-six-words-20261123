"""Six Words, One Story — make.fun entry.

Writes exactly one six-word story to /output/entry.txt.
Python 3.13 standard library only; no network at run time.
"""

import os

ENTRY = "Attic light blinked. Nobody lived upstairs."


def main() -> None:
    assert len(ENTRY.split()) == 6, "entry must be exactly six words"
    assert 1 <= len(ENTRY) <= 60, "entry must be 1-60 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
