import sys
input = sys.stdin.readline
from collections import Counter

lands = [list(map(int, input().split())) for _ in range(3)]
result = sys.maxsize

for i in range(3):
    f1 = Counter(lands[i][0:3]).most_common(1)[0][0]
    f2 = Counter(lands[0:3][i]).most_common(1)[0][0]
    lower1 = sum(abs(f1 - lands[j][i]) for j in range(3))
    lower2 = sum(abs(f2 - lands[i][j]) for j in range(3))
    result = min(result, lower1, lower2)

print(result)
