import sys

N, K = map(int, sys.stdin.readline().split())
coin_list = [int(sys.stdin.readline().strip()) for _ in range(N)]

cnt = 0
rest_money = K
for c in coin_list[::-1]:
    cnt += rest_money // c
    rest_money -= (c * (rest_money // c))
    if rest_money == 0:
        break

print(cnt)