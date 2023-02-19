from collections import deque
def solution(maps):
    graph = []
    start = False
    lebber = False
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == "S":
                start = [y,x]
            elif maps[y][x] == "L":
                lebber = [y,x]
        
            
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def findTarget(y,x,target):
        queue = deque([])
        queue.append((y,x,0))
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        while queue:
            y,x,cnt = queue.popleft()
            if maps[y][x] == target:
                return cnt
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx < 0 or ny >= len(maps) or nx >= len(maps[0]):
                    continue
                if visited[ny][nx] or maps[ny][nx] == "X":
                    continue
                visited[ny][nx] = True
                queue.append((ny,nx,cnt+1))
        return -1
    
    distanceLebber = findTarget(start[0],start[1],"L")
    if distanceLebber == -1:
        return -1
    distanceEnd = findTarget(lebber[0],lebber[1],"E")
    if distanceEnd == -1:
        return -1
    return distanceLebber + distanceEnd