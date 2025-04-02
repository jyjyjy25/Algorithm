import sys

N = int(sys.stdin.readline())
trees = list(map(int, sys.stdin.readline().split()))

trees.sort(reverse=True)

days = 1
growing_days = []
for tree in trees:
    days += 1  # 묘목을 심는다.
    growing_days.append(days + tree)  # 묘목을 심고 다 자라는 데까지 걸리는 날짜

print(max(growing_days))