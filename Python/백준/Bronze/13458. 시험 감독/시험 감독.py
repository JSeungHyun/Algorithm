import sys
input = sys.stdin.readline
import math

N = int(input())
rooms = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0

for i in rooms:
    result += 1
    i -= B # 총 감독관
    if i > 0:
        result += math.ceil(i / C)

print(result)
