import sys
input = sys.stdin.readline

n = int(input())
result_x, result_y = 0, sys.maxsize 
for _ in range(n):
    x, y = map(int, input().split())
    if y < result_y:
        result_x = x
        result_y = y

print(result_x, result_y)