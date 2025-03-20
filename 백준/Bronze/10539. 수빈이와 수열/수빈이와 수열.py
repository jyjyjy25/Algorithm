import sys

N = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
A = []

sum = 0
for i in range(1, len(B)+1):
    if i == 1:
        A.append(B[i-1])
        sum += B[i-1]
        continue
    
    A.append(B[i-1] * (i) - sum)
    sum += A[i-1]

print(" ".join(list(map(str, A))))