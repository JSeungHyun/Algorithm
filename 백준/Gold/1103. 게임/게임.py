import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dp = [[-1] * M for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def solution(y, x):
    global result
    if (y < 0 or x < 0 or y >= N or x >= M) or graph[y][x] == 'H': # 탈출 조건
        return 0    
    
    if visited[y][x]: # 이미 방문했던곳, 사이클 생성
        print(-1)
        exit(0)

    if dp[y][x] != -1:
        return dp[y][x]

    visited[y][x] = True
    value = int(graph[y][x])
    result = 0

    for i in range(4):
        ny = y + (dy[i] * value)
        nx = x + (dx[i] * value)

        result = max(result, solution(ny, nx))
    
    visited[y][x] = False
    dp[y][x] = result + 1
    return dp[y][x]

print(solution(0, 0))
