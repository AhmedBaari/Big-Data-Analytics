import sys

# custom hash using ascii sum
def custom_hash(word):
    x = sum(ord(c) for c in word)   # sum of ASCII values
    return (2 * x + 3) % 10         # (2x+3) % 10 → bucket index

for line in sys.stdin:
    words = line.strip().split()
    for w in words:
        h = custom_hash(w)
        # Emit index where this word maps
        print(f"{h}\t1")