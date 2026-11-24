#!/usr/bin/env python3
"""Fortune in a Pot — emit the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Reads entry.txt next to this script, validates it against the contest gate
(UTF-8, 1-120 characters, not only whitespace, single line), then writes the
exact normalized bytes to the output directory. Pure Python stdlib only.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(here, "entry.txt")

    try:
        with open(src_path, "rb") as f:
            raw = f.read()
    except OSError as exc:
        print("error: cannot read entry.txt: %s" % exc, file=sys.stderr)
        return 1

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        print("error: entry.txt is not valid UTF-8: %s" % exc, file=sys.stderr)
        return 1

    # Drop at most one trailing newline, then at most one trailing CR.
    if text.endswith("\n"):
        text = text[:-1]
    if text.endswith("\r"):
        text = text[:-1]

    if not 1 <= len(text) <= 120:
        print("error: entry must be 1-120 characters, got %d" % len(text),
              file=sys.stderr)
        return 1
    if not text.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output/")
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "wb") as f:
            f.write(text.encode("utf-8"))
        os.chmod(out_path, 0o644)
    except OSError as exc:
        print("error: cannot write output: %s" % exc, file=sys.stderr)
        return 1

    print("characters: %d" % len(text))
    return 0


if __name__ == "__main__":
    sys.exit(main())
