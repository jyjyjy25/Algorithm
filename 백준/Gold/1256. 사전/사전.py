import sys

N, M, K = map(int, sys.stdin.readline().split())
dp = [[1 for _ in range(M+1)] for _ in range(N+1)]  # dp[a][z] = a개, z개 남았을 때 만들 수 있는 문자열 개수
dp[0][0] = 1

for i in range(1, N+1):  # a 개수
    for j in range(1, M+1):  # z 개수
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

if dp[N][M] < K:
    print(-1)
else:
    result = ""
    a = N  # 남은 a의 개수
    z = M  # 남은 z의 개수
    while a > 0 and z > 0:
        if a > 0 and dp[a-1][z] >= K:  # 맨 앞에 ‘a’를 넣으면 dp[a-1][z] 개수의 문자열이 가능함. 이게 K보다 크면 K번째는 ‘a’를 선택했을 때 안에 있음.
            result += "a"
            a -= 1
        else:  # 이게 K보다 작으면 ‘a’로 시작하는 것들은 K번째보다 앞에 다 몰려있음. 따라서 ‘z’를 선택하고 앞에 a로 시작하는 경우 수만큼 K를 줄여야 함.
            K -= dp[a-1][z]
            result += "z"
            z -= 1
    result += "a"*a
    result += "z"*z
    print(result)