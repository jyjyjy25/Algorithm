import sys

K, N = map(int, sys.stdin.readline().split())
line = [int(sys.stdin.readline()) for _ in range(K)]


def cal_line_num(height):
    sum = 0
    for l in line:
        sum += l // height
    return sum


low = 1
high = max(line)

while (low <= high):
    mid = (low+high) // 2 # 랜선의 길이
    mid_line_num = cal_line_num(mid) # 랜선의 개수
    
    if mid_line_num >= N:
        low = mid + 1
    else:
        high = mid - 1

print(high)