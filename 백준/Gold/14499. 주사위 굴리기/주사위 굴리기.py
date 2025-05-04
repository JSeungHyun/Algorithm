import sys
input = sys.stdin.readline

N, M, y, x, K = map(int, input().split())
direct = [(0, 1), (0, -1), (-1, 0), (1, 0)]
graph = []
dice = [0] * 6 # FRONT, TOP, BACK, BOTTOM, LEFT, RIGHT
for _ in range(N):
    graph.append(list(map(int, input().split())))

commands = list(map(int, input().split()))

def move_dice(num):
    front, top, back, bottom, left, right = dice
    if num == 1:  # 동쪽
        new_dice = [front, left, back, right, bottom, top]
    elif num == 2:  # 서쪽
        new_dice = [front, right, back, left, top, bottom]
    elif num == 3:  # 북쪽
        new_dice = [bottom, front, top, back, left, right]
    else:  # 남쪽
        new_dice = [top, back, bottom, front, left, right]
    return new_dice

for command in commands:
    ny = y + direct[command - 1][0]
    nx = x + direct[command - 1][1]

    if ny < 0 or nx < 0 or ny >= N or nx >= M:
        continue
    y = ny
    x = nx
    dice = move_dice(command)
    if not graph[ny][nx]:
        graph[ny][nx] = dice[3]
    else:
        dice[3] = graph[ny][nx]
        graph[ny][nx] = 0
    
    print(dice[1])