import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())

A = [[] for _ in range(N)]
visited = [False] * (N)
EXIST = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    A[a].append(b)
    A[b].append(a)


def DFS(i, depth):
    global EXIST
    visited[i] = True
    
    if depth == 5:
        EXIST = 1
        return

    for k in A[i]:
        if not visited[k]:
            DFS(k, depth + 1)
    visited[i] = False

for i in range(N):
    DFS(i, 1)
    if EXIST:
        break

print(EXIST)