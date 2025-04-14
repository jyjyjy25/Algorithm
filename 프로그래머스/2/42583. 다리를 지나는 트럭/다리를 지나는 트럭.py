from collections import deque

def solution(bridge_length, weight, truck_weights):
    seconds = 0
    
    truck_weights = deque(truck_weights)
    total_weight = truck_weights[0]
    queue = deque([(truck_weights.popleft(), seconds)])
    while queue:
        seconds += 1
        
        if seconds - queue[0][1] == bridge_length:
            total_weight -= queue[0][0]
            queue.popleft()
        
        if truck_weights and total_weight + truck_weights[0] <= weight:
            total_weight += truck_weights[0]
            queue.append((truck_weights.popleft(), seconds))
   
    return seconds+1