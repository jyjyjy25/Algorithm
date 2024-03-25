def solution(n, lost, reserve):
    answer = 0
    
    reserve.sort()
    lost.sort()
    
    # lost, reserve에 공통으로 있는 요소 제거
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
    
    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
    
    answer = n - len(lost)
    return answer