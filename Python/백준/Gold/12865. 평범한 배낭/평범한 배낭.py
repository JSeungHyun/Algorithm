import sys
input = sys.stdin.readline

N, K = map(int, input().split())
result = [0] * (K + 1)

for _ in range(N):
    W, V = map(int, input().split())
    for i in range(K, W-1, -1): # K=7, W=3) i = 7,6,5,4
        result[i] = max(result[i], result[i - W] + V)

print(max(result))