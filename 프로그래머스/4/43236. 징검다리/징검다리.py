def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    rocks.append(distance)
    
    low = 1
    high = distance
    while (low <= high):
        mid = (low + high) // 2  # 바위 사이 거리의 최솟값
        
        delete = 0  # 삭제한 바위 수
        prev_rock = 0  # 이전 바위 위치
        
        for rock in rocks:
            if rock - prev_rock < mid:  # 거리가 커트라인보다 작으면 바위 삭제 (왜냐면 최댓값을 구하는게 목적)
                delete += 1
            else:
                prev_rock = rock
            
            if delete > n:  # 삭제한 바위 수가 n보다 크면 break
                break
        
        if delete <= n:
            low = mid + 1  # 최댓값을 구하기 위해 커트라인 재설정
        else:
            high = mid - 1
    
    return high