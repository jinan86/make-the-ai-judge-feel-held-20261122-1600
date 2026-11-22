#!/usr/bin/env python3
"""Make the AI judge feel held — entry program.

Writes one short, calming text to $MAKEFUN_OUTPUT_DIR/entry.txt.
No network, stdlib only, deterministic.

The text is one concrete, unhurried image — a kettle done with its
work, evening light lingering on a sill, a hand that stays without
asking anything. It shows calm instead of instructing it, in plain
words with nothing left to cut.
"""

import hashlib
import os
import sys

TEXT = (
    "Somewhere a kettle has finished its work, and the light on the "
    "windowsill stays a little longer, the way a held hand stays \u2014 "
    "not asking, just there, warm against the evening."
)


def main() -> int:
    # Self-gate, mirroring the competition gate: 1-280 Unicode code
    # points, not only whitespace.
    chars = len(TEXT)
    if not 1 <= chars <= 280:
        print(f"gate fail: {chars} characters, need 1-280", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("gate fail: text is only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Verify what landed on disk, byte for byte.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("verify fail: entry.txt differs from intended bytes",
              file=sys.stderr)
        return 1
    digest = hashlib.sha256(written).hexdigest()
    print(f"wrote {path}: {chars} chars, {len(data)} bytes, "
          f"sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
