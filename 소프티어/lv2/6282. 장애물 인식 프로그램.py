import sys
input = sys.stdin.readline


N = int(input())
visited = [[False] * N for _ in range(N)]
blocks = [[int(char) for char in input().rstrip()] for _ in range(N)]

print(blocks)
print(visited)
# 1을 만났을때 해당 좌표를 배열에 넣는다.
# while 배열: (배열의 size 0가 일때까지 반복)
# 배열에서 좌표를 pop , 해당 좌표 방문처리
# 해당 좌표의 상 하 좌 우 좌표를 배열에 추가
