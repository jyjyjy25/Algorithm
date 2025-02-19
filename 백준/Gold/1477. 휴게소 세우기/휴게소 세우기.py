import sys

N, M, road_length = map(int, sys.stdin.readline().split())  # 현재 휴개소 개수, 지으러는 휴개소 개수, 고속도로 길이
rest_areas = list(map(int, sys.stdin.readline().split()))  # 휴개소의 위치

rest_areas.append(0)
rest_areas.append(road_length)
rest_areas.sort()

rest_area_distances = []
for i in range(len(rest_areas)-1):
    rest_area_distances.append(rest_areas[i+1] - rest_areas[i])

low, high = 1, road_length - 1
while low <= high:
    mid = (low + high) // 2

    rest_area_cnt = 0
    for rest_area_distance in rest_area_distances:
        if rest_area_distance > mid:
            rest_area_cnt += (rest_area_distance - 1) // mid
    
    if rest_area_cnt <= M:  # 지어진 휴개소의 수가 세우려는 휴개소의 수보다 작은 경우 -> 더 많이 지어야 함 -> 구간을 줄여야 함
        high = mid - 1
    else:
        low = mid + 1

print(low)