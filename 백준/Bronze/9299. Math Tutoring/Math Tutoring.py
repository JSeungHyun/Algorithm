import sys
input = sys.stdin.readline

for i in range(int(input())):
    data = input().split()
    highest = int(data[0])
    items = list(map(int, data[1:]))
    result = []

    for j in range(len(items)):
        item = items[j]
        v = (highest - j) * item
        result.append(v)

    print(f'Case {i+1}: {highest - 1}', end=' ')
    print(*result[:-1])            

