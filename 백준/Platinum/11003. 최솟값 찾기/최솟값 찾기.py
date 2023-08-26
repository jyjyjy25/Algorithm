import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
D = deque()

for i, a in enumerate(A):
    while D and D[-1][1] > a:
        D.pop()
    D.append((i, a))
    
    if D[0][0] <= i - L:
        D.popleft()
    print(D[0][1], end=' ')