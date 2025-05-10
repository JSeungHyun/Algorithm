import sys
input = sys.stdin.readline

graph = [list(input().split()) for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = set() # 중복 제거를 위해 set 으로 저장


def dfs(y, x, letters):
    if len(letters) == 6: # 문자의 길이가 6이 되면
        res.add(letters) # 결과에 추가 후
        return  # 해당 재귀 종료

    letters += graph[y][x] # 문자열에 추가
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= 5 or nx >= 5:
            continue
        dfs(ny, nx, letters)

# 숫자보드 모두 탐색
for i in range(5):
    for j in range(5):
        dfs(i, j, '')
print(len(res))
