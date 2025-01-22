import heapq as hq

def solution(operations):
    min_queue = []  # 최소힙
    max_queue = []  # 최대힙
    
    for op in operations:
        command, data = op.split()
        
        if command == "I":
            hq.heappush(min_queue, int(data))
            hq.heappush(max_queue, -int(data))
        elif command == "D":
            if data == "-1" and min_queue:
                temp = hq.heappop(min_queue)
                max_queue.remove(-temp)
            elif data == "1" and max_queue:
                temp = hq.heappop(max_queue)
                min_queue.remove(-temp)

    if min_queue or max_queue:
        return [-hq.heappop(max_queue), hq.heappop(min_queue)]
    else:
        return [0, 0]
