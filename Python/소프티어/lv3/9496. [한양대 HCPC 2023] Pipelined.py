import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))

print(max(li) + N - 1)