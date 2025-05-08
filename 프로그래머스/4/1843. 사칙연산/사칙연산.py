def solution(arr):
    N = len(arr)

    for i in range(0, N, 2):
        arr[i] = int(arr[i])

    max_dp = [[0 for _ in range(N)] for _ in range(N)]
    min_dp = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(0, N, 2):
        max_dp[i][i] = arr[i]
        min_dp[i][i] = arr[i]
    
    for x in range(3, N+1, 2):
        for left in range(0, N, 2):
            right = x + left - 1
            if right >= N: break
            
            candidates_max, candidates_min = [], []
            for k in range(left+1, right, 2):
                if arr[k] == "+":
                    candidates_max.append(max_dp[left][k-1] + max_dp[k+1][right])
                    candidates_min.append(min_dp[left][k-1] + min_dp[k+1][right])
                elif arr[k] == "-":
                    candidates_max.append(max_dp[left][k-1] - min_dp[k+1][right])
                    candidates_min.append(min_dp[left][k-1] - max_dp[k+1][right])
            
            max_dp[left][right] = max(candidates_max)
            min_dp[left][right] = min(candidates_min)

    return max_dp[0][-1]