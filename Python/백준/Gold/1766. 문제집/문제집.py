import sys
input = sys.stdin.readline

import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1) # 진입차수

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

result = []
heap = [i for i in range(1, N+1) if indegree[i] == 0]
heapq.heapify(heap)

while heap:
    value = heapq.heappop(heap)
    result.append(value)

    for i in graph[value]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(heap, i)
    
print(' '.join(map(str, result)))