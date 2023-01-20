import sys
input = sys.stdin.readline
from collections import deque

N = int(input()) # 도시의 수
M = int(input()) # 버스 노선의 수
cities = [[] for _ in range(N+1)]
visited = [sys.maxsize] * (N+1) # 방문 비용

for _ in range(M):
    s,e,cost = map(int,input().split())
    cities[s].append((e,cost))

s,e = map(int,input().split())
queue = deque([])
queue.append((s,0)) # 시작점 추가
visited[s] = 0 # 시작점의 비용은 0으로 초기화

while queue:
    node,cost = queue.popleft()
    if visited[node] < cost: # 지금 있는 비용이 갱신할 비용 보다 작으면 continue
        continue
    for n,c in cities[node]:
        newCost = cost + c
        if visited[n] > newCost:
            visited[n] = newCost;
            queue.append((n,newCost))

print(visited[e])