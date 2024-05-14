def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    def DFS(v):
        visited[v] = True
        print(visited)
        for i, n in enumerate(computers[v]):
            if i == v:  # 같은 인덱스일 경우 제외
                continue
            if n == 1 and not visited[i]:
                print(v, i, computers[v])
                DFS(i)
    
    for i in range(n):
        if not visited[i]:
            print(i)
            DFS(i)
            answer += 1
    print(visited)
        
    return answer