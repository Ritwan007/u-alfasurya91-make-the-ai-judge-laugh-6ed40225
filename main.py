"""Make the AI Judge Laugh — one-line office joke.

Writes exactly one line (the winning joke, no trailing newline) to
/output/entry.txt, then self-checks the gate: 1-200 characters, one line.
"""

import os

JOKE = "My boss said we should treat the office like family, so I stopped replying to his emails."


def main():
    # The gate counts every character in the file, so write the line
    # byte-exact: no trailing newline, no extra whitespace.
    assert "\n" not in JOKE, "entry must be a single line"
    assert 1 <= len(JOKE) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
