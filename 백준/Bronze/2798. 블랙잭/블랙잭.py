import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

cases = list(map(sum, combinations(cards, 3)))
cases.sort(reverse=True)
for c in cases:
    if c <= M:
        print(c)
        break
