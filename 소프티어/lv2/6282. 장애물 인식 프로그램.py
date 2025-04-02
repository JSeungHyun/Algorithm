import sys
input = sys.stdin.readline


N = int(input())
visited = [[False] * N for _ in range(N)]
blocks = [[int(char) for char in input().rstrip()] for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
stack = []
result = []

for y in range(N):
    for x in range(N):
        if blocks[y][x] == 0: # 장애물이 없으면
            continue
        if visited[y][x] == True: # 이미 방문한 곳이면
            continue
        
        # 탐색 시작
        block_count = 0
        stack.append((y, x))
        visited[y][x] = True # 방문처리
        while stack:
            block_count += 1
            cy, cx = stack.pop(0)
            
            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]

                if ny < 0 or nx < 0 or ny >= N or nx >= N:
                    continue
                
                if visited[ny][nx] == False and blocks[ny][nx] == 1:
                    visited[ny][nx] = True # 방문처리
                    stack.append((ny, nx))

        result.append(block_count)

print(len(result))
for x in sorted(result):
    print(x)
