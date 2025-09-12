import sys

for line in sys.stdin:
    parts = line.strip().split()
    if len(parts) != 2:
        continue
    year, temp = parts
    print(f"{year}\t{temp}")
