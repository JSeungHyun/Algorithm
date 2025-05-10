import sys
input = sys.stdin.readline

T = int(input())
for case in range(1, T + 1):
    data = list(map(int, input().split()))
    n = data[0]

    items = data[1:]
    result = [(n - i) * coeff for i, coeff in enumerate(items[:-1])]

    print(f"Case {case}: {n - 1}", end=" ")
    print(*result)