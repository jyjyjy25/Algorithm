N = map(int, input())
N = list(N)
N.sort(reverse=True)

for x in N:
    print(x, end='')
