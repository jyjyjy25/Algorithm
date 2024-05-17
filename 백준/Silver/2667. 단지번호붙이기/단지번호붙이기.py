import sys
input = sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]
n=int(input().rstrip())
matrix=[list(input().rstrip()) for _ in range(n)]

cnt = 0
result=[]

def dfs(x,y) :
    global cnt
    matrix[x][y] = "0" #방문한 곳 0으로 만들기
    cnt+=1 #카운트 수 늘리기
    for i in range(4) : #상하좌우로 움직이기
        nx = x +dx[i]
        ny = y +dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n :
            #만약 움직인 좌표가 범위를 벗어났다면 continue
            continue
        if matrix[nx][ny] == "1" :
            #움직인 좌표에 집이 있다면 다시 dfs탐색
            dfs(nx,ny)

for i in range(n) :
    for j in range(n) :
        #이중 for문으로 matrix를 하나하나 돌으면서 1인 구간 찾기(시작점 찾기)
        if matrix[i][j]=="1" :
            cnt = 0 #시작 전 카운트 초기화
            dfs(i,j)
            result.append(cnt) #탐색 끝난 후 카운트 값 저장

print(len(result))
result.sort()
for c in result :
    print(c)