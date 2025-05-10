import sys
input = sys.stdin.readline
from collections import deque

alphas = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

message = deque(input().rstrip())
key = list(dict.fromkeys(input().rstrip())) # 순서유지하면서 중복제거 후 배열
result = ''

# 5 * 5 키 이중 배열로 만들기
for alpha in alphas: # 없는 문자 순서대로 추가
    if alpha not in key:
        key.append(alpha)

key_list = [] # 키 저장
key_dict = {} # 키의 배열 인덱스 위치 저장
temp = []
y = x = 0

for k in key:
    temp.append(k)
    key_dict[k] = (y, x)
    x += 1
    if len(temp) == 5:
        key_list.append(temp)
        temp = []

        x = 0
        y += 1

encrypt_message = ''
while message:
    s1 = message.popleft()
    if message:
        if s1 != message[0]:
            s2 = message.popleft()
            encrypt_message += s1 + s2
        else:
            if s1 == 'X':
                encrypt_message += s1 + 'Q'
            else:
                encrypt_message += s1 + 'X'
    else:
        encrypt_message += s1 + 'X'

for i in range(0, len(encrypt_message), 2):
    s1, s2 = encrypt_message[i], encrypt_message[i + 1]
    y1, x1 = key_dict[s1]
    y2, x2 = key_dict[s2]

    if y1 == y2:
        r1 = key_list[y1][(x1 + 1) % 5]
        r2 = key_list[y2][(x2 + 1) % 5]
    elif x1 == x2:
        r1 = key_list[(y1 + 1) % 5][x1]
        r2 = key_list[(y2 + 1) % 5][x2]
    else:
        r1 = key_list[y1][x2]
        r2 = key_list[y2][x1]
    
    result += r1 + r2

print(result)
