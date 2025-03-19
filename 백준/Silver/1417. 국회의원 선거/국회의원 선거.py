import sys
import heapq

N = int(sys.stdin.readline())
dasom = int(sys.stdin.readline())
votes = []
for _ in range(N-1):
    x = int(sys.stdin.readline())
    heapq.heappush(votes, -x)

buys = 0

while votes:
    a = heapq.heappop(votes)
    if -a >= dasom:
        buys += 1
        dasom += 1
        heapq.heappush(votes, a+1)
    else:
        break

print(buys)

