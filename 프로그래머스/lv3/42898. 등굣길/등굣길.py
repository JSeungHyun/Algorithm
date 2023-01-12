def solution(m, n, puddles):
    answer = 0
    graph = [[1] * m for _ in range(n)]
    for a,b in puddles:
        graph[b-1][a-1] = 0
    tmp = 1
    for i in range(m):
        if graph[0][i] == 0:
            tmp = 0
        graph[0][i] = tmp
    tmp = 1
    for i in range(n):
        if graph[i][0] == 0:
            tmp = 0
        graph[i][0] = tmp
    
    for y in range(1,n):
        for x in range(1,m):
            if graph[y][x] != 0:
                graph[y][x] = (graph[y-1][x] + graph[y][x-1]) % 1000000007
    return graph[n-1][m-1]