import sys

A, P = map(int, sys.stdin.readline().split())

set_nums = set([])
set_nums.add(A)
pre_num = A
num_list = [A]

while True:
    new_num = 0
    for s in str(pre_num):
        new_num += int(s) ** P
    
    if new_num not in set_nums:
        if new_num not in num_list:
            set_nums.add(new_num)
            num_list.append(new_num)
        else:
            break
    elif new_num in set_nums:
        set_nums.remove(new_num)

    pre_num = new_num

print(len(set_nums)) 
