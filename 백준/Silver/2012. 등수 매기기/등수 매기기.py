import sys

N = int(sys.stdin.readline())
expect_ranks = [int(sys.stdin.readline()) for _ in range(N)]

expect_ranks.sort()
answer = 0

for i in range(len(expect_ranks)):
    answer += abs((i+1) - expect_ranks[i])

print(answer)