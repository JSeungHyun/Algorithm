from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def bfs(start):
        nonlocal answer
        queue = deque([start])
        while queue:
            v = queue.popleft()
            visited[v] = True
            for i in range(n):
                if computers[v][i] == 1 and not visited[i]:
                    queue.append(i)
    for i in range(n):
        if not visited[i]:
            answer += 1
            bfs(i)
            
    return answer