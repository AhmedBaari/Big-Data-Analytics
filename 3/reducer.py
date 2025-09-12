import sys

# Bloom filter bit array of size 10
bit_array = [0] * 10

for line in sys.stdin:
    idx, _ = line.strip().split("\t")
    idx = int(idx)
    bit_array[idx] = 1   # set the bit at that position

# Print final Bloom filter bit array
print("BloomFilter:", " ".join(map(str, bit_array)))