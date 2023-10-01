import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

sorted_list = [num_list[0]]
for i in range(1, N):
    curr_num = num_list[i]
    sorted_list.append(curr_num)
    for j in range(i-1, -1, -1):
        if sorted_list[j] > curr_num:
            sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
        else:
            break

temp_sum = 0
result = 0
for i, n in enumerate(sorted_list):
    temp_sum += n
    result += temp_sum

print(result)