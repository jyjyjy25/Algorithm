def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


m, n = map(int, input().split())
print(int(factorial(m) / (factorial(n) * factorial(m-n))))