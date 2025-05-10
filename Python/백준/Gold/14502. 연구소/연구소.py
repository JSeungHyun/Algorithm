from collections import deque
import copy
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([])  # 바이러스의 위치를 저장할 Queue
    board = copy.deepcopy(graph)
    for y in range(N):
        for x in range(M):
            if board[y][x] == 2:
                queue.append((y, x))
    
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if board[ny][nx] == 0:
                board[ny][nx] = 2
                queue.append((ny,nx))
    
    global answer
    res = 0
    for i in range(N):
        res += board[i].count(0)
    answer = max(answer, res) # 안전지대의 개수 최대를 갱신

# 3개의 벽을 모두 세워본 후 BFS 실행
def makeWall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 0:
                graph[y][x] = 1
                makeWall(cnt+1)
                graph[y][x] = 0

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]        
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = -sys.maxsize

makeWall(0)
print(answer)

