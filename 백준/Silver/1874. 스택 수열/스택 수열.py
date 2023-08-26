import sys

N = int(sys.stdin.readline())
num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

stack = []
i = 1
sequence = []
answer = []
for num in num_list:
    while (1):
        if i <= num:
            stack.append(i)
            i += 1
            answer.append('+')
        else:
            sequence.append(stack.pop())
            answer.append('-')
            break

if sequence == num_list:
    for a in answer:
        print(a)
else:
    print('NO')