import sys
N, M = map(int, sys.stdin.readline().split())
lesson = list(map(int, sys.stdin.readline().split()))


def cal_bluelay_cnt(lesson, mid):
    bluelay_cnt = 1
    lesson_sum = 0
    for le in lesson:
        lesson_sum += le
        if lesson_sum > mid:
            bluelay_cnt += 1
            lesson_sum = le
    
    return bluelay_cnt


start = max(lesson)
end = sum(lesson)
while start <= end:
    mid = (start + end) // 2
    bluelay_cnt = cal_bluelay_cnt(lesson, mid)

    if bluelay_cnt > M:
        start = mid + 1
    elif bluelay_cnt <= M:
        end = mid - 1

print(start)