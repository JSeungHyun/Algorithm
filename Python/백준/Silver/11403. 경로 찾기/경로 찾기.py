from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]


def bfs(start):
    li = [0] * N
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in range(N):
            if graph[v][i] == 1 and li[i] == 0:
                li[i] = 1
                queue.append(i)
    print(*li)

for i in range(N):
    bfs(i)