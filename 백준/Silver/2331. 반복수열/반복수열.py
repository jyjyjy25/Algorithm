import sys

A, P = map(int, sys.stdin.readline().split())

pre_num = A
num_list = [A]

while True:
    new_num = 0
    for s in str(pre_num):
        new_num += int(s) ** P
    
    if new_num in num_list:  # 현재 숫자가 수열에 존재한다면
        idx = num_list.index(new_num)
        break
    else:
        num_list.append(new_num)
        pre_num = new_num

print(idx)
