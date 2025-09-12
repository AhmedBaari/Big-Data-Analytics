import sys

damping = 0.85

page_links = {}
page_ranks = {}

for line in sys.stdin:
    page, value = line.strip().split("\t", 1)

    # If it's structure (list of links)
    if " " in value:
        page_links[page] = value
    else:
        # rank contribution
        val = float(value)
        page_ranks[page] = page_ranks.get(page, 0) + val

# Apply damping factor
for page in set(list(page_links.keys()) + list(page_ranks.keys())):
    rank_sum = page_ranks.get(page, 0.0)
    new_rank = (1 - damping) + damping * rank_sum
    links = page_links.get(page, "")
    print(f"{page}\t{new_rank}\t{links}")