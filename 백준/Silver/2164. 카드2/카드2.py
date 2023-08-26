import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
for i in range(N, 0, -1):
    queue.append(i)

i = 0
while (1):
    if len(queue) == 1:
        break

    i += 1
    if i % 2 == 1:
        queue.pop()
    else:
        queue.appendleft(queue.pop())

print(queue.pop())