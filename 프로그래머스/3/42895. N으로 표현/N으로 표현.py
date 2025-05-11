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
               
            num1 = int(str(N)*(i-j))
            num2 = int(str(N)*j)
            
            dp[i].add(num1+num2)
            dp[i].add(num1-num2)
            dp[i].add(num1*num2)
            dp[i].add(num1//num2)
            
            for k in dp[j]:
                dp[i].add(k+num1)
                dp[i].add(k-num1)
                dp[i].add(k*num1)
                dp[i].add(k//num1)
                
                dp[i].add(num1-k)
                if k != 0:
                    dp[i].add(num1//k)
                
                for l in dp[i-j]:
                    dp[i].add(k+l)
                    dp[i].add(k-l)
                    dp[i].add(k*l)
                    if l != 0:
                        dp[i].add(k//l)
                    
                    dp[i].add(l-k)
                    if k != 0:
                        dp[i].add(l//k)
        
        if number in dp[i]:
            return i
    return -1