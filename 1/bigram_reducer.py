import sys

current_bigram = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t')
    if len(parts) != 2:
        continue
    bigram, count = parts
    try:
        count = int(count)
    except ValueError:
        continue
    if bigram == current_bigram:
        current_count += count
    else:
        if current_bigram:
            print("%s\t%d" % (current_bigram, current_count))
        current_bigram = bigram
        current_count = count

if current_bigram:
    print("%s\t%d" % (current_bigram, current_count))