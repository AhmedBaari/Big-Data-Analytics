import sys

max_trailing = {}

for line in sys.stdin:
    word, tz = line.strip().split("\t")
    tz = int(tz)
    if word not in max_trailing:
        max_trailing[word] = tz
    else:
        max_trailing[word] = max(max_trailing[word], tz)

# FM estimate: 2^R
for word, r in max_trailing.items():
    print(f"{word}\tApproxFreq={2**r}")