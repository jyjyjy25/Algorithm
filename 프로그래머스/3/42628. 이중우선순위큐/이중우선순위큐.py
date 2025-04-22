# 6:00~ 
import heapq as hp

def solution(operations):
    max_heap, min_heap = [], []
    hp.heapify(max_heap)
    hp.heapify(min_heap)
    
    for op in operations:
        ops = op.split()
        if ops[0] == "I":
            hp.heappush(min_heap, int(ops[1]))
        elif ops[0] == "D":
            if ops[1] == "1":
                while min_heap:  # 최대힙으로 변경
                    hp.heappush(max_heap, -hp.heappop(min_heap))
                if max_heap: 
                    hp.heappop(max_heap)
            elif ops[1] == "-1":
                while max_heap:  # 최소힙으로 변경
                    hp.heappush(min_heap, -hp.heappop(max_heap))
                if min_heap:
                    hp.heappop(min_heap)

    if not min_heap and not max_heap:
        return [0, 0]
    else:
        while max_heap:
            hp.heappush(min_heap, -hp.heappop(max_heap))
        min_value = hp.heappop(min_heap)

        while min_heap:
            hp.heappush(max_heap, -hp.heappop(min_heap))
        if max_heap:
            max_value = -hp.heappop(max_heap)
        else:
            max_value = min_value

        return [max_value, min_value]