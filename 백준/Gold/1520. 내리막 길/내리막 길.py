import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
memo = [[-1] * N for _ in range(M)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def solution(y, x):
    if y == M - 1 and x == N - 1:
        return 1
    
    if memo[y][x] != -1:
        return memo[y][x]
    
    res = 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= M or nx >= N:
            continue
        
        if graph[y][x] > graph[ny][nx]:
            res += solution(ny, nx)

    memo[y][x] = res
    return memo[y][x]

print(solution(0, 0))