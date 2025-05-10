import sys
input = sys.stdin.readline

N, M = map(int, input().split())
W = list(map(int, input().split()))
best = [True for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    if W[a] > W[b]:
        best[b] = False
    elif W[a] < W[b]:
        best[a] = False
    else:
        best[b] = False
        best[a] = False

print(best.count(True))