import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
result = 0
items = list(input().rstrip())
# visited = [False for _ in range(len(items))]
robot_index = [i for i in range(N) if items[i] == 'P'] # 로봇들의 인덱스
# total_robot = items.count('P') # 전체 로봇의 수

""" def dfs(depth, pick_count):
    global result

    if depth == total_robot:
        result = max(result, pick_count)
        return
    
    cur_robot_idx = robot_index[depth]
    for i in range(max(0, cur_robot_idx - K), min(N, cur_robot_idx + K + 1)): # 현재 로봇위치에서 +- K 번째까지 탐색
        if items[i] == 'H' and not visited[i]: # 아직 선택하지 않은 부품
            visited[i] = True
            dfs(depth + 1, pick_count + 1)
            visited[i] = False

    dfs(depth + 1, pick_count) # 아무 부품도 짚지 않은 경우도 추가

dfs(0, 0) """

for r in robot_index:
    for i in range(max(0, r - K), min(N, r + K + 1)):
        if items[i] == 'H':
            items[i] = 'S'
            result += 1
            break;            

print(result)           
