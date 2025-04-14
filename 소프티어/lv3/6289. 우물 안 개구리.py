import sys
from collections import defaultdict, deque

input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
W = list(map(int, input().split()))


graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)

visited = [False] * N
result = 0

def bfs(start):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                queue.append(n)

# 그래프에 있는 노드들에 대해 연결 요소 확인
for node in range(N):
    if node in graph and not visited[node]:
        bfs(node)
        result += 1

# 방문되지 않은 노드들 카운트
for node in range(N):
    if not visited[node]:
        result += 1

print(result)
