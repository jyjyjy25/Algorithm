import sys
from collections import deque

N = int(sys.stdin.readline().strip())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
distance = [0] * (N+1)

for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    node = temp[0]
    data = temp[1:]
    for i in range(0, len(data), 2):
        if data[i] == -1:
            break
        A[node].append((data[i], data[i+1]))


def BFS(v):
    queue = deque()
    visited[v] = True
    queue.append(v)
    while queue:
        node = queue.popleft()
        for i in A[node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                distance[i[0]] = distance[node] + i[1]
                queue.append(i[0])


BFS(1)
max_idx = 1
for i in range(2, N+1):
    if distance[max_idx] < distance[i]:
        max_idx = i

visited = [False] * (N+1)
distance = [0] * (N+1)
BFS(max_idx)

print(max(distance))