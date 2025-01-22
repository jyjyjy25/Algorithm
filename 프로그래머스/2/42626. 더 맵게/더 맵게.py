from collections import deque

def solution(scoville, K):
    
    scoville.sort()
    scoville = deque(scoville)
    queue = deque()
    
    cnt = 0
    while (scoville and scoville[0] < K) or (queue and queue[0] < K):
        if len(scoville) + len(queue) < 2:
            return -1
        
        m = [0, 0]
        for i in range(2):
            if scoville and queue:
                if scoville[0] >= queue[0]:
                    m[i] = queue.popleft()
                else:
                    m[i] = scoville.popleft()
            elif scoville:
                m[i] = scoville.popleft()
            elif queue:
                m[i] = queue.popleft()
    
        queue.append(m[0] + m[1] * 2)
        cnt += 1
    
    return cnt