import heapq
import sys
input = sys.stdin.readline

V,E = map(int,input().split())
start = int(input())
visited = [sys.maxsize] * (V+1)
graph = [[] for _ in range(V+1)]

for _ in range(E):
    s,e,cost = map(int,input().split())
    graph[s].append((cost,e))

visited[start] = 0
heap = []
heapq.heappush(heap,(0,start))

while heap:
    cost,now = heapq.heappop(heap)
    if visited[now] < cost:
        continue
    
    for c,n in graph[now]:
        newCost = c + cost
        if visited[n] > newCost:
            visited[n] = newCost
            heapq.heappush(heap,(newCost,n))
            
for i in range(1,V+1):
    print("INF" if visited[i] == sys.maxsize else visited[i])
