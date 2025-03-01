# 12:00~
def solution(money):
    
    # 첫 번째 집을 선택하는 경우 (마지막 집은 선택 x)
    dp = [0] * (len(money) + 1)
    dp[1] = money[0]
    dp[2] = money[1]
    
    for i in range(3, len(money)):
        dp[i] = max(dp[i-2], dp[i-3]) + money[i-1]
                
    max_1 = max(dp)
    
    # 두 번째 집을 선택하는 경우
    dp = [0] * (len(money) + 1)
    dp[1] = money[1]
    dp[2] = money[2]
    
    for i in range(3, len(money)):
        dp[i] = max(dp[i-2], dp[i-3]) + money[i]
    
    max_2 = max(dp)
    
    return max(max_1, max_2)
