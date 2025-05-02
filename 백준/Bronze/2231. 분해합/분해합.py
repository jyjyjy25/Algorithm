import sys

N = int(sys.stdin.readline())
for i in range(N+1):
    creator = i
    for s in str(i):
        creator += int(s)
    
    if creator == N:
        print(i)
        break
else:
    print(0)