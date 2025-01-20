import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

maps = [0] * (100000+1)

move = [1, 1, 2]
cal = ["-", "+", "*"]

def BFS(v):
    queue = deque([v])

    while queue:
        n = queue.popleft()
        if n == K:
            return maps[K]
        for m, c in zip(move, cal):
            expression = str(n) + c + str(m)
            x = eval(expression)
            if x >= 0 and x <= 100000 and maps[x] == 0:
                maps[x] = maps[n] + 1
                queue.append(x)

print(BFS(N))
# print(maps[K])
