import sys
input = sys.stdin.readline

n,m = map(int, input().split())
rooms = {}

for _ in range(n):
    room = input().rstrip()
    rooms[room] = [0] * 9

for _ in range(m):
    room, s, e = input().split()
    s = int(s) - 9
    e = int(e) - 9
    rooms[room][s:e] = [1] * (e - s) # 예약된 시간은 1로 변경

keys = sorted(rooms.keys())
for i in range(n):
    key = keys[i]
    room = rooms[key]
    print(f'Room {key}:')
    
    available = [] 
    start = None
    for j in range(9):
        if room[j] == 0: # 이용 가능
            if start == None:
                start = str(j + 9).zfill(2)
        else: # 이용 불가능
            if start != None:
                start = start + '-' + str(j + 9).zfill(2)
                available.append(start)
                start = None
        

    if start != None:
        available.append(start + '-18')

    if len(available) > 0:
        print(f'{len(available)} available:')
        for a in available:
            print(a)
    else:
        print('Not available')

    if i != (n - 1):
        print('-----')
