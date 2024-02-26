import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

stack = []
v = 1
while arr:
    if arr[0] == v:
        v += 1
        arr.pop(0)
    else:
        stack.append(arr.pop(0))
    
    while stack:
        if stack[-1] == v:
            stack.pop()
            v += 1
        else:
            break


if not stack:
    print("Nice")
else:
    print("Sad")
