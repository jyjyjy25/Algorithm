import sys

N, M = map(int, sys.stdin.readline().split())

answer = []
names = {}

for i in range(N+M):
    k = sys.stdin.readline().rstrip()
    if k in names:
        names[k] += 1
    else:
        names[k] = 1

for key, value in names.items():
    if value == 2:
        answer.append(key)

answer.sort()
print(len(answer))
for i in answer:
    print(i)