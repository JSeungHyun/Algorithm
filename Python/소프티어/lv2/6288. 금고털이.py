import sys
input = sys.stdin.readline
import heapq

W, N = map(int, input().split())
heap = []

for _ in range(N):
    M, P = map(int, input().split())
    heapq.heappush(heap, (-P, M))

result = 0
while W > 0 and heap:
    P, M = heapq.heappop(heap)
    P = -P 
    take = min(M, W)
    result += P * take
    W -= take

print(result)