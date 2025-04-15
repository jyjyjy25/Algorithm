# 19:53~
from collections import deque

def solution(priorities, location):
    new_priorities = []
    for i, p in enumerate(priorities):
        new_priorities.append((p, i))
    
    priorities = deque(new_priorities)
    order = 0
    while priorities:
        max_priority = priorities.popleft()
        is_excute = True
        for p in priorities:
            if p[0] > max_priority[0]:
                priorities.append(max_priority)
                is_excute = False
                break
        
        if is_excute:
            order += 1
            if max_priority[1] == location:
                return order