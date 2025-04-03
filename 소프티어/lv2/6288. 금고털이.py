import sys
input = sys.stdin.readline
import heapq

W,N = map(int, input().split())
result = 0
heap = []

for _ in range(N):
    M, P = map(int, input().split())
    heapq.heappush(heap, (P, M))

while W > 0 and heap:
    P, M = heap.pop()
    if W > M:
        W -= M
        result += (P * M)
    else:
        result += (P * W)
        W = 0

print(result)