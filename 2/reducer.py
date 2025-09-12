import sys

coolest_year = None
min_temp = float("inf")

for line in sys.stdin:
    year, temp = line.strip().split("\t")
    temp = int(temp)

    if temp < min_temp:
        min_temp = temp
        coolest_year = year

print(f"Coolest Year: {coolest_year}, Temperature: {min_temp}")