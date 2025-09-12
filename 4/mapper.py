import sys
import hashlib

def custom_hash(word):
    # convert word → int
    x = int(hashlib.md5(word.encode()).hexdigest(), 16)
    return (2 * x + 3) % 10   # (2x+3)%10

def trailing_zeros(x):
    if x == 0:
        return 32   # arbitrary large (since FM assumes infinite zeros)
    tz = 0
    while (x & 1) == 0:
        tz += 1
        x >>= 1
    return tz

for line in sys.stdin:
    words = line.strip().split()
    for w in words:
        h = custom_hash(w)
        tz = trailing_zeros(h)
        print(f"{w}\t{tz}")