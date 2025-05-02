import sys

A, B = map(int, sys.stdin.readline().split())
candidates = []

def DFS(x, depth):
    if x > B:
        return
    elif x == B:
        candidates.append(depth)
        return
    else:
        DFS(x*2, depth+1)
        DFS(int(str(x)+"1"), depth+1)

DFS(A, 1)
if candidates:
    print(min(candidates))
else:
    print(-1)