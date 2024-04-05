def solution(triangle):
    answer = 0
    
    dp = []
    dp.append(triangle[0])
    
    for i in range(1, len(triangle)):
        temp = []
        for j, t in enumerate(triangle[i]):
            if j == 0:
                temp.append(dp[i-1][j] + t)
            elif j == len(triangle[i])-1:
                temp.append(dp[i-1][-1] + t)
            else:
                temp.append(max(dp[i-1][j-1] + t, dp[i-1][j] + t))
        dp.append(temp)
                
    return max(dp[-1])