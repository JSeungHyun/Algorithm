import sys
input = sys.stdin.readline

n = int(input())
fertile = list(map(int, input().split()))
fertile.sort()

print(max(fertile[0] * fertile[1], fertile[-1] * fertile[-2]))