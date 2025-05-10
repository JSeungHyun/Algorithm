from collections import deque
def solution(n, edge):
    answer = [-1,[]]
    graph = [[] for _ in range(n+1)]
    for s,e in edge:
        graph[s].append(e)
        graph[e].append(s)
    
    queue = deque([])
    visited = [False] * (n+1)
    queue.append((1,0))
    visited[1] = True
    while queue:
        node,distance = queue.popleft()
        if distance > answer[0]:
            answer[0] = distance
            answer[1] = [node]
        elif distance == answer[0]:
            answer[1].append(node)
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append((i,distance+1))
    
    return len(answer[1])