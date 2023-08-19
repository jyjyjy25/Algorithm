import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

cnt = 0
for i in range(N):
    start_pointer = 0
    end_pointer = N - 1
    good_num = nums[i]
    while (start_pointer < end_pointer):
        if nums[start_pointer] + nums[end_pointer] < good_num:
            start_pointer += 1
        elif nums[start_pointer] + nums[end_pointer] > good_num:
            end_pointer -= 1
        else:
            if start_pointer == i:
                start_pointer += 1
            elif end_pointer == i:
                end_pointer -= 1
            else:
                cnt += 1
                break

print(cnt)