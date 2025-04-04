import sys
input = sys.stdin.readline
from itertools import permutations

N, M, K = map(int, input().split())
boxes = list(map(int, input().split()))
print(*permutations(boxes, N))
