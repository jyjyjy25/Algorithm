import sys

A = list(sys.stdin.readline().rstrip().split('-'))

cal = []
for i in range(len(A)):
    result = 0
    temp = list(A[i].split('+'))
    for t in temp:
        result += int(t)
    cal.append(result)

ans = cal[0]
for i in range(1, len(cal)):
    ans -= cal[i]

print(ans)