import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int,input().split())
    graph[e].append(s)

res_count = 0
res = []

for i in range(1,N+1):
    visited = [False] * (N+1)
    cnt = 0
    queue = deque([i])
    visited[i] = True

    while queue:
        idx = queue.popleft()
        for k in graph[idx]:
            if not visited[k]:
                visited[k] = True
                queue.append(k)
                cnt += 1

    if cnt > res_count:
        res = [i]
        res_count = cnt
    elif cnt == res_count:
        res.append(i)

print(*res)
