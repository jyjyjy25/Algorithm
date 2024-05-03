import sys

## 절단 높이를 작게하면 가져가는 나무 길이가 크고, 절단 높이를 크게하면 가져가는 나무 길이가 작다.

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))


def cal_tree(height):
    sum = 0
    for t in tree:
        if t-height > 0:
            sum += t - height
    return sum


low = 0
high = max(tree)
while (low <= high):
    mid = (low+high) // 2 # 절단 높이
    tree_height = cal_tree(mid) # 가져가는 나무 길이

    if tree_height == M:
        print(mid)
        break
    else:
        if tree_height < M:
            # 나무 길이를 더 늘리려면 절단 높이를 줄여야 함
            high = mid - 1
        elif tree_height > M:
            low = mid + 1

if low > high:
    print(high)