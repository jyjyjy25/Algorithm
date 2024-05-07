import sys

N = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

card_list.sort()

result = [0] * len(num_list)
for idx, num in enumerate(num_list):
    low = 0
    high = len(card_list)-1

    while (low <= high):
        mid = (low+high) // 2  # 인덱스
        mid_value = card_list[mid]

        if mid_value == num:
            result[idx] = 1
            break
        elif mid_value > num:
            high = mid - 1
        elif mid_value < num:
            low = mid + 1
    
print(*result)