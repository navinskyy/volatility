"""Try every single-byte XOR key on a hex string and print readable results.

Usage: python xor_try.py <hex-string>
"""
import sys

data = bytes.fromhex(sys.argv[1])

for key in range(256):
    out = bytes(b ^ key for b in data)
    if all(32 <= c < 127 for c in out):
        print(f"{key:3d}  {chr(key)!r:6}  {out.decode()}")
