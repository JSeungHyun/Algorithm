import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
houses = list(map(int, input().split()))
result = Counter()

def getDivisor(num):
    res = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            res.append(i)
            if i != num // i:
                res.append(num // i)
    return res

for house in houses:
    result += Counter(getDivisor(house))

print(result.most_common(2)[1][1])