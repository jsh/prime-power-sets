# search for largest power of two that can be used as a list index

import sys

p = 2  # default
if len(sys.argv) > 1:
    p = int(sys.argv[1])
for k in range(100):
    if p**k > sys.maxsize:
        print(f"{k=}, {p}**k > sys.maxsize")
        print(f"largest allowed power: {k - 1}")
        sys.exit(0)
