import heapq
import sys
import itertools

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for t in temp:
        arr.append(t)
    
    arr = heapq.nlargest(N, arr)

print(heapq.nlargest(N, arr)[-1])