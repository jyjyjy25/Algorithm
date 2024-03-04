import sys

N, K = map(int, sys.stdin.readline().split())
A = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

cnt = 0
for a in reversed(A):
    cnt += K // a
    K %= a  

print(cnt)