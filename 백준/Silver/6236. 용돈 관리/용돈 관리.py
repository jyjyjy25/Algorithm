import sys

N, M = map(int, sys.stdin.readline().split())
spend_money = [int(sys.stdin.readline()) for _ in range(N)]

low = max(spend_money)
high = sum(spend_money)

while low <= high:
    current_money = 0  # 현재 남은 금액
    withdraw_cnt = 0  # 돈을 인출한 횟수

    mid = (low + high) // 2

    for money in spend_money:
        if current_money - money < 0:  # 사용할 금액이 남은 금액보다 큰 경우 -> 돈 인출
            current_money = mid
            withdraw_cnt += 1
        current_money -= money
    
    if withdraw_cnt <= M:  # 돈 인출 횟수가 적은 경우 -> 인출 금액을 줄여야 함
        high = mid - 1
    elif withdraw_cnt > M:  # 돈 인출 횟수가 많은 경우 -> 인출 금액을 높여야 함
        low = mid + 1

print(low)
