import sys
import heapq

N = int(sys.stdin.readline().strip())

cards = []
for _ in range(N):
    x = int(sys.stdin.readline().strip())
    heapq.heappush(cards, x)

cnt = 0
while len(cards) >= 2:
    temp_card = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, temp_card)
    cnt += temp_card

print(cnt)