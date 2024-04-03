import sys


def fib_recur(n):
    global recur_cnt
    if n == 1 or n == 2:
        recur_cnt += 1
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)


def fib_dp(n):
    global dp_cnt
    f = [0] * (n+1)
    f[1] = f[2] = 1
    for i in range(3, n+1):
        dp_cnt += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]


N = int(sys.stdin.readline())
recur_cnt = dp_cnt = 0

fib_recur(N)
fib_dp(N)

print(recur_cnt, dp_cnt)