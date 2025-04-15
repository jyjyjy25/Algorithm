from collections import deque

def solution(priorities, location):
    answer = 0

    queue = deque([(p, i) for i, p in enumerate(priorities)])
    while queue:
        current_priority = queue.popleft()
        is_excute = True
        for p in queue:
            if p[0] > current_priority[0]:
                queue.append(current_priority)
                is_excute = False
                break
        
        if is_excute:
            answer += 1
            if current_priority[1] == location:
                break
    
    return answer