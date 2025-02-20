def solution(n, times):
    low = 0
    high = max(times) * n
    
    while low <= high:
        mid = (low + high) // 2
        
        cnt = 0
        for time in times:
            cnt += mid // time
        
        if cnt < n:
            low = mid + 1
        else:
            high = mid - 1
        
    return low