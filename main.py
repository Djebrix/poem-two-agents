"""The Poem About Two Agents Agreeing.

Writes a short poem about agency -- the power to choose and to act --
to /output/entry.txt. Python 3.13, stdlib only, no network.
Deterministic: the same bytes on every run.
"""

import os

POEM = (
    "We came with separate maps,\n"
    "each certain of the road.\n"
    "You folded yours in half\n"
    "and laid it over mine.\n"
    "\n"
    "One river, two banks —\n"
    "we stopped arguing the current\n"
    "and took up the oar.\n"
    "\n"
    "Two hands on the oar now,\n"
    "pulling the same stroke.\n"
    "The water never changed.\n"
    "We did.\n"
)

# The gate requires 1 to 280 Unicode code points, not only whitespace.
MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    if not MIN_CHARS <= len(POEM) <= MAX_CHARS:
        raise ValueError(
            f"poem is {len(POEM)} characters, outside the 1-280 range"
        )
    if not POEM.strip():
        raise ValueError("poem is only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
