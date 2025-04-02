import sys
input = sys.stdin.readline


N = int(input())
visited = [[False] * N for _ in range(N)]
blocks = [[int(char) for char in input().rstrip()] for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


for y in range(N):
    for x in range(N):
        if visited[y][x] == True:
            continue
        if blocks[y][x] == 0:
            continue