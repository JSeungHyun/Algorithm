import sys
input = sys.stdin.readline

N, M = map(int, input().split())
limits = []
speeds = []

for _ in range(N):
    dist, speed = map(int, input().split())
    for _ in range(dist):
        limits.append(speed) 

for _ in range(M):
    dist, speed = map(int, input().split())
    for _ in range(dist):
        speeds.append(speed)

max_value = max(speeds[i] - limits[i] for i in range(100))
print(max(0, max_value))
