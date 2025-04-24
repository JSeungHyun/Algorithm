import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def solution(y, x):    
    value = int(graph[y][x])
    for i in range(4):
        ny = y + (dy[i] * value)
        nx = x + (dx[i] * value)

        if (ny < 0 or nx < 0 or ny >= N or nx >= M) or graph[ny][nx] == 'H':
            continue

        if dp[ny][nx] != 0: # 이미 방문했던곳, 사이클 생성
            raise Exception
        
        dp[ny][nx] = dp[y][x] + 1
        solution(ny, nx)

try:
    dp[0][0] = 1
    solution(0, 0)
    print(max(max(dp)))
except:
    print(-1)