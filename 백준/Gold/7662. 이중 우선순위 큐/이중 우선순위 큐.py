import sys
import heapq as hq

T = int(sys.stdin.readline())

for _ in range(T):
    K = int(sys.stdin.readline())
    min_Q = []  # 최소힙
    max_Q = []  # 최대힙
    is_available = {}

    for _ in range(K):
        command, data = sys.stdin.readline().split()
        
        if command == "I":
            hq.heappush(min_Q, int(data))
            hq.heappush(max_Q, -int(data))
            
            if int(data) in is_available:
                is_available[int(data)] += 1
            else:
                is_available[int(data)] = 1

        elif command == "D":
            while True:
                if data == "-1" and min_Q:
                    temp = hq.heappop(min_Q)
                    if is_available[temp]:
                        is_available[temp] -= 1
                        break
                elif data == "1" and max_Q:
                    temp = -hq.heappop(max_Q)
                    if is_available[temp]:
                        is_available[temp] -= 1
                        break
                else:
                    break

    if sum(is_available.values()):
        arr = [k for k in is_available.keys() if is_available[k] >= 1]
        print(f"{max(arr)} {min(arr)}")
    else:
        print("EMPTY")
