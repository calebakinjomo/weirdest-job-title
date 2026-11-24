"""Weirdest Job Title — make.fun bounty entry.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt) and prints exactly the same line to stdout.

The title is 44 characters, within the 60-character limit.
"""

import os

ENTRY = "Lead Lighthouse Keeper for a Landlocked Town"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR is the directory; fall back gracefully if a file
    # path was supplied instead.
    if output_dir.endswith(".txt"):
        path = output_dir
    else:
        path = os.path.join(output_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
