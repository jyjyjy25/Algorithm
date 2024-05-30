import heapq

def solution(operations):
    heap = []
    
    for oper in operations:
        ch, num = oper.split(' ')
        num = int(num)
        
        if ch == "I":  # 삽입 연산
            heapq.heappush(heap, num)

        elif ch == "D" and len(heap):  # 삭제 연산
            if num == -1:  # 최솟값 삭제
                heapq.heappop(heap)
            elif num == 1:  # 최댓값 삭제
                heap.remove(max(heap))
    
    if heap:
        return [max(heap), heapq.heappop(heap)]
    else:
        return [0,0]