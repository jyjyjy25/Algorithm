# 3:04~

def solution(N, number):
    if N == number:
        return 1
    
    dp = [set() for _ in range(10)]  #  dp[1] = N 1개로 만들 수 있는 모든 수
    dp[1].add(N)
    
    for i in range(2, 9):
        for j in range(0, i//2+1):
            if j == 0:
                dp[i].add(int(str(N)*i))
                continue
            
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1+op2)
                    dp[i].add(op1-op2)
                    dp[i].add(op1-op2)
                    dp[i].add(op1*op2)
                    if op1 != 0: dp[i].add(op2//op1)
                    if op2 != 0: dp[i].add(op1//op2)
        
        if number in dp[i]:
            return i
    return -1