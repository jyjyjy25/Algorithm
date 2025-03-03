import sys

N = int(sys.stdin.readline())

stack = []
for _ in range(N):
    input_arr = list(sys.stdin.readline().split())
    if len(input_arr) == 2:
        if input_arr[0] == "push":
            stack.append(input_arr[1])
    elif len(input_arr) == 1:
        if input_arr[0] == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif input_arr[0] == "size":
            print(len(stack))
        elif input_arr[0] == "empty":
            if stack:
                print(0)
            else:
                print(1)
        elif input_arr[0] == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)