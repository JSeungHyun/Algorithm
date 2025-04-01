import sys
input = sys.stdin.readline

items = []

for _ in range(int(input())):
    s = input().rstrip()
    if '.' in s:
        items.append(list(map(int, s.split('.'))))
    else:
        items.append([int(s), -1])

items.sort(key=lambda x:(x[0], x[1]))
for a, b in items:
    if b == -1:
        print(a)
    else:
        print(f'{a}.{b}')
