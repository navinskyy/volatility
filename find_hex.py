"""Find interesting hex strings in a memory dump (ASCII and UTF-16).

Usage: python find_hex.py <dump-file>
"""
import re
import sys

data = open(sys.argv[1], "rb").read()

ascii_hits = [m.decode() for m in re.findall(rb"[0-9a-f]{20,}", data)]
utf16_hits = [m.decode("utf-16-le") for m in re.findall(rb"(?:[0-9a-f]\x00){20,}", data)]

# Skip junk like "aaaaaaaa..." (too few distinct characters) and huge blocks.
found = {s for s in ascii_hits + utf16_hits if len(set(s)) >= 8 and len(s) < 300}

for s in sorted(found, key=len, reverse=True)[:40]:
    print(s)
