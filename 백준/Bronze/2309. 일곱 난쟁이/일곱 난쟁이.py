import sys

arr = [int(sys.stdin.readline()) for _ in range(9)]
visited = [False for _ in range(9)]

temp = []  # 난쟁이 키
find = False

def DFS(depth):
    global find
    if find:
        return
    
    if depth == 7:
        if sum(temp) == 100:
            find = True
            temp.sort()
            for t in temp:
                print(t)
    else:
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                temp.append(arr[i])
                DFS(depth+1)
                visited[i] = False
                temp.pop()


DFS(0)