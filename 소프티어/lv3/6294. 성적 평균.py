import sys
input = sys.stdin.readline

N, K = map(int, input().split())
grades = list(map(int, input().split()))

for _ in range(K):
    s, e = map(int, input().split())
    print(f"{round(sum(grades[s-1:e]) / (e - s + 1), 2):.2f}")