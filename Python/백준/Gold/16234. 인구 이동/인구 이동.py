import sys
input = sys.stdin.readline

result = 0
N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

while True:
    changed = False
    visited = set()
    for y in range(N):
        for x in range(N):
            if (y, x) not in visited:
                conn = set()
                q = [(y, x)]
                s = 0
                while q:
                    cy, cx = q.pop()
                    if (cy, cx) not in visited:
                        visited.add((cy, cx))
                        conn.add((cy, cx))
                        s += graph[cy][cx]
                        if cy > 0 and (cy - 1, cx) not in visited and L <= abs(graph[cy - 1][cx] - graph[cy][cx]) <= R:
                            q.append((cy - 1, cx))
                        if cy < N - 1 and (cy + 1, cx) not in visited and L <= abs(graph[cy + 1][cx] - graph[cy][cx]) <= R:
                            q.append((cy + 1, cx))
                        if cx > 0 and (cy, cx - 1) not in visited and L <= abs(graph[cy][cx - 1] - graph[cy][cx]) <= R:
                            q.append((cy, cx - 1))
                        if cx < N - 1 and (cy, cx + 1) not in visited and L <= abs(graph[cy][cx + 1] - graph[cy][cx]) <= R:
                            q.append((cy, cx + 1))
                if len(conn) > 1:
                    avg = s // len(conn)
                    for cy, cx in conn:
                        graph[cy][cx] = avg
                    changed = True
    if not changed:
        break
    result += 1

print(result)