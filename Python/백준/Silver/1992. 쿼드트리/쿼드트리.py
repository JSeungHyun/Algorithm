import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
result = ""


def quadTree(y, x, n):
    global result
    check = graph[y][x]
    for i in range(y, y + n):
        for j in range(x, x + n):
            if graph[i][j] != check:
                check = -1
                break

    if check == -1:
        n //= 2
        result += "("
        quadTree(y, x, n)  # 왼쪽 상단
        quadTree(y, x + n, n)  # 우측 상단
        quadTree(y + n, x, n)  # 왼쪽 하단
        quadTree(y + n, x + n, n)  # 우측 하단
        result += ")"

    elif check == 1:
        result += '1'
    else:
        result += '0'


quadTree(0, 0, N)
print(result)
