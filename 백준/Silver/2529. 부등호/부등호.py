import sys
input = sys.stdin.readline

n = int(input())
sign = list(input().split())
visited = [False] * 10
max_ans, min_ans = "", ""

def pos(i, j, op):
    if op == '<':
        return i < j
    else:
        return i > j

def solution(depth, s):
    global max_ans, min_ans
    if depth == n + 1: # 부등호의 수 + 1이면 종료
        if not len(min_ans):
            min_ans = s
        else:
            max_ans = s
        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or pos(s[-1], str(i), sign[depth - 1]):
                visited[i] = True
                solution(depth+1, s+str(i))
                visited[i] = False

solution(0, "")
print(max_ans)
print(min_ans)
