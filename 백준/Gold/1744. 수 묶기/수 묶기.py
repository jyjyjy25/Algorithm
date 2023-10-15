import sys
from queue import PriorityQueue

N = int(sys.stdin.readline().strip())

pos_nums = []
nag_nums = PriorityQueue()
one = 0
zero = 0

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x > 1:
        pos_nums.append(x)
    elif x < 0:
        nag_nums.put(x)
    elif x == 1:
        one += 1
    elif x == 0:
        zero += 1

sum = 0

pos_nums.sort(reverse=True)
for i in range(0, len(pos_nums) - 1, 2):
    sum += pos_nums[i] * pos_nums[i+1]

# 양수의 개수가 홀수일 경우
if len(pos_nums) % 2 == 1:
    sum += pos_nums[-1]

while nag_nums.qsize() >= 2:
    sum += nag_nums.get() * nag_nums.get()

# 음수의 개수가 홀수일 경우
if nag_nums.qsize() % 2 == 1:
    if zero != 0:
        sum += 0
    elif zero == 0:
        sum += nag_nums.get()

for i in range(one):
    sum += 1

print(sum)