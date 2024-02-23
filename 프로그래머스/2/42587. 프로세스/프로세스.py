from collections import deque

def solution(priorities, location):
    answer = 0     
    
    queue = [(i,p) for i,p in enumerate(priorities)]
    queue = deque(queue)
    while (queue):
        x = queue.popleft()
        is_pop = True
        for q in queue:
            if q[1] > x[1]:
                queue.append(x)
                is_pop = False
                break
        
        if is_pop:
            answer += 1
        
        if is_pop and x[0] == location:
            break
                
    return answer