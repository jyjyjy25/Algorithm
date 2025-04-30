import sys

def is_palindrome(x):
    l, r = 0, len(x)-1
    while l <= r:
        if l == r:
            break

        if x[l] == x[r]:
            l += 1
            r -= 1
        else:
            return False
    return True


S = sys.stdin.readline().rstrip()

answer = len(S)
for i in range(len(S)):
    s = S[i:]
    if is_palindrome(s):
        break
    else:
        answer += 1

print(answer)
