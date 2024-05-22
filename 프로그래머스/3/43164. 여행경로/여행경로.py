def solution(tickets):
    routes = []
    visited = [False] * len(tickets)
    
    def DFS(airport, route):
        if len(route) == len(tickets)+1:
            routes.append(route)
            return
                
        for idx, ticket in enumerate(tickets):
            if airport == ticket[0] and visited[idx] == False:
                visited[idx] = True
                DFS(ticket[1], route+[ticket[1]])
                visited[idx] = False
            
    route = ["ICN"]
    DFS("ICN", route)
    
    return sorted(routes)[0]