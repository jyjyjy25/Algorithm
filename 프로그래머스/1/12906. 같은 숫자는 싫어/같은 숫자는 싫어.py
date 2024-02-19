def solution(arr):
    stack = []
    for a in arr:
        if len(stack) == 0:
            stack.append(a)
        else:
            if stack[-1] != a:
                stack.append(a)
    
    return stack