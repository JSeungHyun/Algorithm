import sys
from collections import deque
def solution(n, wires):
    answer = sys.maxsize
    graph = [[] for _ in range(n+1)]
    for s,e in wires:
        graph[s].append(e)
        graph[e].append(s)
    
    def bfs(k):
        queue = deque([1])
        visited = [False] * (n+1)
        visited[1] = True
        cnt = 1
        
        while queue:
            v = queue.popleft()
            for i in graph[v]:
                if not visited[i] and i != k:
                    visited[i] = True
                    cnt += 1
                    queue.append(i)
        return abs(n - cnt * 2)
    
    for i in range(2,n+1):
        answer = min(answer,bfs(i))
    return answer