import sys
from collections import deque

dx = ["*2", "-1", "+1"]
dt = [0, 1, 1]

def BFS(x, time):
    queue = deque([(x, time)])
    visited[x] = True
    while queue:
        now, t = queue.popleft()
        if now == K:
            return t
        for ax, at in zip(dx, dt):
            nx = int(eval(str(now) + ax))
            nt = t + at
            if 100000 >= nx >= 0:
                if not visited[nx]:
                    visited[nx] = True
                    queue.append((nx, nt))


N, K = map(int, sys.stdin.readline().split())
visited = [False for _ in range(100000+1)]
print(BFS(N, 0))