def solution(n, times):
    answer = 0

    low = 1
    high = max(times) * n
    while (low<=high):
        mid = (low+high) // 2
        
        cnt = 0
        for time in times:
            cnt += mid // time
        
        if cnt >= n:
            answer = mid
            high = mid - 1
        elif cnt < n:
            low = mid + 1
            
        print(low, high, mid, cnt)
    
    print(answer)
    return answer