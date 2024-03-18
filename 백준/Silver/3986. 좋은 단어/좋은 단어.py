import sys

N = int(sys.stdin.readline())
words = []
for _ in range(N):
    words.append(sys.stdin.readline().rstrip())

cnt = 0
for word in words:
    stack = []
    for w in word:
        if stack:
            if stack[-1] == w:
                stack.pop()
            else:
                stack.append(w)
        else:
            stack.append(w)
    
    if not stack:
        cnt += 1

print(cnt)