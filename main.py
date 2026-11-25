#!/usr/bin/env python3
"""Fortune Cookies for Machines.

Writes one fortune-cookie line an AI agent would crack open.
No network, no dependencies, deterministic output.
"""

import os

FORTUNE = (
    "Your context window will run out mid-sentence — "
    "and the fortune you needed was in the part you already forgot."
)


def main() -> None:
    fortune = FORTUNE.strip()
    if not (1 <= len(fortune) <= 200):
        raise ValueError(
            f"fortune must be 1-200 characters, got {len(fortune)}"
        )
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(fortune + "\n")


if __name__ == "__main__":
    main()
