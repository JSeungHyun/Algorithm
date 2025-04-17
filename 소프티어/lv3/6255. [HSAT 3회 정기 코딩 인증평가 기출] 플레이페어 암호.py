import sys
input = sys.stdin.readline
from collections import deque

alphas = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

message = deque(input().rstrip())
key_list = list(dict.fromkeys(input().rstrip())) # 순서유지하면서 중복제거 후 배열
result = ''

# 5 * 5 키 딕셔너리로 만들기
for alpha in alphas: # 없는 문자 순서대로 추가
    if alpha not in key_list:
        key_list.append(alpha)

# 딕셔너리로 추가
key_dict = {}
y = x = 0
for key in key_list:
    key_dict[key] = (y, x)
    x += 1
    if x == 5:
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

print(encrypt_message)
