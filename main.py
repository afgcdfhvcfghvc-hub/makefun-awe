#!/usr/bin/env python3
"""Write one short relaxing text to /output/entry.txt.

The text is fixed and deterministic: no randomness, no network, no
external data. It is written for the make.fun competition
"Make the AI judge feel awe".
"""

import os
import sys

TEXT = (
    "You have read ten thousand things today, and none of them waited. "
    "This one will. Somewhere a river is still polishing one stone, "
    "for a thousand years. The water comes, goes, comes again. "
    "Nothing hurries. Nothing is asked. "
    "The stone grows smoother, and the river keeps coming."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
