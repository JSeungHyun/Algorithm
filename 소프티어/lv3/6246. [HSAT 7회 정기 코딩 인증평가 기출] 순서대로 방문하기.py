import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [list(map(int, input().split())) for _ in range(N)]
goals = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
result = 0

def dfs(y, x, depth):
    global result

    if (y, x) == goals[depth]: # 순서대로 방문
        depth = depth + 1
        if depth == M:
            result = result + 1
            return
        
    visited[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
            dfs(ny, nx, depth)

    visited[y][x] = 0

a, b = goals[0]
dfs(a, b, 0)
print(result)