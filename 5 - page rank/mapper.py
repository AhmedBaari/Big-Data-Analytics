import sys

for line in sys.stdin:
    parts = line.strip().split()
    if len(parts) == 0:
        continue

    page = parts[0]        # current page
    links = parts[1:]      # outgoing links
    num_links = len(links)

    # Emit structure info (to preserve graph structure)
    print(f"{page}\t{' '.join(links)}")

    # If page has rank (initial assume 1.0), distribute equally
    rank = 1.0
    if num_links > 0:
        contribution = rank / num_links
        for link in links:
            print(f"{link}\t{contribution}")