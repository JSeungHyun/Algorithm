import sys
input = sys.stdin.readline

def solution(N, heights, parts):
    result = 0
    directions = [(0, 1), (1, 0)]  # 오른쪽, 아래쪽
    visited = [[False for _ in range(N)] for _ in range(N)]

    def back(depth, total):
        nonlocal result
        if depth == parts:
            result = max(result, total)
            return
        
        for y in range(N):
            for x in range(N):
                if visited[y][x]:
                    continue
                for dy, dx in directions:
                    ny = y + dy
                    nx = x + dx
                    if ny < 0 or ny >= N or nx < 0 or nx >= N:
                        continue
                    if visited[ny][nx]:
                        continue
                    visited[y][x] = visited[ny][nx] = True
                    back(depth + 1, total + heights[y][x] + heights[ny][nx])
                    visited[y][x] = visited[ny][nx] = False
    back(0, 0)
    return result

N = int(input())
parts = 2 if N == 2 else 4
heights = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, heights, parts))
    
