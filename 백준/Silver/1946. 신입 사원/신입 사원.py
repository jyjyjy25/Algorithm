import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    
    rank = []
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        rank.append((a, b))
    rank.sort()  # 서류를 기준으로 정렬

    cnt = 1  # 서류 1등은 무조건 합격
    max = rank[0][1]  # 합격 기준 등수
    for i in range(1, N):
        if max > rank[i][1]:  # 면접 등수가 합격 기준 등수보다 높다면
            cnt += 1
            max = rank[i][1]
    
    print(cnt)