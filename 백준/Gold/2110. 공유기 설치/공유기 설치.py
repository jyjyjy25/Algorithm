import sys

N, C = map(int, sys.stdin.readline().split())
houses = sorted([int(sys.stdin.readline()) for _ in range(N)])

low = 1
high = houses[-1] - houses[0]

while (low <= high):
    mid = (low + high) // 2
    
    pre_house = houses[0]
    cnt = 1
    for house in houses:
        if house - pre_house >= mid:
            cnt += 1
            pre_house = house
    
    if cnt < C:  # 거리가 너무 넓어서 공유기를 더 설치하지 못한 경우
        high = mid - 1
    elif cnt >= C:  # 거리가 너무 좁아서 공유기를 더 많이 설치한 경우
        low = mid + 1

print(high)