import sys
import heapq as hq

N = int(sys.stdin.readline())
card_list = []

for _ in range(N):
    card_list.append(int(sys.stdin.readline()))

hq.heapify(card_list)

cnt = 0
for _ in range(N-1):
    a = hq.heappop(card_list)
    b = hq.heappop(card_list)
    hq.heappush(card_list, a + b)
    cnt += a + b

print(cnt)