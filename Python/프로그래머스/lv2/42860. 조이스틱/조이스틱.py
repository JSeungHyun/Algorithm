from collections import deque
def solution(name):
    queue = deque([])
    queue.append((name, 0, 0))
    while queue:
        cur, idx, cnt = queue.popleft() # 현재 문자열, 인덱스, 조작횟수
        if cur[idx] != 'A': 
            if cur[idx] <= 'M': # M보다 작거나 같으면 A까지 빼는게 유리
                cnt += ord(cur[idx]) - ord('A')
            else:
                cnt += (ord('Z') + 1) - ord(cur[idx]) # 크면 더하는게 유리
        res = cur[:idx] + 'A' + cur[idx+1:] # 현재 인덱스를 'A'로 바꾼 문자열
        if res == 'A' * len(name): # 'A'로만 이루어진 문자열이 되면
            return cnt
        left = idx - 1 if idx != 0 else len(name) - 1 # 현재 인덱스가 0이면 끝으로 이동
        right = idx + 1 if idx != len(name) - 1 else 0 # 현재 인덱스가 문자열 끝이면 처음으로 이동
        queue.append((res, left, cnt+1))
        queue.append((res, right, cnt+1))
        
                
        
    