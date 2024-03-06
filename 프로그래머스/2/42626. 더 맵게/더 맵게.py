import heapq

def solution(scoville, K):
    answer = 0
        
    heapq.heapify(scoville)
    while(scoville[0] < K):
        min_0 = heapq.heappop(scoville)
        if len(scoville) == 0:
            answer = -1
            break
        min_1 = heapq.heappop(scoville)
        heapq.heappush(scoville, min_0 + min_1*2)
        # heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        answer += 1 
    
    return answer