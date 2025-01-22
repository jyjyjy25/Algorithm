import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    cnt = 0
    while(scoville[0] < K):
        if len(scoville) == 1:
            return -1
        
        m1 = heapq.heappop(scoville)
        m2 = heapq.heappop(scoville)
        heapq.heappush(scoville, m1 + m2*2)
        cnt += 1
    
    return cnt