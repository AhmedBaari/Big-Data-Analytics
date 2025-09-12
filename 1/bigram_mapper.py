import sys

for line in sys.stdin:
    words = line.strip().split()
    for i in range(len(words) - 1):
        bigram = "%s %s" % (words[i], words[i+1])
        print("%s\t1" % bigram)