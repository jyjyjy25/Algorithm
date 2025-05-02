import sys
from itertools import permutations

N = int(sys.stdin.readline())
arr = list(range(1, N+1))

cases = list(permutations(arr, N))
cases.sort()
for case in cases:
    print(" ".join(map(str, list(case))))